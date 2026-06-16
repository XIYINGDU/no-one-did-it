# `.claude/` 运行时协同分析

> 分析日期：2026-06-16 · 分支：`analysis/dot-agents-architecture` · 作者：duxiying

---

## 零、问题

`.claude/` 下有 10 个子系统、~120 个文件。它们各自解决了什么问题？当一条命令被执行时，它们如何协同？为什么这种协同不是巧合而是设计？

---

## 一、一场具体的运行时旅程：`/produce-chapter 04`

### 第一步：命令 → 路由

用户键入 `/produce-chapter 04-the-proxy-and-the-sponsor`。

`commands/produce-chapter.md` 被读取。它的 frontmatter 声明 `owner: jerry-crew-chief`。命令本身不执行逻辑——它只是一个**路由入口**。命令文件的作用是：(a) 声明哪个 agent 处理该任务，(b) 提供 argument-hint，(c) 包含正确调用的示例。执行被委托给 owner agent。

### 第二步：Agent 加载上下文

Jerry（`agents/jerry-crew-chief.md`）被激活。系统同时注入三层上下文：

| 注入来源 | 内容 | 作用 |
|----------|------|------|
| `skills` frontmatter 字段 | 7 个技能（`case-file-method`、`chapter-blueprint` 等）的方法论 | Jerry 知道每个任务可用的决策框架 |
| `rules/` 目录 | 15 条宪法式规则 | Jerry 知道每一步必须遵守的约束 |
| `agent-memory/jerry-crew-chief/MEMORY.md` | 记忆索引，链接到 6 个具体记忆文件 | Jerry 记得之前的决策——Part III 排序、gloss 归因触发线、surrogate 替代模式 |

Jerry 读取 `book/STATUS.md` 确认 ch-04 状态，然后按 `docs/book-production-workflow.md` 定义的 10 阶段管道推进。

### 第三步：派遣子 Agent — 角色边界激活

Jerry 派遣 `delon-research-director`。这时 rule 03 的角色边界被激活：

- Delon 的 agent 定义声明 `Owns: 研究系统、案例文件质量、来源包标准` 和 `Does not own: 撰写最终章节、做出法律结论`
- Delon 的工具是 `Agent(shirley, selina, warren, loki)` — 他可以派遣这 4 位研究员，但不能再往下派生
- Delon 判断 ch-04 涉及战争/国家策略领域，派遣 `selina-war-statecraft-researcher`

**协同点：** agent 的 `Owns/Does not own` 边界 + `tools:` 字段 + DAG 深度限制（≤ 2）共同构成了**运行时角色隔离**。Delon 不能写散文，Selina 不能设计书脊，Jerry 不能做事实核查。

### 第四步：技能执行 — 方法论激活

Selina 被调用后，她的 skills 被加载到上下文中。她按以下顺序使用它们：

1. `primary-source-playbooks` → 知道 OHCHR、ICC 案卷、ICRC 评注是该领域的最高权威来源
2. `case-file-method` → 按结构化模板构建案例文件（八个诊断问题 + 证据等级）
3. `evidence-grading` → 每个承重声明走完五步决策树（来源类型 → 佐证数量 → 程序阶段 → 利益相关方 → 活跃事件）
4. `responsibility-chain-mapping` → 绘制公共链 vs 责任链，记录每个行动者的控制/利益/知情/可预防性
5. `counter-case-method` → 为每个替罪羊案例构建配对反方案例（四种拦截类型）

她输出 `book/evidence/case-files/mh17-case-card.md`，以 `Handoff: Stephen（事实核查）` 结尾。

### 第五步：Hooks 自动触发 — 规则执行

文件写入时，`settings.json` 注册的所有 PostToolUse hooks **全部自动运行**：

```
Write mh17-case-card.md
  → check-agent-frontmatter.py   —— 验证 agent frontmatter 格式
  → scan-overclaim.py            —— 扫描 "knew""lied""guilty" 等禁用动词
  → scan-implication.py          —— 扫描结构性隐含（匿名链条、链梯等）
  → scan-cite-density.py         —— 检查 [CITE:] 标记是否仅含 slug
  → scan-pronoun-discipline.py   —— 检查 "you""this chapter" 等违规
```

**协同点：** rules/ 不是"写下来就完了"。hooks/ 是 rules/ 的代码执行层。Rule 05（过度声明语言）→ `scan-overclaim.py`。Rule 07（隐含负担）→ `scan-implication.py`。Rule 13（引用形式）→ `scan-cite-density.py`。Rule 14（作者站位）→ `scan-pronoun-discipline.py`。**每次编辑后，规则被自动验证。** 这是从文档约束到可执行栅栏的降层。

### 第六步：关卡链 — 多角色串联验证

案例文件沿着关卡链流转，每个关卡由一个不同角色拥有：

```
Selina（来源包）
  ↓ Handoff
Stephen（事实核查：A/B/C/D 分级）
  ↓ 派遣 Alan，指定 IHL 领域框架
Alan（验证战争法声明对照日内瓦/罗马规约）
  ↓ Handoff
Laura（红队："最强反方论证是什么？"）
  ↓ Handoff
Nancy（法律审查："在世个人措辞是否匹配程序阶段？"）
  ↓ Handoff
Bonnie（架构："这个案例在章节中占据什么位置？"）
  ↓ Handoff
Wayne（散文："将案例文件转化为叙事散文"）
  ↓ Handoff
Stephen + Laura + Nancy（对草稿的最终审查）
  ↓ Handoff
Jerry（提升为 status: ready）
```

**每一步都以 `Handoff:` schema 字段结尾。** agent 定义中的 "Default response schema" 将其设为强制字段。跨 cell 交接全部显式记录——这本身就是 rule 05（清晰交接）+ rule 03（不可重叠角色）的运行时执行。

### 第七步：状态持久化 — 可恢复性

每个阶段完成后，Jerry 更新 `book/STATUS.md`。Session 中断后：

1. 下一个 session 启动时，`session-context.py` hook 读取 `state/current-focus.md` 并注入为 `additionalContext`
2. Jerry 读取 `book/STATUS.md` 找到上次中断的阶段
3. `scripts/check_agent_graph.py` 验证 agent 图仍然无环、深度 ≤ 2
4. 管道从下一个未完成阶段继续

### 第八步：跨 Session 记忆 — 决策连续性

关键决策存入 `agent-memory/`。例如，当 Bonnie 在设计阶段发现 "ch-4 的分析锚点（Crimea）不应是按时间顺序的开场（MH17 更早但锚点是 Crimea 的代理-赞助者映射）"，这个决策被写入 `agent-memory/bonnie-book-architect/project_ch4_part2_opener.md`。下次 Bonnie 被调用，她的 `MEMORY.md` 索引将这个文件加载到上下文中。

**协同点：** agent-memory 是跨 session 的"免疫记忆"。没有它，每次新 session 都会丢失之前的决策，agent 会重复犯错（如将相近数字混淆的 gloss 归因错误被记录在 `jerry-crew-chief/feedback_research_gloss_attribution.md` 中，后续派遣的研究人员会加载此记忆并避免同样的错误）。

---

## 二、系统分层模型

上述旅程揭示了 `.claude/` 的 **7 层架构**：

```
┌──────────────────────────────────────────────────┐
│ 第 1 层：入口（commands/）                         │
│ 用户 → 系统的桥梁。声明 owner agent。不执行逻辑。      │
├──────────────────────────────────────────────────┤
│ 第 2 层：调度（agents/）                          │
│ 角色定义 + 派遣逻辑。Owns/Does-not-own 硬边界。      │
│ 统一的 opus 模型。按角色加权的 maxTurns。            │
├──────────────────────────────────────────────────┤
│ 第 3 层：方法（skills/）                          │
│ 可复用决策框架。每个技能定义：Usable/Weak 标准、       │
│ 冲突处理方法、升级条件、边界案例处理。                 │
├──────────────────────────────────────────────────┤
│ 第 4 层：约束（rules/）                           │
│ 宪法式规则体系。有层级（宪法→框架→工艺→流程→体验→产物）。 │
│ 有作用域（scope）。有"为什么存在"。                   │
├──────────────────────────────────────────────────┤
│ 第 5 层：执行（hooks/）                           │
│ 规则→代码的自动栅栏。每次 Write/Edit 触发。          │
│ 5 个 warn-mode 扫描器 + 1 个 deny 关卡。            │
├──────────────────────────────────────────────────┤
│ 第 6 层：持久（state/ + agent-memory/）            │
│ 跨 session 连续性。sprint 状态 + 决策记忆。          │
│ SessionStart hook 注入上下文。                     │
├──────────────────────────────────────────────────┤
│ 第 7 层：参考（docs/）                            │
│ 人类可读的快照文档。其声明由 scripts/ 独立验证。      │
└──────────────────────────────────────────────────┘
```

**这些层不是"互相调用"的关系——它们是同一个系统的不同抽象层。** 上层定义意图，下层执行约束：

| 层 | 定义 | 执行 |
|----|------|------|
| rules/ | "不得使用 `knew` 无引用" | hooks/ 每次编辑自动扫描 |
| rules/ | "章节在 `status: ready` 时必须包含所有节奏段落" | hooks/ deny 提升操作 |
| agents/ | "Stephen 拥有验证，不拥有论证设计" | tools 字段不授予 WebSearch（如不需要） |
| skills/ | "可用产出必须映射全部六个链维度" | case-file-method 的决策标准被 agent 执行时遵循 |
| state/ | "当前 sprint：后章节剩余工作" | SessionStart hook 在每次新 session 注入上下文 |

---

## 三、关键协同机制

### 3.1 五大原则的自动同步

`rules/00-five-values.md` 是宪法源文件。`scripts/sync_five_over_rules.py` 将其自动同步到所有包含 `<!-- GENERATED:five-over-rules:start -->` 标记的 28 个目标文件中——涵盖 agents、skills、docs、rules。修改单一源文件后，运行脚本，所有目标自动更新。`--check` 模式在 pytest 中验证字节级一致性。

**为什么是设计而非偶然：** 如果五大原则分散在 28 个文件中手动维护，任何单点修改都会导致不同步。自动同步消除了这个问题——28 个文件是**一个源**的生成视图。

### 3.2 Handoff 作为跨层路由协议

每个 agent 的产出以 `Handoff: <next-agent>` 结尾。这不仅仅是文档约定——它是跨 cell 的异步路由通道。没有嵌套的 `Agent()` 调用跨越 cell 边界。agent 的 DAG 深度 ≤ 2，且叶子节点（Wayne、Bonnie、Laura、Nancy、Blair）不派生子 agent，因此 Handoff 是唯一的信息传递机制。

### 3.3 Hooks/规则/技能的三位一体

| 规则 | Hook（自动执行） | 技能（深层审查） |
|------|-------------------|-------------------|
| Rule 05（过度声明） | `scan-overclaim.py`（每次编辑） | `defamation-wording`（法律审查时） |
| Rule 07（隐含负担） | `scan-implication.py`（每次编辑） | `implication-audit`（红队/事实核查时） |
| Rule 13（引用形式） | `scan-cite-density.py`（每次编辑） | `cite-density-audit`（全书编译前） |
| Rule 14（作者站位） | `scan-pronoun-discipline.py`（每次编辑） | `pronoun-discipline-audit`（红队/起草时） |

Hook 是廉价的模式层扫描——每次编辑后立即运行。技能是深层读取——在特定关卡由特定 agent 执行。两者互补：Hook 捕获机械违规（"有一个 `knew` 没有 `[CITE:]`"），技能捕获判断级别的违规（"这个段落的视点聚焦隐含了记录不支撑的知情"）。

### 3.4 否决权的独立性

Rule 03 赋予 Laura 和 Nancy 独立否决权——它们不经过 Jerry 的调度链。如果 Laura 检测到 V1/V3/V8 倒退，她可以直接中止章节改写周期。如果 Nancy 检测到 rule-05 或 rule-07 的诽谤风险面，她同样可以直接中止。只有 xaiolai 可以推翻。Rule 15 赋予 the-reader 对 v3 出版物形式的同等否决权。

**这是对"责任洗涤"的免疫设计：** 如果否决权握在推进改写的同一个人手里（Jerry），审查就会变成橡皮图章。独立否决权将审查者与被审查者分离——这正是本书诊断的原则在系统内部的实现。

### 3.5 状态文件作为编排中枢

`book/STATUS.md` 是唯一的编排状态板。每章的 10 个阶段各有自己的列（Brief→Draft→Stephen→Nancy→Alan→Laura→Bonnie→Principal→Jerry→State）。`/produce-chapter` 读取它来确定下一个未完成阶段。跨 session 可恢复：状态板是真相源，不是内存状态。

`state/current-focus.md` 是 sprint 级的快照——待办事项、定时时钟、开放证据线索。`session-context.py` hook 在 SessionStart 将其注入为附加上下文。

### 3.6 Agent 记忆作为免疫系统

`agent-memory/` 存储两类记忆：

- **`project_*`：** 项目级别的决策和知识（"Part III 排序已授权"、"下游纯粹替罪羊锚点关卡"）
- **`feedback_*`：** agent 收到的纠正反馈（"gloss 归因触发线"、"信条 gloss 必须归因"）

当一个 agent 犯了错误，该错误作为 `feedback_*` 记忆被记录下来。下次该 agent 被调用时，记忆被加载，错误不再重复。**这不是提示词优化——这是系统在积累免疫记忆。**

---

## 四、为什么这种协同不是巧合

上述协同机制都是从一个根命题推导出来的：**"书籍诊断的责任洗涤模式不能出现在生产系统内部。"**

| 诊断的外部模式 | 系统的内部免疫 |
|----------------|----------------|
| 通过程序距离分离控制者和代价承担者 | 角色不可重叠（rule 03）——每个细胞有一个指名的负责人 |
| 用可见替罪羊遮盖真实责任链 | 独立否决权（rule 03 修正）——审查者独立于推进者 |
| 弱证据被叙事技术硬化 | 隐含负担规则（rule 07）+ hooks 自动扫描 |
| 制度"修复"无声覆盖原始记录 | 改写生命周期快照（rule 09）——永不覆盖先前的审计 |
| 委员会使控制不可见 | 单一关卡负责人——Nancy 是照片权利的单一 go/no-go |
| 跨工具不一致成为责任扩散的温床 | Symlink 桥接——技能只有一份，AGENTS.md 是唯一真相源 |
| 作者-读者语言距离制造权威假象 | 代词纪律（rule 14）——"我们"而非"你"/"读者" |

---

## 五、局限与结构性张力

1. **Hooks 的 warn-only 模式。** 7 个 PostToolUse hook 中 6 个是 warn-mode——它们报告问题但不阻止操作。只有 `check-agent-frontmatter.py` 在 `status: ready` + 缺失节奏段落时 deny。这是有意设计（允许创作过程中的中间状态），但依赖人工对 warn 消息的行动。

2. **Agent 记忆的负载边界。** 当每个 agent 积累大量记忆时，上下文注入的量会增长。目前 ~47 个记忆文件尚可管理；如果增长到数百个，可能需要记忆检索的相关性过滤。

3. **单点编排瓶颈。** Jerry 是所有管道的必经之路。如果 Jerry 的上下文因调度复杂性而饱和（maxTurns 40），编排本身可能成为瓶颈。

4. **Codex/Gemini 桥接不完整。** 7 个 hook 中仅 3 个被桥接到 Codex（`.codex/hooks.json`），Gemini hooks 完全为空。使用 Codex 或 Gemini 时会失去部分自动化栅栏。

---

Owner: duxiying
Task: 分析 `.claude/` 目录下各子系统如何协同工作
Inputs reviewed: `.claude/` 全部 10 个子系统，`AGENTS.md`，`book/STATUS.md`，`process/analysis/dot-claude-architecture.md`
Evidence grade: A（分析基于项目一手文件）
Open questions: 无
Handoff: 文档在 `process/analysis/dot-claude-runtime-collaboration.md`
