---
name: contract-audit
description: 对照章节的声明每章合同审计章节，验证章节交付了声明的 knows、can_discriminate、feels 和 primed_for 槽位。feels: 槽位通过 rule 12 读者体验价值解析；通过需要结构性交付和核心价值保存两者兼备。
version: 1.0.0
---

# 合同审计

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 何时使用

- 在 `structural-polish` 或 `full-craft-rewrite` 等级的章节改写之后。
- 合同 YAML 在周期中被编辑时。
- 合同章节从 `in-review` 到 `ready` 过渡之前。
- 更低等级不需要合同——本技能不适用于它们。

## 决策标准

**knows:：** 每个 concept-id 在散文中被命名并实际使用。**can_discriminate:：** 每个 distinction-id 既有指明段落也有演示段落。**feels:：** 每个立场转换有一个识别节拍，符合 V1（获得非制造）和 V3（同情跟随链条）。**primed_for:：** 每个 fair-clue 播种在可验证位置。

## 冲突处理

章节交付超过合同声明 → 允许，记录为超交付。不足 → 失败，回退 `in-rewrite`。概念 id 不在认知弧中 → 软失败。feels: 槽位被 Laura 红队判为 V3 违规 → 硬失败，不能提升至 ready。

## 输出格式

Per-slot: | Slot | Element | Verdict | Evidence (line anchors) | Required action |
Per-feels: | Transition | Recognition beat | V1 | V3 | V8 | Overall |
