---
description: 展示书籍的当前生产状态——哪些章节处于哪个阶段、什么在阻塞、下一步运行什么。读取 book/STATUS.md 并呈现摘要视图及下一步行动建议。
owner: jerry-crew-chief
---

# Book Status

派遣 `jerry-crew-chief` agent 读取 `book/STATUS.md`，返回书籍生产状态的简洁快照及推荐的下一步行动。Jerry 是 crew chief；阅读状态看板并指明下一步行动是他的跨 cell 路由职责。

## 返回内容

1. **头条状态。**
   - 处于 `status: ready` 的章节：13 中的计数
   - 进行中的章节（任何 cell 被触及，尚未 ready）：计数 + slug 列表
   - 排队中的章节：计数 + slug 列表
   - 当前波次（按推荐生产顺序）

2. **下一步行动。** 一句话 + 运行它的 slash 命令。例如：
   - `"运行 /produce-chapter 03-who-could-have-stopped-it — Wave 1，第 3 章是强制 Part I 顺序中的下一章。"`
   - `"Wave 2 case-file 研究正在进行中；在下次派遣前检查研究人员的产出。"`

3. **未来 14 天内到期的日期触发项。** 特别是 ch-02 slot 8（乌克兰儿童）的 Nancy 30 天重审（2026-06-24 到期）。

4. **累积工作范围。** 开放的 `[EVIDENCE NEEDED]` 项目总数；是否需要在波次结束后进行组合 Nancy 审查。

## 不做什么

- 不修改 `STATUS.md`。这是只读状态报告。
- 不派遣 agent。要推进章节，使用 `/produce-chapter <slug>`。
- 不推断 `STATUS.md` 中不存在的状态。

## 响应格式

30 行以内。紧凑的摘要，非叙述文。
