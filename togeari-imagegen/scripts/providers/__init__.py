"""Provider interface for togeari image generation API layer."""

from __future__ import annotations

import base64
import json
import os
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


# -- Cross-platform API key resolution ------------------------------------
# Priority: system env (platform-injected) > ~/.togeari/.env (fallback)

_DOTENV_PATH = Path(os.environ.get("TOGEARI_DOTENV_PATH", str(Path.home() / ".togeari" / ".env")))
_dotenv_cache: Optional[dict[str, str]] = None


def _load_dotenv() -> dict[str, str]:
    """Parse ~/.togeari/.env (KEY=value format). Cached after first call."""
    global _dotenv_cache
    if _dotenv_cache is not None:
        return _dotenv_cache
    _dotenv_cache = {}
    if _DOTENV_PATH.is_file():
        for line in _DOTENV_PATH.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip().strip("'\"")
                if key:
                    _dotenv_cache[key] = value
    return _dotenv_cache


def resolve_api_key(env_var: str) -> str:
    """Resolve an API key: system env first, then ~/.togeari/.env fallback."""
    value = os.environ.get(env_var, "").strip()
    if value:
        return value
    return _load_dotenv().get(env_var, "")


@dataclass
class GenerateRequest:
    """Agent passes this to the script as JSON."""
    prompt: str
    provider: str = "openai"
    model: Optional[str] = None
    aspect_ratio: str = "auto"
    quality: str = "auto"
    output_format: str = "jpeg"
    output_path: str = "output/image.jpeg"
    reference_images: list[str] = field(default_factory=list)
    n: int = 1

    @classmethod
    def from_dict(cls, data: dict) -> "GenerateRequest":
        return cls(
            prompt=data["prompt"],
            provider=data.get("provider", "openai"),
            model=data.get("model"),
            aspect_ratio=data.get("aspect_ratio", "auto"),
            quality=data.get("quality", "auto"),
            output_format=data.get("output_format", "jpeg"),
            output_path=data.get("output", "output/image.jpeg"),
            reference_images=data.get("reference_images", []),
            n=data.get("n", 1),
        )


@dataclass
class GenerateResult:
    """Script returns this to the Agent as JSON."""
    status: str  # "ok" | "error"
    paths: list[str] = field(default_factory=list)
    size: str = ""
    provider: str = ""
    model: str = ""
    elapsed_ms: int = 0
    error: Optional[str] = None

    def to_json(self) -> str:
        d = asdict(self)
        if d["error"] is None:
            del d["error"]
        return json.dumps(d, ensure_ascii=False)


ALLOWED_ASPECT_RATIOS = {"auto", "1:1", "16:9", "9:16", "4:3", "3:4", "3:2", "2:3"}
ALLOWED_QUALITIES = {"auto", "preview", "standard", "high"}
ALLOWED_FORMATS = {"png", "jpeg", "webp"}

_EXT_TO_MEDIA_TYPE: dict[str, str] = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
}


def resolve_image_input(value: str) -> tuple[bytes, str]:
    """Resolve a reference image string to (raw_bytes, media_type).

    Accepts two formats:
      - File path: reads the file and detects media type from extension.
      - Data URI: ``data:image/<subtype>;base64,<data>`` — extracts and decodes.
    """
    if not value:
        raise ValueError("reference image value must not be empty")

    # -- Data URI ----------------------------------------------------------
    if value.startswith("data:"):
        # Expected: data:<media_type>;base64,<encoded>
        try:
            header, encoded = value.split(",", 1)
        except ValueError:
            raise ValueError(f"Invalid data URI format: missing comma")
        # header looks like "data:image/png;base64"
        if ";base64" not in header:
            raise ValueError(f"Invalid data URI: expected base64 encoding")
        media_type = header[len("data:"):].split(";")[0]
        if not media_type.startswith("image/"):
            raise ValueError(
                f"Invalid data URI: expected image/* media type, got '{media_type}'"
            )
        try:
            decoded = base64.b64decode(encoded, validate=True)
        except Exception as exc:
            raise ValueError(f"Invalid base64 in data URI: {exc}") from exc
        return decoded, media_type

    # -- File path ---------------------------------------------------------
    p = Path(value)
    if not p.is_file():
        raise FileNotFoundError(f"Reference image file not found: {value}")
    ext = p.suffix.lower()
    media_type = _EXT_TO_MEDIA_TYPE.get(ext)
    if media_type is None:
        raise ValueError(
            f"Unknown image extension '{ext}'. "
            f"Supported: {sorted(_EXT_TO_MEDIA_TYPE.keys())}"
        )
    return p.read_bytes(), media_type


def validate_request(req: GenerateRequest) -> list[str]:
    """Validate common fields. Returns list of error messages (empty = ok)."""
    errors = []
    if not req.prompt or not req.prompt.strip():
        errors.append("prompt is required")
    if req.aspect_ratio not in ALLOWED_ASPECT_RATIOS:
        errors.append(f"aspect_ratio must be one of {sorted(ALLOWED_ASPECT_RATIOS)}")
    if req.quality not in ALLOWED_QUALITIES:
        errors.append(f"quality must be one of {sorted(ALLOWED_QUALITIES)}")
    if req.output_format not in ALLOWED_FORMATS:
        errors.append(f"output_format must be one of {sorted(ALLOWED_FORMATS)}")
    if req.n < 1 or req.n > 10:
        errors.append("n must be between 1 and 10")
    # -- reference_images --------------------------------------------------
    if len(req.reference_images) > 16:
        errors.append("reference_images must have at most 16 entries")
    for i, entry in enumerate(req.reference_images):
        if not isinstance(entry, str) or not entry:
            errors.append(f"reference_images[{i}] must be a non-empty string")
    return errors


# Provider registry
_PROVIDERS: dict[str, type] = {}


def register_provider(name: str):
    """Decorator to register a provider class."""
    def decorator(cls):
        _PROVIDERS[name] = cls
        return cls
    return decorator


def get_provider(name: str):
    """Get a provider instance by name."""
    if name not in _PROVIDERS:
        available = sorted(_PROVIDERS.keys())
        raise ValueError(f"Unknown provider '{name}'. Available: {available}")
    return _PROVIDERS[name]()


# Import provider modules so their @register_provider decorators run
from . import openai_api as _openai_api  # noqa: E402, F401
