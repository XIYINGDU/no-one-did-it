---
name: motif-audit
description: 审计追踪跨章节重复出现的对象、短语和图像的书籍级母题注册表。对每个母题验证声明的出现存在、无母题出现在 forbidden_in 的章节中、频次下限满足、以及声明的演进确实推进。
version: 1.0.0
---

# 母题审计

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 决策标准

**Pass 1: 出现验证。** 每个声明的出现，母题的识别细节须在指名的章节中出现。**Pass 2: forbidden_in 合规。** `forbidden_in:` 中每章的散文不得包含该母题的识别细节。**Pass 3: 频次下限。** 总经验证出现 ≥ `frequency_floor:`（通常 ≥ 3 章）。**Pass 4: 演进推进。** 出现按序符合声明的演进；扁平重复是软失败。

## 产出格式

| Motif id | Pass 1 | Pass 2 | Pass 3 | Pass 4 | Action |
候选母题：| Candidate image | 重复章节 | 应注册？| Recommendation |
