# togeari-image2-codex — 安装指南

## 安装

### Codex 桌面端

在 Codex 对话中说：

> 帮我安装 GitHub 上的 skill：github.com/KKL08/AIGC/togeari-image2-codex

或者手动克隆到 Codex 的 skill 目录：

```bash
git clone https://github.com/KKL08/AIGC.git /tmp/aigc
mkdir -p ~/.codex/skills/togeari-image2-codex
cp -r /tmp/aigc/togeari-image2-codex/{SKILL.md,skills,references,gallery} \
      ~/.codex/skills/togeari-image2-codex/
rm -rf /tmp/aigc
```

> `docs/`、`README.md`、`INSTALL.md` 是 GitHub 展示用的，Skill 运行不需要，不用安装。

安装完成后重启 Codex 桌面端即可使用。

> Skill 依赖 Codex 内置的 Image Generation 功能（基于 gpt-image-2），新版 Codex 默认已开启。如遇生图不可用，检查 `~/.codex/config.toml` 中 `image_generation = true` 是否存在。

Gallery 数据（649 条验证 prompt + 7 个领域指南 + 索引）已包含在仓库中，无需额外安装步骤。

### 其他平台

Claude Code、通用 Agent 平台的支持正在开发中，敬请期待。

## 使用

在对话中直接描述你的图像需求：

> 帮我做一张赛博朋克风的咖啡店海报

Skill 会自动引导你从灵感到最终出图 — 意图理解、方向收敛、Gallery 检索、Prompt 组装、生图、Review，全流程协作完成。

## 目录结构

```
togeari-image2-codex/
├── SKILL.md                           ← 主入口（togeari-producer）
├── skills/                            ← 子 skills
│   ├── tomo-map/SKILL.md              ← Gallery 方向发现 [Tomo]
│   ├── tomo-scan/SKILL.md             ← Gallery Prompt 检索 [Tomo]
│   ├── rupa-craft/SKILL.md            ← Prompt 组装 [Rupa]
│   └── subaru-judge/SKILL.md          ← 图片 Review [Subaru]
├── references/
│   └── openai-image-guide.md          ← gpt-image-2 参考指南
└── gallery/
    └── evolinkai/
        ├── index/                     ← 按领域拆分的索引（7 个文件）
        ├── domains/*.md               ← 7 个领域指南（Creativity Maps）
        └── prompts/**/*.md            ← 649 个完整 prompt
```

## 卸载

```bash
rm -rf ~/.codex/skills/togeari-image2-codex
```
