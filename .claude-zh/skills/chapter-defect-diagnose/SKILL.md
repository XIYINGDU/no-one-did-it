---
name: chapter-defect-diagnose
description: 按照 rule 12 的 10 项读者体验价值（5 核心 + 5 工艺）对章节进行诊断，构建缺陷图，指明哪些价值失败并附带引用的散文证据，推荐 rule 08 中五种处理等级之一。
version: 1.0.0
---

# 章节缺陷诊断

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 何时使用

- 任何章节改写周期被授权之前。缺陷图是 rule 09 下 `chapter-status: in-rewrite` 的前提条件。
- 在可能改变了哪些价值通过的实质性修订之后。
- 在任何全书改写项目的 Phase 0 中。

## 决策标准

对每个价值回答三个问题：章节在现有文本下是否通过该价值？哪些具体段落是裁决的证据？需要什么处理？

所有 10 项价值诊断后，挑选一个处理等级：全部通过 → `no-change`；仅工艺价值失败 → `prose-polish`；V7/V8 在活跃内容声明上失败 → `defamation-safe-tighten`；1-2 工艺 + 最多 1 核心失败且失败为结构性 → `structural-polish`；2+ 核心失败或需要 Bucket 1 工具箱 → `full-craft-rewrite`。

## 冲突处理

核心价值通过工艺但未通过证据 → 记录为失败并注明原因。诊断输出与先前审计不一致 → 诊断优先。无法在两个处理等级间决定 → 选择更高等级。V6 因无 beta-reader 数据标记为 `unscored` → 使用结构性代理评分。

## 输出格式

两个产物：`process/defect-map/<n>-<slug>.md`（包含摘要、逐值诊断、处理等级建议）和追加到 `book/registries/treatment-classes.yml` 的行。
