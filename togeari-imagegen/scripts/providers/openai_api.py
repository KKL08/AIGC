"""OpenAI Images API provider for togeari image generation.

Zero external dependencies — uses only Python stdlib (urllib, json, base64).
"""

from __future__ import annotations

import base64
import json
import sys
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path
from typing import Any, Optional

from . import (
    GenerateRequest,
    GenerateResult,
    _EXT_TO_MEDIA_TYPE,
    register_provider,
    resolve_api_key,
    resolve_image_input,
    validate_request,
)

# (quality, aspect_ratio) → "WxH"
# All dimensions are multiples of 16.
# Constraints: 655,360 ≤ W*H ≤ 8,294,400 | max edge ≤ 3840 | max(W,H)/min(W,H) ≤ 3
SIZE_MAP: dict[str, dict[str, str]] = {
    "preview": {
        "1:1":  "1024x1024",
        "16:9": "1280x720",
        "9:16": "720x1280",
        "4:3":  "1024x768",
        "3:4":  "768x1024",
        "3:2":  "1536x1024",
        "2:3":  "1024x1536",
    },
    "standard": {
        "1:1":  "1536x1536",
        "16:9": "2048x1152",
        "9:16": "1152x2048",
        "4:3":  "1536x1152",
        "3:4":  "1152x1536",
        "3:2":  "1920x1280",
        "2:3":  "1280x1920",
    },
    "high": {
        "1:1":  "2048x2048",
        "16:9": "3840x2160",
        "9:16": "2160x3840",
        "4:3":  "2560x1920",
        "3:4":  "1920x2560",
        "3:2":  "3072x2048",
        "2:3":  "2048x3072",
    },
}

# Map our quality presets to OpenAI API quality parameter values
QUALITY_MAP: dict[str, str] = {
    "preview":  "low",
    "standard": "medium",
    "high":     "high",
}

OPENAI_IMAGES_URL = "https://api.openai.com/v1/images/generations"
OPENAI_EDITS_URL = "https://api.openai.com/v1/images/edits"

# Inverse of _EXT_TO_MEDIA_TYPE: media_type → extension (without dot)
_MEDIA_TO_EXT: dict[str, str] = {
    v: k.lstrip(".") for k, v in _EXT_TO_MEDIA_TYPE.items()
}

# Transient HTTP status codes that should trigger a retry
_TRANSIENT_STATUS_CODES = {429, 500, 502, 503, 504}
_MAX_ATTEMPTS = 3
_BASE_BACKOFF = 1.0  # seconds


def _call_api(api_key: str, payload: dict[str, Any]) -> dict[str, Any]:
    """POST to OpenAI Images API. Returns parsed JSON response.

    Raises urllib.error.HTTPError on non-2xx status,
    or other exceptions on network failure.
    """
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OPENAI_IMAGES_URL,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _build_multipart_body(
    fields: dict[str, str],
    images: list[tuple[bytes, str]],
) -> tuple[bytes, str]:
    """Build a multipart/form-data body from text fields and image data.

    Returns (body_bytes, content_type_header).
    Raises ValueError if the images list is empty.
    """
    if not images:
        raise ValueError("images list must contain at least one image")

    boundary = uuid.uuid4().hex
    parts: list[bytes] = []

    for name, value in fields.items():
        parts.append(
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="{name}"\r\n'
            f"\r\n"
            f"{value}\r\n".encode("utf-8")
        )

    for idx, (img_bytes, media_type) in enumerate(images):
        ext = _MEDIA_TO_EXT.get(media_type, "png")
        parts.append(
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="image[]"; filename="ref_{idx}.{ext}"\r\n'
            f"Content-Type: {media_type}\r\n"
            f"\r\n".encode("utf-8")
            + img_bytes
            + b"\r\n"
        )

    parts.append(f"--{boundary}--\r\n".encode("utf-8"))

    body = b"".join(parts)
    content_type = f"multipart/form-data; boundary={boundary}"
    return body, content_type


def _call_edits_api(
    api_key: str,
    fields: dict[str, str],
    images: list[tuple[bytes, str]],
) -> dict[str, Any]:
    """POST to OpenAI Images Edits API with multipart body. Returns parsed JSON.

    Raises urllib.error.HTTPError on non-2xx status,
    or other exceptions on network failure.
    """
    body, content_type = _build_multipart_body(fields, images)
    req = urllib.request.Request(
        OPENAI_EDITS_URL,
        data=body,
        headers={
            "Content-Type": content_type,
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _extract_retry_after(exc: urllib.error.HTTPError) -> Optional[float]:
    """Try to extract Retry-After header value from an HTTPError."""
    header = exc.headers.get("retry-after") if exc.headers else None
    if header is not None:
        try:
            return float(header)
        except (ValueError, TypeError):
            pass
    return None


def _extract_error_message(exc: urllib.error.HTTPError) -> str:
    """Try to parse the error body for a human-readable message."""
    try:
        body = exc.read().decode("utf-8")
        data = json.loads(body)
        if "error" in data and "message" in data["error"]:
            return f"OpenAI API error ({exc.code}): {data['error']['message']}"
    except Exception:
        pass
    return f"OpenAI API error: HTTP {exc.code}"


@register_provider("openai")
class OpenAIProvider:
    """Provider that calls the OpenAI Images API (gpt-image-2).

    Zero dependencies — uses urllib.request from Python stdlib.
    """

    default_model: str = "gpt-image-2"

    # ------------------------------------------------------------------
    # Capability queries
    # ------------------------------------------------------------------

    def supports_reference_images(self) -> bool:
        return True

    def supports_transparency(self) -> bool:
        return False

    def max_batch_concurrency(self) -> int:
        return 5

    # ------------------------------------------------------------------
    # Size / quality helpers
    # ------------------------------------------------------------------

    def resolve_size(self, aspect_ratio: str, quality: str) -> str:
        """Return the 'WxH' string for the given quality/aspect_ratio combo."""
        quality_map = SIZE_MAP.get(quality)
        if quality_map is None:
            raise ValueError(f"Unknown quality '{quality}'")
        size = quality_map.get(aspect_ratio)
        if size is None:
            raise ValueError(f"Unknown aspect_ratio '{aspect_ratio}' for quality '{quality}'")
        return size

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def validate(self, req: GenerateRequest) -> list[str]:
        """Validate the request. Returns list of error strings (empty = ok)."""
        errors = validate_request(req)
        return errors

    # ------------------------------------------------------------------
    # Generation
    # ------------------------------------------------------------------

    def generate(self, req: GenerateRequest) -> GenerateResult:
        """Call the OpenAI Images API and write output files."""
        t0 = time.monotonic()

        # --- pre-flight checks ----------------------------------------
        api_key = resolve_api_key("OPENAI_API_KEY")
        if not api_key:
            return GenerateResult(
                status="error",
                error="OPENAI_API_KEY environment variable is not set",
            )

        errors = self.validate(req)
        if errors:
            return GenerateResult(
                status="error",
                error="; ".join(errors),
            )

        # --- resolve parameters ----------------------------------------
        model = req.model or self.default_model
        use_auto_size = req.aspect_ratio == "auto"
        use_auto_quality = req.quality == "auto"
        size = "auto" if use_auto_size else self.resolve_size(req.aspect_ratio, req.quality)
        api_quality = "auto" if use_auto_quality else QUALITY_MAP[req.quality]
        use_edits = bool(req.reference_images)

        # --- resolve reference images (edits path) --------------------
        resolved_images: list[tuple[bytes, str]] = []
        if use_edits:
            for ref in req.reference_images:
                try:
                    resolved_images.append(resolve_image_input(ref))
                except (FileNotFoundError, ValueError) as exc:
                    return GenerateResult(
                        status="error",
                        error=str(exc),
                        provider="openai",
                        model=model,
                    )

        # --- call API with retry ---------------------------------------
        response_data: Optional[dict[str, Any]] = None
        last_error: Optional[str] = None

        for attempt in range(_MAX_ATTEMPTS):
            try:
                if use_edits:
                    fields: dict[str, str] = {
                        "model": model,
                        "prompt": req.prompt,
                        "n": str(req.n),
                        "output_format": req.output_format,
                    }
                    if not use_auto_size:
                        fields["size"] = size
                    if not use_auto_quality:
                        fields["quality"] = api_quality
                    response_data = _call_edits_api(
                        api_key, fields, resolved_images,
                    )
                else:
                    payload: dict[str, Any] = {
                        "model": model,
                        "prompt": req.prompt,
                        "n": req.n,
                        "output_format": req.output_format,
                    }
                    if not use_auto_size:
                        payload["size"] = size
                    if not use_auto_quality:
                        payload["quality"] = api_quality
                    response_data = _call_api(api_key, payload)
                last_error = None
                break
            except urllib.error.HTTPError as exc:
                if exc.code in _TRANSIENT_STATUS_CODES and attempt < _MAX_ATTEMPTS - 1:
                    wait = _extract_retry_after(exc)
                    if wait is None:
                        wait = _BASE_BACKOFF * (2 ** attempt)
                    print(
                        f"Attempt {attempt + 1}/{_MAX_ATTEMPTS} failed (HTTP {exc.code}); "
                        f"retrying in {wait:.1f}s",
                        file=sys.stderr,
                    )
                    time.sleep(wait)
                    continue
                last_error = _extract_error_message(exc)
                break
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                if attempt < _MAX_ATTEMPTS - 1:
                    wait = _BASE_BACKOFF * (2 ** attempt)
                    print(
                        f"Attempt {attempt + 1}/{_MAX_ATTEMPTS} failed ({type(exc).__name__}); "
                        f"retrying in {wait:.1f}s",
                        file=sys.stderr,
                    )
                    time.sleep(wait)
                    continue
                last_error = f"Network error: {exc}"
                break

        elapsed_ms = int((time.monotonic() - t0) * 1000)

        if last_error or response_data is None:
            return GenerateResult(
                status="error",
                error=last_error or "No response from API",
                provider="openai",
                model=model,
                elapsed_ms=elapsed_ms,
            )

        # --- decode and write files ------------------------------------
        output_path = Path(req.output_path)
        stem = output_path.stem
        suffix = output_path.suffix or f".{req.output_format}"
        parent = output_path.parent

        paths: list[str] = []
        images = response_data.get("data", [])

        if not images:
            return GenerateResult(
                status="error",
                error="API returned no images",
                provider="openai",
                model=model,
                elapsed_ms=elapsed_ms,
            )

        for idx, img_item in enumerate(images):
            b64_str = img_item.get("b64_json", "")
            if not b64_str:
                # Fallback: if response contains URL instead of b64
                url = img_item.get("url", "")
                if url:
                    with urllib.request.urlopen(url, timeout=60) as resp:
                        raw = resp.read()
                else:
                    continue
            else:
                raw = base64.b64decode(b64_str)

            if len(images) == 1:
                dest = output_path
            else:
                dest = parent / f"{stem}-{idx + 1}{suffix}"

            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(raw)
            paths.append(str(dest))

        return GenerateResult(
            status="ok",
            paths=paths,
            size=size,
            provider="openai",
            model=model,
            elapsed_ms=elapsed_ms,
        )
