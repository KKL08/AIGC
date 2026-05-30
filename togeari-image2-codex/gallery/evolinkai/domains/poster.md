# Poster — 创意方向地图

基于 232 条 EvoLinkAI 验证 prompt 蒸馏。

---

## 方向 1: 旅行目的地插画海报 (约 35 条)

**视觉特征:** 以城市/国家为主题，融合地标建筑、文化符号与排版设计，风格横跨复古丝网印刷、水彩手绘、3D 立体字到等距鸟瞰图。

**关键技巧:**
- 构图/版式: 竖版构图，大面积负空间，城市名称作主视觉锚点；常见模板化 `[CITY NAME]` / `[LANDMARK]` 变量占位
- 色调/光影: 三色限制（cream background + black linework + one accent color），warm golden sunset lighting，soft watercolor washes，antique printing texture
- 排版/文字: bold sans-serif city name at top，Swiss modernist travel poster aesthetic，subtitle in native language，coordinate numbers，small slogan
- 负向约束: no gradients allowed, no cartoonish feel, no cluttered backgrounds

**代表性 prompt (case2):**
> Modern pencil illustration of Vintage travel poster illustration of the Amalfi Coast, Italy, panoramic coastal cliff road scene, classic 1960s white car driving along a curved seaside road, deep blue Mediterranean sea with small sailboats, colorful pastel hillside village, bright blue sky with soft clouds, lemon tree branches with vibrant yellow lemons framing the foreground, warm summer sunlight, bold vibrant colors, retro 1950s travel poster style, cinematic composition, high detail, screen print texture, graphic illustration. Hand-drawn style, illustration with loose strokes and defined contours. High-contrast color palette, maintaining chromatic harmony between background and elements. Contemporary and decorative aesthetic.

**代表性 prompt (case188):**
> Design a vertical retro mid-century travel poster of [CITY NAME] showcasing [LANDMARK]. Stick to a tight 3-color scheme: cream-toned paper background, black technical line drawing, plus one [COLOR] accent. Aesthetic: minimalist isometric top-down aerial perspective with very fine cross-hatching and silkscreen print grain. Color rules: fill the entire sky in flat solid [COLOR], add small [COLOR] touches on rooftops or street details. Zero gradients allowed. Typography: large bold sans-serif "[CITY NAME]" at the top in cream, with the city's name in its native language set smaller in cream beneath it.

**涵盖 case:** 1, 2, 5, 13, 15, 25, 44, 75, 160, 176, 183, 188, 189, 193, 199, 202, 203, 204, 209, 210, 211, 214, 215, 224 及 120-173 区间中约 10 条旅行主题

---

## 方向 2: 美食摄影与食谱信息图海报 (约 25 条)

**视觉特征:** 以食物/饮品为核心主体，分为两个子类型：(a) 高端食品广告（hero shot + 排版），(b) 食谱流程图/信息图式教学海报。

**关键技巧:**
- 构图/版式: hero dish 居中，step-by-step recipe layout，exploded vertical infographic composition，Pinterest/TikTok infographic vibe，clean modern infographic aesthetic
- 色调/光影: warm natural lighting, cream background, high contrast studio lighting, soft shadows, cinematic food photography, shallow depth of field
- 排版/文字: elegant step-by-step recipe layout, stylish infographic sections with rounded boxes and cute minimal icons, bold modern font with fiery texture
- 负向约束: NO order button or app store icons

**代表性 prompt (case57):**
> Create a premium food preparation poster for [ DISH NAME ], with a beautiful hero dish, warm natural lighting, cream background, elegant step-by-step recipe layout, ingredients, cooking process, premium food photography, refined English typography, luxury restaurant advertisement style, clean design, rich colors, highly detailed, visually irresistible, cinematic masterpiece.

**代表性 prompt (case112):**
> A premium fast food advertisement poster with a cinematic composition and a clean white textured background with soft grey shading for depth. At the top center, place a bold, modern logo text: "EMPIRE" with a minimal crown icon above it, sleek and premium typography. Below the logo, add a large, dramatic headline in bold modern font: "NEW EMPIRE INFERNO BURGER" – The word INFERNO should have a fiery texture with flame elements integrated into the typography.

**涵盖 case:** 3, 27, 30, 37, 40, 57, 63, 95, 100, 103, 110, 112, 113, 116, 119, 219, 223, 225, 226 及 120-173 区间中约 6 条美食主题（含 case133, 145 等）

---

## 方向 3: 时尚编辑与品牌大片海报 (约 28 条)

**视觉特征:** 模拟高端时尚杂志封面或品牌 campaign，黑白或单色为主，强调模特姿态、排版层级与奢侈品质感。

**关键技巧:**
- 构图/版式: magazine cover layout with oversized serif masthead, vertical magazine ratio, split composition (typography panel + character scene), 3-panel collage layout
- 色调/光影: black and white cinematic portrait, dramatic studio lighting with soft shadows, high contrast, monochrome aesthetic, premium commercial finish
- 排版/文字: large bold serif title ("VOGUE", "VOID ELITE"), issue date, cover lines, holographic glitch-style label over eyes, oversized distressed font
- 负向约束: minimal color palette, balanced negative space

**代表性 prompt (case97):**
> Ultra-realistic high-fashion magazine cover, black and white cinematic portrait of a confident young female model, slightly messy wet-look hair, sharp jawline, intense gaze, natural glossy lips, wearing a premium black leather trench coat over a minimal outfit. The model is posing slightly tilted forward with attitude, hands adjusting the coat, accessorized with multiple rings, ear piercings, and layered chain necklaces. Lighting is dramatic studio lighting with soft shadows, high contrast, editorial Vogue-style aesthetic, ultra-detailed skin texture, 8K resolution, sharp focus.

**代表性 prompt (case51):**
> Create a premium luxury sportswear campaign poster featuring a confident female athlete in a modern studio environment. Full body pose with strong fashion attitude, standing tall while holding a basketball at her side, chin raised slightly, direct powerful expression. Athletic toned physique, sleek pulled back hair, clean glowing skin, sharp editorial posture. ... Background is a clean light gray studio wall with giant bold condensed black typography reading "POWER" stretched vertically across the backdrop behind the model.

**涵盖 case:** 33, 39, 43, 51, 52, 58, 61, 93, 96, 97, 105, 106, 107, 108, 118, 181, 194, 198, 228, 229, 232 及 120-173 区间中约 7 条时尚主题

---

## 方向 4: 暗黑史诗/电影概念海报 (约 18 条)

**视觉特征:** 模拟好莱坞大片主海报的暗黑仪式感，以单一体积光束切割黑暗空间，核心主体居中被"审判式"光源照亮。

**关键技巧:**
- 构图/版式: 80% 视觉 20% 文字，斜向张力构图，中央偏右核心主体 + 左下角高密度文字锚点，大量纯黑负空间
- 色调/光影: 极深黑暗空间 + 单一强光（Tyndall effect 体积光），cinematic matte painting，高预算 90 年代好莱坞史诗大片气质
- 排版/文字: 主标题沿光束垂直排布，左下角 credits 风格占位文字，署名如正式电影概念海报落款
- 负向约束: 不使用轮廓线/平面化描边，不允许风格污染，不允许多系统互相打架

**代表性 prompt (case31):**
> 围绕【主题】自动生成一张顶级暗黑史诗概念海报 / 电影感信息图海报。... 高预算 90 年代好莱坞史诗大片海报气质,融合 cinematic matte painting、超写实摄影质感、极强明暗对比、厚重空间叙事、暗黑英雄主义与仪式感构图。... 一个巨大、压迫感极强的黑暗封闭空间 / 一束从上方斜向切入的强烈体积光 / 中央偏右或光束终点位置的核心主体与承载结构 / 左下角作为高密度标题与信息锚点

**代表性 prompt (case38):**
> 请围绕【主题】自动生成一张顶级概念海报 / 信息图式电影海报。... 超写实 3D 商业 CGI 渲染,融合电影级布光、奢侈品视觉语言、未来感概念设计与史诗级构图。画面必须具有"唯一主视觉核心"

**涵盖 case:** 14, 23, 26, 29, 31, 38, 46, 47, 48, 53, 82, 99, 177, 185, 216, 218 及部分 120-173 区间

---

## 方向 5: 科普百科信息图海报 (约 22 条)

**视觉特征:** 模块化知识卡片，兼具图鉴感、百科感与信息结构感，面向社交媒体传播的知识型内容。

**关键技巧:**
- 构图/版式: 竖版模块化布局，圆角信息框，局部特征放大细节，可视化评分卡 / Top 5 模块，timeline / staircase 结构
- 色调/光影: 浅色干净背景，柔和配色，轻阴影，精致小图标，信息密度高但不拥挤
- 排版/文字: 清楚的标题层级与重点标签，thin pointer lines with labels，bilingual captions
- 负向约束: 不做成普通商业宣传海报，突出"知识整理 + 模块信息 + 图鉴式展示"

**代表性 prompt (case22):**
> 请根据【主题】生成一张高质量竖版「科普百科图」。这张图不是普通海报,也不是单纯插画,而是一张兼具"图鉴感、百科感、信息结构感、收藏感"的模块化科普信息图。整体风格参考高级博物图鉴、现代百科书页、生活方式知识卡和社交媒体高传播信息图的结合。

**代表性 prompt (case67):**
> {"type":"vintage editorial infographic poster","subject":"Claude Shannon and information theory","style":{"era":"1940s Bell Labs archival poster","look":"aged cream paper, blueprint drafting grid, thin ink linework, muted navy and charcoal printing, subtle stains and paper wear, technical illustration mixed with newspaper editorial design"...}

**涵盖 case:** 16, 22, 36, 38, 64, 67, 88, 95, 101, 115, 179, 221, 227 及 120-173 区间中约 9 条信息图/科普主题

---

## 方向 6: 角色设计/参考图谱 (约 20 条)

**视觉特征:** 多视角/多姿态角色展示，包括 turnaround sheet、pose reference grid、character profile 与概念设定图。

**关键技巧:**
- 构图/版式: grid layout (4x4, 3x2)，multiple poses with consistent outfit and scale，personality board with handwritten notes，full-body turnaround (front, 3/4, profile, rear)
- 色调/光影: clean even studio lighting, plain light gray seamless backdrop, sharp realistic anatomy, consistent distance framing
- 排版/文字: numbered labels in top-left corner of each cell, thin black divider lines, handwritten personality notes, production annotations
- 负向约束: face intentionally blurred or obscured (in some), maintain cohesive theme across all panels

**代表性 prompt (case78):**
> {"type":"pose reference sheet","subject":{"theme":"hip-hop dance and combat-ready movement chart"...},"layout":{"grid":{"rows":4,"columns":4,"count":16},"numbering":{"count":16,"labels":["1"..."16"],"position":"top-left corner of each cell"},"cell_borders":"thin black divider lines between all panels"}...}

**代表性 prompt (case197):**
> A stylish illustrated character profile sheet of a handsome young man sketchbook aesthetic, mixed media ink and watercolor style, highly detailed fashion portrait... The page layout includes multiple poses and close-up portraits, surrounded by handwritten notes, doodles, symbols, travel sketches... Modern concept art meets fashion illustration, dynamic ink strokes, expressive line art, textured watercolor shading, warm paper background, cinematic composition, Pinterest aesthetic

**涵盖 case:** 18, 21, 69, 70, 71, 72, 73, 76, 78, 79, 80, 81, 86, 90, 197, 212, 213, 218, 231 及部分 120-173 区间

---

## 方向 7: 产品广告与科技发布海报 (约 18 条)

**视觉特征:** 以消费电子、奢侈品或汽车为主体，融合产品摄影、UI 信息标注与未来科技感视觉语言。

**关键技巧:**
- 构图/版式: product hero shot with forced perspective, futuristic UI overlays with floating labels, exploded view breakdown, infographic feature callouts with thin glowing connector lines
- 色调/光影: deep cosmic blue space background, soft studio lighting with neutral-to-cool tones, glossy reflections, high-end contrast, automotive studio setup
- 排版/文字: glassmorphism panel listing specs, bold clean headline text, Futuristic UI overlays with thin minimal lines and nodes, premium modernist poster layout
- 负向约束: no humans, no messy text, no watermark, no plastic gloss

**代表性 prompt (case102):**
> Ultra-realistic premium smartphone advertisement, featuring a confident young woman... holding a Xiaomi 17 Pro smartphone toward the camera in a bold hero shot with strong forced perspective... Futuristic UI overlays: thin minimal white/purple lines and nodes pointing to features with floating labels: "Leica Camera System" "Secondary Display Integration" "Ultra-Slim Premium Design" Glassmorphism panel... listing: "Flagship Performance" "Advanced AI Imaging"

**代表性 prompt (case115):**
> Create a premium futuristic infographic poster for Samsung Galaxy S25 in a vertical 3:4 aspect ratio. Center the Galaxy S25 phone lineup with multiple sleek smartphones shown from front and back angles... Use a deep cosmic blue space background with stars, glowing light trails, luminous orbit rings, reflective glass floor... Design the poster as a modern tech infographic with thin glowing connector lines, circular icon badges, and clean feature callouts around the phones.

**涵盖 case:** 24, 34, 49, 50, 56, 59, 62, 102, 115, 220 及 120-173 区间中约 8 条产品/科技主题（含 case130 运动鞋广告等）

---

## 方向 8: 中国水墨/国风美学海报 (约 12 条)

**视觉特征:** 以中国传统水墨、宣纸质感和东方极简留白为核心，涵盖新中式山水、道教图谱、古典人物与连环画风格。

**关键技巧:**
- 构图/版式: 竖版 9:16，S 形蜿蜒构图，大面积留白，中轴对称宗教卷轴式布局
- 色调/光影: 淡雅灰白底色，纸艺剪影般立体感，antique parchment / sepia ink / muted jade / cinnabar red，aged rice paper with ink splatters
- 排版/文字: 黑色楷体题字，红色印章，古典书法标题，classical seal stamps
- 负向约束: 身体比例错误，廉价质感，杂乱背景

**代表性 prompt (case4):**
> 极简新中式美学风格，画面以淡雅的灰白色为底，呈现出一种纸艺剪影般的立体感。一条S形蜿蜒的裂痕状边缘将画面分割，仿佛撕开了一层纸面，露出内部色彩斑斓的东方山水景象。

**代表性 prompt (case66):**
> A highly detailed vertical Taoist esoteric infographic poster in the style of an ancient Chinese religious scroll, printed on aged beige rice paper with fine ornamental borders, inked calligraphy, faded stains, and classical diagram annotations. At the top center, large black brush-calligraphy title text reads... The composition is perfectly symmetrical and centered on a glowing vertical spiritual axis...

**涵盖 case:** 4, 11, 17, 19, 45, 46, 47, 48, 66, 68 及部分 120-173 区间

---

## 方向 9: 动态运动/体育海报 (约 12 条)

**视觉特征:** 运动员动态瞬间的戏剧性捕捉，融合街头涂鸦、Nike 风 campaign 美学与高对比影棚打光。

**关键技巧:**
- 构图/版式: dramatic low-angle perspective, dynamic action pose, oversized bold typography behind athlete, mixed-media collage with halftone dots and motion streaks
- 色调/光影: high contrast shadows, stadium lights through rain, cinematic lighting with water droplets frozen in motion, warm highlights
- 排版/文字: bold typography overlay ("NO EXCUSES. JUST RESULTS."), hand-painted graffiti lettering, Nike-style campaign aesthetic
- 负向约束: 无

**代表性 prompt (case117):**
> A dynamic sports poster of a professional football player mid-strike, captured in a dramatic low-angle perspective, stadium lights blazing through light rain, water droplets frozen in motion, intense facial expression, muscular tension visible, cinematic lighting, high contrast shadows, ultra-detailed textures, motion blur on ball, sharp focus on athlete, bold typography overlay: "NO EXCUSES. JUST RESULTS.", modern sports branding style, Nike-style campaign aesthetic

**代表性 prompt (case54):**
> Avant-garde sports fashion advertisement, oversized basketball posed like a monumental sculpture, female athlete reclining across the ball's curved surface as if modern furniture, giant word "ELEVATE" in bold typography behind, burnt orange studio backdrop, glossy reflective floor, luxury athletic editorial aesthetic, cinematic lighting, ultra-clean composition

**涵盖 case:** 12, 54, 55, 114, 117, 222, 230 及 120-173 区间中约 5 条运动主题（含 case130 球鞋广告等）

---

## 方向 10: 动漫角色/二次元潮流海报 (约 22 条)

**视觉特征:** 将动漫 IP 角色重新诠释为潮流时装或 campaign 视觉，融合 anime illustration + streetwear fashion + editorial poster composition。

**关键技巧:**
- 构图/版式: vertical composition, off-center framing, strong diagonal movement, layered foreground/background depth, split composition (typography panel + anime scene)
- 色调/光影: clean white dominant background, signature character color as main accent, cinematic anime lighting, cel shading, reflective glasses with manga panels
- 排版/文字: bold graphic typography, Japanese text elements, logos, promotional stickers, menu-style side panels, grunge textures, anime key visual title
- 负向约束: ultra-clean linework, no realistic rendering

**代表性 prompt (case120):**
> Create a premium stylized illustration of {character_name} from {franchise}, designed as a modern anime-inspired streetwear poster with bold visual identity and cinematic composition. ... Blend: anime illustration aesthetics, modern streetwear / techwear fashion design, high-end graphic poster composition

**代表性 prompt (case178):**
> Stylized anime streetwear brand poster of a fast-food mascot character, full-body dynamic pose, highly detailed manga/anime illustration, modern urban fashion outfit inspired by the restaurant brand colors and identity, oversized hoodie, tactical straps, sneakers, chains, branded accessories, holding signature food item, bold graphic typography, editorial magazine layout, Japanese text elements

**涵盖 case:** 42, 69, 70, 71, 72, 85, 87, 89, 91, 120, 123, 127, 140, 147, 150, 167, 170, 178, 196 及部分 120-173 区间

---

## 方向 11: 超现实/概念艺术海报 (约 15 条)

**视觉特征:** 打破物理与视觉常规的超现实意象，包括巨物与微缩对比、维度断裂、液态 3D 雕塑与拼贴解构。

**关键技巧:**
- 构图/版式: 仰拍视角强化大小对比，巨型生物/物体 + 渺小人物，self-intersecting 3D endless loop，macro-photography studio shot
- 色调/光影: 星云/梦幻色彩，mirror-glossy finish reflecting surrounding colors，museum pedestal lighting，shallow depth of field
- 排版/文字: bold heavy rounded white typography outlined in black，minimal subtitle
- 负向约束: no bio-organic textures, no moss or flora (case220), no cartoon atoms (case221)

**代表性 prompt (case10):**
> 一幅超现实主义数字插画风格，采用低角度仰拍视角。画面描绘了一条巨型彩色锦鲤遨游在梦幻般的星云中，四周环绕着色彩鲜艳的星云与气泡。画面中央还站着一个小人，背对观众，神情平静地仰望空中这条巨大的锦鲤

**代表性 prompt (case83):**
> A {argument name="painting style" default="baroque oil painting"} comes to life — its painted figures climbing out of the gilded frame into a {argument name="setting" default="modern white gallery"}, half their bodies still in flat 2D paint, half fully volumetric 3D humans, brushstrokes visible on their skin, the painting's background leaking watercolor clouds into the gallery ceiling

**涵盖 case:** 7, 10, 14, 83, 84, 92, 94, 109, 174, 175, 187, 191, 192, 196, 207

---

## 方向 12: 复古/怀旧风格海报 (约 12 条)

**视觉特征:** 模拟特定年代的印刷工艺与视觉语言，包括 1960s Madison Avenue 广告、90 年代港片胶片风、Super Famicom 游戏包装与 mid-century editorial。

**关键技巧:**
- 构图/版式: 符合目标年代的版式规范，screen print texture with subtle paper grain, hand-painted illustration style, vintage Madison Avenue advertising aesthetic
- 色调/光影: warm sepia atmosphere, antique printing texture, soft retro color tones (beige, caramel, amber gold, dark brown), 胶片颗粒感
- 排版/文字: elegant retro typography, 品牌名突出融入海报设计，authentic 1960s print imperfections
- 负向约束: no cartoonish feel

**代表性 prompt (case217):**
> Authentic 1960s American advertising poster for [BREW], vintage mid-century commercial illustration, [PERSON DESCRIPTION] holding a frosty glass bottle of [BREW], bright optimistic lifestyle scene, nostalgic Americana atmosphere, bold [COLOR 1] and [COLOR 2] color palette, elegant retro typography, the text "[BREW]" prominently integrated into the poster design, authentic screen print texture, subtle paper grain, hand-painted illustration style, vintage Madison Avenue advertising aesthetic

**代表性 prompt (case98):**
> Use the character in image 1 as the main subject. Create a vertical poster ad in American fast food diner style. Low angle, wide lens. Red / yellow / white palette with ketchup splashes, melting cheese graphics, comic burst shapes, retro diner typography, and bold fast food poster collage aesthetic.

**涵盖 case:** 8, 9, 35, 46, 98, 99, 106, 161, 189, 203, 217, 225

---

## 方向 13: 其他/混合类型 (约 5 条)

未能归入上述方向的零散条目，包括：

- **case6, case20** — Doodle Sketch AI Builder（涂鸦素描风格的 AI 主题插画）
- **case28** — Handwritten Medical Prescription Sheet（手写处方单模拟）
- **case41** — 360 Equirectangular Panorama Image（全景图技术型 prompt）
- **case200** — Borussia War Room Interior（体育俱乐部室内概念设计）
- **case205** — Watercolor 2026 Calendar Poster（水彩日历海报）
- **case232** — prompt not available in upstream repo

这些案例或因主题过于独特、或因 prompt 内容过短/缺失，无法与其他方向形成 3 条以上的共性簇。

---

## 覆盖统计

| 方向 | 估计条数 | 占比 |
|------|---------|------|
| 1. 旅行目的地插画海报 | ~35 | 15% |
| 2. 美食摄影与食谱信息图海报 | ~25 | 11% |
| 3. 时尚编辑与品牌大片海报 | ~28 | 12% |
| 4. 暗黑史诗/电影概念海报 | ~18 | 8% |
| 5. 科普百科信息图海报 | ~22 | 9% |
| 6. 角色设计/参考图谱 | ~20 | 9% |
| 7. 产品广告与科技发布海报 | ~18 | 8% |
| 8. 中国水墨/国风美学海报 | ~12 | 5% |
| 9. 动态运动/体育海报 | ~12 | 5% |
| 10. 动漫角色/二次元潮流海报 | ~22 | 9% |
| 11. 超现实/概念艺术海报 | ~15 | 6% |
| 12. 复古/怀旧风格海报 | ~12 | 5% |
| 13. 其他/混合类型 | ~5 | 2% |
| **合计** | **~232** | **~100%** (含跨方向重叠) |

> 注：部分 prompt 横跨两个方向（如复古旅行海报同属方向 1 和方向 12，运动时尚广告同属方向 3 和方向 9），计入主要方向，统计数字含少量重叠。
