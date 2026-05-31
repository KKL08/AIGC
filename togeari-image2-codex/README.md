# togeari-image2-codex

从模糊灵感到高质量出图 — 你的 GPT-Image-2 创意搭档

这是一个运行在 Codex 桌面端的基于 GPT-Image-2 模型的创意生图 AIGC Agent Skill 包。我们将整个创作流程拆解为五个关键环节 Skill，并特别邀请了来自《GIRLS BAND CRY》里 TOGENASHI TOGEARI 乐队的五位成员——Nina、Momoka、Tomo、Rupa、Subaru——分别负责把关每一个关键 Skill 流程。她们会全程引导协助你把一个模糊的想法变成最终作品。

<p align="center">
  <img src="docs/members/gbc.jpg" width="640">
</p>

## 它能做什么

你有一个模糊的灵感或者你希望把脑海中构思的画面变成完整的图片作品。你试着写 prompt，但写完总觉得差一点——要么画风偏离，要么构图奇怪，要么光影不对味。

从模糊想法到精准画面，需要静下心来梳理：你到底想要什么？什么样的提示词和参考素材能实现它？图出来了怎么继续优化？

现有的方式各有各的卡点：

| 常见做法 | 问题 |
|----------|------|
| 直接在 ChatGPT 里写 prompt | 手敲提示，没有灵感引导和质量保障 |
| 找 Prompt 模板| 杂乱繁多，且限制创意空间 |
| 让 AI 写提示词| 质量不稳定 |
| 讨论灵感用 A 工具、写 prompt 用 B 工具、生图用 C 工具 | 流程割裂，频繁切换工具导致灵感流失 |

**togeari-image2-codex** 把创作拆成五个通用步骤，每个步骤交给一位 GBC 成员，帮你把模糊想法一步步落地成最终成片。整个流程在 Codex 内完成，直接调用 Codex 自带的 gpt-image-2 生图能力，从灵感收敛到 prompt 组装到出图到审阅，Codex 内一站式完成。

## Case 展示

以下均为 togeari-image2-codex 全流程协作生成。

| 瑞幸咖啡「生椰丝绒拿铁」新品广告 | 西安美食旅行海报「长安食味」 |
|:---:|:---:|
| <img src="docs/showcase/case1.png" width="380"> | <img src="docs/showcase/case2.png" width="380"> |
| 城市商业广告画风，产品特写 + 代言人构图 | 水墨国风排版，多道地方美食组合展示 |

| 鸣潮 × 喜茶联名宣传图 | Sony A7R VI 产品信息图 |
|:---:|:---:|
| <img src="docs/showcase/case4.png" width="380"> | <img src="docs/showcase/case3.png" width="380"> |
| 游戏 IP 联名茶饮，水元素氛围渲染 | 结构化参数信息图，深色科技风格 |

| iPhone 17 × 千早爱音 TVC 九宫格分镜 | 河原木桃香 Coser × Galgame UI 壁纸 |
|:---:|:---:|
| <img src="docs/showcase/case5.png" width="380"> | <img src="docs/showcase/case6.png" width="380"> |
| 动画联名广告分镜，9 个镜头批量生成 | 真人写真叠加动画风对话框 UI，9:16 竖屏 |

## 工作流程

你只需要说出想法，五位成员接力完成从灵感到成品的全过程。

### 🎵 成员分工

| 成员 | 位置 | Skill | 职责 | 性格 |
|:---:|------|-------|------|------|
| <img src="docs/members/nina.png" width="50"><br>**Nina** 井芹仁菜 | 🎤 主唱 | togeari-producer | 理解意图，追问收敛，编排流程 | 拒绝含糊，模糊的想法不往下传 |
| <img src="docs/members/momoka.png" width="50"><br>**Momoka** 河原木桃香 | 🎸 吉他 | momoka-route | 给出多个创意方向 | 开朗、果断，专注于创意 |
| <img src="docs/members/tomo.png" width="50"><br>**Tomo** 海老塚智 | 🎹 键盘 | tomo-map / tomo-scan | 从 Gallery 中发现创意方向、检索参考 prompt | 冷眼精准，严谨不将就 |
| <img src="docs/members/rupa.png" width="50"><br>**Rupa** ルパ | 🎸 贝斯 | rupa-craft | 把 brief 和 Gallery 技巧智能整合成最终提示 | 冷静清醒，下笔精准不犹豫 |
| <img src="docs/members/subaru.png" width="50"><br>**Subaru** 安和すばる | 🥁 鼓 | subaru-judge | 逐项审查生成结果，给优化建议和新灵感 | 好胜较真，每个细节都要查到位 |

### 流程

1. 🎤 **Nina 理解意图**。分析你的输入，判断是否需要追问。”帮我做张海报” 这种模糊输入她会追问收敛；已经足够具体的就直接跳到第 3 步。
2. 🎸 **Momoka 收敛方向**。根据意图生成 2-3 个视觉上有明显差异的方向，比如「极简排版」vs「实景氛围」vs「插画手绘」。你选一个继续。
3. 🎹 **Tomo 检索 Gallery**。从 7 个领域的核心技巧和 649 条验证 prompt 中检索匹配的参考方向与素材。
4. 🎸 **Rupa 智能组装 Prompt**。把创意方向、关键细节、Gallery 技巧融合成结构化的专业 prompt。不同领域不同的理念和写法。
5. 🥁 **Subaru 审阅**。对照 brief 逐项检查生成结果，给出具体优化建议，同时推荐同领域的其他创意方向。

单图满意后想做成系列，随时可以切到批量模式。同一风格不同内容、同一主体不同角度、叙事递进都支持，多张图并行生成。

## 安装

**环境要求：**
- Codex 桌面端, 推荐 Mac 环境

**快速安装：**

在 Codex 对话中说：

> 帮我安装 GitHub 上的 skill：github.com/KKL08/AIGC/togeari-image2-codex

详细安装方式与手动安装 → [INSTALL.md](INSTALL.md)

## 领域指南 & Prompt Gallery

Skill 包内置覆盖多个领域的高质量 prompt，并对每个领域的提示词和真实案例进行深度分析，提炼出 **Creativity Map**（领域指南），总结该领域的创意方向和提示词关键技巧。Skill 会根据领域指南引导 Agent 真正理解”一份好的提示词应该怎么写”。

| 领域 | 数量 | 覆盖范围 |
|------|------|----------|
| Portrait 人像 | 100+ | 电影光影、环境肖像、暗调情绪 |
| Poster 海报 | 100+ | 活动海报、音乐视觉、概念排版 |
| Character 角色 | 15+ | 奇幻角色、赛博朋克、Q版设计 |
| Ad Creative 广告 | 80+ | 产品广告、品牌视觉、社交媒体 |
| Ecommerce 电商 | 100+ | 产品摄影、场景化展示、极简风 |
| UI Design | 100+ | App 界面、深色模式、仪表盘 |
| Comparison 对比 | 40+ | 前后对比、A/B 展示 |

当你的灵感靠近某个领域时，Skill 会自动匹配该领域的技巧与参考案例；如果你的想法跨出已有领域，Agent 会用从知识库积累的通用技巧自主组装，不受领域限制。


## 后续 Roadmap

- [ ] Claude Code 与更多通用 Agent 平台适配
- [ ] Gallery 自动更新迭代机制
- [ ] 创作偏好记忆系统
- [ ] 自动化定时任务

## 参考来源

- Prompt Gallery 数据基于 [EvoLinkAI/awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) 整理
- 角色命名灵感来自《Girls Band Cry》（トゲナシトゲアリ / Togenashi Togeari）


