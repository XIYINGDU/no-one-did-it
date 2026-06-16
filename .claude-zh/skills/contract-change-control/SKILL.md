---
name: contract-change-control
description: 在改写周期中管理章节逐章合同的带版本修正。对比修正前后合同，要求每个变更字段说明原因，标记会掩盖 Gate B 失败的修正（如 feels: 槽位被削弱以匹配改写而非其承诺），并将两个版本快照到章节审计历史中。
version: 1.0.0
---

# 合同变更控制

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 不变量

**合同可变；变更必须可见。** 改写可能揭示合同声明错误——这是一个真正的发现。合同应变以匹配发现。但不得无声削弱槽位以匹配表现不佳的改写。

## 决策标准

每个修正须：(1) 修正前合同有快照；(2) 每个变更字段有 `change_reason:`；(3) 分类为 `discovery`/`clarification`/`weakening`/`strengthening`；(4) `weakening` 分类需要 Laura + xaiolai 批准；(5) 跨章依赖已更新。

## 冲突处理

feels: 因部分替罪羊改变 → discovery，允许。knows: 概念移除但其他章是引入点 → 对照认知弧验证。Bonnie 为结构性变化修正合同 → 允许。修正通过但 Laura 随后红队判为 V3 违规 → 修正仍成立但章节 Gate B 失败。删除下游章依赖的 primed_for: → 硬失败，修正被拒绝。

## 输出格式

| Field | Pre | Post | Classification | Reason | Approval |
跨章依赖：| Downstream chapter | Slot referenced | Impact | Action |
