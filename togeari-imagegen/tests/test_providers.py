"""Unit tests for the provider API layer."""

from __future__ import annotations

import sys
import os
from pathlib import Path

# Ensure the scripts package is importable when running from any CWD
_PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

import pytest

import base64

from scripts.providers import (
    GenerateRequest,
    resolve_api_key,
    resolve_image_input,
    validate_request,
    ALLOWED_ASPECT_RATIOS,
    ALLOWED_QUALITIES,
)
import scripts.providers as prov
from scripts.providers.openai_api import SIZE_MAP, OpenAIProvider, _build_multipart_body


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_req(**kwargs) -> GenerateRequest:
    defaults = dict(
        prompt="a test image",
        provider="openai",
        aspect_ratio="1:1",
        quality="standard",
        output_format="png",
        output_path="output/image.png",
        n=1,
    )
    defaults.update(kwargs)
    return GenerateRequest(**defaults)


def _parse_size(size_str: str) -> tuple[int, int]:
    w, h = size_str.split("x")
    return int(w), int(h)


# ---------------------------------------------------------------------------
# validate_request tests
# ---------------------------------------------------------------------------

class TestValidateRequest:
    def test_valid_request_returns_no_errors(self):
        req = _make_req()
        assert validate_request(req) == []

    def test_empty_prompt_returns_error(self):
        req = _make_req(prompt="")
        errors = validate_request(req)
        assert any("prompt" in e for e in errors)

    def test_whitespace_only_prompt_returns_error(self):
        req = _make_req(prompt="   ")
        errors = validate_request(req)
        assert any("prompt" in e for e in errors)

    def test_invalid_aspect_ratio_returns_error(self):
        req = _make_req(aspect_ratio="5:3")
        errors = validate_request(req)
        assert any("aspect_ratio" in e for e in errors)

    def test_invalid_quality_returns_error(self):
        req = _make_req(quality="ultra")
        errors = validate_request(req)
        assert any("quality" in e for e in errors)

    def test_invalid_format_returns_error(self):
        req = _make_req(output_format="gif")
        errors = validate_request(req)
        assert any("output_format" in e for e in errors)

    def test_n_zero_returns_error(self):
        req = _make_req(n=0)
        errors = validate_request(req)
        assert any("n" in e for e in errors)

    def test_n_eleven_returns_error(self):
        req = _make_req(n=11)
        errors = validate_request(req)
        assert any("n" in e for e in errors)

    def test_n_ten_is_valid(self):
        req = _make_req(n=10)
        assert validate_request(req) == []

    def test_n_one_is_valid(self):
        req = _make_req(n=1)
        assert validate_request(req) == []

    def test_multiple_errors_returned(self):
        req = _make_req(prompt="", aspect_ratio="bad", quality="bad")
        errors = validate_request(req)
        assert len(errors) >= 3

    def test_too_many_reference_images_returns_error(self):
        req = _make_req(reference_images=[f"img{i}.png" for i in range(17)])
        errors = validate_request(req)
        assert any("16" in e for e in errors)

    def test_16_reference_images_is_valid(self):
        req = _make_req(reference_images=[f"img{i}.png" for i in range(16)])
        errors = validate_request(req)
        # No reference-image-related errors
        assert not any("reference" in e.lower() for e in errors)

    def test_empty_reference_image_entry_returns_error(self):
        req = _make_req(reference_images=["good.png", ""])
        errors = validate_request(req)
        assert any("reference_images[1]" in e for e in errors)


# ---------------------------------------------------------------------------
# resolve_image_input tests
# ---------------------------------------------------------------------------

class TestResolveImageInput:
    def test_file_path_resolves_to_bytes(self, tmp_path):
        # PNG magic bytes: 89 50 4E 47 0D 0A 1A 0A
        png_magic = b"\x89PNG\r\n\x1a\n" + b"\x00" * 32
        img = tmp_path / "test.png"
        img.write_bytes(png_magic)
        data, media_type = resolve_image_input(str(img))
        assert data[:8] == b"\x89PNG\r\n\x1a\n"
        assert media_type == "image/png"

    def test_jpeg_file_path_detects_media_type(self, tmp_path):
        jpeg_magic = b"\xff\xd8\xff\xe0" + b"\x00" * 32
        img = tmp_path / "photo.jpg"
        img.write_bytes(jpeg_magic)
        data, media_type = resolve_image_input(str(img))
        assert media_type == "image/jpeg"

    def test_webp_file_path_detects_media_type(self, tmp_path):
        # RIFF....WEBP header
        webp_data = b"RIFF" + b"\x00\x00\x00\x00" + b"WEBP" + b"\x00" * 20
        img = tmp_path / "photo.webp"
        img.write_bytes(webp_data)
        data, media_type = resolve_image_input(str(img))
        assert media_type == "image/webp"

    def test_data_uri_resolves_to_bytes(self):
        raw = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16
        encoded = base64.b64encode(raw).decode()
        uri = f"data:image/png;base64,{encoded}"
        data, media_type = resolve_image_input(uri)
        assert data == raw
        assert media_type == "image/png"

    def test_data_uri_jpeg(self):
        raw = b"\xff\xd8\xff\xe0" + b"\x00" * 16
        encoded = base64.b64encode(raw).decode()
        uri = f"data:image/jpeg;base64,{encoded}"
        data, media_type = resolve_image_input(uri)
        assert data == raw
        assert media_type == "image/jpeg"

    def test_nonexistent_file_raises(self):
        with pytest.raises(FileNotFoundError):
            resolve_image_input("/tmp/nonexistent_image_12345.png")

    def test_invalid_data_uri_raises(self):
        uri = "data:text/plain;base64,aGVsbG8="
        with pytest.raises(ValueError, match="data URI"):
            resolve_image_input(uri)

    def test_empty_string_raises(self):
        with pytest.raises(ValueError):
            resolve_image_input("")


# ---------------------------------------------------------------------------
# OpenAIProvider.resolve_size spot checks
# ---------------------------------------------------------------------------

class TestOpenAIProviderResolveSize:
    def setup_method(self):
        self.provider = OpenAIProvider()

    def test_preview_1_1(self):
        assert self.provider.resolve_size("1:1", "preview") == "1024x1024"

    def test_standard_16_9(self):
        assert self.provider.resolve_size("16:9", "standard") == "2048x1152"

    def test_high_9_16(self):
        assert self.provider.resolve_size("9:16", "high") == "2160x3840"

    def test_high_1_1(self):
        assert self.provider.resolve_size("1:1", "high") == "2048x2048"

    def test_standard_4_3(self):
        assert self.provider.resolve_size("4:3", "standard") == "1536x1152"

    def test_unknown_quality_raises(self):
        with pytest.raises(ValueError, match="quality"):
            self.provider.resolve_size("1:1", "ultra")

    def test_unknown_ratio_raises(self):
        with pytest.raises(ValueError, match="aspect_ratio"):
            self.provider.resolve_size("5:3", "standard")


# ---------------------------------------------------------------------------
# SIZE_MAP constraint tests (parameterised over all entries)
# ---------------------------------------------------------------------------

_ALL_SIZES = [
    (quality, ratio, size_str)
    for quality, ratio_map in SIZE_MAP.items()
    for ratio, size_str in ratio_map.items()
]


class TestSizeMapConstraints:
    @pytest.mark.parametrize("quality,ratio,size_str", _ALL_SIZES)
    def test_dimensions_are_multiples_of_16(self, quality, ratio, size_str):
        w, h = _parse_size(size_str)
        assert w % 16 == 0, f"{quality}/{ratio}: width {w} is not a multiple of 16"
        assert h % 16 == 0, f"{quality}/{ratio}: height {h} is not a multiple of 16"

    @pytest.mark.parametrize("quality,ratio,size_str", _ALL_SIZES)
    def test_pixel_count_within_bounds(self, quality, ratio, size_str):
        w, h = _parse_size(size_str)
        px = w * h
        assert px >= 655_360, f"{quality}/{ratio}: {px} px below minimum 655,360"
        assert px <= 8_294_400, f"{quality}/{ratio}: {px} px above maximum 8,294,400"

    @pytest.mark.parametrize("quality,ratio,size_str", _ALL_SIZES)
    def test_max_edge_at_most_3840(self, quality, ratio, size_str):
        w, h = _parse_size(size_str)
        assert max(w, h) <= 3840, f"{quality}/{ratio}: max edge {max(w, h)} > 3840"

    @pytest.mark.parametrize("quality,ratio,size_str", _ALL_SIZES)
    def test_aspect_ratio_at_most_3_to_1(self, quality, ratio, size_str):
        w, h = _parse_size(size_str)
        long_edge = max(w, h)
        short_edge = min(w, h)
        assert long_edge / short_edge <= 3.0 + 1e-9, (
            f"{quality}/{ratio}: ratio {long_edge}/{short_edge} > 3:1"
        )

    def test_all_quality_tiers_present(self):
        assert set(SIZE_MAP.keys()) == {"preview", "standard", "high"}

    def test_all_aspect_ratios_present_in_each_tier(self):
        concrete_ratios = ALLOWED_ASPECT_RATIOS - {"auto"}
        for quality in ("preview", "standard", "high"):
            assert set(SIZE_MAP[quality].keys()) == concrete_ratios, (
                f"Missing ratios in '{quality}'"
            )


# ---------------------------------------------------------------------------
# OpenAIProvider capability & metadata tests
# ---------------------------------------------------------------------------

class TestOpenAIProviderCapabilities:
    def setup_method(self):
        self.provider = OpenAIProvider()

    def test_supports_reference_images(self):
        assert self.provider.supports_reference_images() is True

    def test_supports_transparency(self):
        assert self.provider.supports_transparency() is False

    def test_max_batch_concurrency(self):
        assert self.provider.max_batch_concurrency() == 5

    def test_default_model(self):
        assert self.provider.default_model == "gpt-image-2"

    def test_validate_accepts_valid_request(self):
        req = _make_req()
        assert self.provider.validate(req) == []

    def test_validate_rejects_bad_quality(self):
        req = _make_req(quality="ultra")
        errors = self.provider.validate(req)
        assert len(errors) > 0

    def test_generate_returns_error_without_api_key(self, monkeypatch):
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        # Isolate from real ~/.togeari/.env
        import scripts.providers as prov
        monkeypatch.setattr(prov, "_DOTENV_PATH", Path("/nonexistent/.env"))
        prov._dotenv_cache = None
        req = _make_req()
        result = self.provider.generate(req)
        assert result.status == "error"
        assert "OPENAI_API_KEY" in (result.error or "")


# ---------------------------------------------------------------------------
# resolve_api_key tests
# ---------------------------------------------------------------------------

class TestResolveApiKey:
    def test_reads_from_env_var(self, monkeypatch):
        monkeypatch.setenv("TEST_KEY", "sk-from-env")
        assert resolve_api_key("TEST_KEY") == "sk-from-env"

    def test_returns_empty_when_not_found(self, monkeypatch):
        monkeypatch.delenv("NONEXISTENT_KEY_12345", raising=False)
        prov._dotenv_cache = None
        monkeypatch.setattr(prov, "_DOTENV_PATH", Path("/tmp/does-not-exist/.env"))
        assert resolve_api_key("NONEXISTENT_KEY_12345") == ""

    def test_env_var_takes_priority_over_dotenv(self, monkeypatch, tmp_path):
        dotenv = tmp_path / ".env"
        dotenv.write_text("OPENAI_API_KEY=from-dotenv\n")
        prov._dotenv_cache = None
        monkeypatch.setattr(prov, "_DOTENV_PATH", dotenv)
        monkeypatch.setenv("OPENAI_API_KEY", "from-env")
        assert resolve_api_key("OPENAI_API_KEY") == "from-env"

    def test_reads_from_dotenv_fallback(self, monkeypatch, tmp_path):
        monkeypatch.delenv("TOGEARI_TEST_KEY", raising=False)
        dotenv = tmp_path / ".env"
        dotenv.write_text("TOGEARI_TEST_KEY=from-dotenv\n")
        prov._dotenv_cache = None
        monkeypatch.setattr(prov, "_DOTENV_PATH", dotenv)
        assert resolve_api_key("TOGEARI_TEST_KEY") == "from-dotenv"

    def test_dotenv_ignores_comments_and_blanks(self, monkeypatch, tmp_path):
        dotenv = tmp_path / ".env"
        dotenv.write_text(
            "# this is a comment\n"
            "\n"
            "REAL_KEY=real-value\n"
            "  # another comment\n"
            "\n"
        )
        prov._dotenv_cache = None
        monkeypatch.setattr(prov, "_DOTENV_PATH", dotenv)
        monkeypatch.delenv("REAL_KEY", raising=False)
        assert resolve_api_key("REAL_KEY") == "real-value"

    def test_dotenv_strips_quotes(self, monkeypatch, tmp_path):
        dotenv = tmp_path / ".env"
        dotenv.write_text('QUOTED_KEY="sk-abc123"\n')
        prov._dotenv_cache = None
        monkeypatch.setattr(prov, "_DOTENV_PATH", dotenv)
        monkeypatch.delenv("QUOTED_KEY", raising=False)
        assert resolve_api_key("QUOTED_KEY") == "sk-abc123"

    def test_dotenv_strips_single_quotes(self, monkeypatch, tmp_path):
        dotenv = tmp_path / ".env"
        dotenv.write_text("SINGLE_QUOTED='sk-xyz789'\n")
        prov._dotenv_cache = None
        monkeypatch.setattr(prov, "_DOTENV_PATH", dotenv)
        monkeypatch.delenv("SINGLE_QUOTED", raising=False)
        assert resolve_api_key("SINGLE_QUOTED") == "sk-xyz789"


# ---------------------------------------------------------------------------
# _build_multipart_body tests
# ---------------------------------------------------------------------------

class TestBuildMultipartBody:
    def test_builds_valid_multipart_with_one_image(self):
        fields = {"model": "gpt-image-2", "prompt": "a cat"}
        image_bytes = b"\x89PNG\r\n\x1a\n" + b"\x00" * 32
        images = [(image_bytes, "image/png")]
        body, content_type = _build_multipart_body(fields, images)

        assert b"model" in body
        assert b"gpt-image-2" in body
        assert b"prompt" in body
        assert b"a cat" in body
        assert image_bytes in body
        assert "multipart/form-data; boundary=" in content_type

    def test_builds_valid_multipart_with_multiple_images(self):
        fields = {"model": "gpt-image-2", "prompt": "two cats"}
        img1 = b"\x89PNG" + b"\x00" * 16
        img2 = b"\xff\xd8\xff\xe0" + b"\x00" * 16
        images = [(img1, "image/png"), (img2, "image/jpeg")]
        body, content_type = _build_multipart_body(fields, images)

        assert body.count(b'name="image[]"') == 2

    def test_empty_images_list_raises(self):
        fields = {"model": "gpt-image-2", "prompt": "a cat"}
        with pytest.raises(ValueError, match="at least one image"):
            _build_multipart_body(fields, [])


# ---------------------------------------------------------------------------
# OpenAIProvider edits-path routing tests
# ---------------------------------------------------------------------------

class TestOpenAIProviderEditsRouting:
    def setup_method(self):
        self.provider = OpenAIProvider()

    def test_generate_uses_edits_when_reference_images_present(
        self, tmp_path, monkeypatch
    ):
        """With a real image file as reference, the edits path is entered.

        We set a fake API key so the flow proceeds past the key check and
        actually resolves the reference image. The test expects the HTTP
        call to fail (no real API), but confirms image resolution ran.
        """
        # Create a real PNG file
        png = tmp_path / "ref.png"
        png.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 32)

        # Set a fake API key so we get past the key check
        monkeypatch.setenv("OPENAI_API_KEY", "sk-fake-for-test")

        # Mock _call_edits_api to capture the call without hitting the network
        captured = {}

        def fake_call_edits_api(api_key, fields, images):
            captured["fields"] = fields
            captured["images"] = images
            return {"data": []}

        from scripts.providers import openai_api
        monkeypatch.setattr(openai_api, "_call_edits_api", fake_call_edits_api)

        req = _make_req(
            reference_images=[str(png)],
            output_path=str(tmp_path / "out.png"),
        )
        result = self.provider.generate(req)

        # The edits path was taken: _call_edits_api was called with resolved images
        assert "fields" in captured
        assert len(captured["images"]) == 1
        assert captured["fields"]["output_format"] == "png"
        # API returned no images data, so status is error
        assert result.status == "error"
        assert "no images" in (result.error or "").lower()

    def test_generate_returns_error_for_missing_reference_image(
        self, monkeypatch
    ):
        """A nonexistent reference image path causes an immediate error."""
        monkeypatch.setenv("OPENAI_API_KEY", "sk-fake-for-test")

        req = _make_req(
            reference_images=["/tmp/nonexistent_ref_image_999.png"]
        )
        result = self.provider.generate(req)

        assert result.status == "error"
        assert "not found" in (result.error or "").lower()
