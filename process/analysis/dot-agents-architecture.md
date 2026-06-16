# `.agents` 目录架构分析

> 分析日期：2026-06-16 · 分支：`analysis/dot-agents-architecture` · 作者：duxiying

---

## 一、`.agents` 目录的物理形态

```
.agents/
  skills → ../.claude/skills    # symlink
```

就这一个符号链接。没有配置文件，没有 agent 定义，没有 hook。

**但这恰好是它的设计意图所在。** `.agents` 不是一个"内容目录"——它是一个**桥接 slot（bridge slot）**，由 `cc-suite@xiaolai` 插件在启用时填充。

---

## 二、三工具桥接架构全景

这个项目设计为**三种 AI 编码工具共享同一份上下文**：

```
                    AGENTS.md（唯一真相源）
                    /       |        \
                   /        |         \
              CLAUDE.md  被直接读取  GEMINI.md
            (@AGENTS.md)   (Codex)    (@AGENTS.md)
               /            |            \
          Claude Code    Codex CLI    Gemini CLI
             |               |             |
      .claude/          .agents/       .gemini/
      .claude/settings.json  .codex/   .gemini/skills/
      .claude/agents/     .codex/hooks.json  .gemini/commands/
      .claude/skills/     .codex/config.toml
      .claude/rules/      .codex/prompts/
      .claude/hooks/
      .claude/commands/
```

**核心设计原则：AGENTS.md 是唯一真相源。** CLAUDE.md 和 GEMINI.md 都只是一行 `@AGENTS.md` import。三个工具共享同一套项目指令。

---

## 三、`.agents` 的具体角色：Codex CLI 的 skill 扫描路径

Codex CLI 的技能系统与 Claude Code 不同：

| 工具 | 技能扫描路径 | 技能格式 |
|------|-------------|----------|
| Claude Code | `.claude/skills/` | `SKILL.md` + frontmatter |
| Codex CLI | `.agents/skills/` | 同格式（通过 symlink 桥接） |
| Gemini CLI | `.gemini/skills/` | TOML 格式 |

**`.agents/skills → ../.claude/skills` 这个 symlink 的作用**：让 Codex CLI 能够直接看到 Claude Code 的 14 个项目技能，而不需要维护两份副本。

这是 `cc-suite@xiaolai` 插件的 `/cc-suite:bridge-skills` 命令创建的。AGENTS.md 第 86 行明确指出：

> `.claude/skills/cc-suite/`  symlink (→ `~/.claude/plugins/cache/xiaolai/cc-suite/<ver>/skills/cc-suite`) installed by `/cc-suite:bridge-skills` so Codex sees plugin-provided sub-skills via `.agents/skills`.

---

## 四、`.codex/` — Codex CLI 的完整桥接配置

### 4.1 `config.toml`

```toml
# cc-suite: generated-by-init
# Codex CLI reads AGENTS.md as the project document.
# project_doc_fallback_filenames = ["CLAUDE.md"]  # 注释掉了：不需要回退

# MCP 服务器桥接
[mcp_servers.claude-code]
command = "npx"
args    = ["-y", "claude-octopus@1.0.0"]
```

设计要点：
- Codex 直接读 `AGENTS.md` 作为项目文档——不需要像 Claude 那样的 `CLAUDE.md` → `@AGENTS.md` 间接引用
- MCP 服务器由 `/cc-suite:bridge-mcp` 从 `.mcp.json` 镜像过来
- `project_doc_fallback_filenames` 被注释掉：不需要回退到 `CLAUDE.md`

### 4.2 `hooks.json`

这是 `.claude/settings.json` 的**精选子集**——只桥接了三个 hook：

| Hook | 类型 | 用途 |
|------|------|------|
| `session-context.py` | SessionStart | 注入当前 sprint 上下文 |
| `guard-destructive-bash.py` | PreToolUse | 防止危险 Bash 命令 |
| `check-agent-frontmatter.py` | PostToolUse | 验证 agent 文件 frontmatter |
| `scan-overclaim.py` | PostToolUse | 标记 banned verbs（rule 05） |

**不在 Codex 侧的 hook**（仅在 Claude Code 侧运行）：
- `scan-implication.py`（rule 07）
- `scan-cite-density.py`（rule 13）
- `scan-pronoun-discipline.py`（rule 14）
- `scan-kdp-epub-css.py`（rule 16）
- `log-subagent-finish.py`

这说明 Codex 的 hook 桥接是**选择性**的：只桥接最关键的守卫（agent 格式、危险命令、启动上下文、过度声明扫描），而非全部 7 个 hook。

### 4.3 `prompts/` — 空 slot

`.codex/prompts/.gitkeep` 只有一个占位文件。AGENTS.md 明确说明：

> slot for Codex slash-command prompts (empty by default; populate only when Codex slash-command bridging is required)

**设计意图：** 如果将来需要为 Codex CLI 创建 slash 命令，直接放到这里。不是每个项目都需要——所以默认留空。

---

## 五、`.gemini/` — Gemini CLI 的桥接 slots

```
.gemini/
  commands/.gitkeep    # Gemini 命令 slot（空）
  skills/.gitkeep      # Gemini 技能 slot（空）
```

**两个都是空的。** 原因在 AGENTS.md 第 126 行：

> Optional: Codex CLI and Gemini CLI. Their bridge slots (`.codex/`, `.gemini/`, `.agents/`) are populated by the `cc-suite` plugin when enabled; they stay empty otherwise.

当前项目只启用了 Claude Code 作为主要工作工具。如果将来启用了 Gemini CLI，`/cc-suite:bridge-skills` 命令会填充这些目录。

---

## 六、`.mcp.json` — 跨工具的 MCP 服务器注册

```json
{
  "mcpServers": {
    "codex-cli": {
      "type": "stdio",
      "command": "codex",
      "args": ["mcp-server"]
    }
  }
}
```

这个文件被所有三个工具共享。当前只注册了一个 MCP 服务器——`codex-cli`，它暴露 Codex CLI 的 MCP 接口给 Claude Code 使用。

---

## 七、桥接架构的设计思想总结

### 7.1 问题

三种 AI 工具各有自己的配置格式、技能系统、hook 机制、和 context 加载方式。如果每个都单独配置：

- 规则需要三份（`.claude/rules/` + `.codex/rules/` + `.gemini/rules/`）
- 技能需要三份不同格式的实现
- 每次规则变更需要在三个地方同步
- 实际上是**三个独立的项目**，只是碰巧在做同一本书

### 7.2 解决方案

**分层桥接**：

| 层级 | 策略 | 存放位置 |
|------|------|----------|
| **共享内容** | 一个文件，所有工具读 | `AGENTS.md` |
| **工具原生内容** | 保持在工具自身的配置格式下 | `.claude/`（完整功能）, `.codex/`（精选子集）, `.gemini/`（占位） |
| **技能** | Symlink 桥接，避免维护两份 | `.agents/skills → .claude/skills` |
| **MCP** | 共享注册表 | `.mcp.json` |
| **插件** | 由 `cc-suite` 统一管理桥接 | 通过 `settings.json` 的 `enabledPlugins` |

### 7.3 关键设计权衡

1. **Claude Code 是主工作台。** `.claude/` 下有完整的规则、agents、hooks、skills、commands。 Codex 和 Gemini 的 slots 是**桥接层**，不是平行副本。

2. **选择性桥接，不是全量镜像。** Codex 的 `hooks.json` 只桥接了 3 个 hook，而不是 Claude Code 的全部 7 个。这避免了在不支持或不需要的平台上运行不兼容的检查。

3. **插件负责桥接逻辑。** `cc-suite@xiaolai` 插件提供了 `/cc-suite:bridge-skills`、`/cc-suite:bridge-mcp` 等命令。项目目录里只是一些声明性的 slot 和 symlink。

4. **空 slots 是设计信号。** `.gemini/skills/.gitkeep` 告诉后来的维护者："Gemini CLI 的技能目录在这里，但目前没有启用。如果启用，把技能放这里。"

### 7.4 和书本身的主题的关联

这本书的核心论点是**责任洗涤通过程序距离隐藏控制链**。桥接架构的设计避免了一个对应的陷阱：**跨工具的不一致不应该成为责任扩散的温床。**

- 三种工具共享同一个 `AGENTS.md` → 没有"我用的是 Codex 版的项目指令，跟你的不一样"的借口
- `.agents/skills` 是 symlink 而非副本 → 技能只有一份，修改自动同步
- `.mcp.json` 是所有工具的共同注册表 → MCP 服务器配置也只有一份

**这不是便利性设计——这是免疫系统设计。** 如果三个工具各自维护一份规则，那么当规则变更时，"谁来同步"就是一个无人认领的责任。Symlink + 共享文件消除了这个问题。

---

## 八、当前局限与开放问题

1. **Gemini CLI 完全未启用。** `.gemini/` 下只有 `.gitkeep` 占位文件。如果将来需要 Gemini CLI 参与写作流程，需要填充这些 slots。

2. **Codex hook 桥接不完整。** 三个关键 hook（implication scan、citation density scan、pronoun discipline scan）不在 Codex 的 `hooks.json` 中。这意味着 Codex CLI 用户可以绕过这些检查。这是有意为之（Codex 的 hook 系统可能不完全支持这些检查的粒度）还是遗漏，需要确认。

3. **`.agents/` 下的内容类型没有文档。** 它目前只有一个 symlink，但理论上它可以容纳 Codex 原生的 agent 定义。AGENTS.md 第 156 行说 `.agents/skills/` 是"Codex skill scan path"——这是 Codex 的约定，项目只是遵循了它。

4. **桥接架构依赖于 `cc-suite` 插件。** 如果插件不可用，桥接 slots 保持为空（如 `.gemini/` 当前状态）。这是一个合理的依赖点，但值得显式声明。

---

Owner: duxiying
Task: 分析 `.agents` 目录在三工具桥接架构中的角色
Inputs reviewed: `.agents/`, `.codex/`, `.gemini/`, `.mcp.json`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.claude/settings.json`
Evidence grade: A（所有分析源均为项目内一手文件）
Open questions:
  - Codex hook 桥接的不完整性是有意设计还是遗漏？
  - `claude-octopus@1.0.0` MCP 服务器的功能范围是什么？
Handoff: 文档写入 `process/analysis/dot-agents-architecture.md`；供后续参考或扩展。
