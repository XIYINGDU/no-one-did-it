Owner: Translation Director
Action: dispatch-glossary-master
To: Glossary Master
Chapter: 07-the-record-is-the-battlefield
Source: translation/decision-log/07-term-proposals.md
Date: 2026-06-13

# 第 7 章 Glossary Master 交接

## 章节概况

第 7 章《The Record Is the Battlefield》的主题是**记录控制（record-control）**——谁控制记录，谁就控制责任归属。以英国邮政局 Horizon 丑闻为主案例，论证五角色融合（同一机构同时持有部署者、审计追踪持有者、投诉人、检控方和披露控制者）如何使记录从证据变为武器。本章包含对第 2 章 Therac-25 和第 4 章 MH17 的回调，形成"人工制品层/制度层/国家层"三层并置分析。

## 新术语提案

已识别 14 条 glossary.yml 未覆盖的术语，详见 `translation/decision-log/07-term-proposals.md`。

### 提案概览

| # | 英文 | 提案中文 | forbidden | 领域 |
|---|---|---|---|---|
| 1 | record-control | 记录控制 | 记录管控 | 核心概念 |
| 2 | five-role conflation | 五角色融合 | 五角色混淆, 五角色合并 | 分析方法 |
| 3 | deployer | 部署者 | 实施者, 运用者 | 分析方法 |
| 4 | audit-trail holder | 审计追踪持有者 | 审计记录持有人, 审核追踪持有人 | 分析方法 |
| 5 | complainant | 投诉人 | 控告人, 告诉人 | 法律/英国法 |
| 6 | prosecutor | 检控方 | 公诉人, 起诉方, 控方 | 法律/英国法 |
| 7 | disclosure controller | 披露控制者 | 证据控制者, 开示控制者 | 法律/英国法 |
| 8 | private prosecution | 私人检控 | 私人起诉, 私人公诉, 自诉 | 法律/英国法 |
| 9 | sub-postmaster | 副邮政局长 | 邮政分局局长, 分局局长, 邮政所长 | 角色名/英国邮政 |
| 10 | layered lawful-step defense | 分层合法步骤防御 | 分层合法防御, 分层辩护 | 分析方法 |
| 11 | common-law presumption of computer reliability | 普通法计算机可靠性推定 | 计算机可靠性推定 | 法律/英国普通法 |
| 12 | Group Litigation Order (GLO) | 集团诉讼令 | 团体诉讼令, 集体诉讼令 | 法律/英国民事诉讼 |
| 13 | known error log (KEL) | 已知错误日志 | 已知错误记录, 已知故障日志 | 技术/IT系统 |
| 14 | statutory exoneration | 法定免责 | 法定无罪, 法定豁免, 法定平反 | 法律/英国法 |

## 已有术语覆盖检查

术语表已有且可直接使用（无需修改）：

| 术语 | glossary 译法 | 使用位置 |
|---|---|---|
| record-hardening | 记录固化 | 第 135 行"first of the record-hardening layers had cracked" |
| alibi | 托辞 | 全章多处（"系统/对象托辞"） |
| system/object alibi | 系统/对象托辞 | 第 77 行（Horizon 的两种分类之一） |
| cost-bearing goat | 承担代价的山羊 | 第 77 行（Horizon 的两种分类之二） |
| interception | 拦截 | 第 127 行"interception necessary"、第 159 行"eight channels" |
| responsibility chain | 责任链 | 第 41 行"eight questions diagnostic"（归责链） |
| responsibility laundering | 责任洗白 | 第 37 行"Record-control laundering is not single-shot misinformation" |
| scapegoat | 替罪羊 | 第 57 行起（诊断框架第一问） |
| alibi collapse | 托辞崩塌 | 第 127 行"alibi sustains"动词形态 |
| procedural shell | 程序外壳 | 第 45 行可类比使用 |
| proxy | 代理人 | 第 43 行跨章引用 |
| plausible deniability | 可否认性 | 第 45 行"disclosure controller"机制的关联概念 |

## 翻译策略注意事项（供译者参考，非 glossary 条目）

### 1. 专有名词翻译策略

| 英文 | 中文 | 策略 |
|---|---|---|
| Post Office Ltd | 英国邮政局有限公司 | 首次出现全称，后续"邮政局" |
| Fujitsu Services Ltd | 富士通服务有限公司 | 首次出现全称，后续"富士通" |
| Horizon | Horizon（地平线系统） | 首次出现保留英文+"地平线系统"括号注，后续 Horizon |
| Seema Misra | 西玛·米斯拉 | 印地语人名音译 |
| Alan Bates | 艾伦·贝茨 | 标准音译 |
| Rebecca Thomson | 丽贝卡·汤姆森 | 标准音译 |
| Gareth Jenkins | 加雷思·詹金斯 | 标准音译 |
| Paula Vennells | 保拉·文内尔斯 | 标准音译 |
| Sir Wyn Williams | 温·威廉姆斯爵士 | 标准音译 |
| Mr Justice Peter Fraser | 彼得·弗雷泽法官 | 英国法官尊称译法 |
| Guildford Crown Court | 吉尔福德刑事法庭 | Crown Court→刑事法庭（英国法标准译法） |
| HM Prison Bronzefield | 女王陛下监狱布朗兹菲尔德 | HM→女王陛下（或"皇家"） |
| Craig-y-Don, Llandudno | 兰迪德诺的克雷格-伊-顿 | 威尔士地名音译 |
| Therium | Therium（诉讼融资机构） | 保留英文+括号注 |
| Second Sight Support Services | Second Sight 支持服务 | 保留英文名 |
| Computer Weekly | 《计算机周刊》 | 期刊名英中对照 |
| Cartwright King | 卡特赖特·金律师事务所 | 律所名 |
| CCRC | 刑事案件审查委员会 | Criminal Cases Review Commission 标准译法+英文缩写 |
| JFSA | 副邮政局长正义联盟 | Justice for Subpostmasters Alliance→标准译法+首次英文缩写 |
| KEL | 已知错误日志(KEL) | 已知错误日志(known error log, KEL)首次完整+缩写 |
| GLO | 集团诉讼令(GLO) | 集团诉讼令(Group Litigation Order, GLO)首次完整+缩写 |
| CPIA | 《1996年刑事程序与调查法》 | Criminal Procedure and Investigations Act 1996→首次使用全称+缩写 |
| CPS | 皇家检控署 | Crown Prosecution Service 标准英国法译法 |
| Operation Olympos | "奥林波斯行动" | 以希腊神话神山命名，参考标准警方行动命名译法 |

### 2. 案例名翻译策略
- 案例名以斜体保留英文，首次出现时括号附中文翻译
- 例：*Hamilton & Others v Post Office Ltd* [2021] EWCA Crim 577 → "汉密尔顿等人诉邮政局有限公司案"
- 例：*Bates and Others v Post Office Ltd* → "贝茨等人诉邮政局有限公司案"
- 例：*Castle v Cross* [1984] 1 WLR 1372 → "卡斯尔诉克罗斯案"
- 例：*Horizon Issues* judgment [2019] EWHC 3408 (QB) → "地平线问题判决"
- 例：*Common Issues* judgment [2019] EWHC 606 (QB) → "共同问题判决"

### 3. 法律/制度术语翻译策略
- "CPIA-compliant disclosure" → "符合CPIA规定的披露"
- "the initial duty under section 3 and the continuing duty under section 7A" → "第3条规定的初始义务和第7A条规定的持续义务"
- "common-law presumption" → "普通法推定"
- "statutory under the Inquiries Act 2005" → "依据《2005年调查法》设立的法定调查"
- "an affront to the conscience of the Court" → "对法庭良知的冒犯"（保留引语格式）

### 4. 斜体处理
- 法庭案例名以斜体保留
- 阿拉伯语 *isnad* 以斜体保留（题记）
- 所有法律案例名称（*Horizon Issues*, *Bates* 等）以斜体保留

### 5. 引用/脚注格式
- 正文中 `<sup>N</sup>` 标签保持原样
- References 部分（[^246]-[^250]）的注释保留英文原文（URL 和出处）
- 脚注前面的说明句可以翻译
- Comparison material / bordereau（Dreyfus 案）→ 保留原文单词，括号注中文

### 6. 特殊格式
- 图嵌入块 `:::{.figure-embed}` ×2 → 保留原样，alt text 翻译为中文
- 题记引用 Alfred Guillaume 的话 → 翻译为中文，保留 *isnad* 斜体

### 7. 文内引语翻译
- 第11行题记：Alfred Guillaume 引语
- 第 65 行："an affront to the conscience of the Court"（引语）
- 第 113 行：Rebecca Thomson 文章标题
- 所有引语保持引号格式，注明出处

## 交接

Handoff: Glossary Master（请裁决 14 条提案）
Pending: 裁决后 Translation Director 分派译者
