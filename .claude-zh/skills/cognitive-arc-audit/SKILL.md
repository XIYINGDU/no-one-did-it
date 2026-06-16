---
name: cognitive-arc-audit
description: 审计书籍的认知弧——读者逐章获得的区分能力和概念——对照实际散文。对每个区分验证在所需章节中的引入、巩固和应用。对每个概念验证其被命名和使用。读取 book/registries/cognitive-arc.yml。
version: 1.0.0
---

# 认知弧审计

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 认知弧

区分（discrimination）是读者能应用的一种辨别能力。概念（concept）是章节引入、全书随后使用的命名术语。退役（retirement）是书主动拆除的一种前书误解。

## 决策标准

**Pass 1: 区分安装。** `introduced_in` 章节须有指明区分的段落；`consolidated_by` 章节须有展示区分实际运用的段落；`required_by` 每章须至少使用一次该区分。若某章位于 `consolidated_by` 之前就用了该区分 → 硬失败。

**Pass 2: 概念引入。** 引入章须显式命名并应用概念。前向引用 → 硬失败。

**Pass 3: 退役完整性。** 退役章须显式处理前书框架。后续章节不得将其作为活跃前提重新引入。

## 冲突处理

区分安装段落被改写剪除 → 硬失败。新增对未引入概念的引用 → 前向依赖。章节顺序变更导致所需章先于巩固章 → 硬失败。区分在第 13 章被要求但仅在第 6 章轻描淡写 → 软失败。退役框架在后续章作为承重前提出现 → 硬失败。

## 输出格式

Per-discrimination: | id | Introduced | Consolidated | Required-chapters 使用率 | Action |
Per-concept: | id | 引入章 | 前向引用计数 | Action |
Retirement: | id | 退役章 | 重新引入计数 | Action |
