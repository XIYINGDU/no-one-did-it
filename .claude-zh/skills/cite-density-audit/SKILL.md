---
name: cite-density-audit
description: 审计章节散文中违反 rule-13 slug-only 不变量的冗长内联 [CITE:] 标记。内联括号仅携带卡片 slug；完整引用装置在来源账本卡片中，由编译生成为 Chicago NB 尾注。捕获引用元数据从卡片泄漏到散文的失败模式。是 scan-cite-density.py 的更深层读取。
version: 1.0.0
---

# 引用密度审计

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 决策标准

一章通过审计当每个 `[CITE:]` 括号满足：(1) 仅含 slug；(2) 总长度 ≤ 60 字符；(3) 每个 slug 解析到存在的卡片；(4) 无引用装置措辞（无逗号、引号、"archived at"等）。`pending-stephen-lock` 后缀是唯一允许的非 slug 内容。

## 冲突处理

超 60 字符但仅含有效 slug 的三源括号 → 允许，记录例外。含 `pending-stephen-lock` → 允许。slug 不存在 → 硬失败。第 1 层散文来源命名泄漏进括号 → 硬失败，路由给 Wayne 恢复散文中的命名。括号结构正确但周围段落缺少第 1 层 → 软失败。

## 输出格式

| Chapter | Line | Issue type | Snippet | Suggested fix |。Summary: total / valid / over-length / verbose-content / broken-slug / pending-lock。
