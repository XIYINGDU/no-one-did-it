---
name: evidence-grading
description: 将每个承重声明步行通过确定性决策树来分配 A/B/C/D 证据等级：来源类型 → 佐证数量 → 程序阶段 → 利益相关方检查 → 活跃事件检查。Stephen 用于验证关卡，每位研究人员在交接前用于自我分级。
version: 1.0.0
---

# 证据分级

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 决策树

按序遍历每个承重声明：

1. **来源类型。** 法院判决/官方调查/一手文件 → A 候选。重大调查报道/NGO 调查/同行评议 → B 候选。进行中诉讼/指控/单来源 → C 候选。病毒式传播/无来源 → D。拒绝。
2. **佐证数量。** 3+ 独立来源 → 确认等级。2 来源 → 仅两者均为一手/官方时确认；否则降一级。1 来源 → 降一级（除非来源为判决或审计过的一手文件）。
3. **程序阶段。** 最终判决/正式承认 → 确认。已起诉无判决/DPA/无承认和解 → 上限 B。指控/初步审查/诉前调查 → 上限 C。
4. **利益相关方检查。** 最强来源是否利益攸关？是 → 降一级（除非由无利益来源独立佐证）。记录利益。
5. **活跃事件检查。** 活跃事件且记录仍在变动？是 → 上限 C。

**最终等级 = 上述任何步骤发出的最低等级。**

## 冲突处理

两 A 来源不一致 → 均记录，降为 B。来源虽利益攸关但是唯一可用来源 → 上限 C 附带显式注释。程序阶段在 sprint 期间推进 → 重新分级并更新所有引用旧等级的产物。研究人员与 Stephen 裁决不一致 → Stephen 的裁决优先。

## 升级条件

程序阶段需要领域知识解释 → Alan（配以匹配的领域框架）。未确认等级措辞带诽谤风险 → Nancy。锚点声明在修订周期后不能达到 A/B 且章节不能推进 → Jerry。

## 输出格式

```text
Claim: / Strongest source: / Source type: / Corroboration count:
Procedural stage: / Interested-source: / Live event: / Grade: / Rationale: / Handoff:
```
