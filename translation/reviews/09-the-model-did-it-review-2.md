# 第 9 章翻译稿复查报告（Review 2）

Owner: Reviewer
审核类型: 快速复查（两个指定修复点）
源文件: book/chapters-v6/09-the-model-did-it.md
译文文件: translation/chapters/09-the-model-did-it-draft.md
术语表版本: 1.0.0-pilot (ch-09 terms approved 2026-06-13)

---

## 修复 1 检查：反洗钱 → 反洗白

**原文：** "The first anti-laundering device remains the record"
**要求：** 确认译文使用"反洗白装置"而非"反洗钱装置"，与全书核心术语"洗白"（responsibility laundering）一致
**核查位置：** 第 1052 行

**结果：通过。**

译文为："第一个**反洗白装置**仍然是记录"
`grep` 确认全文中零处残留"反洗钱"。术语统一性合规。

---

## 修复 2 检查：裸英文 "agents" → "自主行动系统（agents）"

**原文：** "When the agents arrive in our work, we already know what to ask."
**要求：** 确认裸英文已替换为中文术语+括号附英文，与前句"自主行动系统"一致
**核查位置：** 第 1064 行

**结果：通过。**

译文为："当**自主行动系统（agents）**到达我们的工作中时，我们已经知道该问什么。"
`grep` 确认全文中"agents"仅以括号注释形式出现在中文术语之后，无裸英文独立出现。

---

## 判决

| 修复 | 状态 |
|---|---|
| 修复 1：反洗钱 → 反洗白 | PASS |
| 修复 2：裸英文 agents → 自主行动系统（agents） | PASS |

**判决：PASS（0 HARD / 0 SOFT）**

两个 Chinese Reader HARD 发现均已在译文中成功修复。无需进一步操作。

交接：Translation Director
