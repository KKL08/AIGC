# Ecommerce — 创意方向地图

基于 20 条 EvoLinkAI 验证 prompt 蒸馏。

## 方向 1: 奢华产品棚拍广告 (约 7 条)

**视觉特征:** 暗色/大理石背景、戏剧性布光、浅景深、金色高光、凝结水珠质感，方形构图的高端美妆/香水/手表广告
**关键技巧:**
- 材质写实: condensation droplets, realistic glass refraction, gold metallic highlights, wet specular highlights
- 布光体系: dramatic warm lighting from upper left, high-contrast, crisp specular highlights, soft luminous bloom
- 构图层次: 产品偏右居中 + 左侧排版文字区(serif headline + subheading + gold line)
- 辅助道具: 烟雾(wisps of elegant smoke)、切水晶碗、花瓶鲜花、缎面布料、黑色大理石盒

**代表性 prompt (case1):**
> A luxurious cinematic product photograph of a classic rectangular perfume bottle inspired by {argument name="brand label" default="N°5 CHANEL PARIS PARFUM"}, placed upright on a glossy black marble surface with white veining... Dramatic warm lighting from the upper left creates golden highlights, deep reflections on the marble, and a soft luminous bloom in the background. Wisps of elegant smoke curl around the bottle on both sides, enhancing a moody high-end advertisement feel.

**覆盖条目:** case1, case2, case5, case6, case8, case13, case18

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

**覆盖条目:** case3, case14, case15, case19

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

**覆盖条目:** case4, case9, case11

---

## 方向 4: 创意概念广告 (约 3 条)

**视觉特征:** 微缩模型(miniature diorama)、环保叙事、可持续时尚等概念驱动的产品广告，超越纯产品展示
**关键技巧:**
- 微缩叙事: tilt-shift miniature aesthetic, tiny figurine workers climbing scaffolding, metaphorical concept
- 叙事植入: 可种植标签(plantable seed tag)从标签长出植物的视觉隐喻
- 场景化: 生活方式(lifestyle)编辑摄影 + editorial product photo + shallow depth of field

**代表性 prompt (case7):**
> A hyper-realistic miniature diorama product advertisement featuring an oversized luxury skincare pump bottle... Tiny figurine construction workers dressed in yellow coveralls and white hard hats swarm around the bottle climbing scaffolding, painting the bottle with rollers, operating a tower crane... Tilt-shift miniature aesthetic, ultra-detailed, commercial product photography, 8K resolution, photorealistic CGI render.

**覆盖条目:** case7, case12, case17

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

**覆盖条目:** case10, case16, case20
