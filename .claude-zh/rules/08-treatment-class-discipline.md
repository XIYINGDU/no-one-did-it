---
description: "处理等级纪律：每章进入改写周期时必须声明恰好一个处理等级（no-change、prose-polish、defamation-safe-tighten、structural-polish、full-craft-rewrite），并附有引证的缺陷证据；等级转换须记录原因。"
---

**每章进入改写周期时必须声明恰好一个处理等级，并附有引证的缺陷证据；等级转换须记录原因。**

# 处理等级纪律

**作用域：** 约束 `book/chapters-v2/` 中进入虚构工艺改写周期的每一章。结束了书籍级别的"完全改写"与"润色处理"之间的虚假二元对立。逐章处理尊重了 13 章不共享同一个缺陷这一事实。

## 五个处理等级

| 等级 | 何时使用 | 代价 | 改变了什么 |
|---|---|---|---|
| `no-change` | 章节通过了 rule `12-reader-experience-values.md` 中所有 10 项读者体验价值；缺陷图显示无可操作的缺陷；进一步的工作将面临倒退风险。 | 零。 | 无。 |
| `prose-polish` | 结构和体系架构合理；存在工艺价值缺陷（节奏、重锤句、音频韵律、声音编织），但核心价值通过。在现有章节架构内应用分析笔记中的铲斗 1 工艺手法 #5、#6、#7、#8。 | 一次轻量 wayne-narrative-lead 处理 + 审计链。 | 句子级别的散文；无结构变化；不需要合同文件。 |
| `defamation-safe-tighten` | 章节在工艺上合理，但存在法律审查标记的 rule-05 或 rule-07 风险面。适用 nancy-legal-risk-counsel 处理（使用 defamation-wording 技能）；wayne 重新渲染。 | 一次 nancy + 一次 wayne 处理 + 审计链。 | 仅特定段落；在章节缺陷图中标记。 |
| `structural-polish` | 核心价值通过；一两个工艺价值缺陷需要结构性移动（场景重排、视点聚焦调整、母题插入），但无需完全改写。 | 一次 bonnie-book-architect 结构处理 + 一次 wayne 处理 + 审计链 + 跨章节审计。 | 场景顺序、视点聚焦者指派、母题放置；需要合同文件；运行 callback/motif/cognitive-arc 审计。 |
| `full-craft-rewrite` | 缺陷图显示核心价值失败且工艺价值失败；章节需要在改写周期内使用完整的铲斗 1 工具箱（文档作为主角、聚焦-后-打破、双轨时间、向上延迟指名、声音编织、重锤句逆转、共鸣回归、一个意象）。 | 一次完整的章节生产周期当量 + 完整审计链 + 跨章节审计 + nancy 时钟 + laura 红队。 | 案例文件卷宗层以下的一切；卷宗保持不变。 |

## 声明形式

`book/registries/treatment-classes.yml` 持有声明：

```yaml
- chapter: 02
  slug: the-four-goats
  class: full-craft-rewrite
  defect_evidence:
    - {value: V3, defect: "读者同情到章节结尾时落在可见的羊身上"}
    - {value: V5, defect: "'部分 vs 纯粹替罪羊'的区分宣布了但未安装"}
    - {value: V6, defect: "令人难忘的场景却没有诊断性传递"}
  defect_map: process/defect-map/02-the-four-goats.md
  declared_at: 2026-05-27
  declared_by: chapter-defect-diagnose
  reviewed_by: [xaiolai]
  reclassifications: []   # 如果在周期中改变等级，追加到此
```

重新分类需要原因和相同的 `reviewed_by` 链：

```yaml
  reclassifications:
    - {from: full-craft-rewrite, to: structural-polish, on: 2026-06-04,
       reason: "试点显示完全改写过度纠正；章节只需要场景重排",
       reviewed_by: [xaiolai]}
```

## 关于这些等级的规则

1. **每章一个等级。** 不允许混合等级；如果一章同时有 prose-polish 和 defamation-safe-tighten 工作，更高的等级胜出（此情况下为 defamation-safe-tighten）。
2. **`no-change` 也需要证据。** 一章不能被分类为 `no-change` 仅仅因为没人看过它；缺陷图必须存在并显示通过的价值。
3. **跨章节审计向上继承。** `structural-polish` 运行跨章节审计（callback、motif、cognitive-arc、dependency）。`full-craft-rewrite` 增加 nancy 时钟和 laura 红队。更低等级仅在其变更可以影响该表面时才继承其上方等级的审计集。
4. **重新分类是允许的，但不是免费的。** 随时允许沿等级阶梯上升，并重新运行更高等级的审计。沿阶梯下降需要记录原因并重新验证更低等级的审计集覆盖了实际变更所触及的每个审计面。
5. **等级是工作流的输入，而非输出。** 一章不会因为有人想写一次完全改写就变成 `full-craft-rewrite`；它变成 `full-craft-rewrite` 是因为缺陷图证据要求它。

<示例>
一章显示出 V6 缺陷（令人难忘的场景但无诊断性传递）和一个 V10 缺陷（音频韵律在识别节拍处中断）。核心价值 V1、V3、V5、V7、V8 均按缺陷图通过。

朴素的解读会说"两个工艺缺陷，full-craft-rewrite"。Rule 08 拒绝这种解读。核心价值通过；V6 需要在现有章节架构内重新安排识别节拍；V10 需要对三个特定段落进行句子节奏工作。

正确的处理等级：`structural-polish`——为 V6 进行场景重排，为 V10 进行散文处理，在现有卷宗内进行。`full-craft-rewrite` 工具箱（文档作为主角、双轨时间、声音编织）并不需要，对已经通过 V1/V3/V5/V7/V8 的章节会过度纠正。
</示例>

## 这条规则为什么存在

Codex 所批评的计划（`dev-docs/fiction-craft-rewrite-implementation-plan.md`，测试 D）将路径 R / 路径 P 呈现为书籍级别的二元选择。诚实的情况是，13 章很可能分布在所有五个等级上。将书视为一个同质处理，迫使要么对稳定章节过度投入，要么对破碎章节投入不足。逐章分类是在作者时间真正产生回报的地方花费时间的唯一方式。

本规则是 `/chapter-defect-diagnose` 和 `/treatment-classify` 的宪法锚点。在改写周期中被 `book/STATUS.md` 章节状态追踪所引用。
