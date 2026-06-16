# 工作流

## 案例到章节管道

```text
候选事件 → 领域研究员案例文件 → 来源账本 → 责任链图 → 事实核查审计 → 红队挑战 → 法律风险扫描 → 书籍架构放置 → 叙事草稿 → 专家审查 → 最终章节修订
```

## Sprint 节奏

1. 周一：Jerry 定义 sprint 并分配负责人。2. 周二–周三：研究人员构建来源包。3. 周四：Stephen 事实核查，Laura 红队。4. 周五：Bonnie 将经批准的包转为章节简报。5. 周末：Wayne 起草或修订散文。

## 起草前需要

一个案例仅当具有完整案例文件、证据等级、来源账本、最强反方论证、法律风险标记和书中功能时才可起草就绪。

## 章节状态 + 提升关卡

`book/chapters-v2/` 下的章节产物须声明 YAML frontmatter：`status: brief | draft | ready | gated`。

关卡行为：`brief` 和 `draft`——章节节奏缺口仅触发警告。`draft → ready` 过渡——缺失章节节奏段落触发 PostToolUse 中的拒绝决定。`ready` 加完整章节节奏通过关卡。

## 命令路由

`.claude/commands/` 下的所有 slash 命令通过声明的 owner agent 路由。命令文件须在 frontmatter 中包含 `owner: <agent-id>`，命令执行须首先派遣 owner agent。技能在 owner agent 内部运行，而非直接在命令层。
