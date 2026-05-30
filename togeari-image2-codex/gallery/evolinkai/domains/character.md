# Character — 创意方向地图

基于 15 条 EvoLinkAI 验证 prompt 蒸馏。

## 方向 1: 角色设定资料卡 (约 4 条)

**视觉特征:** 白色背景、三视图(正面/侧面/背面)、表情差分、装备分解、色板标注，整体有序的参考资料式排版
**关键技巧:**
- 结构: 三视图 + 表情变化 + 服装分解 + 色板，高解像度プロのコンセプトアートスタイル
- 布局: 白背景・整理されたレイアウト、アスペクト比16:9
- 模板化: 从角色+背景出发自动生成公式设定资料，可用于 gal game 角色介绍页或官方设定集

**代表性 prompt (case2):**
> 基于此角色和背景，请制作一份类似官方设定资料的角色资料卡。・包含三视图：正面、侧面和背面・添加角色面部表情的变化・分解并展示服装和装备的详细部分・添加色板・包含世界观设定的简要说明・总体上，使用有组织的布局（白色背景，插画风格）高分辨率、专业概念艺术风格

**覆盖条目:** case2, case3, case4, case11

---

## 方向 2: 电影级角色主视觉 (约 3 条)

**视觉特征:** 35mm 电影镜头感、大量环境叙事细节、体积光/god rays、cinematic anime key visual、色调克制(teal-rust-bone white)
**关键技巧:**
- 镜头语言: 35mm anamorphic lens, slight low angle, shallow depth of field, horizontal lens flares
- 角色塑造: 极细的外貌/装备描述 + 姿态动态 + 表情情绪
- 环境叙事: 完整世界观(废墟海城、竹林古道等)作为角色背景，用环境反衬角色气质
- 后期风格: film grain, high-contrast editorial poster aesthetic, desaturated oceanic palette

**代表性 prompt (case5):**
> A mecha girl mid-teens, pale skin smudged with soot and salt spray, sharp amber eyes with glowing HUD reticles, waist-length ash-white hair tied in a high ponytail whipping in the sea wind, matte gunmetal exoskeleton armor plating her shoulders, forearms and shins... cinematic anime key visual, painterly digital illustration with crisp line art, desaturated oceanic palette of teal, bone-white and rust punched by small warm accent lights, film grain, high-contrast editorial poster aesthetic . Format 16:9.

**覆盖条目:** case5, case8, case12

---

## 方向 3: 游戏风格化场景角色 (约 4 条)

**视觉特征:** 将知名游戏视觉语言(GTA/像素养成)应用于新场景或IP，卡牌网格、概念设计图
**关键技巧:**
- IP 嫁接: 用极简指令将游戏风格移植到真实地点 ({game} in {location})
- 卡牌矩阵: 多宫格卡牌排列 + 角色名标注 (如12宫格黄金圣斗士)
- 像素概念图: 电视剧主题 + 像素养成类游戏概念图，含场景全局、三视图、场景特写、剧情梗概

**代表性 prompt (case9):**
> {argument name="game" default="gta 6"} in {argument name="location" default="Bangalore's market flower"} in India

**覆盖条目:** case6, case9, case10, case13

---

## 方向 4: 动漫壁纸与手机适配 (约 2 条)

**视觉特征:** 适配折叠屏手机分辨率的动漫壁纸，区分鲜艳唯美风与暗酷未来风两种色调方向
**关键技巧:**
- 设备适配: 指定具体设备像素尺寸(内屏/外屏)，要求可裁切大图
- 风格约束: 明确角色性别气质(中性/男性适用)、发型线条要求(整洁不杂乱)
- 色调分流: 色彩多样化鲜艳 vs 黑色手机风格暗色调

**代表性 prompt (case14):**
> 请为我生成一个适用于折叠屏手机（Oppo find N6，内屏2480 × 2248 像素，外屏2616 × 1140 像素，比例适配即可，不需要完全对齐一样的像素大小）的4k壁纸，壁纸主体为动漫，风格中性壁纸适用于男性使用，但是动漫角色是女生，女生略为阳光且内敛，这个女生不能有太多的媚态。风格建议：唯美风。整个图片的色调偏向色彩多样化鲜艳方向，注意头发线条整洁，不要过于杂乱和生硬。直接做一个可以两屏适配的横纵可裁切大图。

**覆盖条目:** case14, case15

---

## 方向 5: 混沌介质角色浮现 (约 2 条)

**视觉特征:** 从混沌笔记/记号/墨迹中浮现角色面部轮廓，黑白+红色点缀，手绘纸笔质感
**关键技巧:**
- 浮现机制: 角色轮廓通过墨迹密度/留白/浓淡自然浮现，不直接描绘
- 质感控制: アナログのノート落書き質感，モノクロ+赤インク，禁止デジタル処理的整然感
- 负面约束(禁止事项): 明确列出不要做什么(写実ポートレート、幾何学模様、カラフル)

**代表性 prompt (case7):**
> 混沌としたメモ書き・記号の集合体からキャラクターの顔を浮かび上がらせるアート --- スタイル - 白い紙の上に黒インクで描かれた大量の手書きメモ、数式、記号、ランダムな線。... --- 禁止事項 - 顔を直接的に描き込む写実ポートレート。- デジタル処理的で整然とした幾何学模様。

**覆盖条目:** case1, case7
