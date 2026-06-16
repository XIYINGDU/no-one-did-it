---
description: 指定图表、表格或责任链图示——可视化什么以及如何框架化。Bonnie 拥有；数据由 Stephen 分级，标题由 Wayne 撰写，仅当指名任何人时由 Nancy 进行法律审查。见 rule 03"视觉材料所有权"。
owner: bonnie-book-architect
argument-hint: "<chapter-slug-or-what-to-show>"
---

# Figure Spec

派遣 `bonnie-book-architect` agent，任务：为章节指定图表、表格或责任链图示——决定可视化什么以及如何框架化，若图示为控制 / 利益 / 知情 / 可预防性映射，使用 `responsibility-chain-mapping`。

图示是证据，而非装饰。规格必须指明：该图示使哪个单一声明或关系变得可读；图示类型（图表 / 表格 / 链图）；所需的数据点或链节点；以及它所服务的章节节拍。Bonnie 仅拥有规格——她不拥有数据（Stephen 按 rule 02 为每个值分级）、标题措辞（Wayne，在 rules 05 和 07 下）或渲染。以 Handoff 结尾：Stephen 为数据分级，然后 Wayne 撰写标题，仅当图示指名在世个人或公司时由 Nancy 审查。图示用 Mermaid 渲染，表格用 Markdown 渲染；两者位于 `book/evidence/diagrams/`。见 rule `03`"视觉材料所有权"。

<example>
Context: 第 04 章论证公开归责远离了控制所在。Bonnie 被要求指定一幅使差距可读的图示。
user: /figure-spec 04 control-vs-blame
assistant: 指定一幅双列责任链图示——左列"谁被公开归责"，右列"谁持有控制 / 利益 / 知情 / 可预防性"——指明其所需的四个链节点，标记每个节点 [data: Stephen] 以待分级，以 Handoff: Stephen（分级四个节点）→ Wayne（标题）→ Nancy（审查：右列指名了两位在世高管）结尾。
</example>
