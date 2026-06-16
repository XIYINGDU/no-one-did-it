---
name: project-crew-memo-hook-exemptions
description: rule-14/过度声明 hook 对 intra-crew 审查备忘录触发——按 rule-14 边界案例 12 属预期假阳性
metadata:
  type: project
---

当任何 crew agent 在 `process/review-memos/` 下撰写审查备忘录时，PostToolUse hook 会标记元框架语言和过度声明动词。这些是预期假阳性：rule-14 边界案例 12 显式豁免 intra-crew 元数据——审查备忘录将章节作为施工中的对象来指导，因此指涉"本章"/"本书"是正确的且必需的。Rule 14 约束面向读者的章节散文，而非 crew 备忘录。
