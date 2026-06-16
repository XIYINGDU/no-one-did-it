# 项目 Hooks 指南

在 `.claude/settings.json` 中配置。四个 hook 作为 Python 3 脚本位于 `.claude/hooks/`；每个从 stdin 读取单个 JSON 对象，向 stdout 写入单个 JSON 对象。

## SessionStart（`session-context.py`）

匹配器：`startup|resume|clear|compact`。读取 `.claude/state/current-focus.md`（最多 4000 字符），将内容作为 `additionalContext` 注入，使每个 session 以相同的 sprint 快照打开。

## PreToolUse: Bash（`guard-destructive-bash.py`）

拒绝匹配破坏性模式的命令（对易变根的递归删除、硬仓库重置、全树强制清理、全局可写递归 chmod 及网络管道 shell 执行）。所有其他命令以显式 `allow` 决定通过。

## PostToolUse: Write/Edit（`check-agent-frontmatter.py`）

仅对 `.claude/agents/*.md` 下的文件运行。验证 YAML frontmatter、必填的 `name:`/`description:` 字段以及 `name:` 的 slug 形状。对其他文件静默跳过。

## SubagentStop（`log-subagent-finish.py`）

追加一行 JSONL 记录到 `.claude/logs/subagent-runs.jsonl`，含时间戳、agent 类型、agent id、会话记录路径和最后消息的前 500 字符。用于 crew 问责和事后审查。
