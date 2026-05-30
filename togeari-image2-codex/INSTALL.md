# togeari-image2-codex — 安装指南

## 方式一：通过 Codex Skill Installer 安装（推荐）

在 Codex 桌面端对话中说：

> 帮我安装 GitHub 上的 skill：github.com/yk/togeari-image2-codex

Codex 的内置 skill-installer 会自动执行：

```bash
# Codex 内部执行的等效命令：
scripts/install-skill-from-github.py --url https://github.com/yk/togeari-image2-codex
```

安装完成后重启 Codex 桌面端即可使用。

Gallery 数据（649 条验证 prompt + 7 个领域指南 + 索引）已包含在仓库中，无需额外安装步骤。

## 方式二：本地开发模式

开发调试时用 symlink 指向本地项目目录：

```bash
ln -sf /path/to/togeari-image2-codex ~/.codex/skills/togeari-image2-codex
```

修改代码后重启 Codex 即可生效，无需重新安装。

## 使用

在 Codex 对话中直接描述你的图像需求：

> 帮我做一张赛博朋克风的咖啡店海报

Codex 会自动识别并使用 togeari-image2-codex skill，引导你从灵感到最终出图。

## 目录结构

```
togeari-image2-codex/
├── SKILL.md                           ← Codex 主入口（togeari-producer）
├── skills/                            ← 子 skills
│   ├── tomo-scan/SKILL.md             ← Gallery 检索 [Tomo]
│   ├── rupa-craft/SKILL.md            ← Prompt 组装 [Rupa]
│   └── subaru-judge/SKILL.md          ← 图片 Review [Subaru]
├── references/
│   └── openai-image-guide.md          ← gpt-image-2 参考指南
├── gallery/
│   └── evolinkai/
│       ├── index.yaml                 ← 649 条索引
│       ├── domains/*.md               ← 7 个领域指南（基于高质量 prompt 提炼）
│       └── prompts/**/*.md            ← 649 个完整 prompt
└── scripts/
    ├── install-gallery.sh             ← 重建 gallery 用（正常安装不需要）
    └── build-evolinkai-index.py       ← 重建索引用（正常安装不需要）
```

## 卸载

```bash
rm -rf ~/.codex/skills/togeari-image2-codex
```
