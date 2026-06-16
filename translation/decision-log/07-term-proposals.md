# 第 7 章新术语提案 — Glossary Pre-Check

Owner: Translation Director
Purpose: 识别第 7 章中 glossary.yml 未覆盖的术语，提案给 Glossary Master 裁决
Source: book/chapters-v6/07-the-record-is-the-battlefield.md
领域：英国邮政史、刑事程序法、侵权诉讼、航空/医疗/国家层面对比案例

## 提案清单（14 条）

---

### 1. record-control

| 字段 | 内容 |
|---|---|
| en | "record-control" |
| zh（提案） | "记录控制" |
| forbidden | ["记录管控"] |
| domain | 核心概念 |
| first_chapter | 7 |
| note | 本章核心分析术语。指通过控制记录（工程日志、审计追踪、源代码、披露文件等）来控制责任归属方向和深度的能力。"记录控制洗白"(record-control laundering)是本章论证的责任洗白子机制——谁控制记录，谁就控制责任归属。与第4章"record-hardening→记录固化"（将事件固定在制度性记录中的事后过程）互补：记录固化是事后固定事实，记录控制是事前控制记录的可访问性和解释权。 |

### 2. five-role conflation

| 字段 | 内容 |
|---|---|
| en | "five-role conflation" |
| zh（提案） | "五角色融合" |
| forbidden | ["五角色混淆", "五角色合并", "五角色重叠"] |
| domain | 分析方法 |
| first_chapter | 7 |
| note | 本章核心分析框架术语——同一机构同时持有部署者(deployer)、审计追踪持有者(audit-trail holder)、投诉人(complainant)、检控方(prosecutor)和披露控制者(disclosure controller)五个角色时，记录不再是证据，而是武器。'融合'(conflation)强调这些角色在制度层面的不可分性——不是偶然重叠，而是结构性的角色集中。禁止'混淆'——中文"混淆"暗示无意错误，而原文的 conflation 是有意的制度设计。 |

### 3. deployer

| 字段 | 内容 |
|---|---|
| en | "deployer" |
| zh（提案） | "部署者" |
| forbidden | ["实施者", "运用者", "部署方"] |
| domain | 分析方法 |
| first_chapter | 7 |
| note | 五角色之一——部署（如Horizon）系统的机构。指购买软件并在每个终端运行的机构（本章中为Post Office Ltd）。'部署者'在IT/系统语境中是最自然的译法。 |

### 4. audit-trail holder

| 字段 | 内容 |
|---|---|
| en | "audit-trail holder" |
| zh（提案） | "审计追踪持有者" |
| forbidden | ["审计记录持有人", "审核追踪持有人", "审计跟踪持有者"] |
| domain | 分析方法 |
| first_chapter | 7 |
| note | 五角色之一——持有系统审计追踪（已知错误日志KEL、源代码、远程访问日志、工程记录等）的机构。原文第45行说明audit trail包括"The Known Error Log (KEL), the source code, the remote-access logs, and the engineering records"。'审计追踪'是中文IT/法律审计领域的标准术语。 |

### 5. complainant

| 字段 | 内容 |
|---|---|
| en | "complainant" |
| zh（提案） | "投诉人" |
| forbidden | ["控告人", "告诉人", "申述人"] |
| domain | 法律/英国法 |
| first_chapter | 7 |
| note | 五角色之一——在Horizon短款出现时识别并指控副邮政局长的机构。在英国刑事诉讼语境下，complainant指向警方/法院报告犯罪的一方。在本章中，Post Office同时是投诉人和检控方——它识别"犯罪"（短款）、提出指控并自行起诉。'投诉人'在中文法律语境中与complainant对应。 |

### 6. prosecutor

| 字段 | 内容 |
|---|---|
| en | "prosecutor" |
| zh（提案） | "检控方" |
| forbidden | ["公诉人", "起诉方", "控方"] |
| domain | 法律/英国法 |
| first_chapter | 7 |
| note | 五角色之一——直接提起刑事诉讼的机构。在本章特指Post Office依据英国法自己提起公诉的权力（私人检控）。使用'检控方'而非'公诉人'——因为Post Office不是国家公诉机关(CPS)，而是entity bringing private prosecution。'检控方'在中文中既可用于公共检控也可用于私人检控，保留了英国法下"任何主体均可提起刑事诉讼"的制度特征。 |

### 7. disclosure controller

| 字段 | 内容 |
|---|---|
| en | "disclosure controller" |
| zh（提案） | "披露控制者" |
| forbidden | ["证据控制者", "开示控制者", "信息披露人"] |
| domain | 法律/英国法 |
| first_chapter | 7 |
| note | 五角色之一——负责向辩方披露可能削弱控方案件或协助辩方的材料的机构。根据英国《1996年刑事程序与调查法》(CPIA)，控方有法定披露义务（§3初始义务和§7A持续义务）。在本章中，披露控制者与检控方是同一机构（Post Office），因此CPIA下的披露义务的履行完全由同体自我监督。'披露控制者'区别于一般的"信息披露人"——强调其制度性控制权而非单纯的披露行为。 |

### 8. private prosecution

| 字段 | 内容 |
|---|---|
| en | "private prosecution" |
| zh（提案） | "私人检控" |
| forbidden | ["私人起诉", "私人公诉", "自诉"] |
| domain | 法律/英国法 |
| first_chapter | 7 |
| note | 英国法律允许非国家机构(如Post Office)在未经皇家检控署(CPS)审查的情况下直接提起刑事诉讼的制度。本章中这是五角色融合的关键支撑层——第101行指出"英国法律允许Post Office直接提起刑事检控，无需CPS的审查……同一机构站在了检控席上"。使用'检控'而非'起诉'——'检控'在中文法律语境中更接近prosecution的制度性含义。'私人检控'是香港法律界对private prosecution的标准译法。禁止'自诉'——中国刑事诉讼法中的自诉(self-prosecution)与英国private prosecution的法律基础不同。 |

### 9. sub-postmaster

| 字段 | 内容 |
|---|---|
| en | "sub-postmaster" |
| zh（提案） | "副邮政局长" |
| forbidden | ["邮政分局局长", "分局局长", "邮政所长", "邮政支局长"] |
| domain | 角色名/英国邮政 |
| first_chapter | 7 |
| note | 英国邮政局系统的分支/代理机构负责人。英国邮政局(Crown Post Office)系统下有Crown Post Offices（直属局）和sub-post offices（代理局），sub-postmaster负责代理局运营。在Horizon丑闻中，sub-postmasters是以自雇(self-employed)身份签署代理合同的。中文媒体对此丑闻的报道中'副邮政局长'是最常用的译法。'分局局长'禁止——中国"分局"的公安/工商含义与英国post office系统的"sub-branch"完全不同。首次出现建议括号附英文并加注。 |

### 10. layered lawful-step defense

| 字段 | 内容 |
|---|---|
| en | "layered lawful-step defense" |
| zh（提案） | "分层合法步骤防御" |
| forbidden | ["分层合法防御", "分层辩护", "层次防御机制"] |
| domain | 分析方法 |
| first_chapter | 7 |
| note | 本章分析结构术语——指多个独立的合法法律/合同/程序层汇聚为结构性防御的机制。本章列出了五层：(1)个人责任合同条款(2)普通法计算机可靠性推定(3)私人检控(4)受害者地理分散(5)认罪率结构。每一层单独看都不异常，但汇聚产生了记录不可辩驳的效果。'分层合法步骤防御'保留了原文的三层含义：layered（分层的）、lawful（每个步骤本身合法的）、defense（整体的防御性效果）。 |

### 11. common-law presumption of computer reliability

| 字段 | 内容 |
|---|---|
| en | "common-law presumption of computer reliability" |
| zh（提案） | "普通法计算机可靠性推定" |
| forbidden | ["计算机可靠性推定", "普通法计算机正常运作推定"] |
| domain | 法律/英国普通法 |
| first_chapter | 7 |
| note | 英国普通法原则——正确使用的计算机的输出被推定可靠，质疑者承担推翻该推定的责任。源自Castle v Cross [1984] 1 WLR 1372。在Horizon案中，没有工程记录披露的情况下，个体副邮政局长实际上无法推翻该推定。中国人民大学出版社的英国法翻译中多用'普通法计算机可靠性推定'。禁止'计算机正常运作推定'——原文是presumption of reliability（可靠性推定），不是presumption of proper functioning（正常运作推定）。建议首次出现时附英文。 |

### 12. Group Litigation Order (GLO)

| 字段 | 内容 |
|---|---|
| en | "Group Litigation Order (GLO)" |
| zh（提案） | "集团诉讼令" |
| forbidden | ["团体诉讼令", "集体诉讼令", "集团诉讼命令"] |
| domain | 法律/英国民事诉讼 |
| first_chapter | 7 |
| note | 英国民事诉讼程序中的集团诉讼制度(GLO)。GLO将分散的索赔合并为一项由案件管理法官监督的集体行动。2017年3月，高等法院在Bates and Others v Post Office Ltd案中批准了GLO。Therium诉讼融资使该诉讼进入证据开示(discovery)阶段。'集团诉讼令'是中文比较法学者对英国Group Litigation Order的标准译法。建议首次出现时附英文缩写(GLO)。注意区分：英国GLO与美国class action（集团诉讼）不同——GLO是opt-in制度。 |

### 13. known error log (KEL)

| 字段 | 内容 |
|---|---|
| en | "known error log (KEL)" |
| zh（提案） | "已知错误日志" |
| forbidden | ["已知错误记录", "已知故障日志"] |
| domain | 技术/IT系统 |
| first_chapter | 7 |
| note | 富士通(Fujitsu)维护的Horizon系统已知错误/缺陷记录。在Horizon Issues判决和Bates诉讼的证据开示阶段中成为争议焦点。KEL中记录了可能导致分行账户显示短缺的bug（如Dalmellington bug）。'已知错误日志'是IT系统管理中的标准术语（Known Error Database / Known Error Log）。建议首次出现时附英文缩写(KEL)。 |

### 14. statutory exoneration

| 字段 | 内容 |
|---|---|
| en | "statutory exoneration" |
| zh（提案） | "法定免责" |
| forbidden | ["法定无罪", "法定豁免", "法定平反"] |
| domain | 法律/英国法 |
| first_chapter | 7 |
| note | 2024年《邮政局（地平线系统）犯罪法》(Post Office (Horizon System) Offences Act 2024)通过法定方式免除了符合特定标准的定罪，无需个案上诉。与judicial quashing（司法撤销）相对——司法撤销是上诉法院对具体定罪的逐个撤销（Hamilton案中撤销了39个定罪），法定免责是立法机关对符合条件的一类定罪的一次性免责。'法定免责'在中文法律术语中与statutory exoneration对应，不同于'法定无罪'（statutory innocence——英国法并未认定副邮政局长"无罪"，而是从诉讼角度免责）。
