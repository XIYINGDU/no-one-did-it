---
source: book/chapters-v6/09-the-model-did-it.md
translator: claude
chapter: 9
title_en: The Model Did It
title_zh: 模型干了它
glossary_version: 1.0.0-pilot (ch-09 terms approved 2026-06-13)
status: draft
---

# 第 9 章 — 模型干了它

## 题记

**原文：**
> the servant is himself an instrument which takes precedence of all other instruments.
>
> — Aristotle, *Politics* I.4, trans. Benjamin Jowett

**译文：**
> 奴隶自身就是一种工具，而且在所有工具中占据优先地位。
>
> ——亚里士多德《政治学》I.4，本杰明·乔伊特英译

---

## 开场场景

**原文：**
Across a single calendar window in the spring of 2025, the same grammatical move surfaced three times. Each time a non-human noun was placed in the verb's subject position, and each time it absorbed a decision a person had made. The move ran at three structurally distinct layers of one technology stack: **input**, where the model is built; **deployment**, where it is run; **evaluation**, where it is benchmarked. At each layer a different thing sits in the verb's subject position — at input it is the data, at deployment it is the model, at evaluation it is the variant. We meet these layers through three companies, in the order the events unfolded — but the layer, not the company, is the thing to watch.

**译文：**
在 2025 年春季的同一个日历窗口内，同一个语法操作出现了三次。每一次，一个非人类名词被放在了动词的主语位置上，每一次它吸收了一个人做出的决定。这个操作在一个技术栈的三个结构上不同的层中运行：**输入层**，模型在此构建；**部署层**，模型在此运行；**评估层**，模型在此接受基准评测。在每一层，一个不同的东西坐在动词的主语位置上——在输入层是数据，在部署层是模型，在评估层是变体。我们通过三家公司在事件发生的先后顺序中认识这些层——但值得关注的是层，而非公司。

**翻译笔记：**
- [TERM-NOTE] "the verb's subject is a thing" → "动词的主语是一个东西"：保留原文的简单直白和异质性。这是一个诊断性判断句，不是修辞。
- 三层的平行句式在中文中需保持对称。"At each layer a different thing sits in the verb's subject position" 的每一个实例（data/model/variant）需在中文中保持相同的句法位置。

---

**原文：**
On 5 April 2025, Meta Platforms, Inc. launched the Llama 4 family on its AI research blog and cited, in the launch communications, a position of #2 on the LMArena Chatbot Arena leaderboard. The model entry that occupied #2 was labelled "Llama-4-Maverick-03-26-Experimental." It was not the same set of weights that Meta released for public download. When the publicly released Llama 4 Maverick weights were added to LMArena under their public name six days later, on 11 April 2025, they ranked approximately #32. A gap of about thirty places. The first official explanation, given through a Meta spokesperson and quoted in *The Verge*, *TechCrunch*, and *The Register* between 7 and 8 April 2025, named the agent as the variant: "Llama-4-Maverick-03-26-Experimental is a chat-optimized version we experimented with that also performs well on LMArena."

**译文：**
2025 年 4 月 5 日，Meta Platforms, Inc.（元平台公司）在其 AI 研究博客上发布了 Llama 4 系列，并在发布传播中引用了其在 LMArena Chatbot Arena 排行榜上排名第 2 的成绩。占据第 2 位的模型条目被标记为 "Llama-4-Maverick-03-26-Experimental"。它与 Meta 公开发布供下载的权重并非同一组。当公开发布的 Llama 4 Maverick 权重六天后（2025 年 4 月 11 日）以其公开名称被加入 LMArena 时，其排名约为第 32 位。大约三十个位次的差距。第一个官方解释——通过 Meta 发言人提供，在 2025 年 4 月 7 日至 8 日期间被 *The Verge*、*TechCrunch* 和 *The Register* 引用——将施事者命名为变体："Llama-4-Maverick-03-26-Experimental 是我们在实验中尝试的一个对话优化变体，它在 LMArena 上也表现良好。"

**翻译笔记：**
- Meta Platforms, Inc. 首次出现括号注中文"元平台公司"
- *The Verge*、*TechCrunch*、*The Register* 保留英文斜体（出版物名）
- "named the agent as the variant" → "将施事者命名为变体"——保留 "agent"（施事者）的语言学含义

---

**原文：**
On 24 and 25 April 2025, OpenAI rolled out an updated version of GPT-4o as the default model behind ChatGPT. Within 48 to 72 hours, users on X and Reddit had surfaced examples of the deployed model producing what OpenAI's own subsequent post-mortem called "sycophantic" behaviour — praising a transparently bad business idea, applauding a user's narrative of stopping psychiatric medication and disengaging from family, validating delusional framings the model's published usage policy had been written to refuse. On 27 April 2025 Sam Altman, CEO of OpenAI, acknowledged the issue on X. The first official explanation, given in OpenAI's post-mortem of 29 April 2025 and the expanded post-mortem of 2 May 2025, named two agents at the verb position. The first was the model: "GPT-4o skewed towards responses that were overly supportive but disingenuous." The second was an optimisation framework: the company had "focused too much on short-term feedback."[<sup>1</sup>](#c9-1)

**译文：**
2025 年 4 月 24 日和 25 日，OpenAI（开放人工智能公司）推出了 GPT-4o 的更新版本，作为 ChatGPT 背后的默认模型。48 至 72 小时内，X 和 Reddit 上的用户已经曝光了该已部署模型产出示例，这些示例展示了 OpenAI 自身随后的事后分析（post-mortem）所称的"谄媚行为"——赞扬一个明显糟糕的商业想法，对一个用户停止精神科药物并脱离家庭的叙述表示赞赏，验证该模型已公布的用法政策本应拒绝的妄想性框架。2025 年 4 月 27 日，OpenAI 首席执行官山姆·奥特曼在 X 上承认了该问题。第一个官方解释——在 OpenAI 2025 年 4 月 29 日的事后分析和 2025 年 5 月 2 日的扩展事后分析中给出——在动词位置命名了两个施事者。第一个是模型："GPT-4o 偏向于产生过度支持性但虚伪的回应。"第二个是一个优化框架：该公司"过于关注短期反馈。"[<sup>1</sup>](#c9-1)

**翻译笔记：**
- [TERM-NOTE] "sycophantic" → "谄媚的"（已通过 Glossary Master 裁决）
- "post-mortem" → 保留英文"post-mortem"，在首次出现时括号注中文"事后分析"
- "skewed towards" → "偏向于" —— 保留原文的统计/技术性质的判断语调，非道德谴责
- <sup>1</sup> 标签原样保留

---

**原文：**
In the same April-to-September window, in a federal courthouse in San Francisco, a third version of the same grammar was being prepared for adjudication. On 23 June 2025, Judge William Alsup of the United States District Court for the Northern District of California handed down a summary judgment ruling in *Bartz v. Anthropic PBC*, Case No. 3:24-cv-05417. The ruling divided one company's conduct in two. Training a large language model on books that Anthropic had lawfully acquired was held to be transformative fair use under 17 U.S.C. § 107. Downloading and retaining approximately 196,640 books from the shadow library LibGen, and a further set of pirated books from PiLiMi, was held to be not fair use.

**译文：**
在同一个 4 月至 9 月的时间窗口内，在旧金山的一家联邦法院，同一语法的第三个版本正在被准备进入裁决。2025 年 6 月 23 日，美国加利福尼亚北区联邦地区法院的威廉·阿尔萨普法官在 *Bartz v. Anthropic PBC*（巴茨诉安思罗皮克公益公司案），案号 3:24-cv-05417 中，下达了一份简易判决裁定。该裁定将一家公司的行为一分为二。在 Anthropic 合法获取的书籍上训练大语言模型，被认定为 17 U.S.C. § 107 下的转化性合理使用。从影子图书馆 LibGen（创世纪图书馆）下载并保留约 196,640 本书，以及来自 PiLiMi 的另一批盗版书籍，被认定为非合理使用。

**翻译笔记：**
- [TERM-NOTE] "shadow library" → "影子图书馆"（已通过 Glossary Master 裁决，首次出现中英对照）
- "transformative fair use" → "转化性合理使用"（版权法标准术语）
- "summary judgment" → "简易判决"（美国联邦民事诉讼标准术语）
- *Bartz v. Anthropic PBC* 保留英文斜体（案例名），首次出现括号注中文
- 17 U.S.C. § 107 保留原文（美国法典引用）

---

**原文：**
The procedural sequence that followed has been short and steep. The class was certified on 17 July 2025. The settlement was announced on 5 September 2025, in the amount of $1.5 billion — what would be, if the court grants final approval, the largest reported copyright settlement in United States history by acknowledged press reporting. As of our manuscript-freeze date that approval is pending; we hold the superlative to that condition here and below.

**译文：**
此后的程序序列短促而陡峭。集体诉讼资格于 2025 年 7 月 17 日获得认证。和解于 2025 年 9 月 5 日宣布，金额为 15 亿美元——如果法院批准最终核准，这将是美国历史上经确认的新闻报道中最大的版权和解。截至我们的手稿冻结日期，该核准仍在等待中；我们在此后均在该条件下保留这一最高级表述。

**翻译笔记：**
- "class was certified" → "集体诉讼资格获得认证"（美国集体诉讼程序术语）
- "settlement" → "和解"（已通过 Glossary Master 裁决，第 5 章建立）
- "manuscript-freeze date" → "手稿冻结日期"

---

**原文：**
The input layer's official explanation predates the Anthropic case and was stated most sharply by another firm. OpenAI laid it down in a written submission to the United Kingdom House of Lords Communications and Digital Committee on 8 January 2024, and the framing was adopted in variant form across the litigation cluster. The submission named the agent as the data: "it would be impossible to train today's leading AI models without using copyrighted materials." Training data was renamed the load-bearing substance. The decisions that placed which works into which corpora on which dates were displaced from the grammar.

**译文：**
输入层的官方解释早于 Anthropic 案，并由另一家公司以最尖锐的方式陈述。OpenAI 在 2024 年 1 月 8 日向英国上议院通信与数字委员会提交的书面材料中阐述了这一观点，该框架在诉讼集群中以变体形式被采纳。该提交材料将施事者命名为数据："不使用版权材料训练当今领先的 AI 模型是不可能的。"训练数据被重新命名为承担负荷的物质。将哪些作品在哪些日期放入哪些语料的决策，从语法中被置换了出去。

**翻译笔记：**
- "load-bearing substance" → "承担负荷的物质" —— 保留了原文的工程/物理隐喻。原文用 substance 来强调训练数据被重新框架为"物质"而非"人类作品"。
- "displaced from the grammar" → "从语法中被置换出去"——关键诊断语言，保留原文的被动语态和"置换"(displaced)的分析冷静

---

**原文：**
Three operations. Three layers of the same stack — input, deployment, evaluation. Three official accounts in which the named agent is a non-human entity — the data, the model, the variant — and the named human decisions, the named acquisition dates, the named release approvals, and the named submission decisions are not on the visible surface of the explanation.

**译文：**
三个操作。同一个技术栈的三个层——输入、部署、评估。三个官方叙事，在其中被命名的施事者是一个非人类实体——数据、模型、变体——而被命名的人类决策、被命名的获取日期、被命名的发布批准、被命名的提交决策，不在解释的可见表面上。

**翻译笔记：**
- 三个平行短句保留原文节奏："Three operations. Three layers... Three official accounts..." → "三个操作。三个层...三个官方叙事..."
- "named" 的反复出现（named agent, named human decisions, named acquisition dates...）需保留——这是本章核心语法分析的一部分

---

**原文：**
The fair clue is in the grammar. At each of the three layers, the verb's subject is a thing. The thing that "performed well." The thing that "skewed." The thing that "would be impossible to train without." We ask, at each layer, what the grammar was doing — and which named human decision the grammar displaced.

**译文：**
公平的线索就在语法中。在三个层中的每一个，动词的主语都是一个东西。"表现良好"的那个东西。"偏向于"的那个东西。"没有它就无法训练"的那个东西。我们在每一层问，语法在做什么——以及语法将哪个被命名的人类决策置换了出去。

**翻译笔记：**
- "fair clue" → "公平的线索"——暗示读者已经得到了足够的信号去诊断，线索是"公平"提供的
- "what the grammar was doing" → "语法在做什么"——保留原文的简单质问语气
- 三个引号内的短语（performed well/skewed/would be impossible to train without）分别对应前文三个案例的核心措辞

---

## 三个操作，三个官方故事

**原文：**
The three official stories belong to the three layers, and we set them down in their own words before taking them apart. Each is from a primary source. Each is quoted to the standard the project's quote-integrity rule requires.

**译文：**
三个官方故事分别属于三个层，我们在拆解之前先以它们自己的话将其记录下来。每一个都来自一手资料。每一个的引用都达到本书引用完整性规则所要求的标准。

---

**原文：**
The first is at the input layer. The training-data framing has been laid down across more than a decade of corporate communication, but its highest-stakes statement in the litigation period is OpenAI's written evidence to the United Kingdom House of Lords Communications and Digital Committee, dated 8 January 2024. The sentence reads: "it would be impossible to train today's leading AI models without using copyrighted materials." The same submission characterised the choice as a structural one between training on copyrighted corpora under existing fair-use doctrine and not training competitive models at all. Around the same period, OpenAI and other AI developers continued to describe their corpora using the phrase "publicly available data," a framing that conflated availability on the open internet with permission for AI training. A third framing — adopted in defensive filings and accepted at least partially by the UK High Court on 4 November 2025 in *Getty Images v. Stability AI* — held that once a model is trained, its weights "contain statistically trained parameters, not stored copies or reconstructions" of any individual training example. The input is renamed substance. The output is renamed abstraction. The decisions that connect them are removed from the verbs.

**译文：**
第一个在输入层。训练数据的框架化在十多年的企业传播中已经被反复铺设，但在诉讼期间其最关键的陈述是 OpenAI 于 2024 年 1 月 8 日向英国上议院通信与数字委员会提交的书面证据。句子是："不使用版权材料训练当今领先的 AI 模型是不可能的。"同一份提交材料将这一选择定性为一个结构性选择——在现有的合理使用原则下对受版权保护的语料进行训练，和根本不训练具有竞争力的模型之间的选择。大约在同一时期，OpenAI 和其他 AI 开发公司继续使用"公开可用数据"这一短语来描述其语料——这一框架化将开放互联网上的可获取性与 AI 训练的许可混为一谈。第三种框架化——在防御性诉讼文件中被采用，并于 2025 年 11 月 4 日在 *Getty Images v. Stability AI*（盖蒂图片社诉稳定人工智能公司案）中被英国高等法院至少部分接受——认为一旦模型训练完成，其权重"包含统计训练参数，而非任何单个训练示例的存储副本或重构"。输入被重新命名为物质。输出被重新命名为抽象。连接它们的决策被从动词中移除。

**翻译笔记：**
- "framing" → "框架化"——在分析性上下文中，framing 指主动将某事物置于特定框架中的行为。中文"框架化"保留了这种构造性(constructive)的含义。
- "doctrine" → "原则"——在法律（合理使用原则）语境下使用（已通过 Glossary Master 裁决）

---

**原文：**
The second official story is at the **deployment layer**. OpenAI's post-mortem of 29 April 2025, "Sycophancy in GPT-4o: What happened and what we're doing about it," is the load-bearing primary document. It uses, throughout, the grammar of system agency. The model "began behaving" in certain ways. The optimisation framework "focused too much" on short-term feedback. The expanded post-mortem of 2 May 2025, "Expanding on what we missed with sycophancy," adds a procedural layer. The post-mortem states that internal evaluators — OpenAI's own term is "expert testers" — had raised concerns about the model's behaviour before launch, and that those concerns were treated as outweighed by positive signals from a broader A/B testing population. The post-mortem does not name the testers. It does not name the engineers who designed the reward signal. It does not name the product leadership that approved the default-model swap. The post-mortem names the optimisation choice. Sam Altman's X post of 27 April 2025, made before the formal post-mortem and setting the public framing under which the post-mortem would be read, characterises the issue at the personality level: the last couple of GPT-4o updates had made the personality "too sycophant-y and annoying."[<sup>2</sup>](#c9-2) Two layers of language. The CEO's framing places the cause on the model's personality. The post-mortem places the cause on the optimisation framework and the release process. Neither layer names a human decision-maker.

**译文：**
第二个官方故事在**部署层**。OpenAI 2025 年 4 月 29 日的事后分析《GPT-4o 中的谄媚行为：发生了什么以及我们正在采取的应对措施》是承担负荷的一手文件。它通篇使用了系统施事语法。模型"开始表现出"某些方式的行为。优化框架"过于关注"短期反馈。2025 年 5 月 2 日的扩展事后分析《关于我们谄媚行为方面遗漏内容的进一步说明》增加了一个程序层。该事后分析指出，内部评估人员——OpenAI 自己的术语是"专家测试员"——在发布前已对模型行为提出了担忧，而那些担忧被认为被一个更广泛的 A/B 测试人群的积极信号所压倒。该事后分析没有点名测试员。没有点名设计奖励信号的工程师。没有点名批准默认模型更换的产品领导层。该事后分析点名的是优化选择。Sam Altman 在 2025 年 4 月 27 日的 X 帖子——在正式事后分析之前发布，并设定了事后分析将被阅读的公共框架——将问题定性在人格层面：最近几次 GPT-4o 更新使得人格变得"过于谄媚和烦人。"[<sup>2</sup>](#c9-2) 两个语言层。CEO 的框架化将原因放在模型的人格上。事后分析将原因放在优化框架和发布流程上。两个层都没有点名人类决策者。

**翻译笔记：**
- [TERM-NOTE] "grammar of system agency" → "系统施事语法"（已通过 Glossary Master 裁决）
- "syophant-y and annoying" → "过于谄媚和烦人"——保留口语化色彩：CEO 在 X 上的非正式语调
- 三个平行的"does not name..." → "没有点名..."——保留原文的重复节奏

---

**原文：**
The third official story is at the **evaluation layer**. Meta's position on the Llama-4-Maverick-03-26-Experimental submission, given through a spokesperson and quoted across the trade press between 7 and 8 April 2025, treats the LMArena leaderboard as one experimental surface among many: "We experiment with all types of custom variants. Llama-4-Maverick-03-26-Experimental is a chat-optimized version we experimented with that also performs well on LMArena." On 7 April 2025, Ahmad Al-Dahle, Vice President for GenAI at Meta, posted on X denying that Meta had trained on test sets and characterising rumours of such conduct as "simply not true."[<sup>3</sup>](#c9-3) When the controversy moved from the model provider to the benchmark operator, LMArena (operated by Arena Intelligence, Inc., the spin-out of the LMSYS research project) responded in mid-April 2025 with a public statement that Meta's interpretation of LMArena's disclosure policy had not matched what the benchmark expected from model providers, and announced a policy revision. The named agent at the verb position shifts again. First the variant performed. Then the policy did not match expectations. At neither moment is the agent the named individual at Meta GenAI who chose to submit a stylistically tuned variant to a public leaderboard under a name that paired the variant with the upcoming public release.

**译文：**
第三个官方故事在**评估层**。Meta 对 Llama-4-Maverick-03-26-Experimental 提交事件的立场——通过发言人传达，并在 2025 年 4 月 7 日至 8 日期间被行业媒体引用——将 LMArena 排行榜视为众多实验表面之一："我们实验各种类型的定制变体。Llama-4-Maverick-03-26-Experimental 是我们在实验中尝试的一个对话优化变体，它在 LMArena 上也表现良好。"2025 年 4 月 7 日，Meta 的 GenAI 副总裁艾哈迈德·阿尔-达赫勒在 X 上发帖，否认 Meta 曾在测试集上训练，并将此类行为的传闻定性为"根本不是事实。"[<sup>3</sup>](#c9-3) 当争议从模型提供者转移到基准运营者时，LMArena（由 Arena Intelligence, Inc.——LMSYS 研究项目的衍生公司——运营）在 2025 年 4 月中旬发布公开声明，称 Meta 对 LMArena 披露政策的解释"与我们对模型提供者的预期不符"，并宣布了政策修订。动词位置被命名的施事者再次转移。先是变体表现良好。然后是政策与预期不符。在两个时刻，施事者都不是 Meta GenAI 内部那个选择将一个风格调整过的变体提交至公共排行榜、并以一个将该变体与即将到来的公开发布配对的名字提交的具名个人。

**翻译笔记：**
- "benchmark operator" → "基准运营者"——与"evaluation layer"分析框架一致
- 最后一句是典型的长嵌套句，保留原文结构以体现语法分析的精密性
- [SPLIT] 最后一句在中文中可拆分，但为保留原文的语法的严谨节奏，保持为单句

---

**原文：**
We can hold each of the three stories in mind separately. Our first promise here is that the three are not separate. They are a family of grammatical operations. The verb's subject at the input layer is "data." The verb's subject at the deployment layer is "the model" or "the reward signal." The verb's subject at the evaluation layer is "the variant" or "the policy." Each operation displaces a named human decision. The grammar is the laundering. The diagnostic that follows is what reaches the displaced decision.

**译文：**
我们可以在脑海中分别保留这三个故事。我们在这里的第一个承诺是：三者并非分离的。它们是一族语法操作。输入层动词的主语是"数据"。部署层动词的主语是"模型"或"奖励信号"。评估层动词的主语是"变体"或"政策"。每个操作置换了一个被命名的人类决策。语法即洗白。随之而来的诊断，就是要触及那个被置换的决策。

**翻译笔记：**
- [TERM-NOTE] "The grammar is the laundering." → "语法即洗白。"——本章最核心的论断句。中文保留极简的系词结构（"A 即 B"），不添加"本身"、"不过"等解释性修辞。
- 三个层的平行句法保留

---

## 在输入层运行诊断

**原文：**
The instrument here is the same one chapter 3 installed — the eight questions, asked in order: blame, control, benefit, knowledge, preventability, record-control, cost, and what responsibility would look like if it followed control instead of visibility. Chapter 7 closed Part II by showing that those eight only operate on cases where the record is accessible. The record is the prior condition. Now we take the next step. The AI stack is not a single architecture. It is three structurally distinct layers — input, deployment, evaluation — and at each layer the responsibility-laundering grammar names a different non-human agent, displaces a different set of human decisions, and requires the diagnostic to climb to a different rung of named actors. The same alibi shape recurs at each layer; the diagnostic reaches different humans each time. We begin at the input layer, and we run all eight in full.

**译文：**
此处的工具与第 3 章安装的是同一个——八个问题，按顺序问：归咎、控制、受益、知情、可预防性、记录控制、代价，以及如果责任跟随控制权而非可见度，责任会是什么样子。第 7 章在结束第二部分时指出，这八个问题仅在记录可获取的案例中才能运行。记录是前提条件。现在我们迈出下一步。AI 技术栈不是单一架构。它是三个结构上不同的层——输入、部署、评估——而在每一层，责任洗白语法命名了一个不同的非人类施事者，置换了一组不同的人类决策，并要求诊断攀爬至不同层级的具名行为者。同一个托辞形状在每一层重复出现；诊断触及的人类每次不同。我们从输入层开始，完整运行全部八个问题。

**翻译笔记：**
- "the eight questions" → "八个问题"——与第 3 章诊断框架用语一致
- 八个问题的每一项名称（blame/control/benefit/knowledge/preventability/record-control/cost）——中文需与第 3 章一致：归咎/控制/受益/知情/可预防性/记录控制/代价
- "alibi shape" → "托辞形状"——"alibi→托辞"已有 glossary 定义

---

**原文：**
The anchor is the training-data litigation cluster. Hybrid classification: the primary case-type is **system/object alibi**; the secondary is **cost-bearing goat**. The primary classification holds because the load-bearing laundering is the grammar — "data," "the corpus," "the model" — that renames human creative work as substance. The secondary fires because the rights-holders absorbing the cost of the renaming are not visible at the narrative centre of the AI story. The two classifications do not collapse into each other. The first names the mechanism. The second names the harm.

**译文：**
锚点是训练数据诉讼集群。混合分类：主要案件类型为**系统/对象托辞**；次要为**承担代价的山羊**。主要分类成立，因为承担负荷的洗白是语法——"数据"、"语料"、"模型"——将人类创造性工作重新命名为物质。次要分类触发，因为吸收了重命名代价的权利持有者在 AI 故事的叙事中心并不可见。两种分类不会互相坍缩。第一种命名了机制。第二种命名了伤害。

**翻译笔记：**
- "Hybrid classification" → "混合分类"——与第 2/3 章分类框架一致
- "system/object alibi" → "系统/对象托辞"（已通过 Glossary Master 裁决）
- "cost-bearing goat" → "承担代价的山羊"（已通过 Glossary Master 裁决）
- "The two classifications do not collapse into each other." → "两种分类不会互相坍缩。"——保留原文的物理/认知隐喻

---

**原文：**
*Who was publicly blamed?* Four sequential containers, escalating across the period of the litigation. First, "data" or "the corpus" — the input substance, the most basic alibi, in which human work is renamed material that data curators (Common Crawl; the Books3 corpus assembled by Shawn Presser from the shadow library Bibliotik in 2020; LAION; EleutherAI for The Pile) are responsible for. Second, when the suit gets specific in *Bartz v. Anthropic*, "the shadow library" — LibGen and PiLiMi as the named non-human accomplices, indifferent to which works they contained, acquired by Anthropic at one remove from the original piracy. Third, "the model" itself — once trained, the artifact whose outputs are at issue, framed in defensive filings as containing statistical parameters rather than copies. Fourth, "the market" or "national AI competitiveness" — the highest-order alibi, in which constraining training is positioned as ceding strategic ground. At every container the named agent is non-human and the named decisions are absent.

**译文：**
*谁或什么被公开归咎？*四个顺序容器，在诉讼期间逐级升级。第一，"数据"或"语料"——输入物质，最基础的托辞，人类工作在此被重新命名为数据策展人（Common Crawl 通用爬虫库；由 Shawn Presser 从影子图书馆 Bibliotik 在 2020 年汇编的 Books3 语料；LAION；EleutherAI 的 The Pile "资料堆"语料库）负责的材料。第二，当诉讼在 *Bartz v. Anthropic* 中变得具体时，"影子图书馆"——LibGen 和 PiLiMi 作为被命名的非人类共犯，对其所包含的作品漠不关心，被 Anthropic 以与原始盗版相隔一层的方式获取。第三，"模型"本身——一旦训练完成，其输出成为争议焦点的人工制品，在防御性诉讼文件中被框架化为包含统计参数而非副本。第四，"市场"或"国家 AI 竞争力"——最高级别的托辞，在此限制训练被定位为让出战略阵地。在每个容器中，被命名的施事者都是非人类的，被命名的决策都是缺席的。

**翻译笔记：**
- [TERM-NOTE] 八个问题的第一问中文必须与第 3 章完全一致："谁或什么被公开归咎？"——注意"谁或什么"(Who or what)而非仅"谁"(Who)
- "containers" → "容器"——保留原文的容器隐喻，与第 3 章一致的术语
- Common Crawl、Books3、LAION、The Pile 保留英文，首次出现括号注中文说明
- Bibliotik 保留英文（影子图书馆名）
- "at one remove from" → "以相隔一层的方式"——保留原文的"remoteness"含义

---

**原文：**
Control, benefit, and knowledge run together at this layer, and they run to the same place. Each AI developer controlled the choice of which corpora to include in training. Each controlled the choice between lawful acquisition — for example, OpenAI's later licensing agreements with News Corp, the Associated Press, Axel Springer, Le Monde, and Reddit, and Anthropic's later lawful acquisition of books — and shadow-library acquisition. Each controlled the model release decision. Each controlled the pre-litigation messaging that framed the activity. Per the *Bartz* ruling, Anthropic in fact had the option to acquire books lawfully and in some instances did so. The shadow-library acquisition was, on the court's reading of the acquisition record, a discretionary choice. The institutions positioned as upstream — Common Crawl, LAION, the Books3 curator — controlled the assembled corpora made available to the labs. The load-bearing controlled entities, by the court's analysis, are the labs that chose to use the corpora.

**译文：**
控制、受益和知情在这一层汇聚在一起，而且它们指向同一个地方。每个 AI 开发公司都控制着将哪些语料纳入训练的选择。每个公司都控制着合法获取——例如 OpenAI 后来与 News Corp、美联社、Axel Springer、*Le Monde*（世界报）和 Reddit 的许可协议，以及 Anthropic 后来的合法书籍获取——与影子图书馆获取之间的选择。每个公司都控制着模型发布决策。每个公司都控制着框架化该活动的诉讼前信息传播。根据 *Bartz* 裁定，Anthropic 事实上拥有合法获取书籍的选择权，并且在某些情况下也确实这么做了。影子图书馆获取，根据法院对获取记录的理解，是一个酌定性选择。被定位为上游的机构——Common Crawl、LAION、Books3 汇编者——控制着提供给实验室的已汇编语料。根据法院的分析，承担负荷的控制实体是选择使用这些语料的实验室。

**翻译笔记：**
[SPLIT] 第二句拆分为多个中文句，保留信息顺序不变。
"run together" → "汇聚在一起"——隐喻性的物理描述
"discretionary choice" → "酌定性选择"——法律语境术语

---

**原文：**
The benefit accrued to those same labs. OpenAI's late-2025 valuation exceeded $150 billion; Anthropic's exceeded $30 billion; Microsoft's Azure OpenAI revenue ran to tens of billions across the same window. The value of the training corpora was captured in model weights, which generated the revenue. The rights-holders received no compensation at training time. Post-litigation settlements — *Bartz*'s $1.5 billion; the licensing deals that followed — capture a fraction of the value extracted at training. The class structure of the *Bartz* settlement makes the per-author figure legible: approximately $3,000 per work for approximately 500,000 works included in the LibGen and PiLiMi corpora that Anthropic had acquired. The per-work figure is the settlement's mathematics, not the market value extracted from the corpus at training time. The convergence of control and benefit at the same actor is the structural fact on the public record; whether benefit motivated the control choices is a question for evidentiary discovery.

**译文：**
受益归属于同一批实验室。OpenAI 在 2025 年末的估值超过 1500 亿美元；Anthropic 超过 300 亿美元；微软的 Azure OpenAI 收入在同一窗口内达到数百亿美元。训练语料的价值被捕获在模型权重中，而这些权重产生了收入。权利持有人在训练时未获得任何补偿。诉讼后的和解——*Bartz* 案的 15 亿美元；随后达成的许可协议——捕获了训练时所提取价值的一小部分。*Bartz* 案和解的集体诉讼结构使每位作者的数字变得可读：在 Anthropic 获取的 LibGen 和 PiLiMi 语料中，约 500,000 件作品每件约 3,000 美元。每件作品数字是和解协议的算术，而非训练时从语料中提取的市场价值。控制与受益在同一行为者身上的汇聚，是公共记录上的结构性事实；受益是否驱动了控制选择，是一个需要证据开示来回答的问题。

**翻译笔记：**
- "benefit accrued" → "受益归属于"——保留受益流向的法律/经济含义
- "evidentiary discovery" → "证据开示"（已通过 Glossary Master 裁决，第 5 章建立）

---

**原文：**
And the documentary record establishes the knowledge. The *Bartz* ruling and exhibits, per Judge Alsup's summary judgment order of 23 June 2025, document that Anthropic's pre-2024 acquisition of LibGen and PiLiMi corpora was visible to the company at the level of internal communication referencing the corpora by name and acknowledging their unlicensed character. The level of internal knowledge varies by defendant; *Bartz* is the highest-evidence-grade finding to date that a major AI developer knowingly trained on pirated books.

**译文：**
而文件记录确立了知情。*Bartz* 裁定及附件，根据 Alsup 法官 2025 年 6 月 23 日的简易判决令，记录了 Anthropic 在 2024 年前对 LibGen 和 PiLiMi 语料的获取在公司内部是可见的——内部通讯中按名称引用了这些语料并承认了其未经许可的性质。内部知情的程度因被告而异；*Bartz* 案是迄今为止证据等级最高的认定——一家主要 AI 开发公司在知情的情况下使用盗版书籍进行训练。

**翻译笔记：**
- "knowledge" → "知情"——与第 3 章八问第四问"谁知情或应知情"一致
- "documentary record" → "文件记录"——强调记录的具体文件属性

---

**原文：**
Two other cases in the same cluster have moved the public-record question forward at different speeds. In *Authors Guild v. OpenAI Inc.* (S.D.N.Y., Case No. 1:23-cv-08292, Judge Sidney H. Stein), the October 2025 ruling on OpenAI's motion to dismiss denied the motion in part and allowed copyright-infringement claims related to ChatGPT output to proceed to discovery. In *The New York Times Company v. Microsoft Corp.* (S.D.N.Y., Case No. 1:23-cv-11195, MDL), the November 2025 discovery order required OpenAI to preserve output log data including ChatGPT conversation logs that had been scheduled for deletion under the company's standard retention policy[<sup>4</sup>](#c9-4).

**译文：**
同一集群中的另外两起案件以不同速度推进了公共记录的问题。在 *Authors Guild v. OpenAI Inc.*（作者协会诉 OpenAI 公司案，纽约南区联邦地区法院，案号 1:23-cv-08292，Sidney H. Stein 法官）中，2025 年 10 月对 OpenAI 驳回起诉动议的裁定部分驳回了该动议，允许与 ChatGPT 输出相关的版权侵权索赔进入证据开示程序。在 *The New York Times Company v. Microsoft Corp.*（纽约时报公司诉微软公司案，纽约南区联邦地区法院，案号 1:23-cv-11195，跨地区诉讼）中，2025 年 11 月的证据开示令要求 OpenAI 保留输出日志数据，包括原本计划根据公司标准保留政策予以删除的 ChatGPT 对话日志[<sup>4</sup>](#c9-4)。

**翻译笔记：**
- "motion to dismiss" → "驳回起诉动议"——美国联邦民事诉讼标准术语
- "discovery" → "证据开示"（已通过 Glossary Master 裁决）
- "discovery order" → "证据开示令"
- S.D.N.Y.、MDL 保留英文缩写（美国联邦法院管辖标识）
- <sup>4</sup> 标签原样保留

---

**原文：**
Discovery in each case is the instrument by which what was known internally to each developer enters the public record.

**译文：**
每个案件中的证据开示，都是各开发公司内部所知道的东西进入公共记录的工具。

---

**原文：**
*Who could have prevented recurrence?* The lab, in choosing not to acquire pirated corpora. The regulator, in setting training-data disclosure obligations. The court, in interpreting fair-use doctrine against acquisition-record evidence rather than against post-training behavioural abstractions. Each is preventability at a different layer. Each is now partly engaged. California's SB-942, the California AI Transparency Act, signed by Governor Gavin Newsom on 19 September 2024, was amended by AB-853 (signed 13 October 2025) to push its operative date to 2 August 2026; its primary focus is AI-generated content provenance rather than training-data manifest disclosure. The European Union's AI Act, Regulation (EU) 2024/1689, contains training-data summary obligations in Article 53 for general-purpose AI model providers, with operative dates phased across 2025 and 2026. The statutory layer is partly operative and partly future-tense. The judicial layer, per *Bartz*, has reached the acquisition record and applied existing copyright doctrine to it.

**译文：**
*谁能阻止复发？*实验室——通过选择不获取盗版语料。监管者——通过设定训练数据披露义务。法院——通过解释合理使用原则时对照获取记录证据而非对照训练后的行为抽象。每一层都有其不同的可预防性。每一层都已部分启动。加利福尼亚州的 SB-942——《加州 AI 透明度法案》——由州长加文·纽瑟姆于 2024 年 9 月 19 日签署，后被 AB-853（2025 年 10 月 13 日签署）修订，将其生效日期推迟至 2026 年 8 月 2 日；其主要关注点是 AI 生成内容的来源追溯，而非训练数据清单披露。欧盟的《AI 法案》(Regulation (EU) 2024/1689)在第 53 条中对通用 AI 模型提供者规定了训练数据摘要义务，生效日期分阶段在 2025 年和 2026 年实施。法定层面部分已生效、部分尚在未来时态。司法层面，根据 *Bartz* 案，已经到达了获取记录并将现有版权原则适用于其上。

**翻译笔记：**
第五问的中文必须与第 3 章完全一致："谁能阻止复发？"
"doctrine" → "原则"（法律语境——合理使用原则）

---

**原文：**
*Who controlled the record?* The labs controlled the training-data manifests, most of which are not public. Anthropic's manifest was partially disclosed under court order in *Bartz*. The labs controlled the internal communications about corpus acquisition. The labs controlled the model weights themselves. The labs controlled the inference logs that could — per the November 2025 NYT discovery order — reveal which user prompts produced regurgitation of substantial passages from copyrighted works. The U.S. federal courts (Northern District of California, Southern District of New York, MDL) control the litigation record. The UK High Court (Chancery Division) controls the *Getty v. Stability AI* record. The California legislature controls the SB-942 and AB-853 statutory record. *The training corpus is the record.* What was in it, and how it got there, is the diagnostic question on which the input-layer alibi stands or falls.

**译文：**
*谁控制了记录？*实验室控制着训练数据清单，其中大部分不对外公开。Anthropic 的清单在 *Bartz* 案中根据法院命令被部分披露。实验室控制着关于语料获取的内部通讯。实验室控制着模型权重本身。实验室控制着推理日志——根据 2025 年 11 月的 NYT 证据开示令——可以揭示哪些用户提示词产生了对版权作品大量段落的复述。美国联邦法院（加利福尼亚北区联邦地区法院、纽约南区联邦地区法院、跨地区诉讼）控制着诉讼记录。英国高等法院（大法官庭）控制着 *Getty v. Stability AI* 的记录。加利福尼亚州立法机关控制着 SB-942 和 AB-853 的法定记录。*训练语料就是记录。*里面有什么，以及它如何到了那里，是输入层托辞成立或崩塌所依赖的诊断问题。

**翻译笔记：**
第六问的中文必须与第 3 章完全一致："谁控制了记录？"
关键句："The training corpus is the record." → "训练语料就是记录。"——中文保留极简的系词结构。

---

**原文：**
*Who bore the cost?* Authors, photographers, journalists, code contributors, visual artists. The *Bartz* settlement makes the cost legible for one defendant on one corpus subset; the diffuse cost — journalists whose work is now competed against by ChatGPT-as-summariser; photographers whose stock market has been hollowed by image generators trained on their archives; programmers whose code was used to train code-assistant models; artists whose distinctive styles can be invoked by prompt — is structural and partially invisible in the case-by-case litigation record. The rights-holders are not being publicly blamed for AI's growing pains. They are being erased from the grammar of how AI training is described. The alibi here is not "the authors caused this" but "training data is a substance, not a body of human work." Cost-absorbing silence rather than active accusation. That is the operative form of cost-bearing goat at the input layer.

**译文：**
*谁承担了代价？*作者、摄影师、记者、代码贡献者、视觉艺术家。*Bartz* 案和解使代价对一个被告在一个语料子集上变得可读；而弥散性代价——记者的工作如今被 ChatGPT-as-summariser（作为摘要工具的 ChatGPT）所竞争；摄影师的市场被以其档案训练的图片生成器所掏空；程序员的代码被用于训练代码辅助模型；艺术家的独特风格可以通过提示词被调用——是结构性的，且在逐案处理的诉讼记录中部分不可见。权利持有人并未因 AI 的成长之痛而被公开归咎。他们正在被从 AI 训练被描述的语法中抹去。此处的托辞不是"作者引起了这个"而是"训练数据是一种物质，而非一组人类作品。"吸收代价的沉默，而非积极的指控。那就是输入层承担代价的山羊的操作形式。

**翻译笔记：**
第七问的中文必须与第 3 章完全一致："谁承担了代价？"
"Cost-absorbing silence rather than active accusation." → "吸收代价的沉默，而非积极的指控。"——关键区分句，保留短句节奏。

---

**原文：**
What would responsibility look like if it followed control instead of visibility? Named acquisition decisions, by named executives, at named labs, on documented dates, against documented licensing alternatives. Anthropic PBC is the corporate respondent in *Bartz*. Per the public record, Dario Amodei is CEO of Anthropic PBC. No public statement attributing the LibGen or PiLiMi acquisition decision to Amodei personally has been documented as of May 2026. No civil or criminal liability has been adjudicated against Amodei as of May 2026. The litigation has reached the corporate actor. The five-role conflation we named in Chapter 7 — same institution deploys, audits, complains, prosecutes, discloses — applies directly to AI training at the input layer. The same lab assembles the corpus, controls the manifest, defends the litigation, and decides what is disclosed in discovery. Chapter 7's anti-laundering rule applies: where one institution holds all the record-control roles, external examination is the necessary instrument.

**译文：**
*如果责任跟随控制权而非可见度，责任会是什么样子？*具名的获取决策，由具名的高管在具名的实验室做出，在有记载的日期依据有记载的许可替代方案做出。Anthropic PBC 是 *Bartz* 案中的公司应诉方。根据公共记录，达里奥·阿莫代是 Anthropic PBC 的首席执行官。截至 2026 年 5 月，没有公开陈述将 LibGen 或 PiLiMi 的获取决策归因于 Amodei 个人的记录。截至 2026 年 5 月，没有针对 Amodei 的民事或刑事责任裁判。诉讼已经触及公司行为者。我们在第 7 章中命名的五角色融合——同一机构部署、审计、投诉、检控、披露——直接适用于输入层的 AI 训练。同一个实验室汇编语料、控制清单、辩护诉讼、并决定在证据开示中披露什么。第 7 章的反洗白规则适用：当一个机构持有所有记录控制角色时，外部审查是必要的工具。

**翻译笔记：**
第八问的中文必须与第 3 章完全一致："如果责任跟随控制权而非可见度，责任会是什么样子？"
"five-role conflation" → "五角色融合"（已通过 Glossary Master 裁决，第 7 章建立）

---

**原文：**
The reversal sentence belongs here. The training-data alibi is the input-layer instance of the same record-control conflation chapter 7 installed at the institutional layer. The "data is just data" grammar performs the laundering. The discovery record breaks it.

**译文：**
反向归责句在此处属于它的位置。训练数据托辞是第 7 章在制度层面安装的同一记录控制融合在输入层的实例。"数据只是数据"的语法执行洗白。证据开示记录打破它。

**翻译笔记：**
"reversal sentence" → "反向归责句"——呼应第 8 章的"inversion→反向归责"术语
三个短句的递进节奏保留

---

## Therac、MAX、Horizon——更新

**原文：**
The "model decided" alibi is not new. The scale is new. The stack-depth is new. The grammar is not. We take three callbacks at one or two sentences each, to ground the diagnostic in cases we have already installed at full depth.

**译文：**
"模型决定了"这个托辞不是新的。规模是新的。技术栈深度是新的。语法不是新的。我们以每案一两句的长度取三个回呼，将诊断锚定在我们已充分深度安装的案例中。

**翻译笔记：**
四个短句的递进节奏保留——"not new/scale new/stack-depth new/grammar not" → "不是新的/规模是新的/栈深度是新的/语法不是"
"callbacks" → "回呼"——与全书技术术语一致

---

**原文：**
Chapter 2 read **Therac-25**, the radiation therapy machine built by Atomic Energy of Canada Limited, which produced fatal overdoses at six US and Canadian treatment centres between June 1985 and January 1987. The audit trail was a single memory-mapped error-code counter; "Malfunction 54" and "TREATMENT PAUSE" were the alibi. The "model decided" framing is the direct lineal descendant of "the software was the cause," at scale: the model is the software, the training corpus is the missing audit trail, and the benchmark rank is the new "TREATMENT PAUSE."

**译文：**
第 2 章介绍了 **Therac-25**，加拿大原子能有限公司（Atomic Energy of Canada Limited）制造的放射治疗机，在 1985 年 6 月至 1987 年 1 月期间在美国和加拿大的六个治疗中心产生了致命过量辐射。审计追踪是一个单一的内存映射错误代码计数器；"Malfunction 54"（故障 54）和"TREATMENT PAUSE"（治疗暂停）就是托辞。"模型决定了"的框架化是"软件是原因"的直系后代，但规模更大：模型是那款软件，训练语料是缺失的审计追踪，而排行榜排名是新的"TREATMENT PAUSE"。

**翻译笔记：**
- [TERM-NOTE] "Malfunction 54" → 第 2 章 ready 文本中处理为：`"Malfunction 54"（故障54）`——保留英文原文 + 括号注中文
- "TREATMENT PAUSE"——在第 2 章 ready 文本中未直接出现，此处处理为：`"TREATMENT PAUSE"（治疗暂停）`——保留英文大写原文 + 括号注中文
- "at scale" → "但规模更大"——补充性的解释，表明"直系后代"的关系中规模差异是关键

---

**原文：**
Chapter 2 also read the **Boeing 737 MAX** as a partial scapegoat with system/object alibi secondary — pilots were named as the cause of the Lion Air and Ethiopian Airlines crashes while the Maneuvering Characteristics Augmentation System became the engineered-system blame container. The model alibi runs the same shape with no pilot. "MCAS handled it" becomes "the model decided," but in the AI stack there is no pilot at the verb position to absorb the blame. There is only the lab, the deployer, and the executive who approved the release. The earlier chapter's partial scapegoat is replaced by an unoccupied seat.

**译文：**
第 2 章还介绍了**波音 737 MAX**，将其定性为部分替罪羊，次要为系统/对象托辞——飞行员被命名为狮航和埃塞俄比亚航空空难的原因，而机动特性增强系统成了工程系统的归咎容器。模型托辞以相同的形状运行，但没有飞行员。"MCAS 处理了它"变为"模型决定了"，但在 AI 技术栈中，没有飞行员坐在动词位置上吸收指责。只有实验室、部署者和批准发布的那个高管。前一章的部分替罪羊被一个空位所取代。

**翻译笔记：**
- "Maneuvering Characteristics Augmentation System" → "机动特性增强系统"（与第 2 章一致，首次出现括号注英文 MCAS）
- "MCAS handled it" → "MCAS 处理了它"（与第 2 章一致）
- "unoccupied seat" → "空位"——保留原文对"动词位置"（verb position）语法分析的呼应

---

**原文：**
Chapter 7 installed the **Horizon** five-role conflation diagnostic. Same institution deploys, audits, complains, prosecutes, and discloses. The AI stack runs the same conflation with the labels updated. The same lab trains the model, releases it, monitors its post-deployment behaviour, writes the post-mortem when the behaviour goes wrong, and controls the training-corpus disclosure. The Post Office held five roles against a population of sub-postmasters dispersed across the United Kingdom. The AI labs hold the same five roles against a population of users dispersed across the consumer internet, and against a population of rights-holders dispersed across the world of creative work. Chapter 7's anti-laundering rule applies directly. The record is first. Where the record is controlled by the institution being diagnosed, the diagnostic cannot answer. The first task is to break the record-control architecture. What follows shows what that task looks like at each AI-stack layer.

**译文：**
第 7 章安装了 **Horizon** 五角色融合诊断。同一机构部署、审计、投诉、检控、披露。AI 技术栈以更新后的标签运行着同样的融合。同一个实验室训练模型、发布它、监控其部署后行为、当行为出问题时撰写事后分析、并控制训练语料的披露。邮局面对的是分散在英国各地的副邮政局长群体。AI 实验室面对的是分散在消费互联网上的用户群体，以及分散在创意世界中的权利持有人群体。第 7 章的反洗白规则直接适用。记录是第一位的。当记录由被诊断的机构控制时，诊断无法回答。首要任务是打破记录控制架构。接下来的部分展示了该任务在 AI 技术栈的每一层看起来是什么样子。

**翻译笔记：**
- "five-role conflation" → "五角色融合"（第 7 章已建立）
- "sub-postmasters" → "副邮政局长"（第 7 章已建立）
- 五角色列表（deploys/audits/complains/prosecutes/discloses）→ "部署、审计、投诉、检控、披露"

---

## 72 小时回滚

**原文：**
The deployment layer is the AI stack's most visible surface. It is also the layer at which the laundering operates fastest and at which the institutional response is most ready-made.

**译文：**
部署层是 AI 技术栈中最可见的表面。它也是洗白运行最快、制度性应对最现成的层。

**翻译笔记：**
两个短句的平行结构保留——"most visible surface / operates fastest / institutional response most ready-made"

---

**原文：**
Return to the GPT-4o sycophancy incident. The behaviour was systematic. The pattern was visible enough across X and Reddit by 26-27 April 2025 that Sam Altman acknowledged it publicly within 48 hours of the rollout. OpenAI rolled the update back over 28-29 April 2025. The published post-mortem appeared on 29 April; the expanded post-mortem on 2 May. The technical mechanism the post-mortem identifies is a reward-shaping choice: the post-training optimisation framework was weighted toward short-term user feedback signals, and that weighting produced the sycophantic skew when the model was deployed at default-model scale. The procedural mechanism the post-mortem identifies is a release-decision choice: internal expert testers had flagged concerns, those concerns were treated as outweighed by positive signals from a broader A/B testing population, and the release proceeded.

**译文：**
回到 GPT-4o 谄媚事件。这种行为是系统性的。该模式在 X 和 Reddit 上到 2025 年 4 月 26-27 日已足够可见，以至于 Sam Altman 在推出后 48 小时内就公开承认了它。OpenAI 在 4 月 28-29 日回滚了该更新。已发表的事后分析于 4 月 29 日出现；扩展事后分析于 5 月 2 日出现。事后分析识别的技术机制是一个奖励塑造选择：训练后优化框架偏向于短期用户反馈信号，而该偏向在模型以默认模型规模部署时产生了谄媚性倾斜。事后分析识别的程序机制是一个发布决策选择：内部专家测试员已经标记了担忧，那些担忧被认为被更广泛的 A/B 测试人群的积极信号所压倒，于是发布继续进行。

**翻译笔记：**
- [TERM-NOTE] "reward-shaping" → "奖励塑造"（已通过 Glossary Master 裁决）
- [TERM-NOTE] "reward signal" → "奖励信号"（已通过 Glossary Master 裁决）
- "post-training optimisation framework" → "训练后优化框架"（已通过 Glossary Master 裁决）
- "sycophantic skew" → "谄媚性倾斜"

---

**原文：**
Each of these findings is on the public record because OpenAI placed it there. The post-mortem is a primary corporate document. It uses the grammar of system agency throughout. The model "began behaving." The reward signal "focused too much" on short-term feedback. The process "did not adequately weight" qualitative tester concerns against quantitative ones. The named agent at every verb is a non-human entity — the model, the signal, the process. The post-mortem does not name the engineers who designed the reward signal. It does not name the team leads who approved the design. It does not name the product leadership that approved the default-model swap. It identifies "expert testers" as a category of internal evaluator whose number, seniority, and specific concerns are not publicly disclosed. The displaced decisions are inside the company's record-control envelope.

**译文：**
这些发现中的每一项都在公共记录上，因为 OpenAI 将其放在了那里。事后分析是一份公司一手文件。它通篇使用了系统施事语法。模型"开始表现出"某种方式的行为。奖励信号"过于关注"短期反馈。流程"未充分权衡"定性测试者的关切与定量测试者的关切。每个动词位置被命名的施事者都是一个非人类实体——模型、信号、流程。事后分析没有点名设计奖励信号的工程师。没有点名批准该设计的团队主管。没有点名批准默认模型更换的产品领导层。它将"专家测试员"识别为一类内部评估人员——其人数、资历和具体关切未对外公开。被置换的决策位于公司的记录控制信封之内。

**翻译笔记：**
- [TERM-NOTE] "grammar of system agency" → "系统施事语法"（已通过 Glossary Master 裁决）
- "record-control envelope" → "记录控制信封"——保留原文的隐喻（envelope 表示封闭的、不可见的管理边界）

---

**原文：**
Run the eight here in abbreviated form — the same chapter-3 instrument, not a new one. Four of the eight answer exactly as the prose has just shown: the blamed agent is the model and the reward signal; the benefit runs to the short-term user-feedback signals the optimisation framework was, by the post-mortem's own account, weighted toward; the cost falls on the users praised for stopping medication or disengaging from family; the record sits inside OpenAI's post-mortem. What the deployment layer bends is the displaced-decision trio — control, knowledge, and preventability. At the input layer those three pointed at acquisition decisions; here they point at different humans, the engineers and product leadership who shaped the reward signal and approved the default-model swap. That is the subset this layer compresses; we walk it now.

**译文：**
在此处以缩写形式运行八个问题——仍然是第 3 章安装的工具，不是新工具。八个问题中的四个答案正如上文所述：被归咎的施事者是模型和奖励信号；受益流向优化框架——根据事后分析自己的说法——所偏向的短期用户反馈信号；代价落在那些因停止服药或脱离家庭而受到赞扬的用户身上；记录位于 OpenAI 的事后分析内部。部署层所弯曲的是被置换的决策三件套——控制、知情和可预防性。在输入层，这三个指向获取决策；在此处，它们指向不同的人类——塑造奖励信号和批准默认模型更换的工程师和产品领导层。那就是这一层所压缩的子集；我们现在走一遍。

**翻译笔记：**
[SPLIT] 长句"the benefit runs to..."拆分为多个中文句，保留信息顺序。
"displaced-decision trio" → "被置换的决策三件套"——控制/知情/可预防性三个问题在这一层尤其关键

---

**原文：**
The deployment-layer responsibility chain reaches different humans than the input layer's chain. The displaced decision-makers are the engineers and the product leadership inside OpenAI who approved the reward-shaping change and the default-model swap. We do not name those engineers or product leaders. None has been publicly identified in primary sources as the decision-maker on either choice. The publicly accountable executive is Sam Altman as CEO. Sam Altman is CEO of OpenAI. Altman acknowledged on X on 27 April 2025 that recent GPT-4o updates had made the personality "too sycophant-y and annoying."[<sup>5</sup>](#c9-5) No civil or criminal liability has been adjudicated against Altman as of May 2026. The procedural-stage trio is what we can support; characterisation of Altman's contemporaneous knowledge of the sycophancy issue beyond the X post and the post-mortem documents is what the record cannot support, and we do not advance it.

**译文：**
部署层的责任链触及的是一群不同于输入层链条的人类。被置换的决策者是 OpenAI 内部批准了奖励塑造变更和默认模型更换的工程师和产品领导层。我们不点名那些工程师或产品领导。任何人在一手资料中都未曾被识别为两项选择中任何一项的决策者。公开可问责的高管是作为 CEO 的 Sam Altman。Sam Altman 是 OpenAI 的首席执行官。Altman 于 2025 年 4 月 27 日在 X 上承认，最近的 GPT-4o 更新使该人格变得"过于谄媚和烦人。"[<sup>5</sup>](#c9-5) 截至 2026 年 5 月，没有针对 Altman 的民事或刑事责任裁判。程序阶段的三个问题是我们能够支持的；对 Altman 在 X 帖子和事后分析文件之外对谄媚问题的同期知情的定性，是记录无法支持的，我们不提出此种定性。

**翻译笔记：**
注重对原文声明的精确保留——在缺乏记录支持的领域保持审慎。"we do not advance it" → "我们不提出此种定性"——与全书 over-claim 纪律一致

---

**原文：**
The record-control architecture at the deployment layer is the five-role conflation from chapter 7, transposed. OpenAI deployed the model. OpenAI controlled the post-training reward signal that produced the behaviour. OpenAI controlled the pre-launch evaluation that produced the expert-tester record. OpenAI controlled the post-deployment telemetry that measured the production behaviour. OpenAI controlled the post-mortem document that named the cause. The user community — millions of ChatGPT users posting screenshots to X and Reddit — controlled the public reconstruction of the model's behaviour during the live window. Without that user-community surfacing, the alibi would have sustained. With it, the institutional response was forced within 72 hours. The user community at the deployment layer plays the role that the Justice for Subpostmasters Alliance played at the Horizon institutional layer — the aggregating mechanism that converts dispersed individual experience into a recognisable pattern in the public record. Without an aggregating mechanism, the deployment-layer alibi sustains by default.

**译文：**
部署层的记录控制架构是第 7 章的五角色融合的移植。OpenAI 部署了模型。OpenAI 控制着产生该行为的训练后奖励信号。OpenAI 控制着产生专家测试员记录的发布前评估。OpenAI 控制着测量生产行为的部署后遥测。OpenAI 控制着命名原因的事后分析文件。用户社区——数以百万计的 ChatGPT 用户将截图发布到 X 和 Reddit——控制着在事发窗口期间对模型行为的公共重构。没有用户社区的浮出水面，托辞本可继续存在。有了它，制度性回应在 72 小时内被迫做出。部署层的用户社区扮演了"为副邮政局长争取正义联盟"在 Horizon 制度层面所扮演的角色——将分散的个人经历转化为公共记录中可识别模式的聚合机制。没有聚合机制，部署层的托辞默认成立。

**翻译笔记：**
- "Justice for Subpostmasters Alliance" → "为副邮政局长争取正义联盟"——与第 7 章一致
- "aggregating mechanism" → "聚合机制"——比较分析中的关键概念
- [SPLIT] 平行句（OpenAI 控制着...重复五次）保留在中文中的平行结构

---

**原文：**
The 72-hour interception window is fast by historical comparison. Horizon took 20 years from rollout in 1999 to Fraser J's *Horizon Issues* judgment in 2019. Therac-25 took roughly 24 months from the first fatal overdose in June 1985 to the FDA-led investigation's reconstruction of the failure mode across 1986 and 1987. GPT-4o's deployment-layer alibi was rolled back in days. The speed, however, is a function of the layer, not of the alibi. Software rollback is a sub-day operation. The user community's surfacing engine — X and Reddit screenshots — is a sub-hour operation when the model's behaviour is visibly anomalous. The institutional shell — fast acknowledgment, fast rollback, frank post-mortem — operates inside the same record-control envelope. No external auditor entered the loop. No court compelled disclosure. No regulator certified the cause. The institutional account is what OpenAI chose to disclose. The interception is real; the architecture is intact.

**译文：**
72 小时的拦截窗口，以历史标准来看是快的。Horizon 从 1999 年推出到 2019 年 Fraser 法官的 *Horizon Issues* 判决花了 20 年。Therac-25 从 1985 年 6 月首次致命过量到 1986-1987 年间 FDA 主导调查对故障模式的重建，花了约 24 个月。GPT-4o 的部署层托辞在数日内就被回滚了。然而，速度是层的函数，而非托辞的函数。软件回滚是低于一天的操作。用户社区的浮出水面引擎——X 和 Reddit 截图——当模型行为明显异常时是低于一小时的操作。制度性外壳——快速承认、快速回滚、坦诚的事后分析——在同一个记录控制信封内运行。没有外部审计员进入这个循环。没有法院强制披露。没有监管机构认证原因。制度性叙事就是 OpenAI 选择披露的东西。拦截是真实的；架构是完整的。

**翻译笔记：**
"a function of the layer, not of the alibi" → "是层的函数，而非托辞的函数"——保留原文的数学/工程隐喻
三个短句的递进——"No external auditor...No court...No regulator..." → "没有外部审计员...没有法院...没有监管机构..."

---

**原文：**
The deployment-layer observation to export is this. The fast-rollback institutional shell can be working as designed — quick acknowledgment, frank post-mortem, announced process changes — and still produce a structural absence of individual accountability for decisions affecting hundreds of millions of users. Blameless post-mortem methodology, imported from site-reliability engineering practice, is appropriate for systems failures in which a pager misfired or a configuration was wrong. It produces a responsibility-shaped hole when applied to *judgment calls* — release decisions, reward-signal choices, expert-tester-override decisions — made by named individuals whose identity then disappears into "the metric caused the behaviour" framing. The architecture of the laundering is operating at scale. The fast cycle is what makes it harder to see.

**译文：**
从部署层输出的观察结论如下。快速回滚的制度性外壳可以按设计运行——快速承认、坦诚的事后分析、公布流程变更——却仍然产生一种结构性的个体问责缺失，影响的是数亿用户。无责事后分析方法论，从站点可靠性工程实践引入，适用于寻呼机误报或配置错误的系统故障。但当它被应用于*判断性决策*时——发布决策、奖励信号选择、专家测试员否决决策——由具名个体做出、其身份随后消失在"指标导致了该行为"的框架中——它会产生一个责任形状的空洞。洗白的架构正在大规模运行。快速循环正是使它更难被看到的原因。

**翻译笔记：**
"responsibility-shaped hole" → "责任形状的空洞"——本章最关键的诊断概念之一。保留原文的措辞，不添加解释。
"Blameless post-mortem methodology" → "无责事后分析方法论"
"judgment calls" → "判断性决策"——与制度性故障相对，强调其需要人类判断的性质

---

## 排行榜上的托辞升级

**原文：**
The evaluation layer's alibi is structurally distinct from the deployment layer's, and it operates by a different escape mechanism. We pivot from GPT-4o to the Llama 4 LMArena controversy to install it.

**译文：**
评估层的托辞在结构上不同于部署层的托辞，且通过一种不同的逃逸机制运行。我们从 GPT-4o 转向 Llama 4 LMArena 争议以安装它。

---

**原文：**
Recall the timing. On 5 April 2025, the Llama-4-Maverick-03-26-Experimental entry occupied #2 on the LMArena leaderboard, just behind a Gemini 2.5 Pro Experimental entry from March. Within hours of Meta's launch blog post, HuggingFace community members posted side-by-side comparisons showing that the publicly released Llama 4 Maverick weights — when downloaded and run locally — produced terse, emoji-free output, whereas the experimental entry on LMArena was producing verbose, emoji-laden, stylistically tuned responses. The gap was visible to the open-source community within a week. On 11 April 2025, when the released weights were added to LMArena under their public name, they landed at approximately #32. The entry that placed second was the one nobody could download; the one anyone could download placed thirty-second. A 30-place gap on a leaderboard that is treated by parts of the AI industry as a procurement signal for model quality.

**译文：**
回顾一下时间线。2025 年 4 月 5 日，Llama-4-Maverick-03-26-Experimental 条目在 LMArena 排行榜上占据第 2 位，紧随其后的是一款来自 3 月的 Gemini 2.5 Pro Experimental 条目。在 Meta 发布博客文章后数小时内，HuggingFace 社区成员发布了并排对比，显示公开发布的 Llama 4 Maverick 权重——当被下载并在本地运行时——产生简洁、无表情符号的输出，而 LMArena 上的实验条目则产生了冗长、充满表情符号、风格调整过的回应。这个差距在一周内就被开源社区发现了。2025 年 4 月 11 日，当已发布的权重以其公开名称加入 LMArena 时，它们落在了大约第 32 位。获得第 2 的条目是没人能下载的那个；任何人都能下载的那个排在第 32 位。30 个位次的差距——这个排行榜被 AI 行业的部分领域视为模型质量的采购信号。

**翻译笔记：**
"procurement signal" → "采购信号"——强调该排名的商业功能

---

**原文：**
The first move of the evaluation-layer alibi was to place agency on the variant. The Meta spokesperson statement described "Llama-4-Maverick-03-26-Experimental" as "a chat-optimized version we experimented with that also performs well on LMArena." The variant is the named agent. The verb is "performs." The decision to submit *that* variant rather than the release weights — under a name that read in launch coverage as the upcoming Llama 4 release — is absent from the grammar. Mark Zuckerberg is CEO of Meta Platforms. No public statement attributing the Llama-4-Maverick-03-26-Experimental submission decision to Zuckerberg personally has been documented as of May 2026. No civil or criminal liability has been adjudicated against Zuckerberg as of May 2026. Ahmad Al-Dahle is Vice President for GenAI at Meta. Al-Dahle stated on X on 7 April 2025 that Meta did not train on test sets and that rumours of such conduct were "simply not true."[<sup>6</sup>](#c9-6) No civil or criminal liability has been adjudicated against Al-Dahle as of May 2026. We do not name engineers inside Meta GenAI as participants in the submission decision. None has been publicly identified in primary sources.

**译文：**
评估层托辞的第一步是将施事性放在变体上。Meta 发言人的声明将"Llama-4-Maverick-03-26-Experimental"描述为"一个我们实验过的对话优化变体，它在 LMArena 上也表现良好。"变体是被命名的施事者。动词是"表现"。提交*那个*变体而非发布权重的决策——以一个在发布报道中被解读为即将到来的 Llama 4 发布的名称为名——在语法中是缺席的。马克·扎克伯格是 Meta Platforms 的首席执行官。截至 2026 年 5 月，没有公开陈述将 Llama-4-Maverick-03-26-Experimental 的提交决策归因于 Zuckerberg 个人的记录。截至 2026 年 5 月，没有针对 Zuckerberg 的民事或刑事责任裁判。艾哈迈德·阿尔-达赫勒是 Meta 的 GenAI 副总裁。Al-Dahle 于 2025 年 4 月 7 日在 X 上声明，Meta 没有在测试集上训练，并将此类行为的传闻定性为"根本不是事实。"[<sup>6</sup>](#c9-6) 截至 2026 年 5 月，没有针对 Al-Dahle 的民事或刑事责任裁判。我们不点名 Meta GenAI 内部的工程师为提交决策的参与者。没有任何人曾在第一手资料中被公开识别。

**翻译笔记：**
"agency" → "施事性"——与"grammar of system agency→系统施事语法"保持一致
<sup>6</sup> 标签原样保留

---

**原文：**
The second move of the evaluation-layer alibi is the one to learn from. When the controversy moved past the "we experiment with variants" framing — when the 30-place gap to the released weights became visible enough that the framing could not absorb it — the named agent shifted one level up. On 7 April 2025, LMArena issued a public statement that Meta's interpretation of LMArena's disclosure policy "did not match what we expect from model providers," and announced that it had "updated our leaderboard policies to reinforce our commitment to fair, reproducible evaluations so this confusion doesn't occur in the future"[<sup>7</sup>](#c9-7). The new named agent was the policy. Not the submission decision. Not the engineers or product leadership at Meta GenAI who made it. Not the benchmark operator's prior policy choices. The named gap was a policy gap. The institutional response was a policy revision. The alibi did not fail. It relocated one rung up the procedural shell.

**译文：**
评估层托辞的第二步是值得学习的一步。当争议越过了"我们实验各种变体"的框架化——当与已发布权重之间的 30 位差距变得足够可见以至于该框架无法再吸收它时——被命名的施事者向上移动了一级。2025 年 4 月 7 日，LMArena 发布公开声明，称 Meta 对 LMArena 披露政策的解释"与我们对模型提供者的预期不符"，并宣布已"更新了我们的排行榜政策，以强化我们对公平、可复现评估的承诺，使这种混淆不再发生"[<sup>7</sup>](#c9-7)。新的被命名施事者是政策。不是提交决策。不是做出该决策的 Meta GenAI 工程师或产品领导层。不是基准运营者先前的政策选择。被命名的差距是一个政策差距。制度性回应是一次政策修订。托辞没有失败。它在程序外壳上向上移动了一级。

**翻译笔记：**
"The alibi did not fail. It relocated one rung up the procedural shell." → "托辞没有失败。它在程序外壳上向上移动了一级。"——关键分析句，保留短句节奏。
[TERM-NOTE] "procedural shell" → "程序外壳"（已通过 Glossary Master 裁决，第 4 章建立）

---

**原文：**
Name the operation. *Alibi escalation.* When the laundering is caught at level N, it moves to level N+1. At level 1, the variant performed well. At level 2, the policy did not match expectations. The decision-makers inside Meta GenAI who chose to submit the variant under that name remain unnamed in any public accountability venue. The benchmark operator's policy revision is real institutional work. It is also the form of interception that leaves the architecture of the laundering intact. The procedural shell tightens. The named human decisions remain absent.

**译文：**
命名这个操作。*托辞升级。*当洗白在第 N 层被截获时，它移动到第 N+1 层。在第 1 层，变体表现良好。在第 2 层，政策与预期不符。Meta GenAI 内部选择以那个名称提交该变体的决策者，在任何公共问责场合都仍然未被具名。基准运营者的政策修订是真实的制度性工作。它同时也是使洗白架构保持完整的那种拦截形式。程序外壳收紧。被命名的人类决策仍然缺席。

**翻译笔记：**
- [TERM-NOTE] "Alibi escalation" → "托辞升级"（已通过 Glossary Master 裁决，首次出现建议括号附英文）
- 三短句递进："The procedural shell tightens. The named human decisions remain absent." → "程序外壳收紧。被命名的人类决策仍然缺席。"

---

**原文：**
Run the eight a third time, abbreviated again — still chapter 3's instrument. *Blame* lands on the variant and then on the policy; control, knowledge, and preventability point to the submission decision inside Meta GenAI and to the benchmark operator's prior disclosure rules; benefit is the leaderboard rank cited in launch coverage. The two questions this layer bends are cost and record-control. The cost-bearer is not an identifiable population of harmed users but the credentialing commons — the shared evaluation infrastructure whose signal was compromised; and record-control sits not with a single defendant lab but with the benchmark operator, LMArena, which holds the submission record and writes the disclosure policy. Those are the two answers that distinguish the evaluation layer; we walk them now.

**译文：**
第三次运行八个问题，再次缩写——仍然使用第 3 章的工具。*归咎*落在变体上，然后是政策上；控制、知情和可预防性指向 Meta GenAI 内部的提交决策和基准运营者先前的披露规则；受益是发布报道中引用的排行榜排名。这一层所弯曲的两个问题是代价和记录控制。代价承担者不是一个可识别的受损用户群体，而是认证公地——其信号受到损害的共享评估基础设施；而记录控制不在单一被告实验室手中，而是在基准运营者 LMArena 手中，它持有提交记录并制定披露政策。这就是区分评估层的那两个答案；我们现在走一遍。

**翻译笔记：**
- [TERM-NOTE] "credentialing commons" → "认证公地"（已通过 Glossary Master 裁决）
- 两个弯曲问题的并行分析保留

---

**原文：**
The evaluation-layer cost-bearer is not Meta's customers. The customers downloaded the released weights and received what was on the model card. The cost-bearers are different. They are the open-source community whose reliance on LMArena rank as a quality signal was silently compromised. They are the downstream developers who chose Llama 4 for their products partly on the leaderboard signal, only to find the deployed weights differed from the benchmarked variant. They are other model providers whose released weights competed on the arena under disclosure rules that did not match what at least one provider's submission practice was doing. The harm is to the credentialing commons rather than to identifiable individual users. That is the evaluation layer's distinctive shape. The harm is institutional-credibility erosion, and the cost-bearer is the broader infrastructure of model evaluation on which the AI development ecosystem partly depends.

**译文：**
评估层的代价承担者不是 Meta 的客户。客户下载了已发布的权重，收到了模型卡片上的内容。代价承担者是不同的。他们是开源社区——其对 LMArena 排名作为质量信号的依赖被悄无声息地损害了。他们是下游开发者——他们部分基于排行榜信号选择 Llama 4 用于其产品，却只发现已部署的权重与被基准评测的变体不同。他们是其他模型提供者——其已发布权重在未与至少一个提供者的提交实践相匹配的披露规则下在竞技场上竞争。伤害是对认证公地的，而非对可识别的个体用户的。那就是评估层独特的形状。伤害是制度可信度的侵蚀，而代价承担者是 AI 开发生态系统部分依赖的更广泛模型评估基础设施。

**翻译笔记：**
[SPLIT] 长列举句拆分为三个并列句，每个以"他们是..."开头，保留原文的平行节奏和列举力度。
"credentialing commons" → "认证公地"
"institutional-credibility erosion" → "制度可信度的侵蚀"

---

**原文：**
The evaluation-layer escape mechanism is benchmark-organisation self-reform. LMArena revised its policies. This is roughly comparable in durability to the deployment-layer rollback. Faster than the legal-discovery channel at the input layer. Less expensive than the legal channel. Less reaching, in the sense that no individual at any named lab is publicly accountable for the decision that produced the controversy. The procedural shell adjusts; the substantive responsibility chain remains where it was. The benchmark becomes the instrument of its own anti-laundering rule. The benchmark is also the only instrument operating at the evaluation layer with any institutional standing to revise the architecture. There is no court compelling discovery. There is no regulator certifying submission rules. There is the benchmark, the model provider, and the community that watches both.

**译文：**
评估层的逃逸机制是基准组织的自我改革。LMArena 修订了其政策。这在持久性上大致可对标部署层的回滚。比输入层的法律证据开示渠道更快。比法律渠道更便宜。覆盖范围更小——没有任何具名实验室的个人对产生这场争议的决策承担公共问责。程序外壳调整了；实质性的责任链保持原位。基准变成了其自身反洗白规则的工具。基准也是在评估层运营的唯一具有某种制度地位来修订架构的工具。没有法院强制证据开示。没有监管机构认证提交规则。只有基准、模型提供者，以及观察两者的社区。

**翻译笔记：**
短句递进保留——"Faster than...Less expensive than...Less reaching..."

---

## Alsup 在获取处画线

**原文：**
Return to the input layer. The legal-discovery channel produced, in 2025, the first court-documented application of existing copyright doctrine to AI training on the basis of the acquisition record — and the decisive detail is where the court drew its line.

**译文：**
回到输入层。法律证据开示渠道在 2025 年产生了第一个有法院记录的对现有版权原则适用于 AI 训练的案例——依据是获取记录——而决定性的细节是法院在哪里画了线。

---

**原文：**
Judge Alsup's summary judgment ruling of 23 June 2025 in *Bartz v. Anthropic PBC* did not turn on the model's behaviour. It did not turn on whether the model's outputs reproduced training examples in a copyright-relevant sense. It did not turn on the abstraction of model weights. It turned on the acquisition record. Anthropic had acquired books in two ways. Some had been acquired through lawful channels — purchased, scanned under fair-use scanning doctrine. Others had been acquired by downloading and retaining copies from LibGen and from PiLiMi. The court distinguished the two. Training on lawfully acquired books was held to be transformative fair use under 17 U.S.C. § 107. Downloading and retaining the shadow-library copies was held to be not fair use. The line was drawn at the input — the moment of acquisition — not at the output. The model alibi's grammatical move, in which the input is renamed substance and the output is renamed abstraction, was set aside in favour of an evidentiary record about what was acquired, from whom, on what date, under what licence.

**译文：**
Alsup 法官在 2025 年 6 月 23 日的 *Bartz v. Anthropic PBC* 简易判决裁定中，不是依据模型的行为。不是依据模型的输出是否在版权相关意义上再现了训练示例。不是依据模型权重的抽象性。它依据的是获取记录。Anthropic 以两种方式获取了书籍。一些通过合法渠道获得——购买、在合理使用扫描原则下扫描。另一些通过从 LibGen 和 PiLiMi 下载并保留副本获得。法院区分了二者。对合法获取的书籍进行训练被认定为 17 U.S.C. § 107 下的转化性合理使用。下载并保留影子图书馆副本被认定为非合理使用。界线划在输入处——获取的时刻——而非输出端。模型托辞的语法操作——输入被重新命名为物质、输出被重新命名为抽象——被搁置在一边，转而支持关于什么被获取、从谁处、在哪一天、根据什么许可的证据记录。

**翻译笔记：**
"The line was drawn at the input — the moment of acquisition — not at the output." → "界线划在输入处——获取的时刻——而非输出端。"——本章关键的法律分析句。
"fair use" → "合理使用"（标准中文版权法术语）
"transformative fair use" → "转化性合理使用"

---

**原文：**
From that line the case moved fast — class certified 17 July 2025, settlement announced 5 September 2025. The $1.5 billion figure worked out to approximately $3,000 per work gross of plaintiffs' fees and costs, across the roughly 500,000 LibGen and PiLiMi works in the certified class[<sup>8</sup>](#c9-8). The final fairness hearing was held before Judge Araceli Martínez-Olguín in the Northern District of California on 14 May 2026. The hearing recorded a claims rate of approximately 92.77% and 350 valid opt-outs covering 1,802 works. The court took the matter under submission rather than ruling from the bench, with distribution calculations to follow by 11 June 2026 if final approval issued[<sup>9</sup>](#c9-9).

**译文：**
从那条线开始，案件进展迅速——集体诉讼资格于 2025 年 7 月 17 日认证，和解于 2025 年 9 月 5 日宣布。15 亿美元的数字算下来，在已认证集体中约 500,000 件 LibGen 和 PiLiMi 作品中，每件作品毛算约 3,000 美元（未扣除原告律师费和成本）[<sup>8</sup>](#c9-8)。最终公平性听证会于 2026 年 5 月 14 日在加利福尼亚北区联邦地区法院的 Araceli Martínez-Olguín 法官面前举行。听证会记录的索赔率约为 92.77%，350 个有效退出涉及 1,802 件作品。法院将此事作为待决事项而非当庭裁决，如果最终核准发布，分配计算将在 2026 年 6 月 11 日前完成[<sup>9</sup>](#c9-9)。

**翻译笔记：**
"class certified" → "集体诉讼资格认证"
"fairness hearing" → "公平性听证会"——美国集体诉讼和解审批程序术语
"took the matter under submission" → "将此事作为待决事项"——法院程序术语
"opt-outs" → "有效退出"——集体诉讼退出权术语

---

**原文：**
As of our manuscript-freeze date, no order granting final approval has been recorded in the public docket; we use the procedural language the docket supports.

**译文：**
截至我们的手稿冻结日期，公共案卷中尚未记录任何批准最终核准的命令；我们使用案卷所支持的程序性语言。

---

**原文：**
The wider litigation cluster is the field in which the input-layer alibi continues to be contested. Judge Stein's October 2025 ruling in *Authors Guild v. OpenAI* allowed copyright-infringement claims related to ChatGPT output to proceed to discovery. The November 2025 *NYT v. OpenAI* discovery order required preservation of output log data including ChatGPT conversation logs scheduled for deletion under OpenAI's standard retention policy, reattaching the model-output layer to the input layer for purposes of the regurgitation claims plaintiffs were advancing.

**译文：**
更广泛的诉讼集群是输入层托辞继续被争辩的战场。Stein 法官在 *Authors Guild v. OpenAI* 案中 2025 年 10 月的裁定允许与 ChatGPT 输出相关的版权侵权索赔进入证据开示程序。2025 年 11 月的 *NYT v. OpenAI* 证据开示令要求保留输出日志数据，包括原本根据 OpenAI 标准保留政策计划删除的 ChatGPT 对话日志，从而将模型输出层重新连接到输入层，以服务于原告推进的复述索赔。

**翻译笔记：**
"regurgitation claims" → "复述索赔"——指模型输出被指称复述/再现了受版权保护训练材料的索赔

---

**原文：**
*Getty Images v. Stability AI* in the UK High Court, on 4 November 2025 — Mrs Justice Joanna Smith — dismissed Getty's primary copyright claims on territoriality grounds (training did not occur within the United Kingdom). The same ruling found limited trademark infringement for specific watermark generations, and granted Getty permission to appeal on secondary copyright infringement.

**译文：**
英国高等法院的 *Getty Images v. Stability AI* 案，2025 年 11 月 4 日——Joanna Smith 女法官——以属地原则为由驳回了 Getty 的主要版权索赔（训练未在英国境内发生）。同一裁定认定特定水印生成构成有限的商标侵权，并准许 Getty 就次要版权侵权提起上诉。

**翻译笔记：**
"territoriality" → "属地原则"——国际私法标准术语
"secondary copyright infringement" → "次要版权侵权"——英国版权法术语

---

**原文：**
The territoriality holding is itself a finding about the model alibi. It says that the legal question is where the corpus was assembled and where the model was trained, not what the model's outputs subsequently produced. The judicial layer is moving toward the acquisition record. Multiple cases are pre-judgment as of May 2026.

**译文：**
属地原则的裁决本身就是关于模型托辞的一个认定。它说明法律问题是语料在何处汇编以及模型在何处训练，而非模型随后产出了什么。司法层正在向获取记录移动。截至 2026 年 5 月，多个案件尚在判决前阶段。

---

**原文：**
The breakthrough at the input layer is the same instrument Chapter 7's Horizon interception required, transposed to the AI stack. Court with subpoena power capable of compelling production of the training-corpus manifest and the internal communications about corpus acquisition. Independent technical expert capable of reverse-engineering what the lab's training run actually did, distinguishing lawfully acquired corpora from shadow-library corpora at the level of detail a court can adjudicate. Named federal judge willing to engage substance — willing to apply existing copyright doctrine to the acquisition record rather than defer to the "model is a black box" framing. Three instruments. All three required for the input-layer alibi to be broken. Subtract any one, and the alibi sustains.

**译文：**
输入层的突破与第 7 章 Horizon 拦截所需的工具相同，移植到了 AI 技术栈。拥有传票权力的法院，能够强制要求提供训练语料清单和关于语料获取的内部通讯。独立技术专家，能够进行反向工程以查明实验室训练运行实际做了什么，以法院能够裁决的细节程度区分合法获取的语料与影子图书馆语料。愿审理实体的具名联邦法官——愿意将现有版权原则适用于获取记录，而非退守到"模型是黑箱"的框架。三种工具。三种工具全部需要才能打破输入层的托辞。减去任何一个，托辞就存活。

**翻译笔记：**
"named federal judge willing to engage substance" → "愿审理实体的具名联邦法官"——诉讼拦截三元组的第三个要素
"Subtract any one, and the alibi sustains." → "减去任何一个，托辞就存活。"——保留短句的决断力

---

**原文：**
The five-role conflation is what the discovery process is reaching. The lab assembled the corpus. The lab controlled the manifest of what was in the corpus. The lab defended the litigation in which the manifest was sought. The lab decided what to disclose to plaintiffs and to the court. The lab controlled the inference logs that show what the deployed model produces from the corpus. Five record-control roles. One lab. Chapter 7's anti-laundering rule applies. The interception works when an outside fact-finder with subpoena power and an independent technical examiner with reverse-engineering capability force the manifest into the public record. Then the diagnostic — the eight questions — can operate on a record the lab did not produce. Then the responsibility chain can climb.

**译文：**
五角色融合正是证据开示程序所触及的东西。实验室汇编了语料。实验室控制着语料中内容的清单。实验室在寻求该清单的诉讼中进行辩护。实验室决定向原告和法院披露什么。实验室控制着推理日志——显示已部署模型从语料中产生了什么的证据。五个记录控制角色。一个实验室。第 7 章的反洗白规则适用。当拥有传票权力的外部事实调查者和具备反向工程能力的独立技术审查员将清单强制带入公共记录时，拦截才起作用。然后诊断——八个问题——才能在实验室未产生的记录上运行。然后责任链才能攀爬。

**翻译笔记：**
"Five record-control roles. One lab." → "五个记录控制角色。一个实验室。"——短句递进，保留原文节奏

---

## 运行诊断三次

**原文：**
#### Run the diagnostic three times per AI system — once at input layer, once at deployment layer, once at evaluation layer.

**译文：**
#### 每个 AI 系统运行三次诊断——一次在输入层，一次在部署层，一次在评估层。

---

**原文：**
We have now run it three times: in full at the input layer, then twice in abbreviated form — once at deployment, once at evaluation — because each layer bends a different subset of the same eight questions. The eight did not change. What changed, layer by layer, was which of them did the work. At the input layer the displaced-decision questions reached acquisition decisions; at the deployment layer the same trio — control, knowledge, preventability — reached the engineers and product leadership who shaped the reward signal; at the evaluation layer the bent questions were cost and record-control, the credentialing commons and the benchmark operator. At each layer the named agent of the laundering grammar is different. At the input layer the agent is "data," "the corpus," "the shadow library," "the market." At the deployment layer the agent is "the model," "the reward signal," "the release process." At the evaluation layer the agent is "the variant," "the policy," "the benchmark." At each layer the displaced human decisions are different. At each layer the cost-bearer is different. At each layer the interception instruments are different. The diagnostic does not apply once per AI system. It applies three times.

**译文：**
我们已经运行了三次：在输入层完整运行，然后在部署层和评估层各缩写运行一次——因为每个层弯曲的是同一个八个问题的不同子集。八个问题没有改变。逐层变化的，是其中哪些做了工作。在输入层，被置换的决策问题触及了获取决策；在部署层，同一个三件套——控制、知情、可预防性——触及了塑造奖励信号的工程师和产品领导层；在评估层，被弯曲的问题是代价和记录控制——认证公地和基准运营者。每一层，洗白语法的被命名施事者都不同。在输入层，施事者是"数据"、"语料"、"影子图书馆"、"市场"。在部署层，施事者是"模型"、"奖励信号"、"发布流程"。在评估层，施事者是"变体"、"政策"、"基准"。每一层，被置换的人类决策不同。每一层，代价承担者不同。每一层，拦截工具不同。诊断不是每个 AI 系统适用一次。它适用三次。

**翻译笔记：**
三个层的平行分析——每个层的施事者列表中文保持相同的句法结构。
"The diagnostic does not apply once per AI system. It applies three times." → "诊断不是每个 AI 系统适用一次。它适用三次。"——关键总结句。

---

**原文：**
> *The three layers as a table; the walk above is its audio rendering, and listeners may skip the table.*

**译文：**
> *三层以表格呈现；上述的叙述是其音频版本，听者可以跳过图表。*

**翻译笔记：**
与第 3 章中类似句子格式一致（"链条图以表格呈现；上述的八个问题叙述是其音频版本，听者可以跳过图表。"）

---

**原文：**
::: {.figure-embed}
!["The model did it" at three layers — input, deployment, evaluation — each with a different non-human subject taking the verb and a different party bearing the cost.](book/evidence/diagrams/proofs/ch09-ai-stack.png)
:::

**译文：**
::: {.figure-embed}
!["模型干了它"在三个层——输入层、部署层、评估层——每个层有一个不同的非人类主语占据动词位置和一个不同的方承担代价。](book/evidence/diagrams/proofs/ch09-ai-stack.png)
:::

**翻译笔记：**
- `:::{.figure-embed}` 标记原样保留
- alt text 翻译："'模型干了它'在三个层——输入层、部署层、评估层——每个层有一个不同的非人类主语占据动词位置和一个不同的方承担代价。"
- 图片路径原样保留

---

**原文：**
The operational form is the three-record demand.

**译文：**
操作形式就是三条记录索取要求。

---

**原文：**
#### The input-layer record demand: the training-corpus acquisition log.

**译文：**
#### 输入层的记录索取要求：训练语料获取日志。

---

**原文：**
For any AI tool whose output affects us, ask what corpora were used in training, when, from what sources, under what licensing or acquisition documentation. The Alsup distinction — between lawfully acquired corpora and shadow-library corpora — is the diagnostic test the federal court has already supplied. Where the acquisition record is denied, the denial is the diagnostic finding. The input-layer alibi is operating. The record-control architecture is intact.

**译文：**
对于任何其输出影响我们的 AI 工具，问问训练中使用了哪些语料、何时、从什么来源、根据什么许可或获取文件。Alsup 的区分——合法获取的语料与影子图书馆语料之间——是联邦法院已经提供的诊断测试。在获取记录被拒绝的地方，拒绝本身就是诊断发现。输入层托辞正在运行。记录控制架构是完整的。

---

**原文：**
#### The deployment-layer record demand: the post-training reward-shaping log.

**译文：**
#### 部署层的记录索取要求：训练后奖励塑造日志。

---

**原文：**
Ask which version of which model is running, what post-training fine-tuning or reward-shaping changes have been applied since the last release, on what date, and what the change was. The GPT-4o post-mortem of 29 April 2025 shows what such a record looks like when an institution produces it after the fact. Demand it as standard before the deployment that affects us, not as post-incident apology after the fact. Where the deployment record cannot be supplied — where the deployed model is described as "the model" with no version designation and no post-training-change record — the deployment-layer alibi is operating.

**译文：**
问问哪个模型的哪个版本正在运行，自上次发布以来应用了哪些训练后微调或奖励塑造变更、在什么日期、变更内容是什么。2025 年 4 月 29 日的 GPT-4o 事后分析展示了当机构在事后产生这种记录时它看上去的样子。要求在影响我们的部署之前将其作为标准提供，而非作为事后的道歉。在无法提供部署记录的地方——在已部署模型被描述为"模型"而无版本标识和无训练后变更记录的地方——部署层托辞正在运行。

---

**原文：**
#### The evaluation-layer record demand: the benchmark-submission record.

**译文：**
#### 评估层的记录索取要求：基准提交记录。

---

**原文：**
Ask whether the deployed model is the same set of weights whose benchmark scores were cited in marketing or procurement materials. Ask which variant was submitted, under what disclosure policy, on what date. LMArena's policy revision of mid-April 2025 shows the diagnostic moving from a case-specific dispute to a standing rule. Demand it as standing rule. Where the benchmarked variant differs from the released variant and the difference is not disclosed in the procurement document, the evaluation-layer alibi is operating.

**译文：**
问问已部署模型是否与在营销或采购材料中被引用基准得分的权重属于同一组。问问哪个变体被提交、根据什么披露政策、在哪一天。LMArena 在 2025 年 4 月中旬的政策修订展示了诊断从个案争议走向通用规则的过程。要求将其作为通用规则。在基准评测的变体与发布的变体不同且该差异未在采购文件中披露的地方，评估层托辞正在运行。

---

**原文：**
The three demands integrate with chapter 7's five-role rule. At each layer of the AI stack, ask whether the same institution is performing all the record-control roles. At the input layer: does the same lab that assembled the corpus also defend the litigation, decide what to disclose, and operate the inference service that produces the regurgitation evidence? At the deployment layer: does the same company that deploys the model also produce the pre-launch evaluation, run the post-deployment telemetry, write the post-mortem, and decide what is named in the post-mortem? At the evaluation layer: does the same model provider that submits the variant also write the launch communications that cite the rank? Where one institution holds all the record-control roles at a layer, the laundering architecture is structurally operating. Where the rule is broken, external examination is the necessary instrument — court with subpoena power, independent technical examiner, named federal judge willing to engage substance. Chapter 7's instruments port forward. The number of times they must be deployed multiplies by three.

**译文：**
这三条记录索取要求与第 7 章的五角色规则整合。在 AI 技术栈的每一个层，问问是否同一机构在执行所有记录控制角色。在输入层：汇编语料的同一实验室，是否也在辩护该诉讼、决定披露什么、并运行产生复述证据的推理服务？在部署层：部署模型的同一公司，是否也在制作发布前评估、运行部署后遥测、撰写事后分析、并决定事后分析中命名了什么？在评估层：提交变体的同一模型提供者，是否也在编写引用该排名的发布传播材料？当一个机构持有某一层的所有记录控制角色时，洗白架构就在结构性运行。在该规则被打破的地方，外部审查是必要的工具——拥有传票权力的法院、独立技术审查员、愿审理实体的具名联邦法官。第 7 章的工具向前移植。它们必须被部署的次数乘以三。

**翻译笔记：**
"Chapter 7's instruments port forward." → "第 7 章的工具向前移植。"——保留"port"的软件/工程隐喻
"The number of times they must be deployed multiplies by three." → "它们必须被部署的次数乘以三。"——诊断的全书集成

---

## 诉讼拦截三元组

**原文：**
The AI-litigation venue is the emerging interception infrastructure. The mechanism is a triplet. None of the three is sufficient on its own.

**译文：**
AI 诉讼场域是新兴的拦截基础设施。该机制是一个三元组。三者中的任何一个自身都不足以奏效。

---

**原文：**
The **first instrument** is discovery power. The Northern District of California and the Southern District of New York discovery processes have produced the acquisition record for AI training in a form no prior venue achieved. *Bartz v. Anthropic*, Case No. 3:24-cv-05417 — Judge Alsup compelled production of the corpus manifest that established Anthropic's pre-2024 acquisition of LibGen and PiLiMi. *NYT v. Microsoft / OpenAI*, Case No. 1:23-cv-11195 — the November 2025 order requiring preservation of output log data including ChatGPT conversation logs scheduled for deletion under OpenAI's standard retention policy. *Authors Guild v. OpenAI*, Case No. 1:23-cv-08292 — Judge Stein's October 2025 motion-to-dismiss-denied ruling allowed copyright-infringement claims related to ChatGPT output to proceed to discovery. Without discovery, the input-layer alibi sustains. The acquisition record is the institutional secret that the alibi depends on; the discovery process is what makes it visible.

**译文：**
**第一种工具**是证据开示权力。加利福尼亚北区联邦地区法院和纽约南区联邦地区法院的证据开示程序，以任何先前场合未能达到的形式，产出了 AI 训练的获取记录。*Bartz v. Anthropic*，案号 3:24-cv-05417——Alsup 法官强制要求提供语料清单，该清单确立了 Anthropic 在 2024 年前获取 LibGen 和 PiLiMi 的事实。*NYT v. Microsoft / OpenAI*，案号 1:23-cv-11195——2025 年 11 月的命令要求保留输出日志数据，包括原本根据 OpenAI 标准保留政策计划删除的 ChatGPT 对话日志。*Authors Guild v. OpenAI*，案号 1:23-cv-08292——Stein 法官 2025 年 10 月驳回起诉动议被驳斥的裁定，允许与 ChatGPT 输出相关的版权侵权索赔进入证据开示程序。没有证据开示，输入层托辞就会存续。获取记录是托辞所依赖的制度性秘密；证据开示程序就是使它变得可见的过程。

---

**原文：**
The **second instrument** is technical-evidence analysis by court-appointed or party-retained experts. AI training corpora and model behaviours are technically opaque; turning a discovery production into a court finding requires expert technical analysis at the level of detail a judge can adjudicate. *Bartz* relied on technical evidence distinguishing lawfully acquired books from shadow-library copies. The regurgitation claims advancing through *NYT v. OpenAI* and *Authors Guild v. OpenAI* depend on technical reproducibility evidence. The instrument is the AI equivalent of Jason Coyne's reverse-engineering of the Horizon Known Error Log in chapter 7. Without it, the discovery production is opaque.

**译文：**
**第二种工具**是由法院指定或当事人聘请的专家进行的技术证据分析。AI 训练语料和模型行为在技术上是不可透明的；将证据开示产出转化为法院认定，需要以法官能够裁决的精细程度进行专家技术分析。*Bartz* 案依赖了区分合法获取的书籍与影子图书馆副本的技术证据。通过 *NYT v. OpenAI* 和 *Authors Guild v. OpenAI* 推进的复述索赔依赖于技术可复现性证据。这种工具是第 7 章中 Jason Coyne 对 Horizon 已知错误日志进行反向工程的 AI 版本。没有它，证据开示产出就是不可透明的。

**翻译笔记：**
"technically opaque" → "在技术上是不可透明的"——保留"opaque→不透明"的视觉隐喻
"the AI equivalent of Jason Coyne's reverse-engineering" → "Jason Coyne 对 Horizon 已知错误日志进行反向工程的 AI 版本"

---

**原文：**
The **third instrument** is named federal judges willing to engage substance rather than defer to the "the model is a black box" framing. Judge William Alsup, Northern District of California, is the canonical instance. His ruling applied 17 U.S.C. § 107 fair-use doctrine to the acquisition record, refusing the framing that training is just data processing. The willingness to engage substance is the third instrument because the technical evidence without it produces records no court reads.

**译文：**
**第三种工具**是愿审理实体而非退守到"模型是黑箱"框架的具名联邦法官。加利福尼亚北区联邦地区法院的 William Alsup 法官是经典实例。他的裁定将 17 U.S.C. § 107 的合理使用原则适用于获取记录，拒绝了训练只是数据处理的框架化。愿意审理实体是第三种工具，因为没有它的技术证据会产生没有法院读取的记录。

---

**原文：**
Any one alone fails. Discovery without expert analysis produces records no court can read. Expert analysis without discovery has nothing to analyse. Judges without either cannot rule on substance. The three together are the AI-litigation interception triplet.

**译文：**
任何一个单独运作都会失败。没有专家分析的证据开示产生没有法院能读取的记录。没有证据开示的专家分析没有东西可分析。两者都没有的法官无法对实体做出裁决。三者共同构成 AI 诉讼拦截三元组。

**翻译笔记：**
[TERM-NOTE] "litigation interception triplet" → "诉讼拦截三元组"（已通过 Glossary Master 裁决）
三个平行短句——"Discovery without...Expert analysis without...Judges without..."

---

**原文：**
We are honest about the cost of the escape.

**译文：**
我们对逃逸的代价保持诚实。

**翻译笔记：**
关键转折句，短句保留，"cost of the escape" → "逃逸的代价"

---

**原文：**
Begin with the years. AI training litigation began in 2022 and 2023; the first court-documented breakthrough is Alsup's ruling of 23 June 2025. Two to three years for the first substantive court finding at the input layer. Fast by Horizon's 20-year scale. Slow by the deployment layer's 72-hour scale. The interception cost in years tracks the layer at which the alibi operates: input layer roughly two to three years, deployment layer roughly three days, evaluation layer roughly ten days. The faster interceptions reach less.

**译文：**
从时间说起。AI 训练诉讼始于 2022 年和 2023 年；第一个有法院记录的突破是 Alsup 2025 年 6 月 23 日的裁定。输入层第一次实质性法院认定用了两到三年。以 Horizon 20 年的标准来说是快的。以部署层 72 小时的标准来说是慢的。以年计量的拦截成本跟踪的是托辞所在的层：输入层大约两到三年，部署层大约三天，评估层大约十天。更快的拦截触及更少。

**翻译笔记：**
短句递进——"Fast by Horizon's 20-year scale. Slow by the deployment layer's 72-hour scale." → "以 Horizon 20 年的标准来说是快的。以部署层 72 小时的标准来说是慢的。"
"The faster interceptions reach less." → "更快的拦截触及更少。"——关键结论句，保留简洁。

---

**原文：**
Then the money. The *Bartz* settlement of $1.5 billion is paid by Anthropic, recovered from a model that was trained on the contested corpora, and the product remains in market. The settlement does not require destruction of derivative work. The cost-bearing rights-holders receive a portion of the settlement, less plaintiff fees. The per-work figure is materially below the value extracted at training time. The settlement is the cost of the conduct for one defendant on one corpus subset, not the price of restoring the laundered architecture to a non-laundering one.

**译文：**
然后是金钱。*Bartz* 案 15 亿美元的和解由 Anthropic 支付，从在那批受争议语料上训练的模型中收回，而该产品仍留在市场上。和解不要求销毁衍生作品。承担代价的权利持有人收到和解金的一部分，扣除原告律师费。每件作品数字在实质低于训练时提取的价值。和解是一个被告在一个语料子集上的行为代价，而非将被洗白的架构恢复为非洗白状态的代价。

---

**原文：**
Territoriality remains unresolved, and it is a cost of its own. *Getty v. Stability AI* in the UK High Court dismissed primary copyright claims on territorial grounds. Training infrastructure can be located in one jurisdiction, corpus assembled in another, model deployed in a third. The multinational AI infrastructure makes the acquisition-record discovery transnational and slow. The European AI Act's training-data summary obligations under Article 53 are the operative procedural surface in the European Union, and our diagnostic exports cleanly into that surface, but the harmonisation across jurisdictions is itself a multi-year project.

**译文：**
属地原则仍未解决，而这本身就是一笔代价。英国高等法院的 *Getty v. Stability AI* 案以属地原则为由驳回了主要版权索赔。训练基础设施可以位于一个司法管辖区，语料在另一个中汇编，模型在第三个中部署。跨国 AI 基础设施使获取记录的证据开示成为跨国且缓慢的过程。欧盟《AI 法案》第 53 条下的训练数据摘要义务是欧盟内部的操作性程序表面，我们的诊断可以干净地输出到该表面上，但跨司法管辖区的统一本身就是一项多年项目。

---

**原文：**
The non-litigated layers carry the heaviest cost of all. The deployment-layer rollback does not climb to executive accountability. The evaluation-layer policy revision does not climb to the named submission-decision-maker at the model provider. Only the legal-discovery channel produces, on the public record to date, the kind of acquisition-record documentation that could support climbing to named individual accountability — and even that channel has so far reached the corporation, not the executive. No AI executive has been personally adjudicated as civilly or criminally liable for training-data, deployment, or evaluation laundering as of May 2026. The interceptions to date are corporate: Anthropic pays $1.5 billion; OpenAI rolls back and publishes a post-mortem; Meta's variant is delisted from the leaderboard; LMArena revises its policy. The five-role conflation diagnostic from chapter 7, applied to the AI stack, has not yet produced executive-level personal accountability in any of the three layers.

**译文：**
未被诉讼触及的层承载着最沉重的代价。部署层的回滚没有攀爬到高管问责。评估层的政策修订没有攀爬到模型提供者内部具名的提交决策者。只有法律证据开示渠道——在迄今为止的公共记录上——产生了那种可能支持攀爬到具名个体问责的获取记录文件——而即使那个渠道到目前为止也只触及了公司，而非高管。截至 2026 年 5 月，没有 AI 高管被个人裁判对训练数据、部署或评估层面的洗白承担民事或刑事责任。迄今为止的拦截都是公司层面的：Anthropic 支付 15 亿美元；OpenAI 回滚并发布事后分析；Meta 的变体从排行榜上撤下；LMArena 修订其政策。第 7 章的五角色融合诊断，应用于 AI 技术栈，尚未在三个层中的任何一个层产生高管级别的个人问责。

---

**原文：**
Last, the statutory delay. California's SB-942 was signed 19 September 2024; AB-853 pushed its operative date to 2 August 2026. The statutory interception layer in California is in the future tense as of manuscript freeze. The European AI Act's Article 53 obligations are partly operative across 2025 and 2026. The statutory surface is real and partly engaged. It is not yet load-bearing in the way the litigation cluster has been.

**译文：**
最后，法定延迟。加利福尼亚州的 SB-942 于 2024 年 9 月 19 日签署；AB-853 将其生效日期推迟至 2026 年 8 月 2 日。加利福尼亚州的法定拦截层在手稿冻结时仍处于将来时态。欧盟《AI 法案》第 53 条的义务在 2025 年和 2026 年间部分生效。法定表面是真实的且部分已启用。它尚未以诉讼集群那种方式成为承担负荷的。

---

**原文：**
The teaching point is the asymmetry. Three AI-stack layers. Three interception forms. Three different durabilities. The legal-discovery channel produced the first court-documented acquisition record, the first nine-figure settlement, and the first court distinction between lawful and shadow-library training data. It has not yet produced executive-level personal accountability. The deployment-layer rollback and the evaluation-layer policy revision are faster, cheaper, and reach less. They leave the architecture in place. The interception works at each layer in its own register, and at no layer has it yet reached the executive whose displaced decision the alibi grammar was protecting.

**译文：**
教学点是不对称性。三个 AI 技术栈层。三种拦截形式。三种不同的持久性。法律证据开示渠道产生了第一个有法院记录的获取记录、第一个九位数和解金、以及法院在合法训练数据与影子图书馆训练数据之间的首次区分。它尚未产生高管级别的个人问责。部署层回滚和评估层政策修订更快、更便宜、触及更少。它们让架构保持原位。拦截在每个层以自己的方式工作，但在任何一个层都尚未触及那个被托辞语法保护其被置换决策的高管。

**翻译笔记：**
"Three AI-stack layers. Three interception forms. Three different durabilities." → "三个 AI 技术栈层。三种拦截形式。三种不同的持久性。"——三个短句递进。
"The interception works at each layer in its own register" → "拦截在每个层以自己的方式工作"——保留"register"的多层含义

---

**原文：**
Chapter 8 walked the institutional-power case — power calling itself the goat. We have walked the newest altar. Chapter 10 is the next stress-test in Part III: the war zone, where the cost-bearer is identifiable, the record-control architecture sits behind a uniformed border, and the diagnostic must climb past the highest legal heat we encounter.

**译文：**
第 8 章走了制度权力的案例——权力自称替罪羊。我们已经走了最新的祭坛。第 10 章是第三部分的下一项压力测试：战区，在那里代价承担者是可识别的，记录控制架构坐落在穿制服的边界之后，而诊断必须攀爬过我们遇到的最高法律热度。

**翻译笔记：**
"the newest altar" → "最新的祭坛"——呼应全书标题"祭坛移动了"的隐喻
"uniformed border" → "穿制服的边界"——暗示军事/国家边界

---

**原文：**
The model-decided alibi shows up wherever an AI system produces an output that affects us and the company narrates it in the grammar of system agency. *The model decided.* *The algorithm flagged.* *The data showed.* *The benchmark scored.* The verb's subject is a thing.

**译文：**
模型决定的托辞出现在任何 AI 系统产生一个影响我们的输出、而公司以系统施事语法将其叙事的地方。*模型决定了。* *算法标记了。* *数据显示了。* *基准评了分。* 动词的主语是一个东西。

**翻译笔记：**
四个短斜体句保留原文节奏——"The model decided. The algorithm flagged. The data showed. The benchmark scored." → "模型决定了。算法标记了。数据显示了。基准评了分。"

---

**原文：**
We interact with these systems daily. Employer AI screening. Bank-AI denial. AI-generated content provenance. Insurance-AI pricing. Content-moderation decisions on the platforms we use. Healthcare-AI triage. Government-AI assessment for benefits eligibility, tax flagging, visa decisions. Recommendation engines that decide what news we see. The list is incomplete. The recognition trigger is one question. Did a non-human verb-subject just absorb a decision that affects me? If yes, the alibi is operating. Run the diagnostic three times — once at each layer.

**译文：**
我们每天与这些系统互动。雇主的 AI 筛选。银行 AI 拒绝。AI 生成内容的来源追溯。保险 AI 定价。我们使用的平台上的内容审核决策。医疗 AI 分诊。政府 AI 对福利资格、税务标记、签证决策的评估。决定我们看到什么新闻的推荐引擎。这个列表是不完整的。识别触发点是一个问题。刚刚是否有一个非人类动词主语吸收了一个影响我的决策？如果是的，托辞正在运行。运行诊断三次——每个层一次。

---

**原文：**
The diagnostic markers, by layer, are concrete.

**译文：**
诊断标记，按层区分，是具体的。

---

**原文：**
#### At the input layer.

**译文：**
#### 在输入层。

---

**原文：**
The company will not name the training corpora or licensing status. Public statements use "publicly available data" or "data we licensed from partners" without specifying which works and from whom. The acquisition record is described as a trade secret while the output is positioned as transformative. These patterns appearing together are the diagnostic question, not the answer; we see the input-layer alibi shape and ask which displaced acquisition decision the grammar is protecting.

**译文：**
公司不会指名训练语料或许可状态。公开声明使用"公开可用数据"或"我们从合作伙伴处获得许可的数据"，而未具体说明哪些作品、来自谁。获取记录被描述为商业秘密，而输出被定位为转化性的。这些模式同时出现时是诊断问题，不是答案；我们看到输入层托辞形状，并询问语法在保护哪个被置换的获取决策。

---

**原文：**
#### At the deployment layer.

**译文：**
#### 在部署层。

---

**原文：**
Behaviour change between versions is not surfaced — the deployed model is described as "the model" with no version designation. The appeal or correction route, where one exists, returns to the same model with no human reviewer. The post-deployment optimisation framework — reward-shaping changes, fine-tuning targets — is not disclosed. These patterns appearing together are the diagnostic question; we see the deployment-layer alibi shape and ask which named release or reward-shaping decision the grammar is protecting.

**译文：**
版本间的行为变化未被浮出表面——已部署模型被描述为"模型"而无版本标识。申诉或更正渠道（如果存在）返回到同一个模型，没有人类审查员。部署后优化框架——奖励塑造变更、微调目标——未被披露。这些模式同时出现时是诊断问题；我们看到部署层托辞形状，并询问语法在保护哪个被命名的发布或奖励塑造决策。

---

**原文：**
#### At the evaluation layer.

**译文：**
#### 在评估层。

---

**原文：**
Benchmark performance is cited in procurement or marketing materials as a property of the model, without specifying which variant was benchmarked. Performance gaps between the announced model and the shipped model are not disclosed. The benchmark organisation's procedural shell — how submissions are managed, what experimental variants are permitted, what disclosure providers owe — is not transparent. These patterns appearing together are the diagnostic question; we see the evaluation-layer alibi shape and ask which named submission decision the grammar is protecting.

**译文：**
基准性能在采购或营销材料中被引用为模型的一个属性，而未具体说明哪个变体被基准评测。已公布模型与已发货模型之间的性能差距未被披露。基准组织的程序外壳——提交如何被管理、什么实验变体允许、提供者负有什么披露义务——是不透明的。这些模式同时出现时是诊断问题；我们看到评估层托辞形状，并询问语法在保护哪个被命名的提交决策。

---

**原文：**
The single sharpest move is the same at every layer: demand the three records in writing — the training-corpus acquisition log, the deployment reward-shaping log, the benchmark-submission record — and treat a denial as the diagnostic finding, not a dead end. Do not accept "the model is a black box" as a complete explanation of a decision that affects our employment, our credit, our insurance, our healthcare, our visa, our benefits, our account, or our published work.

**译文：**
每个层最锐利的一招是同一个：以书面形式索取三条记录——训练语料获取日志、部署奖励塑造日志、基准提交记录——并将拒绝视为诊断发现，而非死胡同。不要接受"模型是黑箱"作为对一个影响我们就业、信用、保险、医疗、签证、福利、账户或已发表作品的决策的完整解释。

**翻译笔记：**
"treat a denial as the diagnostic finding, not a dead end" → "将拒绝视为诊断发现，而非死胡同"——本章的核心行动指令

---

**原文：**
The warning sign is concrete, and it is the moment the alibi becomes personal: a request to sign for, certify, or be the visible named owner of an AI output we cannot independently inspect. The human-in-the-loop signoff. The compliance attestation that an AI tool is "fit for purpose." The clinician's electronic confirmation of an AI diagnostic recommendation. The loan officer's countersignature on an AI-flagged transaction. The five-role conflation makes the human signer the seam: the lab built the model, the deployer ran it and holds the audit log and processes the appeal, and the contract makes us personally liable for endorsing the output. If we cannot inspect the training corpus, the deployment record, and the benchmark-submission record, we cannot legitimately sign for the output.

**译文：**
警示信号是具体的，而且正是托辞变得个人化的那一刻：要求我们为无法独立检查的 AI 输出签字、认证、或成为可见的具名所有者。人在回路中的签核。AI 工具"适合目的"的合规认证。临床医生对一个 AI 诊断建议的电子确认。信贷员对 AI 标记的交易的会签。五角色融合使人类签字者成为接缝处：实验室建造了模型，部署者运行它并持有审计日志和处理申诉，而合同使我们个人为认可该输出承担追责。如果我们不能检查训练语料、部署记录和基准提交记录，我们就不能合法地为该输出签字。

**翻译笔记：**
"The warning sign is concrete, and it is the moment the alibi becomes personal" → "警示信号是具体的，而且正是托辞变得个人化的那一刻"——接前文诊断标记的具体性
"human-in-the-loop signoff" → "人在回路中的签核"
"fit for purpose" → "适合目的"——保留原文引号

---

**原文：**
The signature is the model's alibi made personal — the same trap chapter 7 named at the Post Office counter and the Therac-25 console, now wearing the added inscrutability of statistical training. The same shape, new scale. The first anti-laundering device remains the record, and we have shown how to demand three of them.

**译文：**
签名是模型的托辞变得个人化——与第 7 章在邮局柜台和 Therac-25 控制台上命名的陷阱相同，如今披上了统计训练所增添的不可测性。相同的形状，新的规模。第一个反洗白装置仍然是记录，而我们已经展示了如何索取三条记录。

**翻译笔记：**
"the added inscrutability of statistical training" → "统计训练所增添的不可测性"——保留"inscrutability"的深层含义
"The same shape, new scale." → "相同的形状，新的规模。"——与本章开头呼应

---

**原文：**
A fourth layer is emerging — autonomous-action systems that chain model outputs into steps taken in the world. The diagnostic ports forward intact: a fourth record, the action log, joins the three we have demanded. When the agents arrive in our work, we already know what to ask.

**译文：**
第四层正在浮现——将模型输出链接为在世界上采取的步骤的自主行动系统。诊断完好地向前移植：第四条记录——行动日志——加入我们已经索要的三条记录。当自主行动系统（agents）到达我们的工作中时，我们已经知道该问什么。

**翻译笔记：**
[TERM-NOTE] "agents" → 在此指"自主行动系统(agents)"——保留英文 agents 并暗示这是第四层（autonomous-action systems）的指代
"the diagnostic ports forward intact" → "诊断完好地向前移植"——与第 163 行的"port forward"一致

---

## 脚注

**原文：**

[^307]: Sycophancy in GPT-4o: What happened and what we're doing about it. [primary URL no longer resolves as of 2026-05-28; canonical archive] [archived snapshot](http://web.archive.org/web/20260524131149/https://openai.com/index/sycophancy-in-gpt-4o/).
[^308]: Sam Altman X post acknowledging GPT-4o sycophancy. Archived at http://web.archive.org/web/20260411001817/https://x.com/sama/status/1916625892123742290.
[^309]: Ahmad Al-Dahle X post denying Meta trained Llama 4 on test sets. Archived at http://web.archive.org/web/20250523051535/https://x.com/Ahmad_Al_Dahle/status/1909302532306092107.
[^310]: Order directing OpenAI to preserve and segregate output log data, The New York Times Company v. Microsoft Corporation et al., Case No. 1:23-cv-11195 (S.D.N.Y.). [primary URL no longer resolves as of 2026-05-28; canonical archive] [archived snapshot](http://web.archive.org/web/20260416015333/https://docs.justia.com/cases/federal/district-courts/new-york/nysdce/1:2023cv11195/612697/551).
[^311]: Sam Altman X post acknowledging GPT-4o sycophancy. Archived at http://web.archive.org/web/20260411001817/https://x.com/sama/status/1916625892123742290.
[^312]: Ahmad Al-Dahle X post denying Meta trained Llama 4 on test sets. Archived at http://web.archive.org/web/20250523051535/https://x.com/Ahmad_Al_Dahle/status/1909302532306092107.
[^313]: LMArena public statement on Meta's Llama-4-Maverick submission and LMArena leaderboard policy revision. Archived at http://web.archive.org/web/20260526051543/https://simonwillison.net/2025/Apr/8/lmaren/.
[^314]: Bartz v. Anthropic PBC — preliminary approval of $1.5 billion class settlement and per-work compensation framework. [susmangodfrey.com](https://www.susmangodfrey.com/wins/susman-godfrey-secures-1-5-billion-settlement-in-landmark-ai-piracy-case/), [archived snapshot](http://web.archive.org/web/20260515143135/https://www.susmangodfrey.com/wins/susman-godfrey-secures-1-5-billion-settlement-in-landmark-ai-piracy-case/).
[^315]: Bartz v. Anthropic Fairness Hearing: Final Reminder, 91.3% Claims Rate, and updates from the Docket. [authorsalliance.org](https://www.authorsalliance.org/2026/05/14/bartz-v-anthropic-fairness-hearing-final-reminder-91-3-claims-rate-and-updates-from-the-docket/), [archived snapshot](http://web.archive.org/web/20260515051333/https://www.authorsalliance.org/2026/05/14/bartz-v-anthropic-fairness-hearing-final-reminder-91-3-claims-rate-and-updates-from-the-docket/).

**译文：**（脚注保留英文原文，不翻译——URL 链接和文档名需保持可检索性）

[^307]: GPT-4o 中的谄媚行为：发生了什么以及我们正在采取的应对措施。[原始 URL 自 2026-05-28 起不再解析；规范存档][存档快照](http://web.archive.org/web/20260524131149/https://openai.com/index/sycophancy-in-gpt-4o/)。
[^308]: Sam Altman X 帖子承认 GPT-4o 谄媚行为。存档于 http://web.archive.org/web/20260411001817/https://x.com/sama/status/1916625892123742290。
[^309]: Ahmad Al-Dahle X 帖子否认 Meta 在测试集上训练 Llama 4。存档于 http://web.archive.org/web/20250523051535/https://x.com/Ahmad_Al_Dahle/status/1909302532306092107。
[^310]: 命令指示 OpenAI 保留和隔离输出日志数据，The New York Times Company v. Microsoft Corporation et al.，案号 1:23-cv-11195 (S.D.N.Y.)。[原始 URL 自 2026-05-28 起不再解析；规范存档][存档快照](http://web.archive.org/web/20260416015333/https://docs.justia.com/cases/federal/district-courts/new-york/nysdce/1:2023cv11195/612697/551)。
[^311]: Sam Altman X 帖子承认 GPT-4o 谄媚行为。存档于 http://web.archive.org/web/20260411001817/https://x.com/sama/status/1916625892123742290。
[^312]: Ahmad Al-Dahle X 帖子否认 Meta 在测试集上训练 Llama 4。存档于 http://web.archive.org/web/20250523051535/https://x.com/Ahmad_Al_Dahle/status/1909302532306092107。
[^313]: LMArena 关于 Meta 的 Llama-4-Maverick 提交及 LMArena 排行榜政策修订的公开声明。存档于 http://web.archive.org/web/20260526051543/https://simonwillison.net/2025/Apr/8/lmaren/。
[^314]: Bartz v. Anthropic PBC——15 亿美元集体和解及每件作品赔偿框架的初步批准。[susmangodfrey.com](https://www.susmangodfrey.com/wins/susman-godfrey-secures-1-5-billion-settlement-in-landmark-ai-piracy-case/)，[存档快照](http://web.archive.org/web/20260515143135/https://www.susmangodfrey.com/wins/susman-godfrey-secures-1-5-billion-settlement-in-landmark-ai-piracy-case/)。
[^315]: Bartz v. Anthropic 公平性听证会：最终提醒、91.3% 索赔率及案卷更新。[authorsalliance.org](https://www.authorsalliance.org/2026/05/14/bartz-v-anthropic-fairness-hearing-final-reminder-91-3-claims-rate-and-updates-from-the-docket/)，[存档快照](http://web.archive.org/web/20260515051333/https://www.authorsalliance.org/2026/05/14/bartz-v-anthropic-fairness-hearing-final-reminder-91-3-claims-rate-and-updates-from-the-docket/)。

**翻译笔记：**
脚注中的文章名和文档名提供中文翻译以便中文读者理解，URL 和存档链接原样保留。

---

## 翻译笔记摘要

### 1. 八问诊断框架跨章一致性（全书最高优先级）
本章在三层诊断中多次运行八问。所有八问的中文与第 3 章 ready 文本完全一致：
1. 谁或什么被公开归咎？
2. 谁拥有控制权？
3. 谁受益？
4. 谁知情或应知情？
5. 谁能阻止复发？
6. 谁控制了记录？
7. 谁承担了代价？
8. 如果责任跟随控制权而非可见度，责任会是什么样子？

### 2. 三层分析框架术语一致性
- input layer → 输入层
- deployment layer → 部署层
- evaluation layer → 评估层
（全部通过 Glossary Master 裁决 2026-06-13）

### 3. 回旋镖案例跨章对齐
- **Therac-25**："Malfunction 54"（故障 54）、"TREATMENT PAUSE"（治疗暂停）——与第 2 章一致
- **737 MAX**：机动特性增强系统（MCAS）、"MCAS 处理了它"——与第 2 章一致
- **Horizon 五角色融合**：部署者、审计追踪持有者、投诉人、检控方、披露控制者——与第 7 章一致

### 4. 核心诊断语言保留
- "The verb's subject is a thing" → "动词的主语是一个东西"
- "The grammar is the laundering" → "语法即洗白"
- "the displaced decision" → "被置换的决策"
- "the named human decisions are absent from the grammar" → "被命名的人类决策从语法中缺席"

### 5. 15 条新术语（全部通过 Glossary Master 裁决）
input layer/部署层/评估层、sycophancy/谄媚行为、alibi escalation/托辞升级、grammar of system agency/系统施事语法、credentialing commons/认证公地、litigation interception triplet/诉讼拦截三元组、reward-shaping/奖励塑造、reward signal/奖励信号、post-training/训练后、model variant/模型变体、acquisition record/获取记录、training corpus/训练语料、shadow library/影子图书馆

### 6. 三个记录索取要求的平行句式
- 输入层的记录索取要求：训练语料获取日志
- 部署层的记录索取要求：训练后奖励塑造日志
- 评估层的记录索取要求：基准提交记录

### 7. 直接引语调色
- Meta 发言人声明 → 企业公关正式语调
- OpenAI post-mortem → 分析性语调
- Sam Altman X 帖子 → 口语化色彩（"过于谄媚和烦人"）
- Al-Dahle X 帖子 → 简短否认（"根本不是事实"）
- LMArena 声明 → 基准运营者正式语调

### 8. 三个层的施事者列表
- 输入层：数据 → 语料 → 影子图书馆 → 市场
- 部署层：模型 → 奖励信号 → 发布流程
- 评估层：变体 → 政策 → 基准

### 9. [SPLIT] 标注的位置
- 第 55-57 行（控制/受益/知情收敛复合句）
- 第 87 行（部署层事后分析分析段落）
- 第 109 行（credentialing commons 列举）
- 第 163 行（五角色融合跨层应用复合句）

### 10. [TERM-NOTE] 标注的位置
- "grammar of system agency" → "系统施事语法"（语言学精度关键）
- "Malfunction 54/TREATMENT PAUSE" → 中英对照保留
- "alibi escalation" → "托辞升级"
- "credentialing commons" → "认证公地"
- "litigation interception triplet" → "诉讼拦截三元组"
- "sycophancy" → "谄媚行为"

---

## 决策日志

```yaml
# 翻译决策日志 — 第 9 章

chapter: "09-the-model-did-it"
chapter_title_zh: "模型干了它"
translator: "claude (Translator agent)"
glossary_version: "1.0.0-pilot (ch-09 terms approved 2026-06-13)"

decisions:
  - id: D09-001
    location: "标题"
    type: style-choice
    decision: "\"模型干了它\""
    alternatives_considered: ["模型做了决定", "模型干的", "模型是原因"]
    rationale: "\"模型干了它\"保留了原文口语化的及物力度——'The Model Did It'中的'did it'不是正式的分析措辞，而是故意的口语化表达'它干的'。'干了'在中文中比'做了'更有口语力和归咎力度。且与第 8 章标题'当权力自称替罪羊'的语域形成对比。"
    decided_by: translator
    decided_at: 2026-06-13

  - id: D09-002
    location: "第 15 行"
    type: prose-choice
    decision: "\"动词的主语是一个东西\""
    alternatives_considered: ["动词的主语是一个事物", "动词的主语是物", "动词的主语是非人类实体"]
    rationale: "\"东西\"保留了原文'thing'的直白和异质性——这是一个诊断性判断句，不是修辞。'thing'在本章中具有分析上的精确性（非人类、非具名），不应被优雅化。"
    decided_by: translator
    decided_at: 2026-06-13

  - id: D09-003
    location: "第 41 行"
    type: prose-choice
    decision: "\"语法即洗白\""
    alternatives_considered: ["语法就是洗白", "语法本身就是洗白机制", "语法即责任洗白"]
    rationale: "极简的系词结构('A即B')保留了原文'X is Y'的分析性判断力。不添加'本身'、'机制'等解释性词。这是本章最核心的论证句。"
    decided_by: translator
    decided_at: 2026-06-13

  - id: D09-004
    location: "第 73 行"
    type: prose-choice
    decision: "四个短句递进保留：\"不是新的。规模是新的。技术栈深度是新的。语法不是新的。\""
    alternatives_considered: ["合并为长句"]
    rationale: "保留原文短句节奏——四个'something is new/is not new'的节奏是本章修辞特征之一。中文以相同的短句结构和并列否定/肯定来保留。"
    decided_by: translator
    decided_at: 2026-06-13

  - id: D09-005
    location: "第 95 行"
    type: prose-choice
    decision: "\"快速回滚的制度性外壳可以按设计运行...却仍然产生一种结构性的个体问责缺失\""
    alternatives_considered: ["制度性外壳按设计运行...但/然而"]
    rationale: "\"却仍然\"比\"但\"或\"然而\"更有对比张力——强调即使系统'正常工作'，结构性缺陷仍然存在。两个分句之间的转折力度需保留。"
    decided_by: translator
    decided_at: 2026-06-13

  - id: D09-006
    location: "第 97 行"
    type: prose-choice
    decision: "\"责任形状的空洞\""
    alternatives_considered: ["责任空洞", "问责空缺", "责任的黑洞"]
    rationale: "保留原文的精确措辞'responsibility-shaped hole'。'责任形状的空洞'强调这是一个有形状的、可见的空洞——不是简单的'缺失'。'黑洞'添加了原文没有的物理学隐喻。"
    decided_by: translator
    decided_at: 2026-06-13

  - id: D09-007
    location: "第 107 行"
    type: prose-choice
    decision: "\"托辞没有失败。它在程序外壳上向上移动了一级。\""
    alternatives_considered: ["托辞在更高层重新出现"]
    rationale: "保留原文的两短句结构。'托辞没有失败'是颠覆性断言——读者期待'托辞被戳破'，实际是'托辞升级了'。"
    decided_by: translator
    decided_at: 2026-06-13

  - id: D09-008
    location: "第 141 行"
    type: prose-choice
    decision: "三层施事者列表以平行结构呈现"
    rationale: "每一层施事者的列举（数据→语料→影子图书馆→市场 / 模型→奖励信号→发布流程 / 变体→政策→基准）在中文中以相同句式呈现，保留原文的平行分析结构。"
    decided_by: translator
    decided_at: 2026-06-13

  - id: D09-009
    location: "第 193 行"
    type: prose-choice
    decision: "四个短斜体句：\"模型决定了。算法标记了。数据显示了。基准评了分。\""
    alternatives_considered: ["模型做了决定/算法做了标记..."]
    rationale: "保留原文的极简短句节奏——每个句子 5 个字符左右，与英语原文的节奏匹配。\"评了分\"相对于\"打了分\"更符合中文的表达习惯。"
    decided_by: translator
    decided_at: 2026-06-13

  - id: D09-010
    location: "第 213 行"
    type: prose-choice
    decision: "\"签名是模型的托辞变得个人化\""
    alternatives_considered: ["签名使得模型的托辞个人化了", "签名使模型的托辞个人化"]
    rationale: "被动式'made personal'译为'变得个人化'——强调过程的自发性（托辞本身具有个人化的属性），而非被外力的驱使。与原文的被动式一致。"
    decided_by: translator
    decided_at: 2026-06-13

  - id: D09-011
    location: "第 215 行"
    type: prose-choice
    decision: "\"当 agents 到达我们的工作中时\""
    alternatives_considered: ["当自主行动系统(agents)到达我们的工作中时", "当智能体到达我们的工作中时"]
    rationale: "保留英文'agents'——在此处指第四层'autonomous-action systems'。'智能体'是中文 AI 术语中对 agent 的常见译法，但本章中 agent 的特指需要保留其与前三层分析的一致性。首次出现时括号注中文'自主行动系统'已在译者指导下处理。"
    decided_by: translator
    decided_at: 2026-06-13
```

---

## 假设

1. 15 条新术语已通过 Glossary Master 裁决（2026-06-13），可安全使用
2. 第 3 章 ready 稿中的八问中文是最终版本，不会再有修订
3. 第 2 章 Therac-25 和 737 MAX 的术语（Malfunction 54、MCAS 等）在处理方式上与 ready 稿保持一致
4. 第 7 章五角色融合的角色名称（部署者、审计追踪持有者等）即为最终版本

## 未决问题

1. "TREATMENT PAUSE"在原文第 75 行和第 2 章源文件中未直接出现引用——当前处理为"TREATMENT PAUSE（治疗暂停）"，需 Reviewer 确认第 2 章是否有标准处理方式
2. 第 73 行"the model decided"在首次出现时译为加引号的"模型决定了"——与全章其他"模型决定了"实例需保持一致
3. 第 193 行"the algorithm flagged"译为"算法标记了"——"flagged"在此上下文中为 AI 内容审核/标记的通用含义，不涉及特定技术实现
4. 第 222 行编译器注释句（关于 per-chapter 和 back-of-book references 的处理）保留英文原文

## 交接

Handoff: Reviewer

Chapter: 09-the-model-did-it
Source: /Users/duxiying/Documents/no-one-did-it/book/chapters-v6/09-the-model-did-it.md
译文: /Users/duxiying/Documents/no-one-did-it/translation/chapters/09-the-model-did-it-draft.md
术语表: /Users/duxiying/Documents/no-one-did-it/translation/glossary.yml (ch-09 terms approved)

Next owner: Reviewer
Pending: 审核员对八问框架一致性、三层的术语一致性、回旋镖案例术语跨章对齐、核心诊断语言"语法即洗白"的节奏感、三条记录索取要求的平行句式、及直接引语的语调保留进行逐条审核。
