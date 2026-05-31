#!/usr/bin/env python3
"""Togeari image generation CLI — thin entry point for Agent dispatch.

Reads a JSON request from stdin, delegates to the specified provider,
and outputs a JSON result to stdout. All decision-making (provider choice,
aspect ratio inference, quality selection) is done by the Agent; this script
only validates and executes.

Usage (from Agent via Bash):
    python scripts/togeari-gen.py <<'EOF'
    {"provider": "openai", "prompt": "A cat", "aspect_ratio": "1:1", "quality": "standard", "output": "output/cat.png"}
    EOF
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Ensure scripts/ is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.providers import GenerateRequest, GenerateResult, get_provider, validate_request


def main() -> None:
    # Read JSON from stdin
    try:
        raw = sys.stdin.read()
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        result = GenerateResult(status="error", error=f"Invalid JSON input: {exc}")
        print(result.to_json())
        return

    if not isinstance(data, dict):
        result = GenerateResult(status="error", error="Input must be a JSON object")
        print(result.to_json())
        return

    # Parse request
    try:
        req = GenerateRequest.from_dict(data)
    except KeyError as exc:
        result = GenerateResult(status="error", error=f"Missing required field: {exc}")
        print(result.to_json())
        return

    # Validate common fields
    errors = validate_request(req)
    if errors:
        result = GenerateResult(
            status="error",
            error="; ".join(errors),
            provider=req.provider,
        )
        print(result.to_json())
        return

    # Get provider
    try:
        provider = get_provider(req.provider)
    except ValueError as exc:
        result = GenerateResult(status="error", error=str(exc))
        print(result.to_json())
        return

    # Generate
    result = provider.generate(req)
    # Ensure provider field is always populated for traceability
    if not result.provider:
        result.provider = req.provider
    print(result.to_json())


if __name__ == "__main__":
    main()
