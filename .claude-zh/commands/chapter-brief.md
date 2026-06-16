---
description: 将经批准的案例文件转化为章节简报——场景、论题、案例层级、反方论证、证据空白和交接。使用 chapter-blueprint 技能。结果存储在 book/chapters-v2/ 下。
owner: bonnie-book-architect
argument-hint: "<chapter-slug>"
---

# Chapter Brief

派遣 `bonnie-book-architect` agent，任务：使用经批准的案例文件，通过 `chapter-blueprint` 构建章节简报。

包含场景、论题、案例层级、最强反方论证、证据空白、法律风险标记和交接指令。一个案例只有在通过了 `.claude/docs/workflow.md`（"起草前需要"）中列出的关卡后方可准备就绪。

如果调用时未提供章节名，返回："指明章节（例如 /chapter-brief pure-scapegoat）。"不得凭空创造。
