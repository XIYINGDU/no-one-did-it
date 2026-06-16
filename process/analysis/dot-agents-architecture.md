# `.agents` 目录架构分析

> 分析日期：2026-06-16 · 分支：`analysis/dot-agents-architecture` · 作者：duxiying

---

## 一、物理形态

```
.agents/
  skills → ../.claude/skills    # symlink
```

就一个符号链接。没有配置文件，没有 agent 定义，没有 hook，没有 rule。

---

## 二、它在项目中的位置

`.agents` 位于项目根目录，与 `.claude/`、`.codex/`、`.gemini/` 并列。AGENTS.md 对它的描述只有一句话：

> `.agents/skills/` — symlink to `.claude/skills/`

---

## 三、它解决了什么问题

这个项目有 14 个技能（skills），定义在 `.claude/skills/` 下，是 Claude Code 的原生格式（`SKILL.md` + frontmatter）。

问题是：**有另一个工具需要扫描同一个技能目录，但它不从 `.claude/skills/` 读——它从 `.agents/skills/` 读。**

如果不在两者之间建立联系，维护者有两个选择：

| 方案 | 代价 |
|------|------|
| 复制一份 `.claude/skills/` → `.agents/skills/` | 每次技能变更需要在两处同步；不一致是必然的 |
| 只维护一种，放弃另一种工具 | 损失工具选择 |

Symlink 是第三种方案：**零维护成本的单向同步。** `.claude/skills/` 是 canonical 源，`.agents/skills/` 自动跟随。

---

## 四、设计含义

### 4.1 Symlink 的选择不是偶然的

如果 `.agents/skills/` 是一个独立目录，那么技能变更的"同步"就成了一件需要被记住、被检查、被强制执行的事——也就是一件会被忘记的事。

Symlink 把"同步"从**流程**变成了**文件系统属性**。不需要 hook 检查、不需要 CI 步骤、不需要文档提醒。链接就是链接。

### 4.2 它暴露了一个架构假设

`.agents/` 的存在说明这个项目假设：**技能定义不需要重复，但技能扫描路径需要适配不同工具。** 这是对的——技能是内容（源），而扫描路径是工具的约定（接口）。Symlink 是内容和接口之间的适配器。

### 4.3 它没有 agent 定义

这值得注意。`.claude/agents/` 下有 13 个 agent 定义文件。`.agents/` 下没有任何 agent 定义。

说明当前项目只在 `.claude/agents/` 中维护一份 agent 定义。如果将来有其他工具需要读取 agent 定义但扫描路径不同，`.agents/` 是天然的 slot——加一个 symlink 即可。

---

## 五、和维护成本的关系

| 操作 | 维护者需要做什么 |
|------|------------------|
| 新增一个技能 | 在 `.claude/skills/` 下创建 `SKILL.md` → `.agents/skills/` 自动可见 |
| 修改一个技能 | 编辑 `.claude/skills/<name>/SKILL.md` → 另一端自动跟随 |
| 删除一个技能 | 从 `.claude/skills/` 删除 → `.agents/skills/` 自动消失 |
| 迁移 `.claude/skills/` 路径 | **需要更新 symlink 目标**（唯一的手动操作） |

唯一的维护风险：**如果 `.claude/skills/` 的路径移动了，symlink 会断裂。** 这是一个可以被 `ls -la .agents/skills` 在一秒内验证的事情。

---

## 六、总结

`.agents/` 是一个**适配器目录**。它解决的是一个基础问题：两个工具从不同路径扫描同一份内容。它选择的解决方案——symlink——是这个问题的最简方案：零维护、零同步风险、零流程开销。

它的"空"（只有一个链接，没有原生内容）不是因为它没被完成——而是因为它的正确形态就是空。内容在 `.claude/skills/` 里；`.agents/` 只是一个指针。

---

Owner: duxiying
Task: 分析 `.agents` 目录在项目架构中的角色
Inputs reviewed: `.agents/`, `.claude/skills/`, `AGENTS.md`
Evidence grade: A
Open questions: 无
Handoff: 文档在 `process/analysis/dot-agents-architecture.md`
