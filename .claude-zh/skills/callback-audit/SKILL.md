---
name: callback-audit
description: 审计书籍级别的回调图，追踪跨章节的设置→回报边。验证每个播种的锚点在声明位置有其下游回报，每个回报仍有其上游播种。捕获孤立播种和孤立回报。读取 book/registries/callback-graph.yml；任何图相关章节被改写时全书运行。
version: 1.0.0
---

# 回调审计

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 何时使用

- 在 `structural-polish` 或 `full-craft-rewrite` 等级的任何章节改写之后。
- 在任何参与回调图边（作为播种起点或回报终点）的章节从 `in-review` 提升到 `ready` 之前。
- 在 rule 09 的 Stage 2 基线运行期间，建立改写前的回调状态。
- 每当 `book/registries/callback-graph.yml` 被编辑时。

## 回调图

`book/registries/callback-graph.yml` 是一个边列表。每条边记录一个设置→回报对：

```yaml
- id: foia-folder-marked-classified
  type: object_callback | phrase_callback | scene_callback | rule_callback
  payoff_kind: re-reading | reversal | confirmation | refutation
  required: true
  planted:
    chapter: 02
    section: §3
    line_anchor: "the manila folder, edge stamped"
  paid_off:
    chapter: 09
    section: §7
    line_anchor: "the same edge stamp, now meaningless"
```

## 决策标准

审计对全书运行四次遍历：Plant 验证、Payoff 验证、孤立审计、回调类别完整性审计。

## 冲突处理

1. 播种因 `structural-polish` 改写漂移了 20 行 → 更新边的 `planted.line_anchor`；在 `revision_history` 中记录移动。
2. 回报因场景重排现在位于不同章节 → 与 Bonnie 协调修正。
3. 所需回调在改写中被故意剪切 → 不能无声删除；要么在其他处重新播种，要么降级/删除边并记录原因。
4. 环境播种被审计 → 标记存在但不出错退出；如果播种本应是回调但从未注册边，升级给 Bonnie。
5. 播种和回报都存在但回调类别完整性失败 → 硬失败。恢复对象一致性或重新分类边类型。

## 升级条件

- 播种/回报漂移需要散文调整 → Wayne。
- 回调重新构建需要场景重排 → Bonnie。
- 单次改写周期中 3+ 回调失败 → xaiolai。
- object_callback 引用来源账本中存在争议的产物 → Stephen。
- rule_callback 逻辑松散 → Laura。

## 输出格式

```text
Owner: callback-audit (skill run by <agent>)
Task: Audit book/registries/callback-graph.yml against current chapter prose
Edge-by-edge: | Edge id | Plant 裁决 | Payoff 裁决 | 类别完整性 | Required? | 行动 |
Orphan: | Orphan type | Chapter | Line | Recommendation |
Summary: total edges / pass / drifted / missing / class-integrity-fail / orphans
```
