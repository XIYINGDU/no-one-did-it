---
name: translation-pipeline
description: 翻译流水线 — 初始化或管理由 5 个 AI agent 组成的书籍翻译流水线（Translator / Reviewer / Glossary Master / Chinese Reader / Translation Director）。含三轴审核、追责链、A/B/C/D 评分。
---

# 翻译流水线

## init

初始化翻译流水线到当前项目。

```bash
./init.sh --source <源文件目录> --target <翻译产出目录> [--source-lang en] [--target-lang zh] [--project "项目名"]
```

初始化后可使用以下 5 个 agent：
- **Translator** — 翻译章节，产出双语稿
- **Reviewer** — 三轴审核（准确性/术语/语域），评定 A/B/C/D 等级
- **Glossary Master** — 术语表唯一拥有者，裁决术语争议
- **Chinese Reader** — 冷读中文译文，报告读者体验
- **Translation Director** — 协调流水线，推进章节至 ready

## translate

启动单章翻译。分配 Translator 翻译指定章节。

## review

启动单章审核。分配 Reviewer 对已完成翻译进行三轴审核。

## cold-read

启动冷读。分配 Chinese Reader 以读者身份阅读中文译文。

## status

查看当前流水线状态：各章节进度、等级分布、待处理发现。
