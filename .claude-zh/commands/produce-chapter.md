---
description: 为一章运行逐章生产管道——读取 STATUS.md 以识别下一个未完成阶段，派遣正确的 agent，每个阶段完成后更新 STATUS.md。跨 session 可恢复；在同一章上多次调用是安全的（将从上次停止的地方继续）。
owner: jerry-crew-chief
argument-hint: "<chapter-slug>"
---

# Produce Chapter

派遣 `jerry-crew-chief` agent 编排一章的端到端生产管道，遵循 `.claude/docs/book-production-workflow.md`。Jerry 在每个阶段将工作路由给适当的 cell lead（Bonnie / Wayne / Delon / Stephen / Laura / Nancy / Blair）。参数为章节 slug（如 `03-who-could-have-stopped-it`）。将主作者输入需求（节拍 10 清醒检查、提交、范围扩展、战略转向）浮回给人类，而非自动决定。

## 每个阶段的派遣

| 阶段 | Agent | 产出 |
|-------|-------|------|
| 1（书脊确认） | bonnie-book-architect | 确认或标记漂移 |
| 2（案例文件研究） | delon-research-director → 按领域路由 | 案例文件 + 反方案例文件 |
| 3（Stephen 验证） | stephen-fact-check-director | 按文件分级 |
| 4（章节简报） | bonnie-book-architect | 章节简报 .md |
| 5（散文草稿） | wayne-narrative-lead | 章节 .md 处 status: draft |
| 6（Stephen 章节级） | stephen-fact-check-director | 散文漂移报告 |
| 7（Nancy 章节级） | nancy-legal-risk-counsel | 措辞裁决 |
| 8（Alan 信条） | alan-expert-reviewer | 按框架验证 |
| 9（Laura 红队） | laura-red-team-editor | 过度声明审计 |
| 10a（Bonnie 结构） | bonnie-book-architect | 架构仍成立确认 |
| 10b（主作者 beat-10） | xiaolai（人类）——浮回 | 批准或修订请求 |
| 10c（Jerry 提升） | jerry-crew-chief | 状态编辑 draft → ready |

## 约束

- **诽谤纪律**在案例文件层面和章节散文层面强制执行。
- **词汇纪律 (R51)** 由 NLPM 评分子提交时强制执行。
- **纯粹替罪羊锚点关卡**对 ch-5、ch-7、ch-11、ch-13 触发。

## 不做什么

- 不提交。主作者决定提交。
- 不在压力下跳阶段。每章都经过关卡序列。
- 不修改 `book/toc.yml`。书脊变更是主作者决定。
