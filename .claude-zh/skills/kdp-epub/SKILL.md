---
name: kdp-epub
description: 从 v6 真相源构建并验证可 KDP 上传的 EPUB 3，符合 Amazon Kindle Publishing Guidelines。
version: 1.0.0
---

# KDP EPUB

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 真相源不变量

EPUB 从 `book/chapters-v6/` 编译。构建管道：`book/spine-v6.yml` → `assemble_v6_manuscript.py` → `build_kdp_epub.py` → `.epub`。如果来源仍有未解决的 `[CITE:]` 标记或 `[EVIDENCE NEEDED]` 占位符，构建必须大声失败。

## 格式约束

可重排 EPUB 3。仅相对单位（em/%）用于排版。无 CSS position。无文本元素的 height。段落由缩进或间距区分，不两者都用。每章前分页。封面 2,560×1,600 px JPEG/RGB。

## 验证关卡

1. epubcheck ≥ v5.x — 零错误。2. Kindle Previewer 3 — 零错误转换。3. 手动抽查。

## 谁拥有什么

构建/验证脚本 + 技能（`/kdp-epub`）——确定性；大声失败。Stephen——来源须引用清洁。Nancy——封面及标题/信用。Bonnie——封面方向及内页图。
