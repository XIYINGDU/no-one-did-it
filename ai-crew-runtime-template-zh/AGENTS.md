# AI Crew Runtime — 项目指令

> **唯一真相源。** 此文件由 Claude（`CLAUDE.md` → `@AGENTS.md`）、Codex（`AGENTS.md` 直接读取）和 Gemini（`GEMINI.md` → `@AGENTS.md`）共同加载。三种工具共享此上下文。在此编辑；切勿直接编辑 `CLAUDE.md` 或 `GEMINI.md`。

项目：**AI Crew Runtime** — 一个可复用的 7 层多 agent AI 协作运行时。

## 全局五条核心原则

<!-- GENERATED:five-over-rules:start -->
1. **证据先于优雅。不为了产出干净而弱化证据。**
2. **责任跟随控制权、利益、知情和可预防性。不停止在最可见的行为者。**
3. **保持分类完整。区分不同类别，不为叙事便利而混为一谈。**
4. **最强反方论证先于判断。每个重要断言必须先面对它的最强反方论证。**
5. **清晰交接。每个产出必须声明假设、证据等级、开放问题和下一个负责人。**
<!-- GENERATED:five-over-rules:end -->

## 项目结构

- `.claude/agents/` — 角色定义，含 Owns/Does-not-own 边界、tools、skills 和派遣逻辑。
- `.claude/commands/` — 面向用户的 slash 命令。每条命令声明 `owner:` agent 并提供参数提示。命令只做路由，不执行逻辑。
- `.claude/skills/` — 可复用决策框架。每个技能定义可用/薄弱标准、冲突处理、升级条件和边界案例。
- `.claude/rules/` — 宪法式规则层级（价值观 → 框架 → 工艺 → 流程 → 体验 → 产出）。每条规则带有作用域声明和「为什么存在」。
- `.claude/hooks/` — 规则自动执行。PostToolUse hook 在每次 Write/Edit 触发。warn/deny 分级：模式扫描器捕获机械违规；deny 关卡阻止结构违规上的提升。
- `.claude/state/` — 当前 sprint 焦点，由 SessionStart hook 注入为 additionalContext。跨会话连续性。
- `.claude/agent-memory/` — 每个 agent 的独立记忆，包含项目级决策（`project_*`）和纠正反馈（`feedback_*`）。在 agent 激活时加载。
- `.claude/docs/` — 人类可读参考快照。声明由 `scripts/` 独立验证。

## Agent 派遣规则

1. **Owns/Does-not-own 是硬边界。** agent 不可静默地僭取另一 agent 的权限。跨角色工作需要经过产出 schema 中记录的 `Handoff:`。
2. **DAG 深度 ≤ 2。** 编排者派遣到负责人；负责人派遣到执行者。执行者不再向下派遣。
3. **独立否决权。** 对抗性审查员和质量验证员拥有独立于派遣链的中止权限。只有项目负责人可推翻。
4. **Handoff 是路由协议。** 每个交付物以 `Handoff: <下一个负责人>` 结尾。跨 cell 交接全部显式记录。

## 质量关卡

- **证据 / 来源等级：** A（高置信度一手来源）、B（可信二手来源）、C（有争议/不完整）、D（不可作为事实锚点）。
- **对抗性审查：** 每个承重断言在断言之前必须面对其最强反方论证。
- **质量标准扫描：** 自动 hook 在编辑时捕获机械违规；深层读取 skill 在关卡审查时捕获判断级违规。
- **冷读：** 一个冷读 agent——不读简报、不读规则、不读注册表——报告体验感受；HARD 发现阻止提升。

## 共享记忆

**始终只在 `AGENTS.md` 中记录新指令、规则和记忆。**

切勿直接修改 `CLAUDE.md` 或 `GEMINI.md`——它们只导入 `AGENTS.md`。
这保持 Claude Code、Codex CLI 和 Gemini CLI 共享同一上下文。

## 默认交付物 Schema

每个重要产出必须包含：

```text
Owner:
Task:
Evidence grade:
Assumptions:
Open questions:
Handoff:
```
