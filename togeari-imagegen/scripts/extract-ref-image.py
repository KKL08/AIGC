#!/usr/bin/env python3
"""Extract the most recent user-provided image from the session transcript.

Supports both Claude Code and Codex transcript formats. Designed to be called
by the Agent when a user pastes/drops an image in conversation and the Agent
needs a file path to pass to the generation script.

Usage:
    python3 scripts/extract-ref-image.py [--output DIR] [--index N]

    --output DIR   Directory to save extracted image (default: output/)
    --index N      0 = most recent image, 1 = second most recent, etc. (default: 0)

Output (JSON to stdout):
    {"status": "ok", "path": "output/ref-abc123.png", "media_type": "image/png", "size": 12345, "total_images": 3}
    {"status": "error", "error": "No images found in session transcript", "total_images": 0}
"""

from __future__ import annotations

import base64
import hashlib
import json
import sys
from pathlib import Path
from typing import Optional


def _find_claude_code_transcript() -> Optional[Path]:
    """Find the most recently modified Claude Code session transcript."""
    projects_dir = Path.home() / ".claude" / "projects"
    if not projects_dir.is_dir():
        return None

    # Find project dirs, then find most recent JSONL
    best: Optional[Path] = None
    best_mtime: float = 0

    for project_dir in projects_dir.iterdir():
        if not project_dir.is_dir():
            continue
        for f in project_dir.glob("*.jsonl"):
            mt = f.stat().st_mtime
            if mt > best_mtime:
                best = f
                best_mtime = mt

    return best


def _find_codex_transcript() -> Optional[Path]:
    """Find the most recently modified Codex session transcript."""
    sessions_dir = Path.home() / ".codex" / "sessions"
    if not sessions_dir.is_dir():
        return None

    best: Optional[Path] = None
    best_mtime: float = 0

    for f in sessions_dir.rglob("rollout-*.jsonl"):
        mt = f.stat().st_mtime
        if mt > best_mtime:
            best = f
            best_mtime = mt

    return best


def _extract_images_claude_code(transcript: Path) -> list[dict]:
    """Extract user-provided images from a Claude Code transcript.

    Format: {"type":"image","source":{"type":"base64","media_type":"image/png","data":"..."}}
    """
    images = []
    with open(transcript, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Quick filter before expensive JSON parse
            if '"type":"image"' not in line and '"type": "image"' not in line:
                continue
            try:
                obj = json.loads(line)
                # Only extract from user messages (role == "human" or "user")
                msg = obj.get("message", {})
                role = msg.get("role", "")
                if role not in ("human", "user"):
                    continue
                content = msg.get("content", [])
                if not isinstance(content, list):
                    continue
                for block in content:
                    if not isinstance(block, dict) or block.get("type") != "image":
                        continue
                    source = block.get("source", {})
                    if source.get("type") == "base64" and source.get("data"):
                        images.append({
                            "data": source["data"],
                            "media_type": source.get("media_type", "image/png"),
                        })
            except (json.JSONDecodeError, KeyError):
                continue
    return images


def _extract_images_codex(transcript: Path) -> list[dict]:
    """Extract user-provided images from a Codex transcript.

    Format: {"type":"input_image","image_url":"data:image/jpeg;base64,..."}
    """
    images = []
    with open(transcript, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if '"type":"input_image"' not in line and '"type": "input_image"' not in line:
                continue
            try:
                obj = json.loads(line)
                # Walk the structure to find input_image blocks
                _walk_for_input_images(obj, images)
            except (json.JSONDecodeError, KeyError):
                continue
    return images


def _walk_for_input_images(obj, images: list[dict]):
    """Recursively walk a JSON structure to find input_image blocks."""
    if isinstance(obj, dict):
        if obj.get("type") in ("input_image",):
            image_url = obj.get("image_url", "")
            if image_url.startswith("data:"):
                # Parse data URI: data:image/jpeg;base64,...
                try:
                    header, data = image_url.split(",", 1)
                    media_type = header.split(":")[1].split(";")[0]
                    images.append({"data": data, "media_type": media_type})
                except (ValueError, IndexError):
                    pass
        else:
            for v in obj.values():
                _walk_for_input_images(v, images)
    elif isinstance(obj, list):
        for item in obj:
            _walk_for_input_images(item, images)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Extract reference image from session transcript")
    parser.add_argument("--output", default="workspace/refs", help="Output directory for extracted reference images")
    parser.add_argument("--index", type=int, default=0, help="0=most recent, 1=second most recent")
    args = parser.parse_args()

    # Try Claude Code first, then Codex
    images: list[dict] = []
    platform = "unknown"

    claude_transcript = _find_claude_code_transcript()
    if claude_transcript:
        images = _extract_images_claude_code(claude_transcript)
        platform = "claude-code"

    if not images:
        codex_transcript = _find_codex_transcript()
        if codex_transcript:
            images = _extract_images_codex(codex_transcript)
            platform = "codex"

    if not images:
        print(json.dumps({
            "status": "error",
            "error": "No user-provided images found in session transcript",
            "total_images": 0,
        }))
        return

    # Select the requested image (from the end = most recent)
    if args.index >= len(images):
        print(json.dumps({
            "status": "error",
            "error": f"Requested index {args.index} but only {len(images)} images found",
            "total_images": len(images),
        }))
        return

    selected = images[-(args.index + 1)]  # -1 = last (most recent), -2 = second to last

    # Decode and save
    try:
        raw = base64.b64decode(selected["data"], validate=True)
    except Exception as exc:
        print(json.dumps({
            "status": "error",
            "error": f"Failed to decode image data: {exc}",
            "total_images": len(images),
        }))
        return

    media_type = selected["media_type"]
    ext = {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp"}.get(media_type, ".png")

    # Use content hash for filename (dedup + stable naming)
    content_hash = hashlib.md5(raw).hexdigest()[:8]
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"ref-{content_hash}{ext}"
    out_path.write_bytes(raw)

    print(json.dumps({
        "status": "ok",
        "path": str(out_path),
        "media_type": media_type,
        "size": len(raw),
        "total_images": len(images),
        "platform": platform,
    }))


if __name__ == "__main__":
    main()
