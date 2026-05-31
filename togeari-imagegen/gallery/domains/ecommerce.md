# Ecommerce — Creativity Map | 领域指南

基于 35 条高质量 prompt 提炼而来的 Ecommerce 领域指南。

## 方向 1: 奢华产品棚拍广告 (约 7 条)

**视觉特征:** 暗色/大理石背景、戏剧性布光、浅景深、金色高光、凝结水珠质感，方形构图的高端美妆/香水/手表广告
**关键技巧:**
- 材质写实: condensation droplets, realistic glass refraction, gold metallic highlights, wet specular highlights
- 布光体系: dramatic warm lighting from upper left, high-contrast, crisp specular highlights, soft luminous bloom
- 构图层次: 产品偏右居中 + 左侧排版文字区(serif headline + subheading + gold line)
- 辅助道具: 烟雾(wisps of elegant smoke)、切水晶碗、花瓶鲜花、缎面布料、黑色大理石盒

**代表性 prompt (case1):**
> A luxurious cinematic product photograph of a classic rectangular perfume bottle inspired by {argument name="brand label" default="N°5 CHANEL PARIS PARFUM"}, placed upright on a glossy black marble surface with white veining... Dramatic warm lighting from the upper left creates golden highlights, deep reflections on the marble, and a soft luminous bloom in the background. Wisps of elegant smoke curl around the bottle on both sides, enhancing a moody high-end advertisement feel.

**覆盖条目:** case1, case2, case5, case6, case8, case13, case18, case22, case26, case33

---

## 方向 2: 食品饮料活力海报 (约 4 条)

**视觉特征:** 高饱和色彩、水花飞溅/冰块漂浮动态、新鲜水果元素、大字标题+法语/英语促销文案，阳光沙滩或纯色背景
**关键技巧:**
- 动态元素: dramatic water splashes, scattered clear ice cubes, floating citrus pieces, condensation droplets
- 文案系统: 大标题 + 副标题 + 特色图标列表(SAVEURS NATURELLES等) + 促销徽章 + 生态印章
- 色彩策略: 高能量(high-energy)光泽感，强日光耀斑，饱和柑橘色调
- 产品英雄镜头: 产品瓶身略倾斜、cold condensation droplets、标签细节清晰

**代表性 prompt (case3):**
> Create a vibrant tropical commercial poster for a citrus soda bottle, in a bright summer advertising style. Show a single large plastic bottle of {argument name="product name" default="Soda"} centered slightly to the right, tilted a little left, with a yellow cap and transparent bottle covered in cold condensation droplets, filled with glowing golden-orange soda...

**覆盖条目:** case3, case14, case15, case19, case21, case23, case25

---

## 方向 3: 工业设计展示板 (约 3 条)

**视觉特征:** 中性灰studio背景、网格系统布局、多角度产品渲染、材质特写macro、floating构图
**关键技巧:**
- 网格系统: 3x3 flat lay + hero shots + floating composition 三层结构
- 渲染级别: Unreal Engine 5 render style, hyper-realistic, matte textures, clean silhouettes
- 留白设计: designated blank areas for "Placeholder Branding"，sharp edges
- 适用品类: 消费电子(主板、耳机)、工业产品

**代表性 prompt (case4):**
> Layout & Composition: A {argument name="presentation type" default="professional industrial design presentation sheet"}. The image should be organized into a clean grid system. Top Row: A 3x3 layout showing top-down flat lay views and close-up macro details of materials... Style & Finish: Matte textures, clean silhouettes, and sharp edges. 4k resolution, Unreal Engine 5 render style, hyper-realistic, clean aesthetic.

**覆盖条目:** case4, case9, case11, case29, case30

---

## 方向 4: 创意概念广告 (约 3 条)

**视觉特征:** 微缩模型(miniature diorama)、环保叙事、可持续时尚等概念驱动的产品广告，超越纯产品展示
**关键技巧:**
- 微缩叙事: tilt-shift miniature aesthetic, tiny figurine workers climbing scaffolding, metaphorical concept
- 叙事植入: 可种植标签(plantable seed tag)从标签长出植物的视觉隐喻
- 场景化: 生活方式(lifestyle)编辑摄影 + editorial product photo + shallow depth of field

**代表性 prompt (case7):**
> A hyper-realistic miniature diorama product advertisement featuring an oversized luxury skincare pump bottle... Tiny figurine construction workers dressed in yellow coveralls and white hard hats swarm around the bottle climbing scaffolding, painting the bottle with rollers, operating a tower crane... Tilt-shift miniature aesthetic, ultra-detailed, commercial product photography, 8K resolution, photorealistic CGI render.

**覆盖条目:** case7, case12, case17, case27

---

## 方向 5: 电商详情页全套系统 (约 3 条)

**视觉特征:** 单张图内包含主图+详情页+卖点拆解+冲泡/使用说明+场景图+视频分镜脚本，完整电商上架物料
**关键技巧:**
- 全流程覆盖: 主图/Main image → 详情页/Details → 卖点展示 → 使用指南 → 场景应用 → TVC分镜
- JSON结构化: 用JSON定义每个section的位置、数量、标签文案
- 中文电商语言: 一冲即饮、粉质细腻、独立小袋随身携带 等卖点文案
- 9宫格分镜: 产品TVC分镜脚本(15秒 / 9:16竖屏)，每panel含中文场景标题+时间戳

**代表性 prompt (case10):**
> {"type":"Chinese e-commerce product marketing board","product":{"category":"instant grain powder drink","brand":"五谷磨房","name":"核桃芝麻黑豆粉"...},"layout":{"format":"single tall composite board divided into 5 major sections plus a bottom storyboard table"...}}

**覆盖条目:** case10, case16, case20, case24

---

## 方向 6: 动漫周边产品摄影 (约 4 条)

**视觉特征:** 以动漫角色 IP 为核心的周边商品实物摄影，包括亚克力立牌、手办、日历、包装等，既要呈现产品质感，又要保留动漫美学氛围
**关键技巧:**
- 材质表现: 亚克力透明折射(blue iridescent refraction)、PVC手办光泽/哑光分区、纸张肌理与裁切线
- 氛围布光: 软窗光(soft natural window light)、浅景深背景虚化、暖色木桌/蕾丝布料点缀前景
- 层次结构: 多层亚克力叠加(background plate → character layer → foreground decoration → front nameplate)
- 细节列举: 挂件/吊饰/装饰牌等配件清单式描述，精确到数量和造型

**代表性 prompt (case28):**
> Create a refined product-grade photo of a multi-layer transparent acrylic postcard display stand, like a miniature exhibition cabinet, featuring a dreamy blue-themed anime catgirl character. 4 main acrylic layers: background illustration, character silhouette, foreground decoration, front nameplate. 5 hanging transparent decorations: butterfly, blue teardrop gem, snowflake crystal, 2 round flower ornaments. High-end Japanese anime merchandise photography.

**覆盖条目:** case28, case31, case34

---

## 方向 7: 日式包装设计 (约 3 条)

**视觉特征:** Kawaii 零食袋、高端巧克力礼盒等日系包装商品摄影，以动漫角色/插画为视觉核心，色彩以粉/蓝/薰衣草/奶油为主调
**关键技巧:**
- IP 联名逻辑: 从角色配色/服装/气质出发推导口味、产品名、卖点，使设计与角色气质自然契合
- 包装造型: 礼盒内格(gold divider tray)、铰链翻盖(hinged illustrated lid)、绸带/珍珠点缀
- 插画规格: 盒盖内侧精细动漫插画(mermaid girl 等)，金色角花纹、品牌文字刻印
- 桌面氛围: 散落糖果/丝带/小装饰品，明亮柔和背景，梦幻散景(shimmering bokeh)

**代表性 prompt (case35):**
> Create a luxury macaron-colored product photo of a high-end chocolate gift box with ethereal ocean princess theme. Opened rectangular pale blue box with gold trim and hinged illustrated lid. Lid interior: delicate anime-style mermaid girl... Lower half: 15 individual luxury chocolates in 3x5 gold divider tray. Ultra-fine luxury Japanese confectionery packaging aesthetic, 8K.

**覆盖条目:** case32, case35

---

## 方向 8: 产品渲染与工业设计 (约 2 条)

**视觉特征:** 结合 3D 渲染与手绘草图的工业/包装设计展示，以及手办人物从概念线稿到涂装完成品的转化，呈现专业设计流程感
**关键技巧:**
- 混合媒介: 光拟真渲染(photorealistic rendering)叠加铅笔草图(pencil sketch overlay)，同一画面共存
- 技术视图: 正视/侧视/俯视/底视/角度视图 + 展开刀版图(flat dieline)，含毫米标注和材质手写注释
- 手办转化: 黑白线稿 → 全彩上色 PVC，描述光泽/哑光分区、水贴纸、缝线细节
- 中性展示背景: 简洁渐变灰背景 + 透明展示底座，无多余注释文字

**代表性 prompt (case31):**
> Using reference character design, transform the mecha girl concept into a realistic 1/7 scale painted collectible figure product photo. Convert black-and-white line art to full-color high-quality PVC anime figure with clear molded armor plates, gloss and matte material distinction, subtle seam lines, water-slide decals, toy-like sculpted detail.

**覆盖条目:** case29, case31
