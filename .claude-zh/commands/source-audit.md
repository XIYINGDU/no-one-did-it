---
description: 审计案例文件、章节简报或草稿中的声明、证据等级和来源质量。使用 source-ledger-discipline 和 citation-hygiene 技能。返回可用声明、薄弱声明、不可用声明和来源空白。
owner: stephen-fact-check-director
argument-hint: "<file-path>"
---

# Source Audit

派遣 `stephen-fact-check-director` agent，任务：使用 `source-ledger-discipline` 和 `citation-hygiene` 审计声明、证据等级和来源质量。

产出可用声明、薄弱声明、不可用声明和来源空白的列表。应用来自 `.claude/rules/02-evidence-grades.md` 的 A/B/C/D 等级，并拒绝提升一项仅依赖于 C 级证据的章节级声明（除非该章节的主题本身就是不确定性）。

<example>
Context: Stephen（事实核查 director）需要在 Wayne 推进之前对一份草稿进行关卡审查。
user: /source-audit book/chapters-v2/03-system-object-alibi-draft.md
assistant: 加载 source-ledger-discipline 和 citation-hygiene，遍历每项声明，返回："可用 (A)：7 项声明，关联于 NTSB、JATR、FAA 证词。薄弱 (B)：3 项记者的综合报道需要一手备份。不可用 (C)：1 项内部动机归因（记录中无承认）。空白：缺失 Lion Air 最终报告引用；协调两份分歧的飞行数据引述。"
</example>
