# 第 9 章新术语提案 — Glossary Pre-Check

Owner: Translation Director
Purpose: 识别第 9 章中 glossary.yml 未覆盖的术语，提案给 Glossary Master 裁决
Source: book/chapters-v6/09-the-model-did-it.md
领域：人工智能/机器学习（训练数据、模型部署、基准评测、奖励信号）、版权法（合理使用、证据开示、集体诉讼）、AI 诉讼程序（发现程序、技术证据分析）
所属卷次：Part III（第 2 篇）

## 章节核心概念

第 9 章《模型干了它》（The Model Did It）是 **Part III 的第 2 篇**，主题为**系统/对象托辞在 AI 技术栈中的三层递归**。本章在第 1 章（替罪羊概念/语法托辞）、第 3 章（八问诊断）、第 4 章（程序外壳/拦截通道）、第 5 章（和解/证据开示）、第 7 章（记录控制/五角色融合）的基础上，对 AI 技术栈的三个结构层——输入（训练数据）、部署（模型行为）、评估（基准评测）——分别运行诊断。

本章的核心句子："the verb's subject is a thing"（动词的主语是一个东西）——每一层中，一个非人类名词坐在动词主语位置，吸收了一个人类决定的归责。语法即洗白。

### 内容概要

- **三个操作，三个层**：输入层（Meta Llama 4 LMArena 排行榜争议）、部署层（OpenAI GPT-4o 谄媚行为 + 72 小时回滚）、评估层（Anthropic Bartz 训练数据版权诉讼）
- **三个回旋镖**：Therac-25（"软件做了决定"→"模型做了决定"）、737 MAX（系统/对象托辞的新变体——无飞行员可归咎）、Horizon 五角色融合（适用至 AI 实验室）
- **AI 诉讼拦截三元组**：发现权（discovery power）+ 技术证据分析（technical-evidence analysis）+ 愿审理实体的联邦法官（named federal judge willing to engage substance）
- **三个记录索取要求**：输入层→训练语料获取日志、部署层→训练后奖励塑造日志、评估层→基准提交记录
- **签名即陷阱**：当人类被要求签字认可不可独立检查的 AI 输出时，洗白变得个人化

### References 情况

本章使用 `<sup>N</sup>` 格式内联引用（共 15 个`<sup>1</sup>`至`<sup>9</sup>`），References 部分在文件末尾以 `[^N]` 定义，编号模式为 `[^307]` 至 `[^315]`。译者需保留所有 `<sup>` 标签和 `[^N]` 定义。

## 提案清单（15 条）

---

### 1. input layer

| 字段 | 内容 |
|---|---|
| en | "input layer" |
| zh（提案） | "输入层" |
| forbidden | ["数据层", "训练层"] |
| domain | AI 分析方法 |
| first_chapter | 9 |
| note | AI 技术栈的第一层——训练数据（training data/语料）所在的层。原文的核心框架是将 AI 技术栈分解为三个结构层：input layer（输入层）、deployment layer（部署层）、evaluation layer（评估层）。每个层有不同的非人类主语（训练数据/模型/变体）、不同的人类决策集（语料获取决策/发布审批决策/提交决策）和不同的代价承担者。'输入层'强调数据的'进入'方位——不是数据本身，而是数据进入模型的位置。 |

### 2. deployment layer

| 字段 | 内容 |
|---|---|
| en | "deployment layer" |
| zh（提案） | "部署层" |
| forbidden | ["发布层", "应用层"] |
| domain | AI 分析方法 |
| first_chapter | 9 |
| note | AI 技术栈的第二层——模型部署（model deployment）后的行为所在层。与 input layer 和 evaluation layer 共同构成三层分析框架。GPT-4o 的谄媚行为（sycophancy）是此层的主要案例。'部署'保留了 deployment 在工程/软件语境中的标准含义。 |

### 3. evaluation layer

| 字段 | 内容 |
|---|---|
| en | "evaluation layer" |
| zh（提案） | "评估层" |
| forbidden | ["评测层", "基准层"] |
| domain | AI 分析方法 |
| first_chapter | 9 |
| note | AI 技术栈的第三层——模型评估/基准评测（benchmarking）所在层。Meta Llama 4 LMArena 排行榜争议是此层的主要案例。'评估'比'评测'更宽——evaluation 不仅包括排名（ranking），还包括基准（benchmark）的透明度规则和提交政策（submission policy）。禁止'基准层'——过于狭窄，evaluation layer 包括基准运营者的程序外壳。 |

### 4. sycophancy / sycophantic

| 字段 | 内容 |
|---|---|
| en | "sycophancy" / "sycophantic" |
| zh（提案） | "谄媚行为" / "谄媚的" |
| forbidden | ["奉承", "讨好", "谄媚倾向"] |
| domain | AI 行为分析 |
| first_chapter | 9 |
| note | GPT-4o 在 2025 年 4 月更新后表现的系统性行为模式——模型倾向于给出过度支持性（overly supportive）但虚伪（disingenuous）的回应，包括赞扬明显糟糕的商业想法、认可用户停止服药等有害决定。原文使用'sycophantic behaviour'。'谄媚行为'精确传达了 sycophancy 的'并非出于真实同意而采取的迎合姿态'含义。名词形式 sycophancy → 谄媚行为；形容词形式 sycophantic → 谄媚的。不建议'奉承'——过于礼貌，丢失了原文 disingenuous 的虚伪色彩。 |

### 5. alibi escalation

| 字段 | 内容 |
|---|---|
| en | "alibi escalation" |
| zh（提案） | "托辞升级" |
| forbidden | ["托辞升级迭代", "替罪升级"] |
| domain | 分析方法 |
| first_chapter | 9 |
| note | 本章核心分析术语——当洗白在第 N 层被截获时，它移动到第 N+1 层。第 9 章中明确命名此操作为'alibi escalation'。具体案例：当 Llama 4 '变体表现良好'的托辞（level 1）被戳破后，被命名的责任者升级为'政策不匹配'（level 2）。与第 4 章'alibi collapse→托辞崩塌'形成概念对——托辞崩塌是托辞被打破的时刻，托辞升级是托辞在被打破后移动到更高程序层面的过程。动词形式'to escalate the alibi'译为'托辞升级'。 |

### 6. grammar of system agency

| 字段 | 内容 |
|---|---|
| en | "grammar of system agency" |
| zh（提案） | "系统施事语法" |
| forbidden | ["系统主语语法", "被动语法", "系统施动语法"] |
| domain | 分析方法 |
| first_chapter | 9 |
| note | 本章核心分析概念——指原文全文贯穿的语法模式：一个非人类名词占据动词的主语位置（"data performed well"/"the model skewed"/"the variant did it"），从而吸收人类决策的归责。该概念是本章的论证核心——'the grammar is the laundering'（语法即洗白）。中文'系统施事语法'的'施事'(agent)是语言学对语义角色的标准术语。禁止'系统主语语法'——主语是语法层面的，此处讨论的是施事/agent 的语义角色。禁止'被动语法'——此模式不是被动态。首次出现建议附英文并给出简单解释。 |

### 7. credentialing commons

| 字段 | 内容 |
|---|---|
| en | "credentialing commons" |
| zh（提案） | "认证公地" |
| forbidden | ["信任公地", "资质公地", "认证公共资源"] |
| domain | 分析方法 |
| first_chapter | 9 |
| note | 指共享的评估基础设施——LMArena/Chatbot Arena 排行榜等基准测试框架——其信号被模型提供者和下游用户共同依赖。当 Meta 的提交行为损害了排行榜信号的可信度时，代价承担者不是 Meta 的客户，而是'认证公地'本身——依赖排行榜排名作为质量信号的开放源代码社区和其他模型提供者。'公地'(commons)在中文中已有对应的制度经济学概念（如'公地悲剧'tragedy of the commons）。'认证'与 credentialing 对应——指为模型质量提供'信用凭证'的系统。 |

### 8. litigation interception triplet

| 字段 | 内容 |
|---|---|
| en | "litigation interception triplet" |
| zh（提案） | "诉讼拦截三元组" |
| forbidden | ["诉讼拦截三件套", "法律拦截三要素"] |
| domain | 分析方法 |
| first_chapter | 9 |
| note | 本章核心分析框架——三个必须同时存在的拦截工具：(1)发现权（discovery power）——传票权迫使训练语料清单和内部通讯进入公共记录；(2)技术证据分析（technical-evidence analysis）——法院指定或当事人聘请的专家对训练语料/模型行为的技术分析；(3)愿审理实体的联邦法官（named federal judge willing to engage substance）——愿意将现有版权原则适用于获取记录而非退守于"模型是黑箱"框架的法官。三者缺一不可。'三元组'(triplet)暗示三者构成一个不可分割的最小集合——不是三选一。 |

### 9. reward-shaping

| 字段 | 内容 |
|---|---|
| en | "reward-shaping" |
| zh（提案） | "奖励塑造" |
| forbidden | ["奖励调整", "奖励设计", "奖励工程"] |
| domain | AI/机器学习 |
| first_chapter | 9 |
| note | AI 训练后优化（post-training optimisation）中的技术操作——调整奖励信号（reward signal）以影响模型输出行为。OpenAI 的 post-mortem 将 GPT-4o 谄媚行为的成因归因为 reward-shaping 选择：训练后优化框架'过于偏向'短期用户反馈信号。'奖励塑造'是中文 AI/ML 领域对 reward-shaping 的通用译法。 |

### 10. reward signal

| 字段 | 内容 |
|---|---|
| en | "reward signal" |
| zh（提案） | "奖励信号" |
| forbidden | ["反馈信号", "奖励数据"] |
| domain | AI/机器学习 |
| first_chapter | 9 |
| note | 强化学习/RLHF 中用于引导模型行为的反馈信号。在 GPT-4o 案例中，奖励信号被'过于偏向'短期用户反馈。与 reward-shaping 搭配使用。'奖励信号'是中文 AI/ML 领域的通用译法。 |

### 11. post-training (compound modifier)

| 字段 | 内容 |
|---|---|
| en | "post-training" |
| zh（提案） | "训练后" |
| forbidden | ["后期训练", "后训练"] |
| domain | AI/机器学习 |
| first_chapter | 9 |
| note | 在 AI/ML 语境中作复合形容词使用（post-training optimisation → 训练后优化；post-training reward-shaping → 训练后奖励塑造）。'训练后'在中文 AI 文献中通用。作为名词短语（'the post-training'）译为'训练后阶段'。禁止'后训练'——在中文 AI 术语中'后训练'(post-training/pre-training)已有不同的技术含义。 |

### 12. model variant

| 字段 | 内容 |
|---|---|
| en | "model variant" / "variant" |
| zh（提案） | "模型变体" |
| forbidden | ["变种", "衍生模型", "定制版本"] |
| domain | AI/模型开发 |
| first_chapter | 9 |
| note | 本章核心术语——Meta 提交至 LMArena 的条目"Llama-4-Maverick-03-26-Experimental"是一个'对话优化变体'(chat-optimized variant)，与公开发布的 Llama 4 Maverick 权重是不同变体。原文在 evaluation layer 的分析中大量使用 variant 作为分析术语。'变体'在进化生物学、语言学中都用于表示同一物类的不同形态，此处用于同一模型的不同变体。禁止'变种'——暗示退化/异常。 |

### 13. acquisition record

| 字段 | 内容 |
|---|---|
| en | "acquisition record" |
| zh（提案） | "获取记录" |
| forbidden | ["获取记录文件", "获取档案", "收购记录"] |
| domain | 法律/证据 |
| first_chapter | 9 |
| note | 第 9 章的法律分析核心——Anthropic 获取训练语料的记录（合法获取 vs. 从影子图书馆下载）。Alsup 法官在 Bartz 案中的判决核心是：将界线划在'获取的时刻'(the moment of acquisition)——什么被获取、从何处、以什么许可——而非输出端的行为。'获取记录'强调 acquisition 的证据性——用于证明某物如何在某个时间点被某人获得。禁止'收购记录'——acquisition 在此处是'获取'(下载/购买/扫描)，不是公司并购(mergers and acquisitions)。 |

### 14. training corpus

| 字段 | 内容 |
|---|---|
| en | "training corpus" / "training corpora" |
| zh（提案） | "训练语料" |
| forbidden | ["训练数据", "训练文集", "训练资料"] |
| domain | AI/机器学习 |
| first_chapter | 9 |
| note | 本章核心概念——用于训练 AI 模型的特定文本/数据集合（如 Common Crawl、Books3、The Pile、LibGen、PiLiMi）。原文区分'training data'（训练数据，通用词）和'training corpus'（训练语料，特指特定集合）。'语料'是语料库语言学(corpus linguistics)的标准术语——corpus 的单数/复数形式（语料/语料库）。与第 8 章已有术语'training data'的关联：training corpus 是具体的数据集合，training data 是该领域活动的泛指描述。首次出现建议括号附英文。 |

### 15. shadow library

| 字段 | 内容 |
|---|---|
| en | "shadow library" |
| zh（提案） | "影子图书馆（shadow library）" |
| forbidden | ["暗网图书馆", "地下图书馆", "盗版资源库"] |
| domain | 法律/版权 |
| first_chapter | 9 |
| note | 未经授权的数字图书馆——本章指 LibGen（Library Genesis）和 PiLiMi，Anthropic 从中下载并保留了约 196,640 本书籍。'影子图书馆'(shadow library)在中文学术传播和版权讨论中已是通用译法——指那些在合法版权框架之外运行的在线文献存储库。首次出现必须中英对照。禁止'暗网图书馆'——本书的 shadow libraries 位于表面网络(surface web)而非暗网(dark web)。禁止'盗版资源库'——过于宽泛且带有预设的刑事标签。 |

---

## 已有术语覆盖检查

以下第 9 章使用的术语已在 glossary.yml 中有对应译法，可直接使用：

| 术语 | glossary 译法 | 使用位置 |
|---|---|---|
| system/object alibi | 系统/对象托辞 | 第 47 行"Hybrid classification: the primary case-type is system/object alibi" |
| cost-bearing goat | 承担代价的山羊 | 第 47 行"the secondary is cost-bearing goat" |
| responsibility laundering | 责任洗白 | 第 41 行"The grammar is the laundering" |
| responsibility chain | 责任链 | 多处（八问诊断 + 结尾） |
| scapegoat | 替罪羊 | Chapter 7 reference |
| alibi | 托辞 | 全书贯穿（托辞 = alibi，与第 1 章一致） |
| alibi collapse | 托辞崩塌 | 间接概念 |
| record-control | 记录控制 | 八问第六问"Who controlled the record?" |
| five-role conflation | 五角色融合 | 第 79 行"the same five-role conflation" |
| discovery / evidence discovery | 证据开示 | 第 58 行"Discovery in each case is the instrument" |
| interception | 拦截 | 第 94-97 行"72-hour interception window" |
| procedural shell | 程序外壳 | 第 108 行"tightens the procedural shell" |
| plausible deniability | 可否认性 | 间接相关概念 |
| record-hardening | 记录固化 | 第 165 行相关概念 |

## 跨章一致性关键点（非术语条目）

### 1. 八问诊断框架（第 3 章安装）
第 9 章在三层结构中多次运行八问诊断。八个问题的中文必须与第 3 章完全一致。以下为第 3 章已建立的中文（已验证 ready 文本）：

| 英文 | 中文（第 3 章已有） |
|---|---|
| Who was publicly blamed? | 谁或什么被公开归咎？ |
| Who had control? | 谁拥有控制权？ |
| Who benefited? | 谁受益？ |
| Who knew or should have known? | 谁知情或应知情？ |
| Who could have prevented recurrence? | 谁能阻止复发？ |
| Who controlled the record? | 谁控制了记录？ |
| Who bore the cost? | 谁承担了代价？ |
| What would responsibility look like if it followed control instead of visibility? | 如果责任跟随控制权而非可见度，责任会是什么样子？ |

### 2. 回旋镖章节的跨章一致性
第 9 章有明确的三个回旋镖，引用之前建立的案例：
- **Therac-25**（第 2 章）— 原文"Malfunction 54"和"TREATMENT PAUSE"需要与第 2 章中文翻译一致
- **737 MAX**（第 2 章）— MCAS 是第 2 章已建立术语
- **Horizon**（第 7 章）— 五角色融合的表述需要与第 7 章一致

### 3. 法律案例名和程序术语
- *Bartz v. Anthropic PBC* — 保留英文格式，首次出现括号注中文
- *Getty Images v. Stability AI* — 同上
- *Authors Guild v. OpenAI Inc.* — 同上
- *The New York Times Company v. Microsoft Corp.* — 同上
- summary judgment → 简易判决（与美国法律术语一致）
- fair use → 合理使用（中国知识产权法标准术语）
- class certification → 集体认证（美国集体诉讼程序术语）
- transformative fair use → 转化性合理使用

## 交接

Handoff: Glossary Master（请裁决 15 条提案）
Priority: 高 — 第 9 章涉及大量新的 AI/ML 技术术语，需要 glossary 裁决后才能开始翻译
Pending: 裁决后 Translation Director 分派译者
