---
name: dependency-check
description: 跨章节依赖分析器——将回调图、母题注册表和认知弧组合为单一 DAG。识别前向依赖（硬失败）、对已修订章的横向依赖（带爆炸半径的软失败）和剪切章节的爆炸半径。每次章节改写后运行。
version: 1.0.0
---

# 依赖检查

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 依赖 DAG

读取三种数据文件组合成依赖图：callbacks + motifs + cognitive edges。组合图必须是无环的（DAG）。

## 三次遍历

**Pass 1: 前向依赖（硬失败）。** 任何边指向较早章且较早章需要较晚章的内容。使用授权阅读顺序 DAG，非原始章号。

**Pass 2: 横向依赖（软失败）。** 当第 K 章被改写，识别每个有一条来自 K 的入边的第 L 章。委托给子审计（callback/motif/cognitive）进行实际验证。

**Pass 3: 剪切爆炸半径。** 如果第 K 章被剪除，报告每个有 K 作为端点的边：出边/入边回调、母题频次影响、认知弧角色影响。

## 冲突处理

前向依赖存在于基线中 → 标记为既有技术债务。改写引入了前向依赖 → 必须移除引用或重排章节。横向依赖存在但子审计报告通过 → 无行动需取。剪切半径大但剪切是有意的 → 构建半径报告，人类决定。散文中有边但未在注册表中 → 候选边发现，路由 Bonnie。
