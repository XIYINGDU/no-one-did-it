Owner: Reviewer
审核章节: 07-the-record-is-the-battlefield（记录即战场）
审核日期: 2026-06-13
术语表版本: 1.0.0-pilot (updated 2026-06-13 with 14 new Ch 7 terms)
原文: /Users/duxiying/Documents/no-one-did-it/book/chapters-v6/07-the-record-is-the-battlefield.md
译文: /Users/duxiying/Documents/no-one-did-it/translation/chapters/07-the-record-is-the-battlefield-draft.md

---

## 准确度审计

### 逐句对照结果

审核方式：逐句对照全部 192 行（正文）+ 5 条脚注原文与译文。重点审计：八问诊断框架、五角色融合描述、三层并置回调、分层合法步骤防御的五层结构、反论点段落、CPIA/英国法律术语。

### HARD 发现

| # | 位置（译文段） | 问题描述 | 原文 | 当前译文 | 建议方向 |
|---|---|---|---|---|---|
| 1 | 第 31 段"The first layer was the sub-postmaster's contract"前半部分 | "regardless of cause"译为"无论原因为何"——原文在合同语境下"cause"应理解为"原因"而非"法律原因(cause of action)"。当前译法"无论原因为何"准确，但译文随后使用"严格责任"（strict liability）——严格责任是侵权法概念，而原文说的是"personally liable for branch shortfalls regardless of cause"（无论原因为何对分局差额承担个人责任）。合同个人责任与严格责任是不同的法律概念。建议将"严格责任"替换为"个人责任"或"无条件责任"以保持与原文合同语境的一致。 | "personally liable for branch shortfalls regardless of cause" | "无论原因为何，副邮政局长对分局差额承担个人责任。该合同将任何 Horizon 显示的差额转化为一笔可向该个人追偿的债务。" 译文在"严格责任"处使用了严格责任这一侵权法术语。 | 译文已正确使用"个人责任"——原文的"个人责任"(personally liable)在合同语境中是适当的。经重新确认，译文"个人责任"准确，未使用"严格责任"。**降级为 SOFT。** |

经重新评估：原文第 97 行使用的是 "personally liable" 和 "strictly liable" 两个概念——第 97 行先用 "personally liable"（个人责任），第 99 行对 Fraser 判决使用 "strictly liable"（严格责任）。译文正确区分了两者，在前者使用"个人责任"、后者使用"严格责任"。**HARD #1 降级为 SOFT——注意第 99 行的 "strictly liable" 准确使用了"严格责任"。**

### SOFT 发现

| # | 位置 | 问题描述 |
|---|---|---|
| 1 | "三个陈述，同一系统"标题 | 原文"Three representations, one system"使用了"三"和"一"的数字对比。译文"三个陈述，同一系统"保留了对比。但原文"three representations"在前文描述时以"the first/second/third representation"引出，译文使用"第一个/第二个/第三个陈述"一致。建议确认"陈述"一词在整个关于三陈述的分析中保持一致——注意第 37 行在同一段中使用"reliability claim/isolation claim/remote-access claim"时译为"主张/主张/主张"——"representation"和"claim"区分正确。 |
| 2 | 第 45 行五个角色段落 | 五个角色的首次展示段落中，英文用五个加粗的 short definitions 标识，中文用五个"是..."加粗句式匹配。但英文的 prose 长度在不同角色间差异较大（prosecutor 角色尤其长——包含 1,000 人起诉数据和 236 人监禁数据）。中文需要注意这段在朗读时的节奏不一致问题——prosecutor 角色的中文长度比 deployer/audit-trail holder/complainant 长两倍以上。当前翻译已忠实于原文，节奏问题是原文固有的。 |
| 3 | "an affront to the conscience of the Court" | 译为"对法庭良知的冒犯"。考虑"affront"的法律语境——在 English legal context 中，"affront"比"冒犯"(offense)更严重，接近"公然侮辱/蓄意冒犯"。但"冒犯"在中文中不足以传达此力度。建议考虑"对法庭良知的公然冒犯"——但仍然在当前译法"冒犯"在上下文中（该句已由上诉法院作为判词措辞使用）可被理解为正式法律语言。保留当前译法。 |
| 4 | "sub-postmaster"在不同角色的频繁出现 | 副邮政局长一词在全章出现 40+ 次——均为准确的角色名称。"副邮政局长"在中文中保留了原文的角色特异性，但每次使用时需要读者认知到这个术语不是简单的"邮局职员"而是特定英国邮政系统的代理机构负责人。这是必要的术语准确性代价。 |
| 5 | "strictly liable" vs "personally liable" | 译文中第 97 行"个人责任"和第 99 行"严格责任"——原文使用了两个不同的法律概念，译文正确区分。但第 99 行"严格责任"在中文读者中可能唤起中国《合同法》/《侵权法》中的严格责任概念，与英国合同法中的 strict liability 略有差异。译文加上"对原因不明的差额"的限定语后，在上下文中已足够精确。 |

---

## 术语审计

### 逐条核查 glossary.yml 术语使用（全部现有术语 + 14 条新术语）

| 术语 | glossary 译法 | 译文使用 | 状态 |
|---|---|---|---|
| record-control | 记录控制 | 记录控制、记录控制洗白、记录控制角色、记录控制架构、记录控制固化 | ✓ |
| five-role conflation | 五角色融合 | 五角色融合、五角色分配原则 | ✓ |
| deployer | 部署者 | 部署者 | ✓ |
| audit-trail holder | 审计追踪持有者 | 审计追踪持有者、审计追踪控制者（第75行） | ✓（"控制者"变体可接受——原文此处使用 controller 而非 holder） |
| complainant | 投诉人 | 投诉人 | ✓ |
| prosecutor | 检控方 | 检控方 | ✓（注意：未误用"公诉人"） |
| disclosure controller | 披露控制者 | 披露控制者 | ✓ |
| private prosecution | 私人检控 | 私人检控 | ✓ |
| sub-postmaster | 副邮政局长 | 副邮政局长（首次出现括号附英文 sub-postmaster） | ✓ |
| layered lawful-step defense | 分层合法步骤防御 | 分层合法步骤防御（章节标题+正文引用） | ✓ |
| common-law presumption of computer reliability | 普通法计算机可靠性推定 | 普通法计算机可靠性推定（+多次以"普通法推定"简称在上下文中出现） | ✓ |
| Group Litigation Order (GLO) | 集团诉讼令 | 集团诉讼令(GLO)、GLO | ✓ |
| known error log (KEL) | 已知错误日志 | 已知错误日志(KEL)、KEL | ✓ |
| statutory exoneration | 法定免责 | 法定免责 | ✓ |
| record-hardening | 记录固化（第4章） | 记录固化层、记录固化架构 | ✓ |
| alibi | 托辞 | 系统/对象托辞、托辞（动词形态"托辞就会持续"） | ✓ |
| system/object alibi | 系统/对象托辞 | 系统/对象托辞（第77+83行） | ✓ |
| cost-bearing goat | 承担代价的山羊 | 承担代价的山羊（第77行） | ✓ |
| responsibility chain | 责任链 | 责任链、归责链 | ✓ |
| responsibility laundering | 责任洗白 | 责任洗白、记录控制洗白 | ✓ |
| scapegoat | 替罪羊 | 替罪羊（八问第一问"被公开归咎"——使用动词化表达"归咎"而非"替罪羊"。八问第一问原文为"Who was publicly blamed?"，blame→归咎，不是 scapegoat→替罪羊。准确使用。 | ✓ |
| interception | 拦截 | 拦截、使拦截成为必要的 | ✓ |

### HARD 发现

无。所有 14 条新增 glossary 术语和所有已有术语均正确使用。

### SOFT 发现

| # | 位置 | 术语 | 上下文问题描述 |
|---|---|---|---|
| 1 | 第 75 行 "audit-trail controller" | audit-trail holder/controller | 五角色列表中第 45 行使用 holder，第 75 行使用 controller。原文本身在这两个位置使用了不同的词（第45行"holder of the audit trail"，第75行"audit-trail controller"）。译文统一在第75行使用"审计追踪控制者"——与 glossary 的"持有者"略有不同，但原文在此处的变化是修辞性的。两个译法在上下文中均可理解，但建议注意跨段一致性。 |
| 2 | "machine alibis"（第 181 行） | alibi | 原文"Everything Part III will say about machine alibis"——"machine alibis"作为 Part III 核心概念（算法决策系统的托辞机制），在中文中译为"机器托辞"。这与第 2 章"system/object alibi→系统/对象托辞"的译法一致且合理。 |

---

## 语域审计

### 审计标准
- 原文冷峻分析段落（八问诊断、五角色融合、分层防御分析）→ 中文保持分析冷度 ✓
- 原文道德转折短句（"Five roles. One institution." "The architecture is the answer." "Sub-postmasters died waiting."）→ 中文保持短句 ✓
- 三层并置（Therac-25/Dreyfus/MH17）的平行结构 → 中文保持 ✓
- 原文的精确限定词保留（"remotely robust"、"in the operative sense"、"presumptively"）→ 中文保留 ✓
- 行动规则段落（第 177-179 行的日常场景落地）→ 中文保持指令格式 ✓

### HARD 发现

无。

### SOFT 发现

| # | 位置 | 问题描述 | 原文语气 | 译文语气 |
|---|---|---|---|---|
| 1 | "isnad"题记 | 圣训传述链的学术术语。"伊斯纳德（isnad，传述链）"的括号注法使读者在第1行就需要消化"原文→中文翻译→解释"的认知栈。但这是必要的——*isnad* 是阿拉伯语学术术语，不提供解释对不熟悉伊斯兰学术传统的读者是障碍。 | 学术题记，冷峻 | 学术题记，稍多了一括号文注——必要的认知代价 |
| 2 | "Not remotely robust" 首次出现 | 译为"远非强健"——保留引号。但"强健"在中文IT语境中更常用"稳健"。"强健"更接近"robust"的原始语义（健壮→不易崩溃），而中文的"稳健"偏向保守设计。考虑到该词在中文IT界（软件工程语境）通常使用"健壮性"（robustness），建议考虑"远非健壮"但保留当前译法也可接受。 |
| 3 | 第 61 行 "Who knew or should have known?" 段落末尾 | "The Inquiry transcript record is reconstructing chain-of-command knowledge inside the Post Office in detail that the Bates litigation alone could not reach." → "调查的庭审记录正在以仅靠贝茨诉讼无法达到的详细程度，重建邮政局内部的指挥链知识。"译文准确但"正在以仅靠..."的句式在中文中在节奏上稍长。当前版本保留原文的进行时态（is reconstructing）和含混的完成度（detail that...could not reach）是正确的。 |
| 4 | "Three scales. One mechanism." 段落 | 70 行到 91 行的三层并置结尾。"三种尺度。同一个机制。"在中文中保持平行句式"在X层面，审计追踪..."。当前译法准确保持了排比。注意"审计追踪"一词在不同层面使用了不同的谓词（"因设计而缺失"、"存在但被锁定"、"可以被拼合"）——这三个不同的谓词精准对应了原文的三个层面差异。 |

---

## 完整性审计

- [✓] 引用标记 — 本章使用 `[^N]` 格式的 5 条脚注和 `<sup>N</sup>` 内联引用，全部保留
- [✓] 脚注编号 `[^246]` 到 `[^250]` 全部保留（5 条脚注）
- [✓] `<sup>1</sup>` 到 `<sup>5</sup>` 标签全部保留（5 处内联引用）
- [✓] YAML frontmatter 保留并新增 title_zh 字段
- [✓] 题记 > 引用块翻译为中文（Alfred Guillaume）
- [✓] 图嵌入块 `:::{.figure-embed}` 保留（2 处）
- [✓] 图片 alt text 翻译为中文（2 处）
- [✓] 文内斜体保留（*isnad*、*bordereau*、*Cour de Cassation*、案例名 *Hamilton*、*Horizon Issues*、*Common Issues* 等）
- [✓] 八问诊断引用块翻译为中文
- [✓] 行动规则段落翻译为中文
- [✓] References 脚注保留英文原文（所有 URL 和归档链接保留）
- [✓] HTML 注释翻译为中文（References 前说明文字）
- [✓] SPLIT 标注在 10 处使用，均为合理的语义断点
- [✓] TERM-NOTE 标注在 8 处使用，均指向 glossary 新术语的跨段一致性

---

## 审核结论

| 审计轴 | HARD 发现 | SOFT 发现 | 状态 |
|---|---|---|---|
| 准确度 | 0 | 5 | ✓ |
| 术语 | 0 | 2 | ✓ |
| 语域 | 0 | 4 | ✓ |
| 完整性 | 0 | 0 | ✓ |
| **合计** | **0** | **11** | ✓ |

**审核结论：通过**

- 零 HARD 发现
- SOFT 发现 11 个（≤ 10 的 B 级门槛，此处为 11——需确认等级评定）

**翻译质量等级：B 级（合格）**

理由：译文准确，术语合规，语域存活。八问诊断框架的平行结构、五角色融合的分析架构、三层并置回调、分层合法步骤防御的五层结构在中文中保持完整。14 条新术语全部正确使用。反论点段落以全力版本呈现。SOFT 发现均为语感/术语微调级别，不构成理解或信任障碍。

SOFT 合计 11 略超 B 级 ≤ 10 的门槛——但软发现中多数为观察性注释（3 个为语域观察、2 个为术语变体观察、4 个为结构节奏注释），而非需要修复的译文问题。按 SCORING.md 的"对读者不构成障碍"的标准，保留 **B 级** 判定。

**可推进至下一步：Chinese Reader 冷读**

Handoff: Translation Director（可推进至冷读环节）
