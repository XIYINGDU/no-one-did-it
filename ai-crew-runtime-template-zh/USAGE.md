# 使用指南

## 1. 复制模板到你的项目

```bash
git clone https://github.com/XIYINGDU/ai-crew-runtime-template-zh.git /tmp/rt
# 把所有核心文件复制到你的项目根目录
cp -r /tmp/rt/{.claude,scripts,templates,init.sh,AGENTS.md,CLAUDE.md,GEMINI.md} your-project/
cd your-project
```

## 2. 运行初始化

```bash
chmod +x init.sh
./init.sh --name "你的项目名" --description "一行项目描述"
```

初始化会做五件事：

| 阶段 | 做什么 |
|------|--------|
| 替换占位符 | 所有 `{{项目名称}}`、`{{编排者名称}}` 等标记被替换为实际值 |
| 同步宪法 | 五条核心原则自动传播到所有 agent 和文档 |
| 激活 hooks | 使扫描脚本可执行 |
| 初始化状态 | 写入 `state/current-focus.md` |
| 验证工作区 | 检查目录结构、agent frontmatter、规则完整性 |

## 3. 自定义 agent 名称

四个 agent 的默认名称为 `orchestrator` / `producer` / `reviewer` / `red-team`。可以在初始化时改名：

```bash
./init.sh --name "代码审查系统" \
  --description "多 agent 协作代码审查流水线" \
  --domain code-review \
  --orchestrator dispatcher \
  --producer developer \
  --reviewer auditor \
  --red-team hacker
```

也可以直接修改 `.claude/agents/` 下的文件，按需调整角色描述和派遣逻辑。

## 4. 自定义核心原则

五条默认原则是通用的。可以用你自己的原则覆盖：

```bash
./init.sh --name "我的项目" --description "..." \
  --value1 "测试通过先于功能交付。不为了速度而跳过测试。" \
  --value2 "每个 PR 必须经过至少一人审查。" \
  --value3 "文档和代码同步更新。" \
  --value4 "安全审查先于发布。" \
  --value5 "每个决策记录原因、权衡和负责人。"
```

五条原则写入 `rules/00-core-values.md` 后，`sync_core_values.py` 自动同步到所有 agent 和文档的 `<!-- GENERATED:five-over-rules:start -->` 标记块中。修改原则只需改一处，运行同步脚本即可。

## 5. 定义第一个交付物

编辑 `STATUS.md`，添加一行：

```markdown
| ID | 交付物 | 阶段 | 负责人 | 最后交接 | HARD 发现 | SOFT 发现 |
|----|--------|------|--------|----------|-----------|-----------|
| 01 | 用户认证模块 | 草稿 | developer | — | — | — |
```

## 6. 开始使用

在 Claude Code 中：

```
/status              → 查看当前 sprint 状态
/quality-gate 01     → 对交付物 01 运行完整质量关卡
@developer 实现用户登录功能  → 派遣执行者
@auditor 审查 01 号交付物    → 派遣审查员
@hacker 红队审查 01 号交付物 → 派遣对抗性审查员
```

## 工作流全貌

```
你发出指令
  ↓
/status 或 @orchestrator → 编排者读取状态板，决定下一步
  ↓
@developer → 执行者产出交付物 → 自我审查 → Handoff: auditor
  ↓
@auditor → 审查员验证质量 → A/B/C/D 分级 → Handoff: hacker
  ↓
@hacker → 对抗性审查 → 找弱点、构建反方论证 → Handoff: orchestrator
  ↓
编排者 → 无 HARD 发现 → 提升为 ready
```

每次编辑后，hooks 自动扫描：缺失 schema 字段、未解决的 TODO、禁用措辞——所有机械违规被实时捕获。深度判断由审查员和红队在关卡节点执行。

## 自定义 hooks

`check-deliverable.py` 中的 `SCOPE_RE` 控制扫描哪些路径，`BANNED_ADVERBS` 控制禁用的措辞模式。按你的项目领域修改即可：

```python
# 要扫描的文件（项目相对路径正则）—— 按需修改
SCOPE_RE = re.compile(
    r"^(outputs|deliverables|chapters|src)/.*\.(md|py|js|ts|rs|go)$"
)

# 禁用的替代性副词 —— 添加你项目中的弱断言词
BANNED_ADVERBS = [
    (re.compile(r"\b(clearly|obviously|undeniably)\b", re.IGNORECASE), ...),
]
```

## 目录结构（初始化后）

```
your-project/
├── AGENTS.md              ← 项目指令（Claude/Codex/Gemini 共用真相源）
├── CLAUDE.md              ← @AGENTS.md
├── GEMINI.md              ← @AGENTS.md
├── STATUS.md              ← 交付物状态板（你维护）
├── .claude/
│   ├── agents/            ← 4 个角色（已替换为你的命名）
│   ├── commands/          ← /status + /quality-gate 命令
│   ├── skills/            ← quality-gate 5 维度审查框架
│   ├── rules/             ← 4 条规则（已嵌入你的核心原则）
│   ├── hooks/             ← 自动扫描器（每次 Write/Edit 触发）
│   ├── state/             ← current-focus.md（跨会话持久）
│   └── agent-memory/      ← agent 独立记忆（决策 + 纠正反馈）
├── scripts/               ← sync_core_values.py + validate_workspace.py
└── templates/             ← 交付物 / 决策日志模板
```

## 常见问题

### 初始化后还能改名字吗？

可以。直接编辑 `.claude/agents/` 下对应文件的 `name:` frontmatter 字段，然后确保 `.claude/commands/` 中的 `owner:` 引用一致。运行 `python3 scripts/validate_workspace.py` 检查。

### 怎么添加更多 agent？

在 `.claude/agents/` 下新建 `.md` 文件，按现有 agent 的 frontmatter 格式声明 `name`、`description`、`tools`、`model`、`skills`。如果编排者需要派遣新 agent，更新编排者的 `tools:` 字段。保持 DAG 深度 ≤ 2。

### 怎么添加更多规则？

在 `.claude/rules/` 下新建 `.md` 文件，按现有规则的层级编号（`04-*.md`、`05-*.md`），包含「为什么存在」段落。

### 会话中断了怎么恢复？

SessionStart hook 会自动将 `state/current-focus.md` 注入为新会话的上下文。编排者读取 `STATUS.md` 找到最后完成的阶段，从下一个未完成阶段继续。状态板是真相源——不依赖内存状态。

### HARD 发现怎么解决？

审查员或红队的 HARD 发现会阻止交付物提升为 `ready`。执行者必须逐一回应每个发现。如执行者不同意某个 HARD 发现，升级至编排者。编排者裁决或升级至项目负责人。只有项目负责人可记录推翻。

### 能同时用 Claude Code 和 Codex / Gemini 吗？

`AGENTS.md` 是三种工具共用的唯一真相源——`CLAUDE.md` 和 `GEMINI.md` 都只包含 `@AGENTS.md`。hooks 仅在 Claude Code 中运行（Codex 和 Gemini 的 hook 桥接需额外配置）。
