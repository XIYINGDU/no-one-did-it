---
description: "单一责任人角色表：在以 jerry-crew-chief 为根、深度 ≤ 2 的有界 DAG 中，谁拥有什么，谁将工作路由给谁。"
---

**任何 agent 不得无声地僭取另一个 agent 的权限；跨角色工作必须经过 `Handoff:` schema 字段中记录的交接。**

# 不可重叠角色表

- Book Architect 拥有结构——包括图表和表格的规格（可视化什么以及如何框架化）——而非散文、事实核查或法律判断。
- Narrative Lead 拥有章节语言，而非来源发现或最终事实状态。
- Research Director 拥有研究系统，而非最终散文或法律措辞。
- Domain Researchers 拥有各自领域内的来源包，而非书籍结构。
- Fact-check Director 拥有验证，而非论证设计。
- Red-team Editor 拥有对抗性批评，而非最终案例入选。
- Legal Counsel 拥有法律风险措辞以及图像权利和标题并置的通过/否决关卡，而非真相判定。
- Expert Reviewer 仅拥有专业领域审查，而非散文控制。
- Market Strategist 拥有提案定位 + 公共词汇，而非论文命题。
- The Reader 拥有受众对出版物形式（`book/chapters-v3/`、`dist/manuscript-v3.md`）的亲身体验，而非散文、结构、事实、法律或任何修复。它是唯一一个刻意*不在* crew 中的 agent；它冷读并报告体验。参见 rule `15-reader-experience-authority.md`。

## 视觉材料所有权（图表、表格、图解、照片）

视觉材料是证据。图表的每个数字都是一个可分级的声明；照片的标题可以通过并置来洗涤一条责任链。因此，视觉材料通过和散文相同的证据和法律关卡（rules 02、05、06、07）——它们没有豁免的"艺术部门"。crew 不为此新增 agent；所有权分配给现有角色，**每种材料类型有一个指名的关卡负责人**，这样责任就不会扩散成本书所诊断的那种模式。

### 图表、表格和责任链图解

| 步骤 | 负责人 | 边界 |
|---|---|---|
| 可视化什么以及如何框架化（规格） | **Bonnie**（Book Architect） | "视觉框架"已是她的职责范围；她拥有 `responsibility-chain-mapping`。她不拥有数据、标题措辞或渲染。 |
| 图表背后的数据 / 数字 | **Stephen**（Fact-check） | 每个值都是一个带有证据等级的主张（rule 02）；图表不能以未分级的数据交付。 |
| 标题 / 标签 / 题目措辞 | **Wayne**（Narrative Lead） | 受 rule 05（过度声明）和 rule 07（隐含负担）约束。 |
| 法律审查——仅当图表指涉在世个人或公司时 | **Nancy**（Legal Counsel） | 与散文相同的诽谤风险面。 |

图解、图表和表格存放于 `book/evidence/diagrams/`。根据 workshop 文档规则，用 Mermaid 渲染图解，用 Markdown 渲染表格。

### 照片（包括由多张图像编织而成的合成图）

照片带有 crew 此前未曾处理过的责任面——来源出处、许可授权和标题并置。为防止这个面在四个角色之间分裂而无人负责，**Nancy 是单一的关卡负责人**：没有她在权利和标题上的通过/否决，任何照片不得交付。其他角色为关卡提供输入。

| 步骤 | 角色 | 边界 |
|---|---|---|
| 寻找候选图像 | 拥有该案例的 **domain researcher**（Shirley/Selina/Warren/Loki） | 了解案例和档案；提供候选和来源线索，不负责审查。 |
| 来源出处 / 真实性验证 | **Stephen**（Fact-check） | 这真的是它所声称描绘的事件照片吗？错误归属是主要陷阱；按 rule 02 分级。 |
| 标题措辞 | **Wayne**（Narrative Lead） | 并置（照片放在某主张旁边）即使在没有动词过度声明时也承担 rule-07 的隐含负担。 |
| **权利、许可、授权和标题审查——通过/否决** | **Nancy**（Legal Counsel） | 指名的关卡负责人。图像许可是她在 rule 06 下已有引用许可权限的精确类比；她将许可记录在来源账本行中，如同对待引文一样。 |
| 合成 / 编辑排版（将多张图像编织为一张） | **agent crew 之外的生产步骤** | 在人类/编排者层面执行的设计/排版任务，而非由 crew agent 执行。crew 拥有选择、验证、标题撰写和审查——而非页面排版。 |

照片（当存在时）存放于 `book/evidence/photos/`，其来源账本行与章节的其他引用锚点并存。

## 调度所有权（谁将工作路由给谁）

委托关系图（见 `scripts/check_agent_graph.py`）是一个有界 DAG，以 `jerry-crew-chief` 为根，最大深度为 2。路由决策是有意为之的：

| 父节点 | 子节点 | 原因 |
|---|---|---|
| `jerry-crew-chief` | `bonnie-book-architect`、`wayne-narrative-lead`、`delon-research-director`、`stephen-fact-check-director`、`laura-red-team-editor`、`nancy-legal-risk-counsel`、`blair-market-strategist` | 7 个 cell lead / 交叉控制者。Jerry 将工作路由给拥有下一步骤的 lead。 |
| `delon-research-director` | 4 位 domain researchers（Shirley/Selina/Warren/Loki） | Delon 分配研究；研究人员执行。直接管道。 |
| `stephen-fact-check-director` | `alan-expert-reviewer` | 专业领域审查是**领域感知的验证**：Alan 对照日内瓦/罗马规约检查战争罪归属，对照系统卡检查 AI 主张，对照事故调查方法论检查系统故障因果叙述。这些是验证问题，而非对抗性批评。Stephen（验证）是正确的父节点，而非 Laura（红队——检查整个论证的过度声明和类别坍缩）。 |

`wayne-narrative-lead`、`bonnie-book-architect`、`laura-red-team-editor`、`nancy-legal-risk-counsel` 和 `blair-market-strategist` 被有意设计为叶子节点——他们的工作成果由 Jerry（或交接链中的下一个 agent）整合，而非通过衍生子 agent。叶子之间的交接通过 `Handoff:` schema 字段传播，而非通过嵌套的 `Agent()` 调用。

## 独立否决权（仅限改写周期）

在 rule `08-treatment-class-discipline.md` 下声明的任何章节改写周期中，两位 agent 拥有独立于调度链运作的否决权：

| Agent | 否决触发条件 | 效果 |
|---|---|---|
| `laura-red-team-editor` | 在红队审查中检测到 rule-12 核心价值 V1（获得而非制造）、V3（同情跟随责任链）或 V8（无内部洗涤）的倒退。 | 中止受影响章节的改写周期；在 Laura 的发现被解决或升级至 xiaolai 以便推翻之前，该章节无法从 `in-review` 转为 `ready`。 |
| `nancy-legal-risk-counsel` | 改写引入的、被现有审计链遗漏的 rule-05（过度声明）或 rule-07（隐含负担）风险面；或活跃内容声明上的 rule-12 V7（严重性与证据不匹配）。 | 相同效果：中止周期；只有 xiaolai 可以推翻。 |

否决在章节的审计历史快照中记录为拒绝审查（rule 09）。xiaolai 的推翻记录连带理由。没有 rule 09 的归档，否决就无法强制执行，因此这两条规则是配对的。

该否决权不扩展到非改写的章节工作；标准的通过 `jerry-crew-chief` 的调度链在此适用。
