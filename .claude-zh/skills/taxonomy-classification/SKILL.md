---
name: taxonomy-classification
description: 通过对每个类别行走诊断问题，将事件分类为项目的 4 个规范案例类别。研究人员、Bonnie 和 Alan 在案例类别存在争议或尚未分配时使用。
version: 1.0.0
---

# 分类法分类

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 决策标准

按序遍历 4 个诊断块。第一个返回干净"是"的块即为案例类别。多块返回是 → 混合案例，显式指明。

**块 1 — 纯粹替罪羊：** 被公开归责者实质上无辜；无记录证据将其置于链条中；归责服务于他人；惩罚有记录。**块 2 — 部分替罪羊：** 被归责者至少在执行层面有过错；但归责止步于此，阻止责任上爬；至少一个上游行动者有更多控制/知情却承担更少后果；止步有记录。**块 3 — 系统/对象托辞：** 非人原因被公开指名为原因；该原因有合理的机制性参与；但构建/部署/批准/获利的人类行动者面临较少或没有公众归责。**块 4 — 承受代价的羊：** 个人/群体承担伤害；未被公开指控造成伤害；实际责任承担者避开或最小化其份额；代价承担有记录且不成比例。

无匹配：不是本书分类下的责任洗涤案例。不强行适配。

## 输出

```text
Case: / Diagnostic blocks 1-4: yes|no|partial + evidence /
Primary category: / Secondary category (if hybrid): / Evidence grade: / Handoff:
```
