# 翻译项目指令 — 单一真相源

> 本文件是翻译流水线的宪法。所有译者、审核员、术语管理员和中文读者共享此文件。

源语言：{{SOURCE_LANG}}
目标语言：{{TARGET_LANG}}
源文件目录：`{{SOURCE_DIR}}`
翻译产出目录：`{{TRANSLATION_DIR}}`

## 全局五大铁律

1. **准确先于优雅。** 永远不要为了让译文更流畅而削弱原文含义。
2. **术语跟随词汇表。** 禁止临时创造术语翻译。所有术语使用 `{{GLOSSARY_PATH}}` 中的译法。
3. **语域跟随原文。** 原文的叙事热度保留叙事热度，分析冷度保留分析冷度。
4. **审核先于合入。** 任何章节未经 Reviewer 审核不得进入 `ready`。Reviewer 的 HARD 发现阻止推进。
5. **干净交接。** 每个产出声明假设、不确定项、开放问题、下一负责人。
6. **追责可追溯。** 每条非显而易见的翻译决策记录在决策日志中。每个 Review 发现追踪至修复闭环。

## 角色地图

| 角色 | 拥有 | 不拥有 |
|---|---|---|
| Translation Director | 调度、标准、最终合入 | 翻译、审核 |
| Glossary Master | 术语一致性、术语表 | 翻译、审核 |
| Translator | 章节译文产出 | 审核自己译文、修改术语表 |
| Reviewer | 质量判断、独立否决权、等级评定 | 重写译文 |
| Chinese Reader | 中文读者的阅读体验 | 提议修复、参考原文、查看术语表 |

## 存档规范

| 产出类型 | 位置 | 命名规则 |
|---|---|---|
| 译文稿（双语） | `{{TRANSLATION_DIR}}/chapters/` | `<章节号>-<slug>-draft.md` |
| 纯文本产出 | `{{TRANSLATION_DIR}}/ready/` | `<章节号>-<slug>.md` |
| 审核报告 | `{{TRANSLATION_DIR}}/reviews/` | `<章节号>-<slug>-review-<序号>.md` |
| 冷读报告 | `{{TRANSLATION_DIR}}/reviews/` | `<章节号>-<slug>-chinese-reader-<序号>.md` |
| 决策日志 | `{{TRANSLATION_DIR}}/decision-log/<章节号>-<slug>/` | `decisions.yml` + `resolutions.yml` |
| 术语表 | `{{GLOSSARY_PATH}}` | 单一文件，由 Glossary Master 维护 |
| 评分标准 | `{{SCORING_PATH}}` | 翻译质量等级 A/B/C/D 的宪法 |
| 翻译规范 | `{{TRANSLATION_DIR}}/TRANSLATION.md` | 本文件 |

**双语稿（chapters/）与纯文本（ready/）的分工：**
- `chapters/` 保留双语格式（原文 + 译文 + 翻译笔记）——这是翻译决策的证据链
- `ready/` 为剥离后的纯译文正文 + References——这是合稿和出版的输入源
- 进入 `ready` 后由 Translation Director 或合稿负责人执行剥离（`scripts/extract_ready.py`）

## 决策日志与追责链

每条非显而易见的翻译决策记录在 `{{TRANSLATION_DIR}}/decision-log/<章节号>-<slug>/decisions.yml`。
每条 Reviewer 或 Chinese Reader 的发现追踪至 `resolutions.yml` 中的修复闭环。

### 追责链的八问诊断

1. 谁或什么被公开归咎？
2. 谁有控制权？
3. 谁受益？
4. 谁知情或应知情？
5. 谁能阻止复发？
6. 谁控制了记录？
7. 谁承担了代价？
8. 如果让责任跟随控制权而非可见度，谁应被追问？

## 翻译质量等级

按 `{{SCORING_PATH}}` 规定，每章由 Reviewer 评定 A/B/C/D 四级。

## 产出标准

每个翻译交付物必须包含：

```text
Owner: <角色>
章节:
源文件:
术语表版本:
Assumptions:
Open questions:
Handoff: <下一负责人>
```
