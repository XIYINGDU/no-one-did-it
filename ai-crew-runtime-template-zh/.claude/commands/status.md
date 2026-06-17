---
owner: orchestrator
argument-hint: 无 — 读取当前状态
description: 显示当前 sprint 状态——进行中的工作、阻塞项、交付物阶段、即将到来的截止日期。
example: |
  /status
---

读取 `STATUS.md` 和 `state/current-focus.md`，生成结构化状态报告，覆盖：

1. **Sprint 概览** — 当前 sprint 目标和进行中的工作项
2. **交付物面板** — 每个交付物的当前阶段和负责人
3. **阻塞项** — 哪些被卡住、原因
4. **即将到来的截止日期**
5. **下一步行动** — 编排者应派遣什么

格式为紧凑的表格视图，适合快速站会阅读。
