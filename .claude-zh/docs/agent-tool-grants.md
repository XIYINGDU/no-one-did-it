# Agent 工具授权

## 定向添加

- `laura-red-team-editor`：授予 WebSearch 和 WebFetch（用于对抗性证据检索）。
- `delon-research-director` 及 4 位领域研究员：授予 WebSearch 和 WebFetch（一手来源检索）。
- `stephen-fact-check-director` 和 `nancy-legal-risk-counsel`：授予 WebSearch 和 WebFetch（验证 + 法律状态检查）。
- `blair-market-strategist`：授予 WebSearch 和 WebFetch（同类书和市场研究）。
- `alan-expert-reviewer`：授予 WebSearch 和 WebFetch（领域权威查阅）。

## 按角色加权的 maxTurns 策略

**模型策略：** 所有 13 agent 运行 `opus`（主作者指令）。轮次预算按编排深度和预期决策负载加权：

| 角色组 | maxTurns | 理由 |
|---|---|---|
| `jerry-crew-chief` | 40 | 跨 cell 排序、冲突解决、最终交接路由 |
| Core leads/directors（5人） | 25 | 多步规划/修订循环 |
| Strategic/legal controls | 20 | 中等深度综合，有界产物表面 |
| Researchers（4人）+ Alan | 18 | 来源包构建，更窄权限 |
| `xiaolai` | 20 | 判断替身——调用应紧凑 |
| `the-reader` | 22 | 冷读整章，但不编排或修复 |

## 无 Bash/TodoWrite 策略

无 agent 拥有 Bash 或 TodoWrite。执行和任务列表变更集中保留在顶层编排者 session。所有 agent 的完整拒绝表见此文件。
