---
name: research-card-pipeline
description: 编排将（来源, 声明）对转化为已验证、可查询、可积累的研究卡片的七阶段管道。将来源账本纪律、引用卫生、证据分级和案例文件方法技能连接为单一操作流程。
version: 1.0.0
---

# 研究卡片管道

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 研究卡片

卡片是书中证据的原子单元。一张卡片 = 一个（来源, 声明）对。卡片位于 `book/evidence/source-ledger/cards/<slug>.md`。

## 七阶段管道

```
1 发现 → 2 起草 → 3 验证 → 4 诽谤关卡 → 5 连接到章节 → 6 验证 → 7 积累/替代
```

- **Stage 1 (发现):** 创建卡片及最小 frontmatter（id、来源、声明、未验证等级）。
- **Stage 2 (起草):** 填充除验证字段和诽谤审查外的其余 frontmatter。
- **Stage 3 (验证 - Layer B):** Stephen 运行 5 个强制验证步骤（来源存在、引文字节精确、独立佐证、等级分配、sha256 指纹）。输出 A/B/C 等级。
- **Stage 4 (诽谤关卡 - Layer C):** 如果卡片有在世主体 → Nancy 审查。`nancy_cleared: true` 后方可连接到章节。
- **Stage 5 (连接到章节):** Wayne/Jerry 将 `[CITE: ...]` 锚点连接到 sidecar 中经验证的卡片。
- **Stage 6 (验证 - Layer A):** `validate_source_ledger.py` — schema 合规、slug 唯一性、交叉引用完整性等。
- **Stage 7 (积累/替代):** 重新使用卡片；来源变化时替代；撤回。

## 卡片不验证的内容

引文是否断章取义（Laura 的红队领域）、来源在其领域内是否可靠（等级分配上限非确定性）、章节对来源的解读是否为最强合理阅读（Laura + xiaolai）、译文是否忠实（Stephen + 领域研究员）。管道是机制下限；判断在其之上。
