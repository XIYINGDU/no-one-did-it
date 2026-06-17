# 翻译流水线模板

**一套可复用的 AI agent 翻译工作流，专注于非虚构书籍的翻译质量管理。**

```
Translator → Reviewer → Glossary Master → Chinese Reader → Translation Director
     ↑            ↓              ↑                  ↑                  |
     └──────── 审核闭环 ←────── 术语裁决 ←────── 冷读反馈 ←───────────┘
```

## 核心设计

不追求全自动化——每步有署名，每条决策可追溯。实践了它所翻译的那类书籍的核心论点：**责任跟随控制权，不跟随可见度。**

### 流水线角色

| 角色 | 职责 | 记忆 |
|---|---|---|
| Translator | 双语翻译 + 翻译笔记 | project（独立） |
| Reviewer | 三轴审核 + A/B/C/D 等级评定 | project（独立） |
| Glossary Master | 术语表唯一拥有者 | project（独立） |
| Chinese Reader | 冷读中文，报告体验 | 无（永远冷读） |
| Translation Director | 流水线协调 + 否决权 | project（独立） |

### 质量门控

- **三轴审核**：准确性（逐句对照原文）→ 术语（glossary.yml 合规）→ 语域（朗读中文）
- **A/B/C/D 四级评分**：对标学术证据等级的翻译质量标准
- **独立否决权**：Reviewer HARD 发现阻断推进，只有 Director 可记录否决
- **追责链**：每步决策署名，每项发现追踪至修复闭环

## 快速开始

### 安装

```bash
git clone https://github.com/yourname/translation-pipeline-template.git /tmp/tpl
cp -r /tmp/tpl/{.claude,scripts,templates,init.sh} your-book-project/
cd your-book-project
chmod +x init.sh
```

### 初始化

```bash
./init.sh --source book/chapters/ --target translation/ --lang zh
```

### 启动翻译

在 Claude Code 中：

```
/translate-chapter 1    → Translator 翻译第 1 章
/review-chapter 1        → Reviewer 审核第 1 章
/cold-read-chapter 1     → Chinese Reader 冷读第 1 章
/translation-status      → 查看流水线状态
```

或直接使用 agent 调用：

```
@translator 翻译第 1 章
@reviewer 审核第 1 章
```

## 目录结构

```
your-book-project/
├── .claude/
│   ├── agents/                ← 5 个翻译 agent（初始化生成）
│   └── agent-memory/          ← 角色独立记忆
├── translation/               ← 翻译产出目录
│   ├── TRANSLATION.md         ← 翻译宪法
│   ├── SCORING.md             ← 评分标准
│   ├── glossary.yml           ← 术语表
│   ├── chapters/              ← 双语证据稿
│   ├── ready/                 ← 纯文本产出
│   ├── reviews/               ← 审核 + 冷读报告
│   └── decision-log/          ← 翻译决策 + 审核结论追踪
└── scripts/
    └── extract_ready.py       ← 双语 → 纯文本剥离
```

## 设计原则

1. **准确先于优雅** — 宁可译文稍显生硬，不可丢失信息
2. **术语跟随词汇表** — 零临时造词
3. **语域跟随原文** — 叙事热度/分析冷度存活
4. **审核先于合入** — 零 HARD 方可 ready
5. **追责可追溯** — 每条决策有署名，每条发现有闭环
6. **不追求自动化** — 决策署名不可替代

## 源起

从 *No One Did It: Responsibility Laundering, from the Scapegoat to the Algorithm* 的中文翻译实践抽象而来。那本书的论点是责任洗白将控制者与代价承担者分离——这个翻译流水线实践了它所诊断的东西。
