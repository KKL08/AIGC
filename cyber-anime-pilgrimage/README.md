# ✨ 赛博巡礼相机 · 动漫圣地 AI 打卡神器

![Status](https://img.shields.io/badge/状态-在线-green)
![Agent](https://img.shields.io/badge/🤖_架构-Agent_链路-blueviolet)
![搜索模型](https://img.shields.io/badge/搜索-Gemini_3.5_Flash-blue)
![生图模型](https://img.shields.io/badge/生图-Nano_Banana_2_|_GPT_Image_2-orange)

> 输入名字，Agent 自动搜索取景地、推理关联关系，再生成一张二次元角色亲临圣地的巡礼照。

[**👉 立即体验**](https://cyber-anime-pilgrimage.vercel.app/)

---

## 📸 这是什么？

**赛博巡礼相机** 是一个动漫圣地巡礼工具。
你只需输入角色和作品名称（可选），它就会像一名"巡礼向导"——自动联网搜索、多源推理取景地、判断地理关联性，最后调用图像模型把角色合成到实拍场景中。

**让巡礼不再受地理限制，随时开启你的二次元朝圣。**

---

## 🧭 三步完成一次巡礼

| 操作 | 说明（Agent 视角） |
|------|------------------|
| 1️⃣ **搜角色** | Agent 调用 Gemini 3.5 Flash + Google 搜索，从 ACG 相关信源、地图信息中**推理**出最可能的现实取景地／原型地点。 |
| 2️⃣ **选地点** | Agent 将推理结果标注在地图上，并提供地名、城市、关联作品说明，由你确认最终巡礼点。 |
| 3️⃣ **生成巡礼照** | 上传你选择的二次元角色照片（全身或半身效果最佳） → Agent 根据场景光线、构图自动选择生图策略，调用 Nano Banana 2 或 GPT-Image-2 合成角色，输出一张高融合度的巡礼照。 |

---

## 🧠 为打卡而生的 Agent

- **主动推理**：搜索不只是关键词匹配，而是理解作品与现实地点的内在关系。
- **工具自主组合**：调用搜索、地理编码、图像生成、地图展示等多类组件。

👉 简单说：它是一个 **专做圣地巡礼的 AI Agent**。

---

## ❓ 常见问题

<details>
<summary>需要付费吗？</summary>
目前在线体验版本需要使用者自行准备相关服务商 API Key。可前往官方开通相关服务申请 Key：

- Gemini API Key → [Google AI Studio](https://aistudio.google.com/apikey)
- OpenAI API Key → [OpenAI Platform](https://platform.openai.com/api-keys)
</details>

<details>
<summary>支持哪些角色/作品？</summary>
只要作品有公认的现实取景地或原型地点，Agent 均可检索推理。覆盖面非常广，欢迎多多尝试。
</details>

<details>
<summary>生成的照片会被保存吗？</summary>
我们不会主动保存您的上传照片和生成结果，但建议勿上传含个人隐私的图片。
</details>

---

## 🧩 项目状态

- 在线体验 → [赛博巡礼相机](https://cyber-anime-pilgrimage.vercel.app/)
- 📱 移动端已适配，打开即用。

---

*即刻巡礼，不止于打卡。* 🚀
