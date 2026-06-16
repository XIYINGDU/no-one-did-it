---
owner: Translation Director
action: dispatch-translator
to: Translator
chapter: 09-the-model-did-it
source: /Users/duxiying/Documents/no-one-did-it/book/chapters-v6/09-the-model-did-it.md
glossary: /Users/duxiying/Documents/no-one-did-it/translation/glossary.yml
glossary_version: 1.0.0-pilot (ch-09 terms pending Glossary Master ruling)
date: 2026-06-13
---

# 第 9 章翻译分派

## 章节概况

- **标题：** The Model Did It（模型干了它）
- **所属卷次：** **Part III 第 2 篇**（第 8 章之后、第 10 章之前）
- **篇幅：** 233 行（含 References）
- **证据等级：** A（全部基于一手公共记录——AI 公司官方博文、法院判决、post-mortem 文件、新闻报道）
- **主案例（三个 AI 公司，三个层）：** Meta Llama 4 LMArena 排行争议 → OpenAI GPT-4o 谄媚行为 → Anthropic Bartz v. Anthropic PBC 训练数据版权诉讼
- **回旋镖案例（三个）：** Therac-25（第 2 章）、737 MAX（第 2 章）、Horizon 五角色融合（第 7 章）
- **领域：** AI/ML（训练数据获取、模型部署、基准评测、奖励塑形）、版权法（合理使用、获取记录、集体诉讼）、AI 诉讼程序（发现、技术证据分析）、公司记录控制
- **引用密度：** 中 — 15 个 `<sup>N</sup>` 内联引用，References 部分 9 条脚注 `[^N]`（编号 307-315）。部分脚注有 URL 无法解析标记
- **修辞结构：** 指控场景（三个操作的平行呈现）→ 三个官方故事 → 输入层八问诊断（完整运行）→ 三个回旋镖 → 部署层（72 小时回滚）→ 评估层（托辞升级）→ Alsup 界线 → 三层诊断汇总 + 三个记录索取要求 → 诉讼拦截三元组 → 逃逸代价 → 反洗钱规则 + 警示信号

## 章节结构详解

### 1. 开场场景（第 1–30 行）：三种操作，三种语法

本章以平行句式列举三个 2025 年春的事件，每个以"the verb's subject is a non-human noun"的语法分析贯穿：

- **第 1 段（第 15 行）**：核心论点——三个层（input/deployment/evaluation），每个有一个不同的非人类主语（data/model/variant）
- **第 2 段（第 17 行）**：Meta Llama 4 LMArena 争议——"Llama-4-Maverick-03-26-Experimental"在排行榜排第 2，公开发布后排第 32。官方解释："这是我们在实验中尝试的一个对话优化变体"
- **第 3 段（第 19 行）**：OpenAI GPT-4o 谄媚行为——模型产出"过于支持性但虚伪"的回应。Sam Altman 公开承认。官方解释命名了两个施事：模型（"GPT-4o skewed towards..."）+ 优化框架（"focused too much on..."）
- **第 4-5 段（第 21-26 行）**：Anthropic / Bartz v. Anthropic PBC——Alsup 法官在获取时刻（acquisition）而非输出端画线。1.5B 和解

**翻译要点：** 第 15 行的"the verb's subject is a thing"是全书的一个核心诊断句。中文直译为"动词的主语是一个东西"，保留其简洁有力、稍带异质感的语法判断语气。三个事件的平行呈现——中文必须以相同的平行节奏呈现三个段落，每段的开头结构应保持对称。

### 2. 三个官方故事（第 31–41 行）：按原文呈现

第 35-39 行按顺序呈现三个官方叙事，各自引用一手文件：OpenAI 向英国上议院的书面证据、GPT-4o 的 post-mortem、Meta 发言人的排行榜声明。

**翻译要点：** 第 37 行 OpenAI post-mortem 中显示系统施事语法的例句——"the model began behaving"、"the optimisation framework focused too much"、"the process did not adequately weight"——这些句子必须准确翻译且保留其被动的/非人称施事的语法结构。中文：「模型'开始表现'出某种行为」、「优化框架'过于偏向'短期反馈」、「流程'未充分权衡'定性测试者的关切」。

### 3. 输入层八问诊断（第 43–69 行）：完整运行

第 45-69 行完整运行八问诊断框架于输入层（training-data litigation cluster）：

- 混合分类：primary system/object alibi + secondary cost-bearing goat
- 四个顺序容器：data/corpus → shadow library → model → market
- 控制/受益/知情的三重收敛指向同一批实验室
- 记录控制分析——"The training corpus IS the record"

**翻译要点：**
- **八问必须与第 3 章完全一致**（见下文"跨章一致性关键点"）
- 第 47 行的混合分类声明——"Hybrid classification: the primary case-type is system/object alibi; the secondary is cost-bearing goat"——与第 2 章的术语完全一致，中文为："混合分类：主要案件类型为系统/对象托辞；次要为承担代价的山羊"
- 第 49 行"four sequential containers"——四个顺序容器：data → shadow library → model → market——中文保持相同的递增节奏
- 第 63 行"The training corpus is the record"——训练语料就是记录——此为输入层的关键总结句，中文必须简短有力
- 第 65 行的"Cost-absorbing silence rather than active accusation"——"吸收代价的沉默，而非积极的指控"——关键区分句

### 4. 三个回旋镖（第 71–79 行）：与第 2、7 章回呼

第 73-79 行精炼引用三个此前安装的案例：

- **Therac-25**（第 1 段，第 75 行）："Malfunction 54"和"TREATMENT PAUSE"→ 中文必须与第 2 章一致
- **737 MAX**（第 2 段，第 77 行）："MCAS handled it" → 中文必须与第 2 章一致
- **Horizon 五角色融合**（第 3 段，第 79 行）：five-role conflation → 中文必须与第 7 章一致

**翻译要点：** 每个回旋镖 1-2 句。短、浓缩、精确。不需要在中文中重新解释这些案例——它们只是回呼引用。第 77 行的关键句："MCAS handled it" becomes "the model decided"——"MCAS 处理了它"变为"模型决定了它"。

### 5. 部署层（第 81–98 行）：72 小时回滚

GPT-4o 谄媚事件的详细分析。节奏加快——部署层的拦截速度远快于输入层（72 小时 vs. 诉讼数年）。

**翻译要点：**
- 第 83 行的关键句——"The deployment layer is the AI stack's most visible surface. It is also the layer at which the laundering operates fastest and at which the institutional response is most ready-made."——"部署层是 AI 技术栈中最可见的表面。它也是洗白运行最快、制度性应对最现成的层。"——平行短句节奏需保留
- 第 87 行列出了具体没有被命名的决策者——"the engineers who designed the reward signal, the team leads who approved the design, the product leadership that approved the default-model swap"——中文以三个平行短名词短语保留节奏
- 第 95 行的三个时间比较——Horizon 20 年 → Therac-25 24 个月 → GPT-4o 几天——中文保持递进节奏
- 第 97 行是本章最重要的反洗钱规则之一——"Blameless post-mortem methodology... produces a responsibility-shaped hole when applied to judgment calls"——"无责 post-mortem 方法论...在应用于判断性决策时会产生一个责任形状的空洞"

### 6. 评估层（第 99–115 行）：托辞升级

Meta Llama 4 LMArena 争议的分析。核心概念是"alibi escalation"（托辞升级）：

- Level 1：变体表现良好
- Level 2：政策不匹配
- 决策者仍然没有被命名

**翻译要点：**
- 第 107 行的关键分析句——"Name the operation. Alibi escalation. When the laundering is caught at level N, it moves to level N+1."——"命名这个操作。托辞升级。当洗白在第 N 层被截获时，它移动到第 N+1 层。"——短句节奏需保留
- 第 109 行的"Credentialing commons"——提案中文为"认证公地"（需等 Glossary Master 裁决）
- 第 115 行最后一句——"The procedural shell adjusts; the substantive responsibility chain remains where it was."——"程序外壳调整了；实质性的责任链保持原位。"

### 7. Alsup 在获取处画线（第 117–135 行）：法律拦截

第 119-135 行呈现 Alsup 法官在 Bartz 案中的判决——将界线划在"获取"（acquisition）而非"输出"（output）。

**翻译要点：**
- 第 121 行的关键句——"The line was drawn at the input — the moment of acquisition, not at the output."——"界线划在输入处——获取的时刻，而非输出端。"
- 第 121 行的区分——"Training on lawfully acquired books was held to be transformative fair use... Downloading and retaining the shadow-library copies was held to be not fair use."——"对合法获取的书籍进行训练被认定为转化性合理使用...下载并保留影子图书馆副本被认定为非合理使用。"
- 第 133 行的关键句——"Three instruments. All three required for the input-layer alibi to be broken. Subtract any one, and the alibi sustains."——"三种工具。三种工具全部需要才能打破输入层的托辞。减去任何一个，托辞就存活。"
- 法律术语使用标准中文译法：summary judgment → 简易判决、fair use → 合理使用、transformative fair use → 转化性合理使用

### 8. 三层诊断汇总（第 137–163 行）：三个记录索取要求

第 139-163 行以三个记录索取要求收束诊断分析：

1. 输入层——训练语料获取日志（the training-corpus acquisition log）
2. 部署层——训练后奖励塑造日志（the post-training reward-shaping log）
3. 评估层——基准提交记录（the benchmark-submission record）

**翻译要点：**
- 第 163 行的关键句——"Where one institution holds all the record-control roles at a layer, the laundering architecture is structurally operating."——"当一个机构持有某一层的所有记录控制角色时，洗白架构就在结构性运行。"
- 第 163 行最后一句——"Chapter 7's instruments port forward. The number of times they must be deployed multiplies by three."——"第 7 章的工具向前移植。它们必须被部署的次数乘以三。"
- 三个记录索取要求的句式必须平行——"输入层的记录索取要求：..." / "部署层的记录索取要求：..." / "评估层的记录索取要求：..."

### 9. 诉讼拦截三元组 + 逃逸代价（第 165–189 行）：拦截与代价

第 167-177 行介绍 AI 诉讼拦截三元组（litigation interception triplet）：发现权 + 技术证据分析 + 愿审理实体的法官。第 179-189 行分析逃逸代价：时间、金钱、地域、未被触及的执行层。

**翻译要点：**
- 第 173 行的关键句——"The third instrument is named federal judges willing to engage substance rather than defer to the 'the model is a black box' framing."——"第三种工具是愿审理实体而非退守到'模型是黑箱'框架的具名联邦法官。"
- 第 177 行——"We are honest about the cost of the escape."——"我们对逃逸的代价保持诚实。"
- 第 185 行——"No AI executive has been personally adjudicated as civilly or criminally liable for training-data, deployment, or evaluation laundering as of May 2026."——"截至 2026 年 5 月，尚无任何 AI 高管被个人裁判为对训练数据、部署或评估层面的洗白承担民事或刑事责任。"
- 第 189 行——"The interception works at each layer in its own register, and at no layer has it yet reached the executive whose displaced decision the alibi grammar was protecting."——"拦截在每个层以自己的方式工作，但在任何一个层都尚未触及那个被托辞语法保护其被置换的决策的高管。"

### 10. 反洗钱规则 + 警示信号（第 191–215 行）：收束和诊断标记

第 193-215 行是本章的反洗钱规则和日常诊断标记。三个层面的具体诊断标记：

**翻译要点：**
- 第 193 行的重申——"The model-decided alibi shows up wherever an AI system produces an output that affects us and the company narrates it in the grammar of system agency. The model decided. The algorithm flagged. The data showed. The benchmark scored. The verb's subject is a thing."——"模型决定的托辞出现在任何 AI 系统产生一个影响我们的输出、而公司以系统施事语法将其叙事的地方。模型决定了。算法标记了。数据显示了。基准评了分。动词的主语是一个东西。"
- 第 197-215 行的三个诊断标记列表——输入层/部署层/评估层的具体模式识别标志——中文必须以平行结构呈现
- 第 213 行是全章的最具行动性的句子——"The signature is the model's alibi made personal"——"签名是模型的托辞变得个人化"
- 第 215 行的最后一句话——"When the agents arrive in our work, we already know what to ask."——"当 Agentes 到达我们的工作中时，我们已经知道该问什么。"——开放式的结尾，暗示第四层（autonomous-action systems）

## 新术语

第 9 章新增 **15 条术语**已提交 Glossary Master 裁决。核心新概念：

| # | 英文 | 提案中文 | 说明 |
|---|---|---|---|
| 1 | **input layer** | 输入层 | **核心框架**——AI 技术栈第一层：训练数据 |
| 2 | **deployment layer** | 部署层 | **核心框架**——AI 技术栈第二层：模型行为 |
| 3 | **evaluation layer** | 评估层 | **核心框架**——AI 技术栈第三层：基准评测 |
| 4 | **sycophancy / sycophantic** | 谄媚行为 / 谄媚的 | **核心行为描述**——GPT-4o 的过度支持性虚伪回应 |
| 5 | **alibi escalation** | 托辞升级 | **核心分析模式**——洗白被截获时移动到更高层 |
| 6 | **grammar of system agency** | 系统施事语法 | **核心分析概念**——非人类名词占据动词主语位置 |
| 7 | **credentialing commons** | 认证公地 | **分析框架**——共享的评估基础设施 |
| 8 | **litigation interception triplet** | 诉讼拦截三元组 | **分析框架**——三个必同时存在的拦截条件 |
| 9 | **reward-shaping** | 奖励塑造 | **技术术语**——训练后优化框架的操作 |
| 10 | **reward signal** | 奖励信号 | **技术术语**——RLHF 反馈信号 |
| 11 | **post-training** | 训练后 | **技术术语**——复合形容词 |
| 12 | **model variant / variant** | 模型变体 | **技术术语**——同一个模型的不同优化版本 |
| 13 | **acquisition record** | 获取记录 | **法律/证据**——训练数据获取的证据记录 |
| 14 | **training corpus** | 训练语料 | **技术术语**——特指的训练数据集合 |
| 15 | **shadow library** | 影子图书馆 | **法律/版权**——LibGen、PiLiMi 等 |

请逐条对照 glossary.yml 的最终裁决版本。如果 Glossary Master 修改了提案译法，以最终裁决为准。

## 特别注意事项（按优先级排序）

### 1. 八问诊断的跨章一致性（全书最高优先级）

第 9 章在三层诊断中多次运行八问。八个问题的中文必须与第 3 章完全一致。以下为第 3 章 ready 文本中的已验证中文：

| 英文（第 3 章） | 中文（第 3 章 ready） |
|---|---|
| Who was publicly blamed? | 谁或什么被公开归咎？ |
| Who had control? | 谁拥有控制权？ |
| Who benefited? | 谁受益？ |
| Who knew or should have known? | 谁知情或应知情？ |
| Who could have prevented recurrence? | 谁能阻止复发？ |
| Who controlled the record? | 谁控制了记录？ |
| Who bore the cost? | 谁承担了代价？ |
| What would responsibility look like if it followed control instead of visibility? | 如果责任跟随控制权而非可见度，责任会是什么样子？ |

**关键：** 每一个问题的中文必须与第 3 章完全相同。不得因为上下文不同而改变措辞。注意第 3 章用的是"谁拥有控制权"而非"谁有控制权"——保持完全相同。

### 2. "语法即洗白"——本章的核心诊断语言

本章的核心论点是通过语法分析运行责任洗白诊断——非人类名词占据动词主语位置，吸收人类决策的归责。这是分析性的、语言学的诊断，不是政治指控。中文翻译必须保留这种分析语调的冷峻精确：

- "the verb's subject is a thing" → "动词的主语是一个东西"
- "the verb's subject at the input layer is 'data'" → "输入层动词的主语是'数据'"
- "the grammar is the laundering" → "语法即洗白"
- "the displaced decision" → "被置换的决策"
- "the named human decisions are absent from the grammar" → "被命名的人类决策从语法中缺席"

这些句子是分析判断，不是道德谴责。中文不可添加"显然""令人震惊"等修辞。

### 3. 技术 AI/ML 术语的精确性

本章涉及大量的 AI/ML 技术术语，需要精确区分：

| 英文 | 中文（提案/标准译法） | 备注 |
|---|---|---|
| training data | 训练数据 | 泛指 |
| training corpus / corpora | 训练语料 | 特指特定集合，等待 Glossary |
| model weights | 模型权重 | 标准技术术语 |
| large language model (LLM) | 大语言模型 | 标准译法 |
| benchmark | 基准评测 / 基准 | 标准译法 |
| leaderboard | 排行榜 | 标准译法 |
| LMArena / Chatbot Arena | 保留英文 LMArena | 专有平台名 |
| reward signal | 奖励信号（等待 Glossary） | |
| reward-shaping | 奖励塑造（等待 Glossary） | |
| post-training | 训练后（等待 Glossary） | |
| inference / inference logs | 推理 / 推理日志 | 标准译法 |
| open-source | 开源 | 标准译法 |
| variant | 变体（等待 Glossary） | |
| transformer architecture | 变换器架构 | 标准译法（不常见本章） |
| RLHF | 保留英文缩写 RLHF | 首次出现括号注（基于人类反馈的强化学习） |
| A/B testing | A/B 测试 | 标准译法 |
| black box | 黑箱 | 标准译法 |

### 4. 三个层术语的一致性

"input layer / deployment layer / evaluation layer"是本章的核心分析框架，贯穿全文。在 Glossary Master 裁决前，使用提案中文"输入层/部署层/评估层"。注意：

- 这三个术语可能在全章出现 20 次以上
- 每个层命名不同的非人类施事者（data / model / variant）
- 每个层的人类决策集不同
- 每个层的代价承担者不同

### 5. 法律术语精确性

| 英文 | 中文 | 备注 |
|---|---|---|
| summary judgment | 简易判决 | 美国联邦民事诉讼标准术语 |
| transformative fair use | 转化性合理使用 | 版权法标准术语 |
| fair use | 合理使用 | 中国知识产权法标准译法 |
| discovery | 证据开示 | 已有 glossary 译法（第 5 章建立） |
| deposition | 庭外证言/取证 | |
| class certification | 集体认证 | 美国集体诉讼程序术语 |
| class action | 集团诉讼 | 不同司法管辖区不同，注意通用性 |
| settlement | 和解 | 已有 glossary 译法（第 5 章建立） |
| acquisition record | 获取记录（等待 Glossary） | |
| shadow library | 影子图书馆（等待 Glossary） | |
| territoriality | 属地原则 | 国际私法标准术语 |
| motion to dismiss | 驳回起诉动议 | |
| discovery order | 证据开示令 | 已有 discovery → 证据开示 |
| copyright infringement | 版权侵权 | 标准译法 |

### 6. 公司名/产品名/案件名处理

| 英文 | 中文处理 | 备注 |
|---|---|---|
| Meta Platforms, Inc. | Meta Platforms, Inc.（元平台公司） | 首次出现括号注中文 |
| OpenAI | OpenAI（开放人工智能公司） | 首次出现括号注中文 |
| Anthropic PBC | Anthropic PBC（安思罗皮克公司） | 首次出现括号注中文 |
| Llama 4 / Llama 4 Maverick | 保留英文 | 产品名 |
| GPT-4o | 保留英文 | 产品名 |
| ChatGPT | 保留英文 | 产品名 |
| LMArena | 保留英文 | 平台名 |
| Common Crawl | 保留英文（通用爬虫库） | 首次括号注中文 |
| Books3 | 保留英文 | 语料库名 |
| LAION | 保留英文 | 组织名 |
| The Pile | 保留英文（"资料堆"语料库） | 首次括号注中文 |
| LibGen (Library Genesis) | 保留英文（LibGen——创世纪图书馆） | 首次括号注中文 |
| PiLiMi | 保留英文 | 盗版网站名 |
| *Bartz v. Anthropic PBC* | 斜体保留英文案名 | 首次括号注中文 |
| *The New York Times Company v. Microsoft Corp.* | 斜体保留英文案名 | 同上 |
| *Authors Guild v. OpenAI Inc.* | 斜体保留英文案名 | 同上 |
| *Getty Images v. Stability AI* | 斜体保留英文案名 | 同上 |

### 7. 人名翻译

| 英文 | 中文 | 备注 |
|---|---|---|
| Sam Altman | 山姆·奥特曼 | 标准译法（OpenAI CEO） |
| Mark Zuckerberg | 马克·扎克伯格 | 标准译法 |
| Ahmad Al-Dahle | 艾哈迈德·阿尔-达赫勒 | Meta GenAI 副总裁 |
| William Alsup | 威廉·阿尔萨普 | 联邦地区法官 |
| Sidney H. Stein | 西德尼·H·斯坦 | 联邦地区法官 |
| Araceli Martínez-Olguín | 阿拉塞莉·马丁内斯-奥尔金 | 联邦地区法官 |
| Joanna Smith | 乔安娜·史密斯 | 英国高等法院法官 |
| Dario Amodei | 达里奥·阿莫代 | Anthropic CEO |
| Shawn Presser | 肖恩·普雷瑟 | Books3 语料汇编者 |
| Benjamin Jowett | 本杰明·乔伊特 | 亚里士多德译者 |
| Gavin Newsom | 加文·纽瑟姆 | 加州州长 |

### 8. 非英语处理和引语

**题记（第 11-12 行）：**
> the servant is himself an instrument which takes precedence of all other instruments.
> — Aristotle, *Politics* I.4, trans. Benjamin Jowett

中文使用亚里士多德《政治学》I.4 的权威中译本（如吴寿彭译、颜一译等）。参考译文：
> 奴隶自身就是一种工具，而且在所有工具中占据优先地位。
> ——亚里士多德《政治学》I.4，本杰明·乔伊特英译

注意标注引用来自 Benjamin Jowett 英译。

**直接引语的翻译（第 10 个要点涉及的多处引语）：**

- 第 17 行（Meta 发言人声明）："Llama-4-Maverick-03-26-Experimental is a chat-optimized version we experimented with that also performs well on LMArena."——官方发言人的企业声明，中文需保持企业公关的正式语调

- 第 19-20 行（OpenAI post-mortem）："GPT-4o skewed towards responses that were overly supportive but disingenuous" / "focused too much on short-term feedback"——内部 post-mortem 的分析性语调

- 第 25 行（OpenAI 的 UK House of Lords 提交材料）："it would be impossible to train today's leading AI models without using copyrighted materials."——核心声明句，简洁有力

- 第 37 行（Sam Altman X 帖子）："too sycophant-y and annoying"——CEO 在 X 上的非正式语调，与 post-mortem 的正式语调形成对比。中文需保留其口语化色彩："过于谄媚和烦人"或"太谄媚了、太烦人了"

- 第 39 行（Al-Dahle X 帖子）："simply not true"——"根本不是事实"

- 第 107 行（LMArena 声明）："did not match what we expect from model providers" / "updated our leaderboard policies to reinforce our commitment to fair, reproducible evaluations so this confusion doesn't occur in the future"——基准运营者的正式声明语调

### 9. 回旋镖案例的跨章术语对齐

第 73-79 行引用的三个回旋镖案例，其关键术语必须与各章一致：

**Therac-25 回呼（第 75 行）：**
- "Malfunction 54" — 第 2 章已有中文处理方式
- "TREATMENT PAUSE" — 同上
- "the model is the software, the training corpus is the missing audit trail, and the benchmark rank is the new 'TREATMENT PAUSE'." — "模型是软件，训练语料是缺失的审计追踪，而排行榜排名是新的'TREATMENT PAUSE'"

**737 MAX 回呼（第 77 行）：**
- MCAS (Maneuvering Characteristics Augmentation System) — 第 2 章已有中文
- "MCAS handled it" — 第 2 章已有处理方式
- 本章关键句："'MCAS handled it' becomes 'the model decided,' but in the AI stack there is no pilot at the verb position to absorb the blame." — "'MCAS 处理了它'变为'模型决定了'，但在 AI 技术栈中没有飞行员坐在动词位置吸收指责。"

**Horizon 回呼（第 79 行）：**
- five-role conflation → 五角色融合（第 7 章已建立）
- 五个角色：deployer → 部署者、audit-trail holder → 审计追踪持有者、complainant → 投诉人、prosecutor → 检控方、disclosure controller → 披露控制者（第 7 章建立）

### 10. 图嵌入块

第 145-147 行的 `::: {.figure-embed}` 块嵌入一个比较三个层的图表。alt text 必须翻译：

> "The model did it" at three layers — input, deployment, evaluation — each with a different non-human subject taking the verb and a different party bearing the cost.

参考中文翻译：
> '"模型干了它"在三个层——输入层、部署层、评估层——每个层有一个不同的非人类主语占据动词位置和一个不同的方承担代价。'

`:::{.figure-embed}` 标记和 Markdown 图片路径保留原样。

### 11. 第 141-147 行的表标记

第 141 行包含一个表引入句：

> The three layers as a table; the walk above is its audio rendering, and listeners may skip the table.

这个句子位于 `:::{.figure-embed}` 上方的单独一行，是音频形式（audio form）的提示。中文译为：
> '三层以表格呈现；上述的叙述是其音频版本，听者可以跳过图表。'

注意与第 3 章的格式保持一致——第 3 章中类似句子为：
> '链条图以表格呈现；上述的八个问题叙述是其音频版本，听者可以跳过图表。'

### 12. 长句/复杂结构处理

第 9 章有多个法律和技术分析长句。按 `[SPLIT]` 标注规则处理：

- 第 55-57 行（控制/受益/知情收敛的复合句）：可以拆分，标注 `[SPLIT]`
- 第 87 行（部署层 post-mortem 的分析段落）：有多个嵌套列举——奖励信号设计者/团队主管/产品领导——可以按列举拆分
- 第 121 行（Alsup 判决分析段落）：复合句较多，注意保持法律分析的精确性
- 第 163 行（五角色融合的跨层应用）：多层嵌套条件句，注意中文逻辑链完整

### 13. 特别难点

**"The 'model decided' alibi is not new. The scale is new. The stack-depth is new. The grammar is not."**（第 73 行）
- 三个短句的递进节奏：不是新事物→规模是新的→技术栈深度是新的→语法不是新的
- 中文：""模型决定了"这个托辞不是新的。规模是新的。技术栈深度是新的。语法不是新的。"
- 保持短句节奏，不拉长，不合并

**"Blameless post-mortem methodology, imported from site-reliability engineering practice, is appropriate for systems failures in which a pager misfired or a configuration was wrong. It produces a responsibility-shaped hole when applied to judgment calls..."**（第 97 行）
- 这是本章最锐利的分析语句之一——无责文化在判断性决策中产生的后果
- "responsibility-shaped hole" → "责任形状的空洞"
- 中文需要保留该句的分析冷度，不添油加醋

**"The teaching point is the asymmetry. Three AI-stack layers. Three interception forms. Three different durabilities."**（第 189 行）
- 三个短句递进
- 中文：""教学点是不对称性。三个 AI 技术栈层。三种拦截形式。三种不同的持久性。"

**"The signature is the model's alibi made personal"**（第 213 行）
- "签名是模型的托辞变得个人化"
- made personal = 被变成个人的/个人化的——强调将系统性的责任洗白转嫁为个人的追责标签

**"When the agents arrive in our work, we already know what to ask."**（第 215 行）
- "当 agents 到达我们的工作中时，我们已经知道该问什么。"
- agents 在此处指自主行动系统（autonomous-action systems）——第四层。中文保留英文 agents 并在首次出现时括号注中文"自主行动系统"，或直接译为"自主行动系统（agents）"。

### 14. References 部分

第 220-233 行的 References 部分包含 9 条脚注定义（`[^307]` 至 `[^315]`）。处理规则：
- 脚注前面的说明句（第 222 行注释行）保留英文（这是给编译器的指令）
- URL 链接和归档链接原样保留（不翻译）
- `<sup>` 标签在正文中保留原样
- 脚注中的引用来源（文章名等）保留英文原文（如"Sycophancy in GPT-4o"）
- 注释格式保持原有 Markdown 语法
- PDF 链接和 Justia 案卷链接保留原文
- 注意第 308 行和 311 行是重复引用同一来源（Sam Altman 的 X 帖子）——保留原文编号

## 输出格式

请按 `translation/skills/translate.md` 中定义的对照格式输出至：
`/Users/duxiying/Documents/no-one-did-it/translation/chapters/09-the-model-did-it-draft.md`

格式要求：
- 每段/每节以分段对照呈现（原文 blockquote → 译文正文 → 翻译笔记）
- `<sup>N</sup>` 标签原样保留
- `:::{.figure-embed}` 块原样保留，alt text 翻译
- 非英语原文（拉丁 *Politics* 书名等）以斜体保留
- 法律案例名以斜体保留
- 长句拆分标注 `[SPLIT]`
- 术语摩擦标注 `[TERM-NOTE]`
- 歧义标注 `[AMBIGUOUS]`
- 翻译笔记覆盖：
  - 八问诊断框架与第 3 章的一致性
  - 三层分析框架的术语一致性
  - "语法即洗白"核心论点的节奏感
  - 回旋镖案例的术语跨章对齐
  - 三个记录索取要求的平行句式
  - 技术 AI 术语的精确性
  - 直接引语的语调保留（CEO 非正式 vs. post-mortem 正式 vs. 法律声明正式）

## 交接

Handoff: Reviewer（Translation Director 将在译文提交后分派审核）
Glossary status: 15 条新术语已提交 Glossary Master 裁决——请以 glossary.yml 最终版本为准
