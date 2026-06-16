---
name: translation-director-role
description: Translation Director 协调完整翻译流水线 — 从术语提案到 Glossary Master 到译者到审核员到中文读者到 ready
metadata:
  type: user
---

用户正在以 **Translation Director** 身份操作，启动第 9 章"模型干了它"的翻译流水线。流水线顺序为：

1. 术语识别 → 提案给 Glossary Master
2. Glossary Master 裁决 → 更新 glossary.yml
3. 翻译分派（Translator Brief）
4. Translator 产出双语草稿
5. Reviewer 三轴审核（准确度/术语/语域）
6. 审核通过 → Chinese Reader 冷读
7. 零 HARD → 推进至 ready

用户偏好：
- The chapter title should be directly translated as "模型干了它" preserving the colloquial "did it" force
- 八问必须与第 3 章 ready 文本完全一致（已验证）
- 跨章回旋镖案例（Therac-25, 737 MAX, Horizon）术语必须与对应章节一致
- 三层分析框架（input/deployment/evaluation layer）是核心分析框架，需保持术语一致
- 15 条新术语提案、Glossary Master handoff 和 Translator Brief 已全部写好
