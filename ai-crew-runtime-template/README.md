# AI Crew Runtime — 通用多 Agent 协作运行时模板

**一套可复用的 7 层系统架构，将 AI agent 运行时协作从「提示词集合」提升为「操作系统」。**

每个质量攸关的 AI 多 agent 项目都需要解决同一组问题：谁来调度、谁有否决权、规则如何自动执行、session 中断后如何恢复、错误如何不重复。这套模板提供了经过实战验证的架构骨架——你只需要替换领域血肉。

## 源起

从 *No One Did It: Responsibility Laundering* 书籍项目的 `.claude/` 运行时逆向提取。该项目用 15 个 agent 在 15 条宪法式规则约束下协作产出了 13 个章节。对其协同机制的系统分析（`process/analysis/dot-claude-runtime-collaboration.md`）揭示：这些 agent 不是在「互相调用」——它们运行在一个 7 层系统上。

7 层模型不绑定书籍领域。翻译流水线模板（`translation-pipeline-template/`）是它的第一个垂直实例。这套模板是**上级抽象**——任何需要多 agent 在规则约束下持续产出高质量内容的项目，都可以用它作为起点。

## 快速开始

```bash
git clone https://github.com/yourname/ai-crew-runtime-template.git /tmp/rt
cp -r /tmp/rt/{.claude,scripts,templates,init.sh,AGENTS.md,CLAUDE.md,GEMINI.md} your-project/
cd your-project
chmod +x init.sh
./init.sh --name "My Project" --domain "code-review" --lang en
```

## 7 层架构

```
┌──────────────────────────────────────────────────┐
│ 第 1 层：入口（commands/）                         │
│ 用户 → 系统的桥梁。声明 owner agent。不执行逻辑。      │
├──────────────────────────────────────────────────┤
│ 第 2 层：调度（agents/）                          │
│ 角色定义 + 派遣逻辑。Owns/Does-not-own 硬边界。      │
│ 统一的模型选择。按角色加权的 maxTurns。               │
├──────────────────────────────────────────────────┤
│ 第 3 层：方法（skills/）                          │
│ 可复用决策框架。每个技能定义：可用/薄弱 标准、          │
│ 冲突处理方法、升级条件、边界案例。                     │
├──────────────────────────────────────────────────┤
│ 第 4 层：约束（rules/）                           │
│ 宪法式规则体系。有层级（宪法→框架→工艺→流程→体验→产物）。 │
│ 有作用域。有「为什么存在」。                          │
├──────────────────────────────────────────────────┤
│ 第 5 层：执行（hooks/）                           │
│ 规则→代码的自动栅栏。每次 Write/Edit 触发。          │
│ warn/deny 分级。模式扫描 + 关卡拒绝。                │
├──────────────────────────────────────────────────┤
│ 第 6 层：持久（state/ + agent-memory/）            │
│ 跨 session 连续性。sprint 状态 + 决策记忆。          │
│ SessionStart hook 注入上下文。                     │
├──────────────────────────────────────────────────┤
│ 第 7 层：参考（docs/）                            │
│ 人类可读的快照文档。其声明由 scripts/ 独立验证。      │
└──────────────────────────────────────────────────┘
```

**这些层不是「互相调用」的关系——它们是同一个系统的不同抽象层。** 上层定义意图，下层执行约束：

| 层 | 定义 | 执行 |
|----|------|------|
| rules/ | 「产出必须通过质量关卡」 | hooks/ 每次编辑自动扫描 |
| rules/ | 「产出在 `status: ready` 时必须满足所有条件」 | hooks/ deny 提升操作 |
| agents/ | 「Reviewer 拥有验证，不拥有创作」 | tools 字段限制派遣范围 |
| skills/ | 「质量审查必须覆盖全部维度」 | skill 的决策标准被 agent 执行时遵循 |
| state/ | 「当前 sprint：3 个产出待审查」 | SessionStart hook 在每次新 session 注入上下文 |

## 核心协同机制

### 1. 三位一体（Rule → Hook → Skill）

| 层 | 触发频率 | 审查深度 |
|----|----------|----------|
| **Hook**（自动扫描） | 每次 Write/Edit | 廉价模式匹配——捕获机械违规 |
| **Skill**（深层审查） | 在特定关卡由特定 agent 执行 | 判断级别的违规——需要上下文理解 |
| **Rule**（宪法式约束） | 被 Hook 和 Skill 引用 | 定义什么算违规、为什么 |

Hook 是廉价扫描器，Skill 是深层读取。两者互补：Hook 在任何 agent 都能触发的机械违规上提供全覆盖；Skill 在只有特定角色才能判断的语义违规上提供深度。

### 2. 独立否决权

质量把关人不经过调度链，可直接中止推进。只有项目负责人可推翻。

**为什么：** 如果否决权握在推进产出的同一个人手里，审查就会变成橡皮图章。独立否决权将审查者与被审查者分离——这正是质量控制的核心原则。

### 3. Handoff 作为路由协议

跨 cell 异步交接，显式署名。拒绝嵌套 Agent() 调用跨越 cell 边界。每个产出以 `Handoff: <next-owner>` 结尾。

### 4. 宪法自动同步

单一源文件 → 同步脚本 → 多个目标文件。修改一处，所有目标自动更新。`--check` 模式在验证套件中验证字节级一致性。

### 5. 记忆作为免疫系统

两类记忆：
- **`project_*`**：项目级别的决策和知识
- **`feedback_*`**：agent 收到的纠正反馈

agent 犯错 → 错误记录为 feedback 记忆 → 下次调用时自动加载 → 错误不再重复。这不是提示词优化——这是系统积累免疫记忆。

### 6. 状态文件作为编排中枢

单一的编排状态板追踪所有产出阶段。跨 session 可恢复——状态板是真相源，不是内存状态。SessionStart hook 在每次新 session 注入当前 sprint 上下文。

## 设计原则

1. **证据先于优雅** — 不为了叙事干净而弱化证据
2. **责任跟随控制权** — 不停止在最可见的行为者
3. **保持分类完整** — 区分不同类别，不混为一谈
4. **最强反方论证先于判断** — 每个重要断言必须先面对它的最强反方
5. **清晰交接** — 每个产出声明假设、证据等级、开放问题和下一个负责人
6. **不追求自动化** — 决策署名不可替代；agent 不自动推进关卡

## 目录结构

```
your-project/
├── AGENTS.md                     ← 项目指令（Claude/Codex/Gemini 共用真相源）
├── CLAUDE.md                     ← @AGENTS.md
├── GEMINI.md                     ← @AGENTS.md
├── .claude/
│   ├── settings.json             ← hook 注册 + 权限配置
│   ├── agents/                   ← 角色定义（Owns/Does-not-own + tools + skills）
│   ├── commands/                 ← 用户入口（声明 owner agent，路由请求）
│   ├── skills/                   ← 可复用决策框架
│   ├── rules/                    ← 宪法式规则（层级、作用域、为什么存在）
│   ├── hooks/                    ← 规则自动执行（PostToolUse 扫描器）
│   ├── state/                    ← Sprint 状态（跨 session 持久）
│   ├── agent-memory/             ← 角色独立记忆（决策 + 纠正反馈）
│   └── docs/                     ← 人类可读参考文档
├── scripts/                      ← 验证 + 同步脚本
└── templates/                    ← 初始化时复制到项目的模板文件
```

## 与翻译流水线模板的关系

`translation-pipeline-template/` 是这套模板的一个**垂直实例**——它实例化了 7 层模型中的翻译特定领域：

- commands → `/translate-chapter`, `/review-chapter` 等
- agents → Translator, Reviewer, Glossary Master 等
- skills → 三轴审核方法论
- rules → 翻译特定的 6 条设计原则
- hooks → 翻译质量扫描器
- state → 翻译进度追踪
- docs → 翻译宪法、评分标准

如果你只需要翻译流水线，直接用 `translation-pipeline-template`。如果需要为其他领域搭建多 agent 协作系统，从这套模板开始。

## 何时使用这套模板

- 多 agent 协作产出需要质量控制的内容（书籍、报告、代码库、设计系统）
- 产出需要经过多个独立把关人的审查链
- 跨 session 工作——需要记忆和状态持久化
- 规则需要自动执行而非仅靠 agent 自觉
- 你需要一套架构而不是一堆提示词
