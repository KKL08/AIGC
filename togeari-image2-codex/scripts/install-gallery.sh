#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
GALLERY_DIR="$PROJECT_ROOT/gallery/evolinkai"
TEMP_DIR=$(mktemp -d)

echo "=== togeari-image2-codex: Installing EvoLinkAI Gallery ==="

if [ -f "$GALLERY_DIR/index.yaml" ]; then
    read -p "Gallery already installed. Reinstall? (y/N) " confirm
    [ "$confirm" = "y" ] || { echo "Skipped."; exit 0; }
fi

echo "Cloning EvoLinkAI repo (shallow)..."
git clone --depth 1 https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts.git "$TEMP_DIR/repo"

echo "Copying data..."
cp "$TEMP_DIR/repo/data/ingested_tweets.json" "$GALLERY_DIR/" 2>/dev/null || true

for category_file in "$TEMP_DIR/repo/cases/"*.md; do
    [ -f "$category_file" ] && cp "$category_file" "$GALLERY_DIR/"
done

echo "Building index..."
python3 "$SCRIPT_DIR/build-evolinkai-index.py" "$GALLERY_DIR"

echo "Cleaning up..."
rm -rf "$TEMP_DIR"

echo "=== Done. Gallery installed to $GALLERY_DIR ==="
echo "Index: $GALLERY_DIR/index.yaml"
echo "Prompts: $GALLERY_DIR/prompts/"
