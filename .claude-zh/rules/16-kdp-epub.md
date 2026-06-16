---
description: "KDP EPUB 生产：Kindle/KDP 版以从 v6 真相源构建的可重排 EPUB 3 交付，符合 Amazon Kindle Publishing Guidelines；仅在 epubcheck 零错误通过且 Kindle Previewer 3 干净转换时有效。EPUB 是衍生产物——永远不是 canonical 源。"
---

**Kindle/KDP 版以从 v6 真相源构建的可重排 EPUB 3 交付，符合 Amazon Kindle Publishing Guidelines；仅在 epubcheck 零错误通过且 Kindle Previewer 3 干净转换时有效。EPUB 是衍生产物——永远不是 canonical 源。**

# KDP EPUB 生产

**作用域：** 约束 *No One Did It* Kindle/KDP 电子书版的生产。

## 真相源不变量

EPUB 从 **`book/chapters-v6/`** 编译——v6 canonical 文本——通过声明的书脊。`book/spine-v6.yml` 是阅读顺序的唯一清单；`pipelines/epub/assemble_v6_manuscript.py` 读取它并发出 `dist/manuscript-v6.md`；`pipelines/epub/build_kdp_epub.py` 将该手稿转为 EPUB。`.epub` 和组装的 `manuscript/*.md` 是构建输出：重新生成它们，绝不将它们视为可编辑的母版。任何文本修复落地到 `book/chapters-v6/`（或前/后页来源）；重排序落地到 `book/spine-v6.yml`；然后 EPUB 被重新组装和重新构建。如果来源仍然包含未解决的 `[CITE:]` 标记或 `[EVIDENCE NEEDED]` 占位符，构建**必须大声失败**。

## 格式

| 要求 | 值 |
|---|---|
| 版本类型 | **可重排** EPUB（文字为主的非虚构；读者控制字体/大小） |
| EPUB 版本 | **EPUB 3**（推荐——转换为 Amazon KFX 保真度损失最小） |
| 上传格式 | `.epub` |
| MOBI | **已死亡。** 不再接受用于可重排（自 2021-08-01）或固定版面（自 2025-03-18）。永远不生产 `.mobi`。 |
| 版面 | **单列。** 不**使用 CSS `position:` 进行对齐。 |

## 封面

| 要求 | 值 |
|---|---|
| 理想尺寸 | **2,560 × 1,600 px**（高 × 宽） |
| 长宽比 | **1.6 : 1** |
| 最低 | 最长边不小于 **1,000 px**；始终瞄准理想值 |
| 格式 | **JPEG**（首选）或 TIFF |
| 颜色配置 | **RGB / sRGB** |
| 分辨率 | 推荐 ≥ 300 DPI |
| 内容 | **必须载有书名和作者**；无价格/促销文字 |

## HTML / CSS 子集（可重排）

Kindle 的渲染器不是完整的浏览器。为受支持的子集构建：

- **仅相对单位**用于排版和间距：使用 `em` / `%`，绝不在 `font-size`、`width`、`margin`、`padding`、`text-indent` 上使用 `pt` 或 `px`。
- **正文文本：** 默认大小（`1em`）和默认 `line-height`；不强制的 `font-family`；左右边距 = `0`；不强加的文本颜色；无黑或白强制背景。
- **无 `height`** 在文本元素上（仅在图像上）。**无 `position:`**。
- **段落：** 通过缩进**或**间距区分，不是两者都用；`text-indent` ≤ 4em。
- **分页：** 每章/每部前分页。
- **嵌入字体**（如有）：仅**OTF 或 TTF**。默认不嵌入正文字体。

## 脚注 / 尾注（与 rule 13 对齐）

Kindle 渲染为**弹出框**（EPUB 3 `epub:type="noteref"`/`"footnote"` 标记）。Chicago 尾注满足此要求。

## 验证关卡（两者均需，按顺序）

1. **epubcheck（W3C，≥ v5.x）**——必须报告**零错误**。
2. **Kindle Previewer 3**——将 EPUB 转换为 KFX/KF8 并在模拟设备上渲染；**必须零错误转换**。
3. **手动抽查。**

未通过关卡 1 和 2 的构建不是 KDP 上传的候选。

## 谁拥有什么

- **构建/验证脚本 + 技能（`/kdp-epub`）：** 生产步骤。确定性；大声失败。
- **Stephen（事实核查）：** 来源在构建前必须引用清洁。
- **Nancy（法律）：** 封面和任何标题/信用需在交付前清除 rule-03 图像权利。
- **Bonnie（架构）：** 封面方向 + 可重排版携带哪些内页图。

## 这条规则为什么存在

一本论证记录必须诚实保存的书不能交付一份畸形的版本。KDP 会无声地"修复"不符合规范的文件，而这些无声修复正是本书在其他地方诊断的那种不受控制的转变。锁定 EPUB 3 格式 + 验证关卡使 Kindle 版本成为一个刻意的产物，而非 KDP 转换器无论产生什么都接受的结果。
