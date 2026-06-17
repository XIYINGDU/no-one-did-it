---
owner: orchestrator
argument-hint: <交付物-id>
description: 对交付物运行完整质量关卡——审查员 pass + 对抗性审查 pass + 提升决策。
example: |
  /quality-gate 交付物-03
---

对指定交付物：

1. 派遣 `reviewer` 运行完整质量验证——逐断言证据分级、来源核查、标准合规。
2. 派遣 `red-team` 运行对抗性审查——最强反方论证、过度声明检测、缺口暴露。
3. 整合发现。如审查员和对抗性审查员均无 HARD 发现，提升为 `ready`。如任一返回 HARD 发现，退回执行者并记录中止。
4. 更新 `STATUS.md`。
