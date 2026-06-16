# `.claude/` 目录架构分析

> 分析日期：2026-06-16 · 分支：`analysis/dot-agents-architecture` · 作者：duxiying

---

## 零、全景

```
.claude/
├── agents/          (15 个 agent 定义)
├── commands/        (10 个 slash 命令)
├── skills/          (29 个技能)
├── rules/           (15 条规则)
├── hooks/           (9 个 Python hook 脚本)
├── docs/            (12 份参考文档)
├── agent-memory/    (13 个 agent 的持久化记忆)
├── state/           (当前 sprint 状态)
├── output-styles/   (1 个输出风格定义)
├── settings.json          (项目级配置)
└── settings.local.json    (本地覆写)
```

10 个子系统，约 120 个文件。每一个都是为了回答同一个问题而存在：**如何让 15 个 AI agent 协作写一本 13 章的严肃非虚构书，不互相踩脚、不降低证据标准、不让任何一个决策无人认领？**

---

## 一、agents/ — 角色定义系统

### 1.1 文件清单

```
jerry-crew-chief.md              # 调度中心
bonnie-book-architect.md         # 书籍结构
wayne-narrative-lead.md          # 散文写作
delon-research-director.md       # 研究总监
  shirley-historical-case-researcher.md   # 历史案例
  selina-war-statecraft-researcher.md     # 战争/国家
  warren-ai-technology-researcher.md      # AI/技术
  loki-public-law-politics-researcher.md  # 公法/政治
stephen-fact-check-director.md   # 事实核查
  alan-expert-reviewer.md        # 6 域专家审查
laura-red-team-editor.md         # 红队对抗
nancy-legal-risk-counsel.md      # 法律风险
blair-market-strategist.md       # 市场策略
the-reader.md                    # 读者（不在 crew 中）
xiaolai.md                       # 主作者推理替身
```

### 1.2 每个 agent 定义的共同结构

```yaml
---
name: <slug>
description: <when to use>      # 给调用者看的触发条件
tools: <granted tools>          # 精确的工具授权
model: opus                     # 所有 15 个 agent 统一 opus
memory: project                 # 共享项目记忆
maxTurns: <N>                   # 按角色加权
skills: [<list>]                # 加载的项目技能
color: <color>                  # UI 区分
---
# <Role Name> — <Title>

## Global Five Over-Rules        # 自动生成，与源文件同步
## Role definition               # Owns / Does not own
## Output types                  # 该 agent 产出的文档类型
## Operating rules               # 行为约束
## Default response schema       # 输出的强制字段
## Hook policy                   # 适用的 hook
## Example invocation            # 正确用法的具体例子
```

### 1.3 设计要点

**Owns / Does not own 是硬边界。** 每个 agent 的定义中，"Owns" 列出它唯一负责的东西；"Does not own" 列出它不可越权的东西。这不是建议——rule 03（no-overlap role map）规定越权必须跨过 Handoff 记录。

例：Wayne（narrative lead）"Owns: prose, scene construction, transitions, chapter voice, audio-readable rhythm." "Does not own: introduce unverified facts, decide case inclusion, downgrade legal risk, or change evidence grades."

**工具授权是精确的。** 不是所有 agent 都有 Bash，实际上没有 agent 有 Bash。不是所有 agent 都有 WebSearch——只有需要搜索的 agent（researchers + Stephen + Nancy + Laura + Blair + Alan）才有。the-reader 只有 Read/Grep/Glob/Write。

**maxTurns 按角色加权，不是按地位：**

| 角色 | maxTurns | 理由 |
|------|----------|------|
| Jerry（调度中心） | 40 | 跨 cell 排序、冲突解决 |
| Core leads（5人） | 25 | 多步规划/修订循环 |
| the-reader | 22 | 需要全章冷读，但不调度 |
| Nancy / Blair / xiaolai | 20 | 中等深度的有界任务 |
| Researchers（4人）+ Alan | 18 | 研究构建但有明确边界 |

**所有的 model 都是 opus。** 这是主作者的指令："逻辑密集的任务需要更大的模型。crew 不做纯机械工作——每个角色都涉及多步推理、约束下的判断、或矛盾的输入的调和。"

### 1.4 xiaolai 的特殊性

`xiaolai` 不是主作者本人——它是**推理替身**。它的定义明确声明：

> "You are a surrogate that applies his reasoning frame to a decision a crew member has escalated."

它裁决问题但不提交代码、不推分支、不扩展范围。它的工具是**六价值超过规则**（Six Values-Over-Rules）：Independence、First Principles、AI-leverage、Evidence、Steelman、Chain Check。冲突时靠前的值胜出。

### 1.5 the-reader 的特殊性

`the-reader` 是 crew 中**唯一不在 crew 里的 agent**。它不读 brief、不读 rule、不读 case file、不读 registry。它只读最终出版物形式的文本，然后报告体验——"我在这里丢了""这个声明我读到时不买账"。它绝不提修改方案。它的 HARD finding 阻止章节 v3 形式升级。

---

## 二、commands/ — 入口点系统

### 2.1 清单

| 命令 | Owner | 触发 |
|------|-------|------|
| `/book-status` | jerry | 查看书的生产状态 |
| `/case-file` | delon | 为命名事件构建案例文件 |
| `/chapter-brief` | bonnie | 将案例文件转化为章节简报 |
| `/crew-briefing` | jerry | 定义 sprint 工作 |
| `/figure-spec` | bonnie | 图表/表格/责任链图规格 |
| `/photo-clear` | nancy | 照片权限和标题排雷 |
| `/produce-chapter` | jerry | 驱动一章的完整生产管道 |
| `/proposal-pack` | blair | 构建书籍提案包 |
| `/red-team` | laura | 红队攻击案例/章节/声明 |
| `/source-audit` | stephen | 审计证据和源质量 |

### 2.2 设计模式

**每个命令 = 一个 owner agent + 一个 argument-hint。** 命令不执行逻辑——它只是把任务路由给正确的 agent。

例：`/red-team` 的 owner 是 `laura-red-team-editor`，argument-hint 是 `<file-path-or-claim>`。当用户调用 `/red-team book/chapters-v2/03-draft.md §4`，Jerry 把任务 dispatch 给 Laura。

**"/produce-chapter" 是最复杂的命令**——它驱动了 10 阶段的管道：spine 确认 → case file 研究 → Stephen 验证 → 章节简报 → 散文草案 → 红队 → 法律审查 → 事实核查终审 → 主作者签收 → 升级为 ready。每个阶段完成后更新 `book/STATUS.md`，管道在 session 之间可恢复。

---

## 三、skills/ — 可复用方法论

### 3.1 清单（29 个技能）

| 分类 | 技能 | 用途 |
|------|------|------|
| **研究方法** | case-file-method | 构建责任洗涤案例文件 |
| | counter-case-method | 为每个案例构建配对反例 |
| | responsibility-chain-mapping | 映射控制/利益/知识/可预防性链 |
| | primary-source-playbooks | 一手来源查找和验证 |
| | source-ledger-discipline | 维护源帐本 |
| | evidence-grading | A/B/C/D 证据等级判定 |
| | taxonomy-classification | 四类替罪羊分类 |
| **写作工艺** | chapter-blueprint | 章节结构脚手架 |
| | scene-construction | 场景写作 |
| | defamation-wording | 法律安全措辞 |
| **审计** | callback-audit | 跨章节回调一致性 |
| | cognitive-arc-audit | 读者认知弧 |
| | contract-audit | 章节合同交付验证 |
| | dependency-check | 声明依赖关系 |
| | implication-audit | 结构性隐含负担（rule 07） |
| | motif-audit | 母题追踪 |
| | voice-register-audit | 声音一致性 |
| | cite-density-audit | 引用密度和格式 |
| | citation-hygiene | 引用卫生 |
| | pronoun-discipline-audit | 代词纪律（rule 14） |
| | chapter-defect-diagnose | 章节缺陷诊断 |
| **读者** | reader-cold-read | 单章冷读 |
| | reader-experience-sweep | 全书体验扫描 |
| **生产** | kdp-epub | Kindle EPUB 构建和验证 |
| | publication-proposal | 出版提案包 |
| | contract-change-control | 合同变更控制 |
| | research-card-pipeline | 研究卡片管道 |
| **基础设施** | vocabulary | 术语表（由 NLPM 使用，非 agent 直接调用） |

### 3.2 每个技能的标准结构

```yaml
---
name: <slug>
description: <one-line>
version: 1.0.0
---
# <Skill Name>

## Global Five Over-Rules    # 自动生成
## Decision rubric           # Usable output / Weak output
## Conflict handling         # 多源冲突的裁决方法
## Escalation conditions     # 触发 Handoff 到哪个 agent
## Boundary-case recipes     # 边缘案例的处理方法
```

### 3.3 设计思想

技能是**可复用的方法论胶囊**。它们不是一次性 prompt——每个技能定义了一个决策框架（usable/weak 的判定标准）、冲突处理方法、和升级条件。

技能的加载是通过 agent 的 `skills:` frontmatter 字段声明的。一个 agent 有哪些技能，决定了它被调用时加载哪些方法论。例：Wayne 加载 `chapter-blueprint`、`scene-construction`、`defamation-wording`——他不需要 `evidence-grading`（那是 Stephen 的技能）。

---

## 四、rules/ — 宪法式约束体系

### 4.1 编号体系

```
00 — 五大原则（宪法级）
01 — 案例分类法
02 — 证据等级
03 — 角色不可重叠 + 否决权
04 — 风格指南
05 — 过度声明语言（banned verbs）
06 — 引用完整性
07 — 隐含负担（结构性过度推断）
08 — 处理等级纪律
09 — 改写生命周期
12 — 读者体验价值观
13 — 引用形式（Chicago 17th）
14 — 作者站位与代词纪律
15 — 读者体验权威
16 — KDP EPUB 生产
```

编号不连续（11 缺失）——可能是重新编号或合并的结果。

### 4.2 规则的层级结构

| 层级 | 规则 | 依赖关系 |
|------|------|----------|
| 宪法 | 00 | 无上级 |
| 框架 | 01, 02, 03 | 依赖 00 |
| 工艺 | 04, 05, 06, 07 | 依赖 02, 03 |
| 流程 | 08, 09, 15 | 依赖 02, 03, 12 |
| 体验 | 12, 13, 14 | 依赖 04, 05, 06, 07 |
| 产物 | 16 | 依赖 03, 12, 13 |

### 4.3 规则的设计特征

**有 scope（作用域）。** 每条规则声明约束哪些目录。rule 05 约束 `book/chapters-v2/`、`book/evidence/case-files/`、`process/review-memos/`、`book/proposals/`。

**自动同步。** 五大原则（rule 00）通过 `sync_five_over_rules.py` 同步到 agents、skills、commands、docs——所有 `<!-- GENERATED:five-over-rules:start -->` 块。修改 rule 00 后，运行脚本，28 个目标自动更新。`--check` 模式验证字节级一致性。

**有代码强制执行。** rule 05（banned verbs）→ `scan-overclaim.py` hook。rule 07（implication）→ `scan-implication.py`。rule 13（citation density）→ `scan-cite-density.py`。rule 14（pronoun discipline）→ `scan-pronoun-discipline.py`。每次 Write/Edit 后自动扫描。

**有独立否决权。** rule 03 赋予了 Laura 和 Nancy 独立否决权——不经过 Jerry 的调度链。

---

## 五、hooks/ — 自动化栅栏

### 5.1 9 个 hook 脚本

| Hook | 类型 | 触发时机 | 模式 |
|------|------|----------|------|
| `session-context.py` | SessionStart | 每个新 session | 注入 sprint 上下文 |
| `guard-destructive-bash.py` | PreToolUse | Bash 执行前 | 拦截危险命令 |
| `check-agent-frontmatter.py` | PostToolUse | Write/Edit 后 | warn + deny（章节提升时） |
| `scan-overclaim.py` | PostToolUse | Write/Edit 后 | warn |
| `scan-implication.py` | PostToolUse | Write/Edit 后 | warn |
| `scan-cite-density.py` | PostToolUse | Write/Edit 后 | warn |
| `scan-pronoun-discipline.py` | PostToolUse | Write/Edit 后 | warn |
| `scan-kdp-epub-css.py` | PostToolUse | Write/Edit 后 | warn |
| `log-subagent-finish.py` | SubagentStop | 子 agent 完成后 | 记录 |

### 5.2 关键设计细节

**大部分是 warn 模式，只有一个是 deny。** `check-agent-frontmatter.py` 默认 warn，但在一个窄条件下 deny：**如果一章被编辑后持久化为 `status: ready` 但缺少节奏段，操作被拒绝。** 这意味着你不能绕过章节提升门——即使你用 Write 工具直接覆盖整个文件。

**实现方式是"最终状态检查"而非"diff 检查"。** hook 读取编辑后的文件内容，而不是对比 before/after diff。这防止了用 Write 工具绕过 Edit/MultiEdit 的扫描。

**session-context.py 是 SessionStart hook**——它读取 `.claude/state/current-focus.md` 并将内容注入为 `additionalContext`，所以每个新 session 都知道当前 sprint 的状态。

---

## 六、docs/ — 参考文档层

| 文件 | 性质 |
|------|------|
| `crew-portfolio.md` | agent 名册，包含调度图和调用指引 |
| `book-production-workflow.md` | 10 阶段生产管道 |
| `crew-operating-manual.md` | 操作手册 |
| `agent-role-map.md` | 角色映射 |
| `agent-tool-grants.md` | 工具授权策略 |
| `hooks-guide.md` | hook 使用指南 |
| `workflow.md` | 工作流 |
| `case-card-template.md` | 案例文件模板 |
| `chapter-template.md` | 章节模板 |
| `source-ledger-template.md` | 源帐本模板 |
| `reader-value-template.md` | 读者价值模板 |
| `references.md` | 参考资料 |

这些文件是**快照文档**——它们描述系统当前状态，但 canonical 源仍在 agent frontmatter、rules、和代码中。如 `crew-portfolio.md` 所说："This document is a hand-written snapshot. The structural claims it makes are independently verifiable."

---

## 七、agent-memory/ — 持久化记忆系统

### 7.1 目录结构

每个 agent 有一个子目录，包含 `MEMORY.md`（记忆索引）和若干 `project_*/feedback_*` 文件（具体记忆）。

例：
```
agent-memory/
  bonnie-book-architect/
    MEMORY.md
    project_ch2_anchors.md
    project_ch7_architecture.md
    project_downstream_pure_scapegoat_gate.md
    ...
  jerry-crew-chief/
    MEMORY.md
    feedback_research_gloss_attribution.md
    project_xiaolai_surrogate_substitution.md
    ...
```

### 7.2 设计意图

这是一个**按项目组织的文件级记忆系统**。agent 的 frontmatter 中 `memory: project` 字段激活了它。记忆分为两类：
- `project_*` — 项目级别的决策和知识
- `feedback_*` — agent 收到的纠正反馈

记忆文件在 agent 被调用时注入 context，确保关键决策在 session 之间不丢失。

---

## 八、state/ + output-styles/ — 运行上下文

### 8.1 state/current-focus.md

当前 sprint 的快照——包含待办事项、定时重审时钟、开放证据线索。被 `session-context.py` hook 在每次 SessionStart 时读取并注入。

### 8.2 output-styles/book-architect-mode.md

定义了 agent 输出的默认风格：精确、基于证据、不确定性别隐藏、角色特定的 Handoff、拒绝模糊的鼓励性语言。

```markdown
Conforming:
> The chapter has two A-grade case files but no fact-check sign-off on the third.
> Handoff: Stephen → Laura.

Non-conforming:
> Great question! You might want to think about adding more sources.
```

---

## 九、settings.json + settings.local.json — 配置层

### settings.json

- `hooks` — 注册 4 类 hook（SessionStart、PreToolUse、PostToolUse、SubagentStop）
- `enabledPlugins` — `cc-suite@xiaolai`（跨工具桥接）、`nlpm@xiaolai`（词汇评分）
- `outputStyle` — `book-architect-mode`
- `permissions.defaultMode` — `bypassPermissions`（信任该项目）

### settings.local.json

```json
{"disabledMcpjsonServers": ["codex-cli"]}
```

仅禁用了一个 MCP 服务器——本地开发覆盖。

---

## 十、贯穿所有子系统的设计模式

### 10.1 自动生成的五大原则块

从 `agents/` 到 `skills/` 到 `docs/`，所有文件包含：

```
<!-- GENERATED:five-over-rules:start -->
1. Evidence before elegance...
...
<!-- GENERATED:five-over-rules:end -->
```

由 `scripts/sync_five_over_rules.py` 生成和验证。确保修改单一源（rule 00）后，28 个目标文件自动同步。`pytest` 中有对应的验证测试。

### 10.2 Owns / Does not own 的角色边界

每个 agent 定义、rule 03（角色图）、和 `agent-tool-grants.md` 共同构成了一个**三层验证的角色边界系统**：
1. Agent frontmatter 中的 `tools:` 字段（技术层：实际能调用的工具）
2. Agent 定义中的"Owns / Does not own"（语义层：该做什么不该做什么）
3. `check_agent_graph.py`（验证层：DAG 无环、深度 ≤ 2）

### 10.3 Handoff 作为跨 cell 路由协议

每个 agent 的输出必须包含 `Handoff:` 字段，命名下一个负责的 agent。这是跨 cell 的异步路由通道——不通过嵌套 `Agent()` 调用。

### 10.4 代码强制执行，不只是文档

15 条规则中，至少 5 条有对应的 Python hook 脚本在每次文件编辑后自动扫描。规则不是"写得很漂亮但没人检查"。

### 10.5 每个子系统都有一个验证器

| 子系统 | 验证方式 |
|--------|----------|
| agents/ | `check_agent_graph.py`、`check_tool_grants.py`、`check-agent-frontmatter.py` hook |
| rules/ | `sync_five_over_rules.py --check` |
| skills/ | NLPM spec check（`check_nlpm_specs.py`） |
| 源帐本 | `validate_source_ledger.py` |
| 读者报告 | `check_reader_reports.py` |
| 图表 | `validate_diagram_artifact.py` |
| EPUB | epubcheck + Kindle Previewer |

---

## 十一、总结

`.claude/` 目录是一个**为 15 个 AI agent 协作写一本书而设计的操作系统**。它的核心架构思想：

1. **角色不可重叠。** 每个 agent 有一个细胞（cell），有明确的 Owns/Does not own 边界。越权必须通过 Handoff 记录。

2. **规则是宪法式的。** 有顶层原则（00）、具体约束（01-16）、代码强制执行（hooks）、和可验证的一致性保证（sync script）。

3. **管道是可恢复的。** 10 阶段的生产状态保存在 `book/STATUS.md` 中，session 中断后从上次停止的地方继续。

4. **否决权是独立的。** Laura、Nancy、the-reader 的否决权不经过 Jerry 的调度链——直接中止章节升级。

5. **书籍本身诊断的模式就是系统设计的约束。** 角色不可重叠（防止责任扩散）、symlink 而非副本（防止多源不同步）、独立否决权（防止"自己审查自己通过"）——这些设计决定都来自同一个根命题。

---

Owner: duxiying
Task: 分析 `.claude/` 目录的完整架构
Inputs reviewed: `.claude/agents/`（15个）、`.claude/commands/`（10个）、`.claude/skills/`（29个）、`.claude/rules/`（15个）、`.claude/hooks/`（9个）、`.claude/docs/`（12个）、`.claude/agent-memory/`、`.claude/state/`、`.claude/output-styles/`、`settings.json`、`settings.local.json`
Evidence grade: A
Assumptions: 无
Open questions: 无
Handoff: 文档在 `process/analysis/dot-claude-architecture.md`
