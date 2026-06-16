Owner: Translation Director
Action: dispatch-glossary-master
To: Glossary Master
Chapter: 09-the-model-did-it
Source: translation/decision-log/09-term-proposals.md
Date: 2026-06-13

# 第 9 章 Glossary Master 交接

## 章节概况

第 9 章《The Model Did It》（模型干了它）是 **Part III 的第 2 篇**，主题为**系统/对象托辞在 AI 技术栈中的三层递归**。全章 233 行（含 References），涉及三个主要 AI 公司的案例：

- **Meta Llama 4**（2025 年 4 月）— LMArena 排行榜争议：提交的实验变体排名第 2，公开发布权重排名第 32
- **OpenAI GPT-4o**（2025 年 4 月）— 模型部署后谄媚行为（sycophancy），72 小时回滚 + post-mortem
- **Anthropic / Bartz v. Anthropic PBC**（2025 年 6 月—9 月）— 训练数据版权诉讼，Alsup 法官将界线划在"获取"而非"输出"

本章在第 1 章（替罪羊概念/语法托辞）、第 3 章（八问诊断框架）、第 4 章（程序外壳/拦截通道）、第 5 章（和解/证据开示）和第 7 章（记录控制/五角色融合）的基础上运行。

### 内容概要

- **三个操作，三个层**：输入层（input layer）— 训练数据获取；部署层（deployment layer）— 模型行为控制；评估层（evaluation layer）— 基准提交透明度
- **三个回旋镖**：Therac-25（第 2 章，Malfunction 54 → "模型认为"）、737 MAX（第 2 章，MCAS 托辞 → 无飞行员的 AI 变体）、Horizon 五角色融合（第 7 章 → 同一实验室同时是部署者/审计追踪持有者/投诉人/检控方/披露控制者）
- **AI 诉讼拦截三元组**：发现权 + 技术证据分析 + 愿审理实体的联邦法官
- **三个记录索取要求**：训练语料获取日志 + 训练后奖励塑造日志 + 基准提交记录
- **一个反洗钱规则**：从第 7 章移植的"记录优先"原则——当同一机构持有所有记录控制角色时，外部分析是必要工具
- **签名即陷阱**：如果无法检查训练语料获取记录、部署记录和基准提交记录，就不能合法地为该输出签字

### References 情况

本章使用 `<sup>N</sup>` 格式内联引用（共 15 个），References 部分在文件末尾以 `[^N]` 定义，编号模式为 `[^307]` 至 `[^315]`。译者需保留所有 `<sup>` 标签和 `[^N]` 定义。

## 新术语提案

已识别 15 条 glossary.yml 未覆盖的术语，详见 `translation/decision-log/09-term-proposals.md`。

### 提案概览

| # | 英文 | 提案中文 | forbidden | 领域 |
|---|---|---|---|---|
| 1 | input layer | 输入层 | 数据层, 训练层 | AI 分析方法 |
| 2 | deployment layer | 部署层 | 发布层, 应用层 | AI 分析方法 |
| 3 | evaluation layer | 评估层 | 评测层, 基准层 | AI 分析方法 |
| 4 | sycophancy / sycophantic | 谄媚行为 / 谄媚的 | 奉承, 讨好, 谄媚倾向 | AI 行为分析 |
| 5 | alibi escalation | 托辞升级 | 托辞升级迭代, 替罪升级 | 分析方法 |
| 6 | grammar of system agency | 系统施事语法 | 系统主语语法, 被动语法, 系统施动语法 | 分析方法 |
| 7 | credentialing commons | 认证公地 | 信任公地, 资质公地, 认证公共资源 | 分析方法 |
| 8 | litigation interception triplet | 诉讼拦截三元组 | 诉讼拦截三件套, 法律拦截三要素 | 分析方法 |
| 9 | reward-shaping | 奖励塑造 | 奖励调整, 奖励设计, 奖励工程 | AI/机器学习 |
| 10 | reward signal | 奖励信号 | 反馈信号, 奖励数据 | AI/机器学习 |
| 11 | post-training | 训练后 | 后期训练, 后训练 | AI/机器学习 |
| 12 | model variant / variant | 模型变体 | 变种, 衍生模型, 定制版本 | AI/模型开发 |
| 13 | acquisition record | 获取记录 | 获取记录文件, 获取档案, 收购记录 | 法律/证据 |
| 14 | training corpus | 训练语料 | 训练数据, 训练文集, 训练资料 | AI/机器学习 |
| 15 | shadow library | 影子图书馆（shadow library） | 暗网图书馆, 地下图书馆, 盗版资源库 | 法律/版权 |

### 提案要点说明

**#1-3（三层分析框架）** 是本章的核心分析框架，贯穿全文。必须保持三个术语之间的层级关系清晰——输入层/部署层/评估层，且在 AI 技术栈的语境中唯一对应英文的 input/deployment/evaluation layer。

**#4（sycophancy）** 是关键行为描述术语。OpenAI 官方 post-mortem 使用该词描述 GPT-4o 的过度支持性但虚伪的回应模式。'谄媚行为'保留了 sycophancy 的贬义判断维度——不是简单的'奉承'，而是有策略性的迎合。

**#5（alibi escalation）** 与第 4 章已有术语'alibi collapse（托辞崩塌）'形成概念对。建议保持一致的前缀'alibi→托辞'。

**#6（grammar of system agency）** 是全章的论证核心——"The grammar is the laundering"（语法即洗白）。'系统施事语法'的'施事'是语言学标准术语。首次出现可能需要简短的解释性括号注。

**#8（litigation interception triplet）** 是本章的拦截分析框架。"三元组"暗示三个工具缺一不可——不是三选一的选择。与第 4 章"七个拦截通道"概念兼容但独立。

**#13（acquisition record）** 是法庭判决的核心证据概念。Alsup 法官在 Bartz 案中将界线划在'acquisition'而非 output。该术语在中文法律程序中尚无固定译法——'获取记录'强调证据功能（记录并证明某物如何/何时/被谁获取）。

**#15（shadow library）** 在中文学术传播和版权讨论中已有通用译法'影子图书馆'。首次出现必须中英对照。

## 已有术语覆盖检查

以下第 9 章使用的术语已在 glossary.yml 中有对应译法，无需新增条目：

| 术语 | glossary 译法 | 第 9 章中的使用 |
|---|---|---|
| system/object alibi | 系统/对象托辞 | 第 47 行 main case-type classification |
| cost-bearing goat | 承担代价的山羊 | 第 47 行 secondary classification |
| responsibility laundering | 责任洗白 | 第 41 行关键句"The grammar is the laundering" |
| responsibility chain | 责任链 | 八问诊断 + 结尾段落 |
| record-control | 记录控制 | 八问第六问 |
| five-role conflation | 五角色融合 | 第 79 行 callout to Ch 7 |
| alibi | 托辞 | 全书贯穿 |
| interception | 拦截 | 第 94 行"72-hour interception window" |
| procedural shell | 程序外壳 | 第 108 行"the procedural shell tightens" |
| discovery | 证据开示 | 第 58 行法律程序上下文——作为已有术语（第 5 章首次建立） |
| record-hardening | 记录固化 | 间接概念 |

## 跨章一致性关键点

### 1. 八问诊断的平行句式
第 9 章在三层结构中多次运行八问诊断。八个问题的中文必须与第 3 章完全一致（已验证第 3 章 ready 文本）：

| 英文（第 3 章原始） | 中文（第 3 章 ready 文本） |
|---|---|
| Who was publicly blamed? | 谁或什么被公开归咎？ |
| Who had control? | 谁拥有控制权？ |
| Who benefited? | 谁受益？ |
| Who knew or should have known? | 谁知情或应知情？ |
| Who could have prevented recurrence? | 谁能阻止复发？ |
| Who controlled the record? | 谁控制了记录？ |
| Who bore the cost? | 谁承担了代价？ |
| What would responsibility look like if it followed control instead of visibility? | 如果责任跟随控制权而非可见度，责任会是什么样子？ |

### 2. 回旋镖术语一致性
- **Therac-25**（第 2 章）— "Malfunction 54"和"TREATMENT PAUSE"在第 2 章已有中文处理方式，需跨章对齐
- **MCAS / 737 MAX**（第 2 章）— MCAS（Maneuvering Characteristics Augmentation System）在第 2 章已有中文
- **Horizon / 五角色融合**（第 7 章）— 五角色融合（deployer/audit-trail holder/complainant/prosecutor/disclosure controller）在第 7 章已有中文

### 3. 法律案例名翻译策略
本章的 AI 版权诉讼集群（Bartz, Getty, Authors Guild, NYT v. OpenAI）全部是当前或近期诉讼，需要在中文翻译中保留英文案名的精确性。译者将会按全书规范处理（斜体保留英文，首次出现括号附中文描述性案名）。

## 交接

Handoff: Glossary Master（请裁决 15 条提案）
Priority: 高 — 第 9 章的 15 条提案中 6 条为核心分析框架术语（输入层/部署层/评估层/谄媚行为/托辞升级/系统施事语法），这些术语在译文开始前需要有 glossary 裁决
Pending: 裁决后 Translation Director 分派译者
