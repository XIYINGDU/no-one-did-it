# Glossary Master 裁决 — 第 9 章 "The Model Did It"

Owner: Glossary Master
Date: 2026-06-13
Source: translation/decision-log/09-term-proposals.md

---

## 逐条裁决结果（15 条提案）

### 1. input layer → "输入层"

**裁定：批准。**
用于与 deployment layer 和 evaluation layer 构成三层分析框架的方位标记。'输入层'强调数据进入模型的位置，而不是数据本身。与提案一致。

**理由：** 三层框架的方位标记必须保持一致（输入层 / 部署层 / 评估层），且与技术栈的物理/逻辑结构对应。'输入层'是 AI/ML 工程语境中的标准表述。

**影响章节：** 9

---

### 2. deployment layer → "部署层"

**裁定：批准。**
'部署层'保留了 deployment 在工程/软件语境中的标准含义（模型部署至生产环境）。是三层分析框架的第二层。

**理由：** 与 input layer 和 evaluation layer 构成结构一致的三层框架。'发布层'过于窄化（deployment 包括运行时配置等后续操作），'应用层'过于泛化。

**影响章节：** 9

---

### 3. evaluation layer → "评估层"

**裁定：批准。**
'评估层'涵盖排名和基准透明度的双重含义。'评测'过于偏向技术性能侧，而 evaluation 在本章语境中还包括基准运营者的程序外壳和提交政策。

**理由：** '评估'在中文中比'评测'更宽——可以包括程序性评估和规则性评估。注意原文中 evaluation 涵盖 benchmark 的透明度规则和提交政策，不仅仅是技术指标排名。

**影响章节：** 9

---

### 4. sycophancy → "谄媚行为" / sycophantic → "谄媚的"

**裁定：批准。**
'谄媚行为'精确传达了 sycophancy 在 GPT-4o 案例中的双重含义——(1)过度支持性但不真诚；(2)有策略性的迎合（非出于真实同意）。'奉承'过于礼貌且丢失了 disingenuous 的虚伪色彩。

**理由：** 原文使用 sycophantic behaviour 描述模型行模式——其在语境中的核心语义是"虚伪地讨好/迎合"，而不是简单的"说好话"。'谄媚'在中文中的贬义程度与原文匹配。

**使用要求：** 首次出现在翻译笔记（非正文）中说明 sycophancy 在 AI 伦理文献中的标准用法（模型倾向于迎合用户观点的行为模式）。正文中无需括号附英文——'谄媚行为'已是语义自足的中文。但若原文使用 'sycophantic' 的斜体/引号强调形式，正文中对应保留引号（"谄媚的"）。

**影响章节：** 9

---

### 5. alibi escalation → "托辞升级"

**裁定：批准。**
与第 4 章已有术语 alibi collapse → "托辞崩塌"形成互补概念对。'升级'(escalation)的使用表明同一结构的层级间移动——不是在更高层级解决，而是在更高层级重新出现。动词形式 "to escalate the alibi" → "托辞升级"。

**理由：** '托辞前缀'与第 4 章的 alibi collapse 保持 100% 一致。'托辞升级迭代'禁止——过于啰嗦，且"迭代"并非原文语义成分。

**使用要求：** 首次出现时建议括号附英文 (alibi escalation)，并在翻译笔记中说明其与 alibi collapse（托辞崩塌）的概念对关系——当托辞在第 N 层被截获时，它移动到第 N+1 层（升级）；当托辞被打破时，它在原地失败（崩塌）。

**tags:** translation_strategy | cs-metaphor-extended
**理由：** 该概念对（升级/崩塌）是本书原创分析框架的语言学扩展，中文读者通过"升/崩"的空间隐喻即可理解层级关系。

**影响章节：** 9

---

### 6. grammar of system agency → "系统施事语法"

**裁定：批准。**
'施事'是语言学对语义角色 agent 的标准术语，与 '语法' 搭配构成分析框架名称。禁止的替代词均已正确识别——'主语'是句法学概念而 '施事' 是语义学概念，本章论证重点正是语义层面（施事/agent 的角色分配）。

**理由：** '系统施事语法'在语言学技术上准确：本章论证的非人类名词占据的是语义层面的施事(agent)位置，不仅仅是句法层面的主语(subject)位置。这是本章的核心论证概念——'语法即洗白'(The grammar is the laundering)。

**使用要求：** 首次出现必须括号附英文并给出简短解释，例如：'系统施事语法（grammar of system agency——指一个非人类名词占据动词的施事位置，从而吸收人类决策的归责）'。后续出现可用'系统施事语法'或简短形式'施事语法'。禁止使用 '系统主语语法'——主语是句法概念，此处是语义概念。

**影响章节：** 9

---

### 7. credentialing commons → "认证公地"

**裁定：批准。**
'公地'(commons)在中文制度经济学讨论中已有固定对应（如"公地悲剧"——tragedy of the commons），在此处的用法与该文献传统一致——LMArena 排行榜信号是公共评估基础设施，其可信度被 Meta 的提交行为损害，代价承担者是依赖该信号的社区群体。

**理由：** 翻译精确度检查：'credentialing'（提供信用凭证的过程）→ '认证'；'commons'（共享资源池）→ '公地'。'信任公地'禁止——原文是 credentialing（认证过程），不是 trust。'认证公共资源'禁止——过于直白且丢失了 commons 的概念精确性。

**使用要求：** 首次出现建议括号附英文 (credentialing commons)。无需在正文中展开解释——"认证公地"在上下文（依赖排行榜排名作为质量信号的开源社区）中已有足够的理解锚点。

**impact章节：** 9

---

### 8. litigation interception triplet → "诉讼拦截三元组"

**裁定：批准。**
与已有术语 interception → "拦截"（第 4 章）保持一致。'三元组'传达了三个工具构成不可分割的最小集合这一核心含义——不是三选一，三个必须同时存在。

**理由：** 翻译精确度检查：'litigation'(诉讼) + 'interception'(拦截) + 'triplet'(三元组——缺一不可的最小组)。'诉讼拦截三件套'禁止——语言风格不对（过于口语化）。'法律拦截三要素'禁止——"要素"暗示 list-like 关系，而 triplet 强调 three-as-one 的不可分割性。

**使用要求：** 首次出现建议括号附英文 (litigation interception triplet)，并在翻译笔记中说明三元组的三个构成工具：发现权(discovery power)+技术证据分析(technical-evidence analysis)+愿审理实体的联邦法官(named federal judge willing to engage substance)。

**影响章节：** 9

---

### 9. reward-shaping → "奖励塑造"

**裁定：批准。**
'奖励塑造'是中文 AI/ML 领域对 reward-shaping 的通用译法，在强化学习/RLHF 文献中已成标准术语。

**理由：** 标准技术术语。'奖励调整'禁止——reward tuning/adjustment 是不同概念。'奖励设计'禁止——reward design 是更上层的概念。'奖励工程'禁止——无此中文 AI 技术用语。

**使用要求：** 无需首次出现中英对照——'奖励塑造'在 AI/ML 文献中已有明确含义。正文语境（GPT-4o post-mortem 中的训练后优化框架）已提供足够的理解线索。

**影响章节：** 9

---

### 10. reward signal → "奖励信号"

**裁定：批准。**
强化学习/RLHF 中的标准术语，与 reward-shaping（奖励塑造）搭配使用。

**理由：** 标准 AI/ML 术语。'反馈信号'禁止——feedback signal 可能是另一种技术概念（如基于用户点击的隐式反馈）。'奖励数据'禁止——signal 是信号，data 是数据，reward data（如人类标注的偏好数据集）是不同概念。

**使用要求：** 无需首次出现中英对照。与 reward-shaping 配合使用时注意区分：reward signal 是信号本身，reward-shaping 是调整信号的过程。

**影响章节：** 9

---

### 11. post-training (compound modifier) → "训练后"

**裁定：批准。**
作复合形容词时使用'训练后'（post-training optimisation → 训练后优化；post-training reward-shaping → 训练后奖励塑造）。作名词短语时（'the post-training'）译为'训练后阶段'。

**理由：** 提案的鉴别准确：'后训练'在中文 AI 术语中已有不同技术含义（指 pre-training/post-training 的训练流程划分），不可用作 post-training 的翻译。'后期训练'禁止——暗示时间顺序中较后的训练阶段，与原文的"训练完成后"不同。

**使用要求：** 注意在上下文中与其他时间修饰语（pre-training → 训练前、fine-tuning → 微调）清晰区分。首次出现在翻译笔记中说明此区分即可。

**影响章节：** 9

---

### 12. model variant / variant → "模型变体"

**裁定：批准。**
'变体'在进化生物学、语言学中都用于表示同一物类的不同形态，在此处用于指同一模型的不同变体（如 Llama-4-Maverick-03-26-Experimental 对话优化变体 vs. 公开发布权重）。禁止'变种'——该词暗示退化/异常，而 variant 在本章中是中性描述。

**理由：** 翻译精确度检查：在 Llama 4 案例中 variant 指同一基础模型的不同配置/优化版本，不是不同模型。'衍生模型'(derivative model)和'定制版本'(customized version)都暗示不同的开发路径，不符合 variant 在本章的用法。

**使用要求：** 全文统一。当原文单独使用 'variant' 时同样译为'变体'，不需要每次加 '模型' 前缀。上下文已足够区分是模型的变体。

**影响章节：** 9

---

### 13. acquisition record → "获取记录"

**裁定：批准。**
在法律/证据语境中强调 acquisition 的证据性——记录并证明某物如何/何时/被谁获取。Alsup 法官在 Bartz 案中将界线划在'获取的时刻'(the moment of acquisition)——什么被获取、从何处、以什么许可——而非输出端的行为。

**理由：** 翻译精确度检查：acquisition 在此处是指数据获取（下载/购买/扫描），不是公司并购(mergers and acquisitions)。'获取记录'不同于"记录获取"（record acquisition）——前者是关于获取行为的记录（宾语是记录的内容），后者是获取记录的行为（宾语是记录本身）。

**使用要求：** 首次出现建议括号附英文 (acquisition record) 以明确不是公司并购含义。确保上下文提供足够的区分——正文中 Alsup 判决的讨论已自然区分。

**影响章节：** 9

---

### 14. training corpus / training corpora → "训练语料"

**裁定：批准。**
与"训练数据"(training data)的区分是本章论证的基础——该区分的建立是译者必须完成的关键工作。'语料'是语料库语言学(corpus linguistics)对 corpus 的标准译法，单数/复数（语料/语料库）需在翻译笔记中说明。

**理由：** 本章需要"训练语料"与"训练数据"两个概念在译文中保留精确区分——当原文说 training data 时用"训练数据"（泛指 AI 训练使用的所有数据），当原文说 training corpus 时用"训练语料"（特指特定集合，如 LibGen、PiLiMi 语料）。此区分是 Alsup 判决的核心——界线划在具体语料的获取方式而非泛称的"训练数据"层面。

**使用要求：** 首次出现必须括号附英文 (training corpus)。翻译笔记中需说明 corpus/corpora 的单复数区别。全文必须保持与 training data（训练数据）的精确区分——译者需要在每次遇到这两个词时确认使用的是语料(collection)和数据(material)中的哪一个。

**影响章节：** 9

---

### 15. shadow library → "影子图书馆（shadow library）"

**裁定：批准。**
'影子图书馆'是中文学术传播和版权讨论中已有的通用译法（指南 2025 年百度百科/中文学术讨论中指称 LibGen、Sci-Hub 等的主体术语）。首次出现必须中英对照。

**理由：** 翻译精确度检查：shadow library 是运行于表面网络(surface web)而非暗网(dark web)的公开或半公开资源库。'暗网图书馆'禁止——提供了错误的技术/法律信号（暗示涉及暗网运营，实际为表面网络）。'盗版资源库'禁止——过于宽泛且带有预设的刑事标签，而本书对 shadow libraries 的分析是程序性的而非刑法性的。'地下图书馆'禁止——"地下"在中文中同样暗示非法/隐秘性，与 shadow library 的实际运营特征不完全匹配。

**使用要求：** 首次出现必须用全称（影子图书馆 (shadow library)），后续出现可用'影子图书馆'。翻译笔记中需说明这些图书馆运行于表面网络而非暗网，以避免读者产生"暗网"联想。

**影响章节：** 9

---

## 跨章一致性验证报告

### 1. 八问诊断框架（第 3 章 → 第 9 章）

已验证第 3 章 ready 文本。以下八个问题的中文与提案完全匹配。无需修改。

| 英文 | 中文（第 3 章 ready 文本，已验证） | 提案映射 |
|---|---|---|
| Who was publicly blamed? | 谁或什么被公开归咎？ | ✓ |
| Who had control? | 谁拥有控制权？ | ✓ |
| Who benefited? | 谁受益？ | ✓ |
| Who knew or should have known? | 谁知情或应知情？ | ✓ |
| Who could have prevented recurrence? | 谁能阻止复发？ | ✓ |
| Who controlled the record? | 谁控制了记录？ | ✓ |
| Who bore the cost? | 谁承担了代价？ | ✓ |
| What would responsibility look like if it followed control instead of visibility? | 如果责任跟随控制权而非可见度，责任会是什么样子？ | ✓ |

**结论：完全一致。无需修改。**

### 2. 回旋镖术语跨章一致性

#### Therac-25（第 2 章、第 7 章 → 第 9 章）
- 第 2 章 ready 文本："Malfunction 54"（故障54）——保留英文 + 中文括号注
- 第 7 章 ready 文本："TREATMENT PAUSE（治疗暂停）"——保留英文 + 中文括号注
- 第 9 章译者必须：在第 75 行 "Malfunction 54 和 TREATMENT PAUSE" 的回旋镖参考中，遵循上述保留英文 + 中文括号注的处理模式

#### 737 MAX / MCAS（第 2 章 → 第 9 章）
- 第 2 章 ready 文本：首次出现为"机动特性增强系统（Maneuvering Characteristics Augmentation System）——MCAS"
- 第 9 章译者必须：在 MCAS 的回旋镖参考中，直接使用第 2 章已建立的中文全称"机动特性增强系统"或"MCAS"（取决于上下文是否需要全称）

#### Horizon / 五角色融合（第 7 章 → 第 9 章）
- 已建立术语（glossary.yml）：五角色融合、部署者、审计追踪持有者、投诉人、检控方、披露控制者、私人检控
- 第 79 行原文使用 "deploys, audits, complains, prosecutes, and discloses"——译者注意这些是五角色融合的动词形式中文处理，应译为"部署、审计、投诉、检控、披露"
- **发现：第 7 章 ready 文本第 90 行存在"审计追踪控制者"与 glossary.yml 已锁定的"审计追踪持有者"(audit-trail holder)不一致**。第 7 章的图表说明（第 67 行）使用 glossary 的"审计追踪持有者"，但正文第 90 行使用"审计追踪控制者"。第 9 章译者必须使用 glossary 锁定的"审计追踪持有者"。

### 3. 训练数据处理策略
- "训练数据"(training data) — 不设 glossary 条目，作为通用技术术语由译者自行处理
- "训练语料"(training corpus) — 已批准新增 glossary 条目（#14）
- 两者需严格区分：原文 training data → 训练数据；原文 training corpus → 训练语料

### 4. 法律案例名词组处理
按全书规范：
- *Bartz v. Anthropic PBC* — 首次出现保留英文斜体，括号附中文"巴茨诉 Anthropic PBC 案"
- *Getty Images v. Stability AI* — 同上
- *Authors Guild v. OpenAI Inc.* — 同上
- *The New York Times Company v. Microsoft Corp.* — 同上
- summary judgment → 简易判决（与已有中文法律术语一致）
- fair use → 合理使用（标准版权法术语）
- class certification → 集体认证（美国集体诉讼程序术语）

---

## 已批准术语汇总

| # | 英文 | 中文 | 领域 |
|---|---|---|---|
| 1 | input layer | 输入层 | AI 分析方法 |
| 2 | deployment layer | 部署层 | AI 分析方法 |
| 3 | evaluation layer | 评估层 | AI 分析方法 |
| 4 | sycophancy / sycophantic | 谄媚行为 / 谄媚的 | AI 行为分析 |
| 5 | alibi escalation | 托辞升级 | 分析方法 |
| 6 | grammar of system agency | 系统施事语法 | 分析方法 |
| 7 | credentialing commons | 认证公地 | 分析方法 |
| 8 | litigation interception triplet | 诉讼拦截三元组 | 分析方法 |
| 9 | reward-shaping | 奖励塑造 | AI/机器学习 |
| 10 | reward signal | 奖励信号 | AI/机器学习 |
| 11 | post-training | 训练后 | AI/机器学习 |
| 12 | model variant | 模型变体 | AI/模型开发 |
| 13 | acquisition record | 获取记录 | 法律/证据 |
| 14 | training corpus | 训练语料 | AI/机器学习 |
| 15 | shadow library | 影子图书馆（shadow library） | 法律/版权 |

15 条提案，15 条批准。0 条修改，0 条否决。

---

## 已更新 glossary.yml 内容

新增第 9 章术语区块，见 glossary.yml 文件改动。

---

Handoff: Translation Director
Priority: 已完成 Glossary Master 对 15 条术语提案的裁决 — 15/15 批准
Action required: 将 15 条批准术语写入 glossary.yml（已同步完成）；通知第 9 章译者开始翻译；将跨章一致性注意事项纳入译者简报
Pending: 无
