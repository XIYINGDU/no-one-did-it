---
description: 为指定的历史、政治、法律、企业、战争或 AI 事件构建或更新一份责任洗涤案例文件。使用 case-file-method 和 responsibility-chain-mapping 技能。结果存储在 book/evidence/case-files/ 下。
owner: delon-research-director
argument-hint: "<event-name>"
---

# Case File

派遣 `delon-research-director` agent，任务：使用 `case-file-method` 和 `responsibility-chain-mapping` 为用户指定的事件构建或更新案例文件。

除非另有指示，将产出存储在 `book/evidence/case-files/<slug>-case-card.md`。始终回答八个诊断问题（公开被归责者 / 控制 / 利益 / 知情 / 可预防性 / 记录控制 / 代价承担者 / 如果责任跟随控制会怎样）并分配来自 `.claude/rules/02-evidence-grades.md` 的证据等级。

<example>
Context: Crew Chief 为 AI 系统章节分配一个新案例待撰写。
user: /case-file Boeing 737 MAX MCAS
assistant: 加载 case-file-method 和 responsibility-chain-mapping，回答八个诊断问题，分类案例（部分替罪羊：飞行员归责止步于 FAA/Boeing 高管以下），分配证据等级 A（NTSB 和 JATR 报告），写入 book/evidence/case-files/boeing-737-max-mcas-case-card.md，附带 Handoff: Stephen（事实核查）。
</example>
