# OpenAI Image Generation (gpt-image-2) — Reference Guide

This document is the authoritative reference for Image2 (gpt-image-2) capabilities, constraints, and prompt craft.
All skills (especially rupa-craft) should read this before composing prompts.

---

## Capabilities & Constraints

### Model

- Model ID: `gpt-image-2` (snapshot: `gpt-image-2-2026-04-21`)
- Natively multimodal LLM — understands text and images, not a diffusion model
- Prompt limit: 32,000 characters (sweet spot ~2,000; longer ≠ better)
- The model internally rewrites prompts for improved performance (`revised_prompt` field)
- Supersedes gpt-image-1 as the recommended production model

### Endpoints

| Endpoint | Purpose |
|----------|---------|
| `POST /v1/images/generations` | Text-to-image generation (text prompt only, no image input) |
| `POST /v1/images/edits` | Image-guided generation, editing, inpainting, restyle. Accepts up to 16 reference images via multipart/form-data. When used without a mask, references guide new generation rather than editing. |

### Parameters

| Parameter | Values | Default |
|-----------|--------|---------|
| `size` | **Any `WIDTHxHEIGHT`** where both are multiples of 16, ratio between 1:3 and 3:1, max edge 3840px on either side. Common: `1024x1024`, `1536x1024`, `1024x1536` | `auto` |
| `quality` | `low`, `medium`, `high`, `auto` | `auto` |
| `n` | 1–10 | 1 |
| `output_format` | `png`, `jpeg`, `webp` | `png` |
| `output_compression` | 0–100% (webp/jpeg only) | 100 |
| `moderation` | `auto`, `low` | `auto` |

**Note:** gpt-image-2 does NOT support `background: "transparent"`. Transparent backgrounds are not available — use post-processing or compositing for transparency needs.

### What Image2 Can Do

- **Text rendering**: Significantly better than gpt-image-1, especially for multilingual text. Still imperfect for precise placement.
- **Multi-image input**: Accepts up to 16 reference images via the **edits endpoint** (`/v1/images/edits`, multipart/form-data). Always processed at high fidelity. When used without a mask, reference images guide new generation (not editing). The generations endpoint (`/v1/images/generations`) is text-only and does not accept image input.
- **Arbitrary resolutions**: Any WxH where both edges are multiples of 16, max edge 3840px on either side. Sweet spot ≤2560×1440.
- **Inpainting**: Supply mask (transparent PNG) to regenerate specific regions. Masks are approximate guidance, not pixel-perfect.
- **Full restyle**: Submit source image + new prompt without mask to transform entire image.
- **Stronger instruction-following**: Better at layouts, diagrams, structured compositions, and editing compared to gpt-image-1.
- **World knowledge**: Can infer historical/cultural context from place + date cues (e.g., "Bethel, NY, August 1969" triggers Woodstock-accurate period detail).

### Known Limitations

- **No transparent backgrounds.** This is a regression from gpt-image-1.
- No deterministic seed or reproducibility guarantee.
- Complex text layouts (multiple blocks, specific positions) may still not render exactly as specified.
- Brand logos, specific character designs, real landmarks are more accurate with reference images. Without references, use detailed visual descriptions (colors, shapes, distinctive features) alongside entity names to maximize accuracy.
- Character/brand consistency across multiple generations is unreliable.
- Precise layout/composition control is a weak point — the model has difficulty placing elements exactly.
- Latency: complex prompts can take up to 2 minutes.

---

## Prompt Craft Guide

### Prompt Structure

Order: **background/scene → subject → key details → constraints**. Use line breaks for skimmable segments.

More specifically, build in layers:
1. Subject definition — who/what is in the image
2. Style and medium — artistic style, rendering technique
3. Clothing/pose/material — subject appearance details
4. Environment/background — setting, context
5. Lighting and camera — lighting setup, angle, lens (interpreted as mood hints, not physically simulated)
6. Mood/atmosphere — emotional tone, color palette
7. Text elements — exact content, font, size, position, color
8. Technical specs — aspect ratio, quality level
9. Negative constraints — what to avoid

State the intended use case (ad, UI mock, infographic) upfront — it shifts the model's polish level and framing.

Use action-oriented language: prefer "draw," "edit," "create" over vague "combine," "merge."

### Text-in-Image

- Always specify **exact text content**, repeating it for accuracy.
- Put copy in **quotes or ALL CAPS** for better rendering.
- For difficult words, **spell out letter-by-letter** (e.g., "S-C-H-W-A-R-Z-K-O-P-F").
- Specify font style, size, color, placement as explicit constraints.
- Use `quality: "medium"` or `"high"` for small text, dense panels, or multi-font layouts.
- gpt-image-2 handles multilingual text better than gpt-image-1, but plan for errors — iterative refinement is often needed.

### Reference Images

- **Endpoint:** Reference images are passed via `/v1/images/edits` (multipart/form-data), NOT `/v1/images/generations`. Omit the mask to use references for guided generation rather than inpainting.
- All input images are always processed at high fidelity (no parameter needed).
- Multiple images can synthesize new compositions — index and describe each ("Image 1: product photo... Image 2: style reference").
- Give explicit compositing instructions ("apply Image 2's style to Image 1").
- Explicitly state what to preserve (identity, style, composition) and what to change.
- **Identity preservation:** When a reference image is passed to the API, use short identity-locking language ("Use the person in the reference as the same identity. Do not redesign.") instead of long appearance descriptions. Long descriptions cause the model to synthesize a new similar-looking subject rather than preserving the reference.

### Edit Constraints (critical)

- Always state both "change only X" AND "keep everything else the same."
- Enumerate invariants explicitly (identity, geometry, layout, brand elements, saturation, contrast).
- **Restate the preserve list on every iteration** — omitting it causes drift.

### Character Consistency

- Describe identity-locking details: face shape, hairstyle, skin tone, distinguishing features.
- For multi-page consistency, create a character anchor first, then repeat locked attributes on every subsequent prompt ("Same green tunic, Same facial features... Do not redesign").

### Negative Constraints

- Include explicit avoidance to suppress AI artifacts (extra fingers, plastic skin, warped text, watermarks).
- Use professional vocabulary: "no over-smoothed skin," "no stiff pose," "no artificial symmetry."

### Domain-Specific Patterns

- **Ads/marketing**: Write prompts as **creative briefs** (brand positioning, audience, concept, exact copy), not lists of technical parameters. Let the model make taste decisions within boundaries.
- **UI mockups**: Describe the product "as if it already exists" — shipped-app look, not concept art language.
- **Product photography**: Focus on edge quality — crisp silhouette, no fringing/halos, preserved label text.
- **Virtual try-on**: Lock the person (face, body, pose, hair), allow changes only to garments, require realistic draping/folds/occlusion.
- **Photography**: Use professional terms (focal length, aperture, lighting setups) as mood/composition guidance. Camera specs are interpreted loosely, not physically simulated.

### Resolution Tips

- gpt-image-2 supports arbitrary resolutions (multiples of 16, max 3:1 ratio, max edge 3840px on either side).
- Sweet spot: ≤2560×1440 for reliability. Above that is experimental.
- Square (1024×1024) generates fastest. Start with `quality: "low"` for iteration, escalate for final.

### Iteration Strategy

- Start clean, then make single-change follow-ups.
- Use context references ("same style as before") but re-specify critical details if drift occurs.
- Start with lower quality/resolution for rapid iteration, then increase for final output.

---

## API Layer Parameters

When the API generation path is active (via `scripts/togeari-gen.py`), the following parameters control generation. These are set by the Producer based on user intent — Rupa does not need to consider them when composing prompts.

### Aspect Ratios

Supported: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`

### Quality Presets

| Preset | OpenAI quality | Pixel class | Use case |
|--------|---------------|-------------|----------|
| `preview` | low | 1024px | Quick previews, iteration, Step 5 |
| `standard` | medium | 1536-2048px | Daily output, most use cases |
| `high` | high | 2048-3840px | Print, 4K, final delivery |

### Output Formats

`png` (default), `jpeg`, `webp`

### Common Platform Sizes

| Platform | Recommended | aspect_ratio | quality |
|----------|------------|-------------|---------|
| 手机壁纸 | 1080×1920 equiv | 9:16 | standard |
| 公众号封面 | 2048×1024 equiv | 16:9 | standard |
| 小红书 | 1080×1440 equiv | 3:4 | standard |
| Instagram Story | 1080×1920 equiv | 9:16 | standard |
| Instagram Post | 1080×1080 equiv | 1:1 | standard |
| 海报竖版 | 1152×2048 equiv | 9:16 | standard |
| Banner 横版 | 2048×1152 equiv | 16:9 | standard |
