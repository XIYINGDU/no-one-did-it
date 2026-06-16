---
description: "引用形式：引用遵循 Chicago Manual of Style 第 17 版注释-书目体系，采用三层模型（散文中来源身份 / 内联 [CITE: slug] / 编译生成的尾注 + 精选参考书目）。内联 [CITE:] 括号仅携带卡片 slug。"
---

**引用遵循 Chicago Manual of Style 第 17 版，注释-书目体系，各章分组尾注和配对的精选参考书目；散文中来源命名对每个承重来源均为必备；内联 `[CITE:]` 标记仅携带卡片 slug。**

# 引用形式

**作用域：** 约束 `book/chapters-v2/`、`book/evidence/case-files/`、`process/review-memos/` 和 `book/proposals/` 中的每一篇散文产物。与 rule `06-quote-integrity.md`（管辖引文修改）和 rule `12-reader-experience-values.md`（通过 V10 音频可留存性管辖读者体验）互为姐妹规则。`/cite-density-audit` 和 `/compile-book` Chicago 格式化处理的宪法锚点。

## 三层模型

引用责任拆分到三个产物中：

| 层 | 产物 | 承载 | 受众 |
|---|---|---|---|
| **1. 散文** | 章节句子 | 在叙事声音中指名的来源身份（说话者、场合、日期、法院、调查） | 读者和有声书听众 |
| **2. 内联标记** | 章节散文中的 `[CITE: <card-slug>]` | 卡片标识符，别无其他 | 编译步骤、审查者、事实核查者 |
| **3. 尾注** | 由 `/compile-book` 从卡片元数据生成的书末尾注 | 完整 Chicago NB 引用、存档 URL、佐证列表、访问说明 | 翻到书末的读者；文字编辑；未来的学者 |

每层承载其受众需要的内容。内联 `[CITE:]` 括号不携带引用元数据——那是尾注的职责。

## 第 1 层：散文中来源身份（必备）

每个承重来源必须在散文声音中指涉——说话者、场合、日期、法院、调查、文档名称——在引用该来源的段落内。有声书听众和跳过尾注的读者都必须知道该声明植根于何处。

| 来源类型 | 散文中模式 |
|---|---|
| **陈述 / 证词 / 推文** | "6 月 17 日下午 2:08，Kirstjen Nielsen 在 Twitter 上写道：……" |
| **调查 / 委员会报告** | "2016 年 7 月 6 日发布的伊拉克调查执行摘要发现……" |
| **法院裁决** | "在 *Hamilton & Others v Post Office Ltd* 案中，上诉法院于 2021 年 4 月撤销了 39 项定罪……" |
| **法规 / 规章 / 行政命令** | "1978 年《政府伦理法案》第六章设立了……" |
| **政府报告** | "2009 年 4 月解密的参议院军事委员会调查得出结论……" |
| **学术 / 书籍** | "在 Leveson 和 Turner 的 IEEE Computer 调查中，竞态条件被识别为……" |
| **新闻调查** | "Dominic Gates 和 Mike Baker 自 2019 年 3 月起在获普利策奖的 *Seattle Times* 系列中记录了……" |
| **主要文件** | "2002 年 8 月 1 日 Jay Bybee 的 OLC 备忘录将……重新定义为……" |
| **ICC / 国际机构** | "国际刑事法院第二预审分庭于 2023 年 3 月 17 日发出逮捕令，裁定……" |
| **纪录片 / 广播** | "在 2015 年 3 月 Rossiya-1 纪录片 *Crimea: The Way Home* 中，……" |

每个承重段落来源可命名一次；同段落后续声明可用简短形式引用同一来源。第一次提及即为音频测试提及。

## 第 2 层：内联 `[CITE: <card-slug>]` 标记

每条被引用的声明携带一个指向来源账本卡片 slug 的内联标记。括号内别无其他。

```markdown
[CITE: nielsen-tweet-no-policy-2018-06-17]
[CITE: chilcot-iraq-inquiry-report-2016]
```

多个卡片支撑单一声明时，在一个括号中使用分号分隔的 slug：

```markdown
[CITE: chilcot-iraq-inquiry-report-2016; ssci-phase-i-iraq-prewar-intelligence-2004]
```

## 第 3 层：Chicago NB 尾注（编译生成）

`/compile-book` 技能通过读取每个独特 slug 的来源账本卡片生成尾注。遵循 Chicago 第 17 版注释-书目体系。

### URL 验证——仅内部 QA，绝不面向读者

链接验证是私密质量关卡，**不是读者面向的文案**。发布的尾注仅携带**有效链接**，加上（如存在）**`[存档快照]` 链接**（以及任何访问说明）。不得携带内联验证印章——不得有 `(验证于 YYYY-MM-DD)`、不得有 `[主 URL 截至……已不可用]` 散文、不得有 `(取决于验证检查点)`。

验证*状态*仍然被追踪——只是永不印出。`scripts/verify_card_urls.py` 记录每张卡片的 `verification.url_check` 块，该元数据驱动编辑选择，但存在于来源账本卡片上，从不进入手稿。

## 引用密度不变量

1. **仅 slug 的内联。** 内联 `[CITE:]` 括号仅包含由 `;` 分隔的一个或多个卡片 slug。无逗号。无"参见"。无存档说明。
2. **长度上限。** 内联 `[CITE:]` 括号 ≤ 每括号 60 字符。
3. **卡片存在。** 每个 slug 必须解析到 `book/evidence/source-ledger/cards/<slug>.md` 下存在的卡片。

## 谁拥有什么

- **Wayne（叙事 lead）：** 在起草时写入第 1 层散文中来源命名；发出第 2 层 `[CITE: slug]` 标记；绝不在散文中写入尾注元数据。
- **Stephen（事实核查 director）：** 验证每个 slug 的卡片存在且携带 Chicago 所需元数据；在手稿冻结前锁定待处理标记。
- **Nancy（法律 counsel）：** 将散文中来源命名视作诽谤纪律表面来审查。
- **Jerry（crew chief）：** 为手稿导出运行 `/compile-book`；审查生成的尾注的 Chicago 形式正确性。
- **`/cite-density-audit` 技能 + `scan-cite-density.py` hook：** 自动化。

## 这条规则为什么存在

没有声明的约定，引用形式会发生漂移。第 6 章的 Nielsen 追加在句内塞了 60 词的元数据砖块；在 12 个活跃章节中的类似扩展会使散文无法朗读，并破坏本书的 V10（音频可留存）承诺。

Chicago Manual of Style 第 17 版是本书同类书（Caro、Snyder、Coll、Tooze、Applebaum）公认的严肃非虚构标准。三层模型是本项目在 Chicago 之上的工艺选择。
