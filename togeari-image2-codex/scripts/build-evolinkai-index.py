#!/usr/bin/env python3
"""Parse EvoLinkAI case files into a YAML index + organized prompt files."""

import json
import os
import re
import sys


def parse_case_file(filepath):
    """Parse a category .md file into individual cases.

    Real format:
    ### Case N: [Title](url) (by [@Author](url))
    ...
    **Prompt:**
    ```
    prompt text here
    ```
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    cases = []
    # Split on case headers: ### Case N:
    sections = re.split(r'(?=^###\s+Case\s+\d+)', content, flags=re.MULTILINE)

    for section in sections:
        if not section.strip():
            continue

        # Match: ### Case N: [Title](url) (by [@Author](url))
        header_match = re.match(
            r'^###\s+Case\s+(\d+):\s*\[([^\]]+)\]\([^)]*\)\s*\(by\s*\[@?([^\]]+)\]\([^)]*\)\)',
            section
        )
        if not header_match:
            # Try simpler header format
            header_match = re.match(
                r'^###\s+Case\s+(\d+):\s*(.+?)(?:\(by\s*\[@?([^\]]+)\])?',
                section
            )
            if not header_match:
                continue

        case_num = header_match.group(1)
        title = header_match.group(2).strip()
        author = header_match.group(3).strip() if header_match.group(3) else "unknown"

        # Clean title: remove markdown link syntax if still present
        title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', title)
        title = title.strip().rstrip(')')

        # Extract prompt from code block after **Prompt:**
        prompt_match = re.search(
            r'\*\*Prompt:\*\*\s*\n\s*```(?:\w*)\n(.*?)```',
            section, re.DOTALL
        )
        if not prompt_match:
            # Try alternative: just find any code block
            prompt_match = re.search(r'```(?:\w*)\n(.*?)```', section, re.DOTALL)

        prompt_text = prompt_match.group(1).strip() if prompt_match else ""

        if not prompt_text:
            continue

        # Clean summary
        summary = title
        summary = re.sub(r'[*_`#]', '', summary).strip()

        cases.append({
            "case_num": case_num,
            "title": title,
            "author": author,
            "summary": summary,
            "prompt": prompt_text,
        })

    return cases


def main():
    gallery_dir = sys.argv[1] if len(sys.argv) > 1 else "gallery/evolinkai"

    categories = [
        "ecommerce", "portrait", "poster", "character",
        "ui", "ad-creative", "comparison"
    ]

    index_entries = []
    prompts_dir = os.path.join(gallery_dir, "prompts")

    # Load JSON data for enrichment
    json_path = os.path.join(gallery_dir, "ingested_tweets.json")
    json_data = {}
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            try:
                raw = json.load(f)
                if isinstance(raw, list):
                    for item in raw:
                        key = item.get("title", "")
                        if key:
                            json_data[key] = item
            except json.JSONDecodeError:
                pass

    for cat in categories:
        # Find the English case file (exact match, not localized variants)
        cat_file = os.path.join(gallery_dir, f"{cat}.md")
        if not os.path.exists(cat_file):
            # Try fuzzy match
            for fname in os.listdir(gallery_dir):
                if fname.endswith(".md") and fname.startswith(cat) and "_" not in fname:
                    cat_file = os.path.join(gallery_dir, fname)
                    break

        if not os.path.exists(cat_file):
            print(f"Warning: No case file found for category '{cat}', skipping.")
            continue

        cases = parse_case_file(cat_file)
        print(f"  {cat}: parsed {len(cases)} cases from {os.path.basename(cat_file)}")

        cat_prompt_dir = os.path.join(prompts_dir, cat)
        os.makedirs(cat_prompt_dir, exist_ok=True)

        for i, case in enumerate(cases, 1):
            case_id = f"{cat}_case{i}"
            prompt_filename = f"case{i}.md"
            prompt_filepath = os.path.join(cat_prompt_dir, prompt_filename)

            with open(prompt_filepath, "w", encoding="utf-8") as f:
                f.write(f"# {case['title']}\n\n")
                f.write(f"**Author:** {case['author']}\n")
                f.write(f"**Category:** {cat}\n")
                f.write(f"**Original Case:** {case['case_num']}\n\n")
                f.write(f"## Prompt\n\n{case['prompt']}\n")

            summary = case["summary"]
            if case["title"] in json_data:
                json_item = json_data[case["title"]]
                if "title" in json_item and json_item["title"]:
                    summary = json_item["title"]

            style_keywords = [
                "photography", "illustration", "3d render", "pixel art",
                "watercolor", "oil painting", "anime", "minimalist",
                "cinematic", "sketch", "ink", "retro", "cyberpunk",
                "isometric", "flat design", "chibi", "realistic",
            ]
            style_tags = [s for s in style_keywords
                          if s in case["prompt"].lower()]

            index_entries.append({
                "id": case_id,
                "category": cat,
                "author": case["author"],
                "style_tags": style_tags,
                "summary": summary,
                "file": f"prompts/{cat}/{prompt_filename}",
            })

    # Write YAML index
    index_path = os.path.join(gallery_dir, "index.yaml")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("# EvoLinkAI Prompt Gallery Index\n")
        f.write(f"# Total entries: {len(index_entries)}\n")
        f.write("# Each entry: id, category, author, style_tags, summary (from original repo), file path\n\n")
        for entry in index_entries:
            f.write(f"- id: {entry['id']}\n")
            f.write(f"  category: {entry['category']}\n")
            f.write(f"  author: \"{entry['author']}\"\n")
            tags_str = ", ".join(entry.get('style_tags', []))
            f.write(f"  style_tags: [{tags_str}]\n")
            safe_summary = entry['summary'].replace('"', '\\"')
            f.write(f"  summary: \"{safe_summary}\"\n")
            f.write(f"  file: {entry['file']}\n\n")

    print(f"Index written: {index_path} ({len(index_entries)} entries)")
    print(f"Prompt files written to: {prompts_dir}/")


if __name__ == "__main__":
    main()
