---
description: "改写生命周期规则：处于改写中的章节在已声明的状态之间转换（ready、in-rewrite、in-review）。先前的审计报告在新审计运行前归档；来源账本 sidecar 携带 as_of 版本管理。"
---

**处于改写中的章节在已声明的状态之间转换；先前的审计报告在新审计运行前归档；来源账本 sidecar 带有对应章节版本的版本管理。**

# 改写生命周期规则

**作用域：** 约束 `book/chapters-v2/` 中进入虚构工艺改写周期的每一章，以及 `process/audits/`、`book/evidence/source-ledger/` 和 `process/review-memos/` 中引用这些章节的审计和 sidecar 产物。

## 改写期间的状态流转

章节的 `status:` 字段（front-matter）在改写期间遵循以下状态机：

```text
ready
  └─→ in-rewrite      (当 chapter-defect-diagnose 运行 + 分配处理等级时声明)
        └─→ in-review (当 wayne 完成改写处理时声明)
              └─→ ready (仅当指定的处理等级的审计集通过后才重新提升)
              └─→ in-rewrite (如果任何审计失败或 laura/nancy 行使否决权，重新打开)
```

转换：

- `ready → in-rewrite` 要求章节的处理等级存在于 `book/registries/treatment-classes.yml` 中（rule `08-treatment-class-discipline.md`）。纯粹的 `no-change` 章节不转换；它们保持 `ready`。
- `in-rewrite → in-review` 要求改写处理完成，并且每章合同（如果该处理等级适用）按照 `/contract-audit` 得到满足。
- `in-review → ready` 要求所声明的处理等级的完整审计集通过。如果章节仍然携带节奏段缺口或 rule-07 未解决的警告，`check-agent-frontmatter.py` 会阻止重新提升。
- 回退 `in-review → in-rewrite` 需要在章节的审计历史中记录原因。

## 审计历史归档

在新的审计覆盖先前的审计报告之前，先将先前的报告快照到 `process/audits/history/<n>/<ISO-timestamp>/`。快照是 `pre-edit-chapter-snapshot.py` hook 的职责；手动改写不得跳过此步骤。

目录布局：

```text
process/audits/history/
  02/
    2026-05-27T14-30-00Z/
      audit-chapter.md
      evidence-audit.md
      fair-clue-audit.md
      defamation-wording.md
      contract-audit.md            （如果处理等级为 structural-polish 或更高）
      implication-audit.md         （始终存在）
      callback-audit-touch.md      （书籍级别 callback 审计的每章切片）
      treatment-class.snapshot.yml （快照时 treatment-classes.yml 中该章的行）
    2026-06-04T09-15-00Z/
      ...
```

快照在改写周期中永不删除。它们是回滚单元：一次失败的改写从最近的快照目录加上 git 历史中对应的 `book/chapters-v2/<n>-*.md` 恢复章节。

## 来源账本 sidecar 版本管理

来源账本 sidecar（`book/evidence/source-ledger/<n>-<slug>.yml`）持有每章的引用锚点表。当章节改写添加、删除或重新定位 `[CITE:]` 锚点时，sidecar 必须在同一提交中更新。sidecar 携带 `as_of:` 字段追踪其对应的章节版本：

```yaml
chapter: 02
slug: the-four-goats
as_of: 2026-06-04          # ISO 日期；匹配章节的最后编辑日期
chapter_status: in-review  # 镜像 sidecar 更新时的章节状态
anchors:
  - cite_id: CITE_02_001
    ...
```

如果章节的 sidecar 的 `as_of:` 早于章节最近的内容编辑日期，该章节不能返回 `status: ready`。`post-edit-status-check.py` hook 标记此不匹配。

## 审查备忘录和案例文件的失效管理

改写可能使引用了特定段落的审查备忘录和案例文件推导失效。章节的缺陷图（`process/defect-map/<n>-<slug>.md`）声明哪些下游产物被触及：

```yaml
invalidates:
  - process/review-memos/02-stephen-fact-check.md     # 引用了特定段落的行号
  - process/review-memos/02-laura-red-team.md
preserves:
  - book/evidence/case-files/02-*.md                         # 案例文件卷宗保持稳定
```

已失效的审查备忘录必须在章节返回 `in-review` 之后、返回 `ready` 之前重新运行。保留的产物不需要重新验证；rule `09` 将它们视为承重稳定的。

## 各处理等级特定的生命周期补充

- `prose-polish`：不需要合同文件；仍然需要快照；仍然需要 sidecar 版本管理。
- `defamation-safe-tighten`：nancy 必须明确放行；需要更新审查备忘录。
- `structural-polish`：需要合同文件；需要跨章节审计；更新 motif/callback/cognitive-arc 注册表。
- `full-craft-rewrite`：以上全部加上 laura 红队和 nancy 时钟；需要试点 Gate B 当量方可重新提升。

<示例>
第 07 章（`structural-polish`）走完全部生命周期：

1. **`ready`（2026-05-26）。** 章节自原始章节生产管道关闭以来一直处于 `ready` 状态。
2. **`ready → in-rewrite`（2026-06-04）。** `chapter-defect-diagnose` 运行；缺陷图引用 V6 + V10 缺陷；处理等级 `structural-polish` 被追加到 `book/registries/treatment-classes.yml`。`pre-edit-chapter-snapshot.py` hook 在第一次编辑时触发，将当前审计复制到 `process/audits/history/07/2026-06-04T09-15-00Z/`（包括 `contract-audit.md` 和 `implication-audit.md`）。章节合同文件在 `book/chapters-v2/07-the-clean-record.contract.yml` 中构建。
3. **改写中期。** Bonnie 为 V6 重排场景；Wayne 为 V10 重新渲染三个段落。新增三个 `[CITE:]` 锚点；sidecar `book/evidence/source-ledger/07-the-clean-record.yml` 在同一提交中更新，`as_of: 2026-06-04` 和新锚点行。缺陷图声明 `invalidates: [process/review-memos/07-laura-red-team.md]` 和 `preserves: [book/evidence/case-files/07-*.md]`。
4. **`in-rewrite → in-review`（2026-06-04，稍晚）。** Wayne 的处理结束；`/contract-audit` 验证每章合同的 `feels:` 和 `primed_for:` 槽位仍然交付。已失效的 Laura 红队备忘录重新运行；保留的案例文件卷宗未被触及。
5. **`in-review → ready`（2026-06-04，再晚些）。** 等级特定的审计链（callback + motif + cognitive-arc + dependency + contract + implication + voice-register）绿色运行。`post-edit-status-check.py` 验证 sidecar 的 `as_of` 与章节的最后编辑日期匹配。`check-agent-frontmatter.py` 放行重新提升。状态返回 `ready`。

如果这些审计中任何一个失败，章节将带着记录的原因回退到 `in-rewrite`，且下一次编辑将生成新的快照目录，而非覆盖 `2026-06-04T09-15-00Z/`。
</示例>

## 这条规则为什么存在

Codex 所批评的计划（D2#1 阻拦项）对 `[EVIDENCE NEEDED]` 标记、审计历史、sidecar 或审查备忘录没有迁移方案。没有 rule 09，一个改写周期会无声地覆盖先前的审计工作，并打破引用锚点的保管链条。有了 rule 09，章节改写的每一步都是可恢复的，每个下游产物都知道自己是当前还是过时。

本规则由 `pre-edit-chapter-snapshot.py`（试点校准后为 block 模式）、`post-edit-status-check.py`（warn 模式）和 `check-agent-frontmatter.py` 章节提升关卡强制执行。
