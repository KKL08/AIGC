"""Tests for togeari-gen.py CLI entry point."""

import base64
import json
import subprocess
import sys
import os

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "scripts", "togeari-gen.py")


def run_gen(input_data, env=None) -> dict:
    """Run togeari-gen.py with JSON input, return parsed output."""
    inp = json.dumps(input_data) if isinstance(input_data, dict) else input_data
    result = subprocess.run(
        [sys.executable, SCRIPT],
        input=inp,
        capture_output=True,
        text=True,
        timeout=10,
        env=env,
    )
    return json.loads(result.stdout)


class TestCLIParsing:
    def test_missing_prompt_returns_error(self):
        out = run_gen({"provider": "openai"})
        assert out["status"] == "error"
        assert "prompt" in out["error"].lower() or "prompt" in out["error"]

    def test_unknown_provider_returns_error(self):
        out = run_gen({"provider": "nonexistent", "prompt": "A cat"})
        assert out["status"] == "error"
        assert "nonexistent" in out["error"]

    def test_invalid_json_returns_error(self):
        out = run_gen("this is not json")
        assert out["status"] == "error"
        assert "json" in out["error"].lower()

    def test_invalid_aspect_ratio_returns_error(self):
        out = run_gen({"provider": "openai", "prompt": "A cat", "aspect_ratio": "7:3"})
        assert out["status"] == "error"
        assert "aspect_ratio" in out["error"]

    def test_valid_request_without_api_key_returns_key_error(self):
        env = os.environ.copy()
        env.pop("OPENAI_API_KEY", None)
        env["TOGEARI_DOTENV_PATH"] = "/nonexistent/.env"
        out = run_gen({"provider": "openai", "prompt": "A cat"}, env=env)
        assert out["status"] == "error"
        assert "OPENAI_API_KEY" in out["error"]

    def test_defaults_applied(self):
        env = os.environ.copy()
        env.pop("OPENAI_API_KEY", None)
        env["TOGEARI_DOTENV_PATH"] = "/nonexistent/.env"
        out = run_gen({"prompt": "A cat"}, env=env)
        assert out["status"] == "error"
        assert "OPENAI_API_KEY" in out["error"]
        assert out.get("provider", "") == "openai"

    def test_reference_images_invalid_path_returns_error(self):
        env = os.environ.copy()
        env["OPENAI_API_KEY"] = "sk-test"
        env["TOGEARI_DOTENV_PATH"] = "/nonexistent/.env"
        out = run_gen(
            {"prompt": "A cat", "reference_images": ["/nonexistent/ref.png"]},
            env=env,
        )
        assert out["status"] == "error"
        assert "not found" in out["error"].lower()

    def test_reference_images_data_uri_accepted(self):
        png_stub = b"\x89PNG\r\n\x1a\n" + b"\x00" * 100
        uri = "data:image/png;base64," + base64.b64encode(png_stub).decode()
        env = os.environ.copy()
        env.pop("OPENAI_API_KEY", None)
        env["TOGEARI_DOTENV_PATH"] = "/nonexistent/.env"
        out = run_gen(
            {"prompt": "A cat", "reference_images": [uri]},
            env=env,
        )
        assert out["status"] == "error"
        assert "OPENAI_API_KEY" in out["error"]

    def test_too_many_reference_images_returns_error(self):
        out = run_gen({"prompt": "A cat", "reference_images": ["img.png"] * 17})
        assert out["status"] == "error"
        assert "16" in out["error"]
