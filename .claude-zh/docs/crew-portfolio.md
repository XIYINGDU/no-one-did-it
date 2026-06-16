# Crew 名册——谁对什么负责

## 当你想要 X 时，调用 Y

| 如果你想要…… | 调用 | 负责 agent |
|---|---|---|
| 定义本次 sprint 的工作 | `/crew-briefing` | Jerry |
| 为指名的的事件构建案例文件 | `/case-file <event>` | Delon |
| 审计证据和来源质量 | `/source-audit <file>` | Stephen |
| 将经批准的案例文件转为章节简报 | `/chapter-brief <chapter>` | Bonnie |
| 攻击论题、草稿或声明 | `/red-team <target>` | Laura |
| 构建书籍提案包 | `/proposal-pack` | Blair |
| 专业领域审查 | Stephen 作为 `/source-audit` 的一部分派遣 | Alan |
| 指定图表、表格或责任链图示 | `/figure-spec` | Bonnie |

## 派遣图（有界 DAG，深度 ≤ 2 从 Jerry 开始）

```
Jerry → Bonnie, Wayne, Delon, Stephen, Laura, Nancy, Blair
Delon → Shirley, Selina, Warren, Loki
Stephen → Alan
```

Wayne、Bonnie、Laura、Nancy、Blair 是有意叶子——其工作成果由 Jerry 整合，非通过衍生子 agent。叶子间的交接通过 `Handoff:` schema 字段传播。

## 每个 agent 结束每个可交付成果时附带

```text
Owner: / Task: / Inputs reviewed: / Output: / Evidence grade:
Assumptions: / Open questions: / Risks: / Handoff:
```

## 本名册如何保持诚实

| 断言 | 验证方式 |
|---|---|
| 派遣图无环，深度 ≤ 2 | `scripts/check_agent_graph.py` |
| 每个命令的 owner: 指向真实 agent | `tests/test_command_contracts.py` |
| 工具授权匹配策略文档 | `scripts/check_tool_grants.py` |
| 五大原则跨所有生成目标字节级一致 | `scripts/sync_five_over_rules.py --check` |
