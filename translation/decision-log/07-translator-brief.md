---
owner: Translation Director
action: dispatch-translator
to: Translator
chapter: 07-the-record-is-the-battlefield
source: /Users/duxiying/Documents/no-one-did-it/book/chapters-v6/07-the-record-is-the-battlefield.md
glossary: /Users/duxiying/Documents/no-one-did-it/translation/glossary.yml
glossary_version: 1.0.0-pilot (updated 2026-06-13 with 14 new Ch 7 terms)
date: 2026-06-13
---

# 第 7 章翻译分派

## 章节概况

- **标题：** The Record Is the Battlefield（记录即战场）
- **篇幅：** 192 行（含 References 约 5 条脚注）
- **主案例：** 英国邮政局 Horizon 系统丑闻（Post Office Horizon IT scandal）
- **对比案例回调：** Therac-25（第 2 章）、德雷福斯案（历史锚点）、MH17（第 4 章）
- **领域：** 英国刑事诉讼程序、普通法、IT 系统审计、商业合同
- **引用密度：** 中等 — 主要在案例引用（*Hamilton* [2021]、*Horizon Issues* [2019]、*Common Issues* [2019]、*Castle v Cross* [1984]）及 Inquiry 报告。使用脚注 `[^N]` 格式而非 `[CITE: slug]`
- **修辞结构：** 开场场景 → 三个错误陈述 → 八问诊断（与架构碰撞） → 五角色融合 → 三层并置回调 → 分层合法步骤防御（五层） → 抵抗叙事 → 反论点→反弹 → 时间线突破 → 反洗钱规则 → 八个渠道的不对称性 → 逃逸代价 → 教学点 → 日常场景 → 向 Part III 过渡

## 新术语

第 7 章新增 **14 条术语**已由 Glossary Master 裁决并写入 glossary.yml。核心新概念：

- **record-control** → **记录控制**（核心分析术语——谁控制记录，谁就控制责任归属）
- **five-role conflation** → **五角色融合**（核心分析框架——同一机构持有五个记录控制角色）
- **五角色个体：** deployer→部署者、audit-trail holder→审计追踪持有者、complainant→投诉人、prosecutor→检控方（非"公诉人"）、disclosure controller→披露控制者
- **private prosecution** → **私人检控**（英国法制度，非"自诉"）
- **sub-postmaster** → **副邮政局长**（首次出现括号附英文+注）
- **layered lawful-step defense** → **分层合法步骤防御**
- **common-law presumption of computer reliability** → **普通法计算机可靠性推定**
- **Group Litigation Order (GLO)** → **集团诉讼令**
- **known error log (KEL)** → **已知错误日志**
- **statutory exoneration** → **法定免责**

请逐条对照 glossary.yml 使用。特别注意 "prosecutor" 的译法——它是私人检控语境下的 "检控方"，不是"公诉人"。

## 特别注意事项

### 1. 五角色融合框架（全章核心分析结构）

第 45 行引出五个角色，第 75 行总结。五个角色在中文必须保持术语一致：

- deployer → 部署者
- audit-trail holder → 审计追踪持有者
- complainant → 投诉人
- prosecutor → 检控方
- disclosure controller → 披露控制者

五个角色首次并列出现时（第 45 行原文：*"holder of the audit trail...complainant...prosecutor...disclosure controller"*），建议使用格式：

> 是 Horizon 系统的**部署者**——从富士通购买软件并在每个分局终端上运行的机构；通过其与富士通的合同，是 Horizon 行为**审计追踪的持有者**——包括已知错误日志(KEL)、源代码、远程访问日志和工程记录；是**投诉人**——发现短缺即认定副邮政局长盗窃或虚假记账的一方；是**检控方**——依据英国法直接提起刑事检控，无需皇家检控署(CPS)审查；也是**披露控制者**——负责向辩方披露任何可能削弱控方案件或协助辩方的材料。

五个角色在中文中应形成可识别的格式或节奏。建议使用加粗标记。

### 2. 八问诊断（第 41–74 行）

原文用八问形成了诊断框架与五角色架构的碰撞。在中文中：

- 八个问题使用平行句式（"谁/什么被...？" → "谁拥有...？" → "谁受益...？"）
- 每个问答之间的节奏应保持
- 第 67 行 "Who controlled the record? The institution making the accusation" 是全书最有力的短句之一——中文必须保持短句形式："谁控制了记录？提出指控的机构本身。"
- 第 71–75 行的总结性段落是认知转折点，注意保持短句节奏

### 3. 三层并置回调（第 79–91 行）

本章对 Therac-25（第 2 章）、德雷福斯案（历史锚点）和 MH17（第 4 章）的三层回调是结构性的关键。中文需注意：

- 保持"人工制品层/制度层/国家层"的三层比较结构
- Therac-25 的回调不需要重新展开案例细节（第 2 章已安装），保持简洁聚焦
- 德雷福斯段落是压缩过的历史锚点，需要精确，保留"bordereau"的原文形式
- MH17 的回调需要与第 4 章的术语保持一致（"山毛榉"、"Buk-TELAR"等）

### 4. 分层合法步骤防御（第 93–109 行）

五个层次的平行结构在中文中必须保持相同的句子长度和节奏。五层为：

1. 个人责任合同条款（sub-postmaster contract → 第 97 行）
2. 普通法计算机可靠性推定（common-law presumption → 第 99 行）
3. 私人检控（private prosecution → 第 101 行）
4. 受害者地理分散（dispersion of victims → 第 103 行）
5. 认罪率架构（plea-rate architecture → 第 105 行）

注意第 107 行的总结："None of these layers, taken alone, is unusual... Their convergence did."——"这些层面中，任何一层单独来看都不异常。它们的汇聚产生了[效果]。"

### 5. 反论点反弹（第 125–129 行）

125 行的反论点是全书标准的"全力陈述反对观点"模式。在中文中必须：

- 以全力呈现反对论点（"Horizon 是一场有据可查的司法不公"）
- 区分"反对论点→承认→回应"三结构
- 第 127 行的六个前提条件在中文中保持平行结构

### 6. CPIA 和英国法律术语

- "Criminal Procedure and Investigations Act 1996" → 《1996年刑事程序与调查法》(CPIA) —— 首次出现全称+缩写
- "section 3" → 第 3 条（初始披露义务）
- "section 7A" → 第 7A 条（持续披露义务，由《2003年刑事司法法》增补）
- "private prosecution" → 私人检控（见 glossary）
- "Crown Prosecution Service" → 皇家检控署(CPS)
- "two-stage charging test" → 两阶段起訴审查测试
- "Criminal Cases Review Commission" → 刑事案件审查委员会(CCRC)
- "Court of Appeal (Criminal Division)" → 上诉法院（刑事分庭）

### 7. 专有名词翻译

| 英文 | 中文 |
|---|---|
| Post Office Ltd | 英国邮政局有限公司（首次全称，后续"邮政局"） |
| Fujitsu Services Ltd | 富士通服务有限公司（首次全称，后续"富士通"） |
| Horizon | Horizon（地平线系统）（首次出现中英对照，后续用 Horizon） |
| Seema Misra | 西玛·米斯拉 |
| Alan Bates | 艾伦·贝茨（注意：与 ITV 剧集 *Mr Bates vs The Post Office* 中同名人物） |
| Gareth Jenkins | 加雷思·詹金斯 |
| Paula Vennells | 保拉·文内尔斯 |
| Sir Wyn Williams | 温·威廉姆斯爵士 |
| Mr Justice Peter Fraser | 彼得·弗雷泽法官（英国高等法院法官尊称） |
| Rebecca Thomson | 丽贝卡·汤姆森（Computer Weekly 记者） |
| Karl Flinders | 卡尔·弗林德斯（Computer Weekly 记者） |
| Craig-y-Don, Llandudno | 兰迪德诺的克雷格-伊-顿 |
| Therium | Therium（诉讼融资机构）——保留英文，括号注"诉讼融资机构" |
| Second Sight Support Services | Second Sight 支持服务——保留英文名 |
| Cartwright King | 卡特赖特·金律师事务所 |
| Simon Clarke | 西蒙·克拉克（出庭律师，非《三体》中的西蒙） |
| James Arbuthnot | 詹姆斯·阿巴斯诺特（英国议员） |
| Jason Coyne | 杰森·科因（独立技术审查员） |
| Operation Olympos | "奥林波斯行动" |

### 8. 案例名翻译

- *Hamilton & Others v Post Office Ltd* [2021] EWCA Crim 577 → "汉密尔顿等人诉邮政局有限公司案，[2021] EWCA Crim 577"
- *Bates and Others v Post Office Ltd* → "贝茨等人诉邮政局有限公司案"
- *Castle v Cross* [1984] 1 WLR 1372 → "卡斯尔诉克罗斯案"
- *Horizon Issues* judgment → "地平线问题判决"（Fraser J, [2019] EWHC 3408 (QB)）
- *Common Issues* judgment → "共同问题判决"（Fraser J, [2019] EWHC 606 (QB)）
- *R v Misra (2010)* → "女王诉米斯拉案（2010）"

所有案例名首次出现时以斜体保留英文，括号附中文翻译。

### 9. 题记处理

本章题记来自 Alfred Guillaume 引述的伊斯兰圣训传统中的 *isnad* 概念：

> The *isnad* is a matter of religion; and were it not for the *isnad* any one could say what he pleased.

*isnad*（阿拉伯语，指圣训的传述链/传承谱系）必须保留斜体原文，括号注中文"传述链"。翻译全文时注意该题记与本章"记录控制"主题的呼应——没有传述链，任何人都可以随意声称。中文参考：

> *伊斯纳德（isnad，传述链）* 是信仰之事；若非 *伊斯纳德*，任何人都可以随意声称他所愿的。

建议保留 Arabic *isnad* 以斜体保留，在翻译笔记中说明其含义。

### 10. 引用/脚注格式

- 正文中 `<sup>1</sup>` 等标签保持原样——它们是内联跳转到斜体引用（不是脚注编号）
- 脚注编号 `[^246]` 到 `[^250]` 全部原样保留（5 条脚注）
- References 部分第 184–192 行的 `[^N]` 注释块保留英文原文（URL 和出处）
- 所有 URL 和归档链接必须保持原样

### 11. 图嵌入块

本章有两个 `:::{.figure-embed}` 块（第 51 行和第 161 行），各嵌入一张图片。必须：
- 保留 `:::{.figure-embed}` 标记和 Markdown 图片语法
- alt text 翻译为中文
- 图片路径（`book/evidence/diagrams/proofs/...`）保留原样

### 12. 特殊语言点

- "affront to the conscience of the Court" → "对法庭良知的冒犯"（上诉法院原判词引语，加引号保留）
- "not remotely robust" → "远非强健"（Fraser 判决原语——Fraser J 在 Horizon Issues 判决中用此措辞，注意引语格式）
- "the fair clue" → 第 25 行标题词。原文 "fair clue" 是侦探小说术语（给读者公平的线索）。可译为"公平线索"或"提示"
- "The first anti-laundering device is the record." → 第 149 行标题。这是本章的规则句。建议保持短句格式："第一个反洗钱工具就是记录。"
- "Dalmellington bug" → 达梅灵顿 bug（苏格兰地名 Dalmellington 音译，bug 保留英文）

### 13. 历史人物名
- Alfred Dreyfus → 阿尔弗雷德·德雷福斯
- *bordereau* → 保留法文原文（斜体），括号注"（清单/明细表）"
- Statistical Section of the French Army General Staff → 法国陆军总参谋部统计处
- Cour de Cassation → 保留法文原文（斜体），括号注"（法国最高上诉法院）"

## 输出格式

请按 `translation/skills/translate.md` 中定义的对照格式输出至：
`/Users/duxiying/Documents/no-one-did-it/translation/chapters/07-the-record-is-the-battlefield-draft.md`

格式要求：
- 每段/每节以分段对照呈现（原文 blockquote → 译文正文 → 翻译笔记）
- `[^N]` 标记原样保留
- `<sup>N</sup>` 标签原样保留
- HTML div 块 `:::{.figure-embed}` 原样保留
- 非英语原文（阿拉伯语 *isnad*、法语 *bordereau*、*Cour de Cassation*）以斜体保留
- 法律案例名以斜体保留
- 长句拆分标注 `[SPLIT]`
- 术语摩擦标注 `[TERM-NOTE]`
- 歧义标注 `[AMBIGUOUS]`
- 翻译笔记覆盖：五角色一致性、八问平行结构、反论点结构、普通法术语精确性等

## 交接

Handoff: Reviewer（Translation Director 将在译文提交后分派审核）
