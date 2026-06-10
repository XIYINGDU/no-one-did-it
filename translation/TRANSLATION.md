# 翻译项目指令 — 单一真相源

> 本文件是翻译流水线的宪法。所有译者（Translator）、审核员（Reviewer）、术语管理员（Glossary Master）和中文读者（Chinese Reader）共享此文件。

源语言：英语（美式）
目标语言：简体中文
源文件目录：`book/chapters-v6/`
翻译产出目录：`translation/chapters/`

## 全局五大铁律

1. **准确先于优雅。** 永远不要为了让中文更流畅而削弱原文含义。宁可中文稍显生硬，不可丢失信息。
2. **术语跟随词汇表。** 禁止临时创造术语翻译。所有术语使用 `glossary.yml` 中的译法，零例外。
3. **语域跟随原文。** 原文的叙事热度保留叙事热度，分析冷度保留分析冷度。作者的冷峻/精确/可读的语气在译文中存活。
4. **审核先于合入。** 任何章节未经 Reviewer 审核不得进入 `ready`。Reviewer 的 HARD 发现阻止推进。
5. **干净交接。** 每个产出声明假设、不确定项、开放问题、下一负责人。

## 核心原则

这本书的论点——责任洗白（responsibility laundering）是文明将替代品送上祭坛的循环技术——必须在译文中完整存活。中文读者应该获得与英文读者相同的诊断能力。翻译不是「大致传达意思」，而是在另一种语言中重建诊断工具。

## 风格规则

- 原文的叙事热度 → 中文保留叙事热度（场景描写使用具体、主动的动词）
- 原文的分析冷度 → 中文保留分析冷度（论断句保持简短、不煽情）
- 原文的道德转折短句 → 中文保留短句，不拉长，不加解释性形容词
- 原文的引用标记 `[CITE: slug]` 和脚注编号原样保留
- 德文/法文等非英语原文以斜体保留，首次出现时在括号内给出中文翻译
- 专有名词（人名、地名、机构名、法律名）首次出现时保留原文并括号注中文

## 引用处理

- 原文中的 `>` 引用块：翻译为中文，但脚注保留英文原文引用
- `[CITE: slug]` 标记原样保留，不翻译
- 脚注 `[^N]` 编号原样保留
- `[sup]` 等 HTML 标签原样保留

## 角色地图

| 角色 | 拥有 | 不拥有 |
|---|---|---|
| Translation Director | 调度、标准、最终合入 | 翻译、审核 |
| Glossary Master | 术语一致性、术语表 | 翻译、审核 |
| Translator | 章节译文产出 | 审核自己译文、修改术语表 |
| Reviewer | 质量判断、独立否决权 | 重写译文（只标注问题位置和类型） |
| Chinese Reader | 中文读者的阅读体验 | 提议修复、参考原文、查看术语表 |

## 存档规范

翻译流水线的所有产出均有明确的落盘位置：

| 产出类型 | 位置 | 命名规则 |
|---|---|---|
| 译文稿 | `translation/chapters/` | `<章节号>-<slug>-draft.md` |
| 审核报告 | `translation/reviews/` | `<章节号>-<slug>-review-<序号>.md` |
| 术语表 | `translation/glossary.yml` | 单一文件，由 Glossary Master 维护 |
| 翻译规范 | `translation/TRANSLATION.md` | 本文件 |

审核报告每次审核单独存档，序号递增。报告 frontmatter 必须包含：`review_id`、`chapter`、`reviewer`、`date`、`coverage`、`verdict`。如有前次审核，标注 `previous_review`。

译文稿 frontmatter 必须包含：`source`、`translator`、`chapter`、`title_en`、`title_zh`、`glossary_version`、`status`。

## 产出标准

每个翻译交付物必须包含：

```text
Owner: Translator
章节:
源文件:
术语表版本:
Evidence grade: N/A（翻译项目）
Assumptions:（翻译中的判断和假设）
Open questions:（不确定的译法、需要确认的地方）
Handoff: Reviewer
```
