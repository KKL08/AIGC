# Ad-Creative — 创意方向地图

基于 31 条 EvoLinkAI 验证 prompt 蒸馏。

## 方向 1: 食品饮料动感广告 (约 9 条)

**视觉特征:** 高饱和色彩、水花/粉末飞溅动态、食材漂浮、大字retro typography、cinematic food photography、vertical 9:16 或 square 构图
**关键技巧:**
- 动态食物摄影: dramatic berry juice splashes, floating fruits in mid air, deconstructed gravity, visible steam/smoke
- 排版风格: large retro cream bubble letters, ultra-bold distressed sans-serif, overlapping text on lower third
- 色彩系统: 单色背景(hot pink/matcha green/deep black) + 食材自然色对比
- 多变体批量: 同一模板生成 matcha/berry/chocolate 等口味变体，换色板+食材+headline
- 场景双版: lifestyle版(model in cafe) + product-hero版(studio splash) 成对出现

**代表性 prompt (case22):**
> Vibrant lifestyle food advertisement, smiling woman in a bright hot pink blazer sitting inside a colorful trendy cafe, holding a spoon and eating an acai berry bowl topped with strawberries, blueberries, banana slices, and granola, branded "Berry Loud" jar on wooden table, playful retro typography reading "BERRY LOUD" in large cream bubble letters...

**覆盖条目:** case19, case21, case22, case24, case25, case26, case27, case29, case31

---

## 方向 2: 奢侈品牌电影感广告 (约 7 条)

**视觉特征:** 暗色调、戏剧性布光、浅景深、premium材质(大理石/皮革/金属/皮草)、serif typography、editorial campaign 感
**关键技巧:**
- 产品英雄: clear glass bottle with warm amber liquid, glossy rounded black cap, crisp specular highlights
- 场景构建: 天然材质(苔藓/浮木/皮草)托举产品，earthy still-life 或 Parisian noir interior
- 人物融入: 将上传人像变为 femme fatale / high-fashion model，保留面部特征
- 文案调性: elegant serif headline + tagline("She doesn't follow. She leaves a trace.")
- 奢华质感词: luxury beauty campaign aesthetic, 8K luxury editorial finish, rich blacks, warm gold accents

**代表性 prompt (case12):**
> A high-end editorial product photograph of a single luxury perfume bottle centered in a warm earthy still-life scene... Place the bottle upright on 1 curved piece of pale weathered driftwood, surrounded by a dense carpet of 1 layer of rich green moss...

**覆盖条目:** case8, case12, case13, case17, case18, case20, case23

---

## 方向 3: 运动/潮牌时尚海报 (约 4 条)

**视觉特征:** 高能量动态人物、霓虹/全息光效、街头涂鸦拼贴质感、强烈品牌logo系统、oversized产品道具
**关键技巧:**
- 人物动态: mid-jump athletic pose / low-angle seated fashion pose，面部blur匿名处理
- 产品放大: forced perspective使鞋子oversized dominant，或oversized服装作为雕塑道具
- 品牌系统: 社交媒体handles、barcode sticker、slogan stacked lettering、logo placement规则
- 材质混搭: 摄影(产品) + 涂鸦(手绘doodle) + 拼贴(torn paper) + 印刷(distressed text)

**代表性 prompt (case10):**
> Create a bold streetwear poster advertisement for {argument name="brand name" default="NESS STUDIO"} featuring a young adult model seated casually on the ground in a low-angle fashion pose, one knee raised and one leg extended toward the camera so the sneaker in front appears oversized and dominant...

**覆盖条目:** case9, case10, case11, case28

---

## 方向 4: 品牌识别系统全案 (约 4 条)

**视觉特征:** 多panel网格布局(18-panel/8-card)、品牌DNA分析→形态研究→表情/姿势库→色彩开发→实物应用的完整链路
**关键技巧:**
- 全案结构: Brand DNA Analysis → Concept Moodboard → Form Study → Expression Sheet → Pose Library → Color Development → Digital/Physical Applications
- 吉祥物系统: 3D rendered cute mascot, turnaround view, expression sheet(11个表情), pose library(9个姿势)
- 周边延展: t-shirt/mug/pin badges/keychain/candy packets/storefront mockup
- 双语标注: 中文标题 + 英文副标题(品牌DNA分析 / BRAND DNA ANALYSIS)

**代表性 prompt (case4):**
> {"type": "18-panel brand identity and character design document","brand": {"name": "{argument name=\"brand name\" default=\"沐阳 MUYANG TEA\"}","industry": "{argument name=\"industry\" default=\"tea shop\"}"...},"layout": {"grid": "3 columns by 6 rows","sections": [{"title": "01 品牌DNA分析 / BRAND DNA ANALYSIS"...}]}}

**覆盖条目:** case2, case3, case4, case6

---

## 方向 5: 微缩城市奇观广告 (约 3 条)

**视觉特征:** hyper-detailed miniature city/diorama、isometric视角、tilt-shift效果、产品(珠宝/建筑)与微缩城市融合
**关键技巧:**
- 微缩与巨物: 珠宝变成建筑纪念碑、种子包装长出真实花园、城市规划模型精细到路灯
- 视角: high three-quarter isometric angle, tilt-shift miniature effect
- 奢华渲染: deep crimson red monochrome + gold accents, octane render, ultra realistic 8K
- 叙事隐喻: 产品的物理属性转化为城市/生态系统的隐喻("the packet as the garden it always intended")

**代表性 prompt (case14):**
> A hyper-detailed cinematic isometric miniature city model of {argument name="landmark tower" default="Burj Khalifa"} rising dramatically from the center of a square architectural master-plan board, presented like a luxury urban planning maquette on a black background...

**覆盖条目:** case7, case14, case20

---

## 方向 6: 日式广告排版 (约 2 条)

**视觉特征:** 日本市场的数字广告banner网格、传统外卖传单，强调日文排版、促销价格标注、折扣badge
**关键技巧:**
- 多主题网格: 2x2 grid of Japanese digital advertisement banners，旅行/护肤/美食/教育四合一
- 传单仿真: 红黄配色、Gothic字体阴影、菜单照片网格4x3、优惠券虚线裁切、配送地图
- 文案公式: 日语促销句式(今年こそ、解き放て / 初回限定 78%OFF)

**代表性 prompt (case1):**
> {"type": "2x2 grid of Japanese digital advertisement banners","layout": {"structure": "4 equal quadrants","quadrants": [{"position": "top-left","theme": "Travel","subject": "A couple holding hands on a white sand beach..."...}]}}

**覆盖条目:** case1, case5

---

## 方向 7: 贴纸/拼贴创意转化 (约 2 条)

**视觉特征:** 将真实产品照片转化为贴纸拼贴(sticker reality)或涂鸦(kawaii doodle)风格，scrapbook质感
**关键技巧:**
- 保留主体: preserve the original subject, composition, and background
- 叠加元素: physical stickers, paper cutouts, taped notes, hand-drawn doodles, torn edges
- 平衡感: rich and layered but still visually pleasing, not cluttered
- 适用场景: Instagram story aesthetic, cozy scrapbook journal style

**代表性 prompt (case30):**
> Edit this image while preserving the original subject, composition, and background. Transform the scene into a "sticker reality" collage: Add elements that look like physical stickers, paper cutouts, and taped notes layered over the image...

**覆盖条目:** case15, case30, case31
