# UI — 创意方向地图

基于 95 条 EvoLinkAI 验证 prompt 蒸馏。

## 方向 1: 直播间/社交平台截图仿真 (约 10 条)

**视觉特征:** 9:16竖版、模拟抖音/TikTok直播间的完整UI(弹幕/礼物特效/关注按钮/在线人数/PK对战)、写实人物+平台界面元素叠加
**关键技巧:**
- UI 完整度: 右侧点赞/评论/分享图标、底部弹幕滚动、顶部"直播"标识、礼物动画特效
- 人物写实: cinematic photorealistic portrait + social media UI overlay, natural skin texture
- 幽默融合: 名人(Elon Musk/历史人物/李佳琦)在抖音直播带货的荒诞场景
- 负面约束: 避免模糊/卡通/二次元CG感、文字乱码、界面错误、非中文短视频界面

**代表性 prompt (case15):**
> A 9:16 vertical version, high-detail realistic style Chinese TikTok live screenshot, Elon Musk is talking to the mobile phone camera in the live broadcast room, excited, smiling... There are obvious Chinese TikTok interface elements in the live broadcast screen, including likes, comments and share icons arranged vertically on the right, scrolling Chinese bullet screens...

**覆盖条目:** case4, case5, case6, case7, case15, case16, case18, case22, case31

---

## 方向 2: UI 设计系统生成 (约 5 条)

**视觉特征:** 一张图包含网页/移动端/卡片/控件/按钮等完整UI组件库，可从风格参考图或主题描述生成
**关键技巧:**
- 一句话生成: "用这种风格帮我生成一套UI设计系统，包含网页、移动端、卡片、控件、按钮以及其它"
- 风格迁移: 从上传参考图提取视觉风格→应用到UI系统(宇宙/飞行/蝴蝶主题)
- 赛博朋克变体: 霓虹灯+玻璃建筑反射+紫蓝粉配色→Dashboard/移动端/按钮
- 跨平台: Web + mobile + 小组件(OBS直播叠加)

**代表性 prompt (case1):**
> 用这种风格帮我生成一套UI设计系统，包含网页、移动端、卡片、控件、按钮 以及其它

**覆盖条目:** case1, case8, case17, case21, case68

---

## 方向 3: 信息图/知识拆解图 (约 15 条)

**视觉特征:** 博物馆图鉴式拆解(汉服/产品)、个人形象分析、穿搭拆解、食谱版式、技术架构图、设备参考百科，中文标注为主
**关键技巧:**
- 博物馆图鉴: 米白背景+结构拆解+中文引线标注+材质特写+纹样色板+穿着流程图
- 个人分析: personal color analysis(四季色彩) / male glow-up analysis(发型/胡型/穿搭/脸型)
- 穿搭拆解: outfit breakdown chart, T-pose人物居中，箭头连接各部件cutout
- 设备百科: camera reference infographic，模块化info cards + annotation lines + engineering callouts
- 知识笔记: handwritten study infographic poster, pastel色+笔记本网格质感+荧光笔标记

**代表性 prompt (case10):**
> 请根据【主题】自动生成一张"博物馆图鉴式中文拆解信息图"。要求整张图兼具真实写实主视觉、结构拆解、中文标注、材质说明、纹样寓意、色彩含义和核心特征总结...

**覆盖条目:** case10, case11, case12, case58, case59, case62, case63, case64, case79, case89, case91, case92, case93

---

## 方向 4: 动漫Banner/Key Art (约 18 条)

**视觉特征:** 宽幅cinematic anime illustration、DDLC/游戏角色key visual、详细角色描述+场景氛围+光效粒子+排版文字
**关键技巧:**
- 角色描述精度: 发色/发型/服装件数/表情/姿态/配饰逐一定义(exactly 4 visible clothing pieces)
- 场景融合: 教室夕阳/哥特大教堂废墟/赛博朋克屋顶/音乐厅舞台 等场景+角色组合
- 光效系统: volumetric lighting, glittering particles, sunset light streaming through windows, lens flares
- 文字整合: 大字标题+书脊文字+vertical日文inscription 自然融入画面
- 暗黑变体: cyberpunk witch(404 ERROR主题)、gothic android warrior(NieR风格)

**代表性 prompt (case32):**
> A highly polished anime banner illustration in a warm golden classroom-literature-club setting, wide cinematic composition. On the left half, a large elegant glowing script title reads {argument name="headline text" default="Monika"}... On the right half, a beautiful anime schoolgirl... She wears a Japanese high school uniform with exactly 4 visible clothing pieces: a brown blazer, white shirt, red ribbon tie, and brown argyle sweater vest.

**覆盖条目:** case29, case30, case32, case33, case34, case35, case36, case37, case38, case43, case46, case47, case49, case50, case51, case55, case56

---

## 方向 5: 品牌识别/Moodboard 系统 (约 8 条)

**视觉特征:** 16:9黑底非对称网格、品牌色彩系统+排版层级+视觉语言+应用场景mockup的完整品牌提案板
**关键技巧:**
- 8-card系统: LOGO LOCKUP / EDITORIAL PHOTO / CAMPAIGN BANNER / STORY FORMAT / TYPOGRAPHIC POSTER / COLOR PALETTE / PRODUCT MOCKUP / TYPE PATTERN
- 品牌推理: 从logo自动推断identity traits→选择匹配typography(luxury→serif / tech→geometric sans)
- 应用真实化: packaging/website hero/mobile UI/social media/business card/billboard mockup
- 密度规则: minimum 30-50 elements, no empty or filler space, Behance feature-worthy

**代表性 prompt (case80):**
> Full-blown brand identity system [BRAND NAME] — Brand Identity Moodboard... Single 16:9 flat image. Black (#000–#0A0A0A) background. 8 cards in an asymmetric 3-column grid... RULE: A person who knows this brand must immediately confirm every card belongs to it.

**覆盖条目:** case25, case52, case61, case67, case80, case82, case85, case87

---

## 方向 6: 产品电商信息图 (约 6 条)

**视觉特征:** 产品hero shot + model + 规格typography的电商广告图，单品英雄构图、rainbow prism lens flares、品牌social poster
**关键技巧:**
- 信息层级: massive background text + product name + feature stats(30hrs/1yr warranty) + bottom specs
- 模型+产品: model佩戴/手持产品，product as hero in foreground(macro lens depth blur)
- 汽车海报: 从参考图提取车型→替换为品牌主题色背景+condensed typography+editorial block+specs
- 鸡尾酒/美食: cinematic vertical photo, backlit golden liquid, greenhouse bar setting

**代表性 prompt (case23):**
> High-impact e-commerce infographic for "Apple Pods Pro 3" premium wireless over-ear headphones... Extreme close-up of a hand holding a sleek, matte-white premium over-ear headphone toward the camera... Typography (modern sans-serif, white): TOP CENTER: Massive bold oversized text: "HEADPHONES"...

**覆盖条目:** case23, case24, case40, case45, case52, case53

---

## 方向 7: 分镜脚本板 (约 5 条)

**视觉特征:** 3x4或2x2网格分镜、每panel含场景编号+标题+描述，手绘sketch/3D/电影风，角色一致性
**关键技巧:**
- 模板化: 3x4 grid layout with 12 panels, scene number + title + image + description
- 手绘质感: pencil and ink illustration style, cross-hatching for shadows, aged cream paper texture
- 制作流程: storyboard → Seedance 2.0 animation → final MP4 的完整pipeline
- 多面板: borderless grid, independent images, subject consistency, no text no gap

**代表性 prompt (case57):**
> A professional hand drawn sketch storyboard sheet, pencil and ink illustration style, rough artistic linework, cross-hatching for shadows, loose expressive strokes, monochrome black and white on aged cream/off-white paper texture background, 2x2 grid layout with four equal storyboard panels...

**覆盖条目:** case41, case57, case60, case65

---

## 方向 8: 摄影拼贴/生活方式网格 (约 8 条)

**视觉特征:** 4x4照片网格、胶片质感、candid couple/lifestyle photography、disposable camera feel、nostalgic film grain
**关键技巧:**
- 一致性: same face identity across all 16 panels, consistent amber-brown color grading
- 2D+3D混合: real adult man + anime-style companion，保持光影/透视/色彩一致
- 胶片质感: 35mm point-and-shoot feel, motion blur, bloom around lights, flash overexposure
- 场景多样: 16个不同场景(室内/街头/海边/车内/电梯/夜景)覆盖一次约会全程

**代表性 prompt (case54):**
> {"type":"16-photo nostalgic contact sheet collage","style":"dreamy film photography, soft blur, slightly underexposed, candid youthful romance, flash snapshots mixed with ambient dusk light, subtle grain, sentimental and bittersweet mood"...}

**覆盖条目:** case42, case44, case54, case66, case69, case70, case90

---

## 方向 9: 建筑/空间设计板 (约 5 条)

**视觉特征:** 竞赛级建筑presentation board(3:4竖版)、航拍渲染+生态剖面+分析图层叠加、kinetic architecture概念
**关键技巧:**
- 三层结构: top analytical diagrams → middle aerial rendering → bottom sectional cut
- 生态系统: wetlands/bioswales/hydrology/vegetation，desaturated greens + earthy browns
- 运动建筑: heliotropic tracking mechanics, solar path diagrams → robotic kinematic wireframes → architectural installation
- 纸张质感: subtle paper-grain or printed board texture, competition-board aesthetic

**代表性 prompt (case81):**
> Generate a 3:4 vertical, competition-grade landscape architecture presentation board. The board blends photorealistic aerial rendering with refined architectural diagram language... Layout (three stacked zones): 1. Top zone: analytical ecological diagrams... 2. Middle zone: a large aerial landscape rendering... 3. Bottom zone: a continuous sectional cut...

**覆盖条目:** case81, case83, case84, case88

---

## 方向 10: 创意小品/特殊形式 (约 7 条)

**视觉特征:** 塔罗牌、贴纸、日历、像素马赛克、涂鸦云朵、书法字帖等非标准视觉形式
**关键技巧:**
- 塔罗牌: Rider-Waite classic style, uneven black ink line, flat colors without shading, paper printed texture
- 贴纸化: die-cut sticker illustration, cream border + drop shadow, isolate subject from background
- 日历: 12个月份插画，Korean illustration style, hand-drawn doodle, splatter brushstrokes
- 3D chibi: big head caricature figurine, collector toy aesthetic, glossy vinyl figure finish

**代表性 prompt (case95):**
> Create a Tarot card based on what you know about me, in the classic style of Rider-Waite. Portray me as a drawn figure with an expressive, but slightly uneven black line of ink, with vivid fluctuations and variations in the stroke, with flat colors without shading.

**覆盖条目:** case9, case13, case14, case27, case39, case48, case72, case86, case94, case95

---

## 方向 11: 游戏/幻想场景 (约 4 条)

**视觉特征:** AAA级游戏截图概念、gacha游戏界面、超现实日式未来都市、电影级动作场景
**关键技巧:**
- 游戏概念: AAA video game screenshot concept design
- 日式超现实: 表现拥挤中的无聊、繁华下的孤独，细节到窗户里各式人物
- 电影动作: cinematic city explosion chase, 28mm wide angle, motion blur, debris

**代表性 prompt (case26):**
> AAA Video Game Screenshot Concept Design

**覆盖条目:** case14, case19, case26, case28

---

## 方向 12: 穿搭/形象分析图板 (约 5 条)

**视觉特征:** 以上传人像为中心的形象分析板——穿搭拆解、四季色彩诊断、glow-up前后、glassmorphism UI面板
**关键技巧:**
- 面部保持: uploaded face and identity must remain EXACTLY THE SAME
- 多维分析: 发型推荐 + 胡型 + 穿搭风格(old money/smart casual/luxury streetwear) + 脸型分析 + 最佳角度
- 奢华面板: glassmorphism UI, floating premium panels, champagne gold + matte black
- fashion board: soft pastel cream background, magazine-style composition, sweet preppy aesthetic

**代表性 prompt (case89):**
> Create an ULTRA PREMIUM AI MALE GLOW-UP ANALYSIS POSTER with a luxury fashion-tech aesthetic... The uploaded face and identity must remain EXACTLY THE SAME... HAIRSTYLE SECTION: textured quiff, low taper, side part flow... OUTFIT STYLE SECTION: old money, smart casual, luxury streetwear, classy formal, monochrome black fit...

**覆盖条目:** case59, case62, case64, case89
