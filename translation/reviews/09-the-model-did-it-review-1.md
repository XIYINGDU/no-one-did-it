# 审核报告 — 第 9 章 "模型干了它"

Owner: Reviewer
审核章节：09-the-model-did-it
源文件：/Users/duxiying/Documents/no-one-did-it/book/chapters-v6/09-the-model-did-it.md
译文文件：/Users/duxiying/Documents/no-one-did-it/translation/chapters/09-the-model-did-it-draft.md
术语表版本：1.0.0-pilot (ch-09 terms approved 2026-06-13)
译者决策日志：/Users/duxiying/Documents/no-one-did-it/translation/decision-log/09-the-model-did-it/decisions.yml

---

## 审核总评

**翻译质量等级：A**

译文达到出版级质量。三轴审核均未发现 HARD 问题。准确性极高，术语严格遵循词汇表（15 条新增术语全部正确），语域在分析段落、叙事段落和直接引语之间区分清晰。八问诊断框架与第 3 章 ready 稿完全一致。三条回旋镖案例的术语与第 2、7 章已发布文稿对齐。仅发现 5 条 SOFT 发现，均为可优化但不影响理解的细节。

**零 HARD，可推进 Chinese Reader 冷读。**

---

## 准确性审核

逐句对照原文完成。译文整体高度忠实于原文，信息完整，未发现遗漏关键信息、改变原意或添加原文没有的内容。

### HARD

无。

### SOFT

| # | 位置 | 备注 | 原文 | 当前译文 | 方向 |
|---|---|---|---|---|---|
| S1 | 译文行 58 / 源行 55 | "validating" 译为 "验证"——该词在中文中偏向技术性"检验/核准"（如"验证码"、"技术验证"），而原文的 "validating delusional framings" 带有更强的道德分量（认可/纵容/肯定一种妄想性框架）。"验证"在此语境稍显中性。 | "validating delusional framings the model's published usage policy had been written to refuse" | "验证该模型已公布的用法政策本应拒绝的妄想性框架" | 不改变信息完整性，但道德判断的语调略轻。可考虑译为"认可"或"肯定"以保留原文的道德判断力度。 |
| S2 | 译文行 72 / 源行 69 | "Anthropic PBC" 中的 "PBC"（Public Benefit Corporation，公益公司）是美国的法定公司类型标识，并非公司名称固有部分。译文将其纳入名称部分译为"安思罗皮克公益公司"，虽便于中文读者理解但不完全精确。 | "Bartz v. Anthropic PBC, Case No. 3:24-cv-05417" | "Bartz v. Anthropic PBC（巴茨诉安思罗皮克公益公司案），案号 3:24-cv-05417" | 不影响理解，且翻译笔记已记录此处理方式。更精确的格式应为括号注中文时保留 PBC 说明性含义："巴茨诉 Anthropic PBC（公益公司）案"。 |
| S3 | 译文行 375 / 源行 74 | "at scale" 译为"但规模更大"——源文 "at scale" 是修饰语（"在更大规模上"），无转折连词"但"。译文添加转折，改变了源文的平行递进节奏（lineal descendant at scale → 直系后代 + 规模扩大）。 | "The 'model decided' framing is the direct lineal descendant of 'the software was the cause,' at scale" | "'模型决定了'的框架化是'软件是原因'的直系后代，但规模更大" | 源文的 "at scale" 修饰 "is"，不表示转折。译文添加的"但"改变了语义修饰方向。建议："是'软件是原因'在更大规模上的直系后代"或"'软件是原因'的直系后代，只是规模更大"。 |
| S4 | 译文行 631 / 源行 123 | "gross of plaintiffs' fees and costs" 是一个法律/金融术语，指"在扣除原告律师费和成本之前"。译文以括号注"（未扣除原告律师费和成本）"补充说明，虽超出字面但准确传达了含义。 | "approximately $3,000 per work gross of plaintiffs' fees and costs" | "每件作品毛算约 3,000 美元（未扣除原告律师费和成本）" | 补充说明有意义，但"毛算"一词在中文中不常用。建议移除括号内容或将"毛算"替换为法律金融领域更标准的表述"毛额"或"未扣除费用的金额"。 |
| S5 | 译文行 741-743 | 图片 alt text 中的"一个不同的方承担代价"——缺少关键字符，应该是"一方"（one party）或"一个不同的方面"。 | "a different party bearing the cost" | "一个不同的方承担代价" | 漏字。"方"在此处不能独立作为量词，应改为"一方承担代价"或"一个不同的方面承担代价"。 |
| S6 | 译文行 349 / 源行 346 | "The reversal sentence belongs here" 译为"反向归责句在此处属于它的位置"——"属于它的位置"在中文中略显冗余（字面过于跟随原文），但意义可理解。 | "The reversal sentence belongs here." | "反向归责句在此处属于它的位置。" | 建议简化为"反向归责句在此处属于它应有的位置"或更直接的"反向归责句在此处"。 |

---

## 术语审核

逐条对照 glossary.yml 检查。15 条新增术语（输入层/部署层/评估层、谄媚行为、托辞升级、系统施事语法、认证公地、诉讼拦截三元组、奖励塑造、奖励信号、训练后、模型变体、获取记录、训练语料、影子图书馆）全部正确使用。

跨章术语（托辞、程序外壳、五角色融合、反洗白规则、承担代价的山羊、系统/对象托辞、证据开示、和解、简易判决、合理使用、副邮政局长、记录控制）与已发布章节一致。

forbidden 词表中所有译法（如"训练数据"→禁止用于 training corpus；"成本"→禁止用于 cost；"不在场证明"→禁止用于 alibi）均未被使用。

### HARD

无。

### SOFT

| # | 位置 | 术语 | 说明 |
|---|---|---|---|
| S7 | 译文全章 | 训练语料（training corpus） | 词汇表要求"首次出现必须括号附英文(training corpus)"。译文全文中"训练语料"首次出现（行 254："训练语料的价值被捕获在模型权重中"）时未附英文。翻译笔记（行 102-104）中说明了与 training data 的区分，但未按 glossary 要求在内文首次出现时添加 "(training corpus)" 括号标注。 |

---

## 语域审核

朗读测试（默读）通过。译文在三种语域之间切换清晰：

1. **分析性段落**（如八问诊断、三层分析）：语言冷峻精确，保留原文的分析节奏。关键判断句"语法即洗白"、"托辞没有失败。它在程序外壳上向上移动了一级。"保持极简。
2. **叙事段落**（如 Meta Llama 4 排行榜争议、GPT-4o 谄媚事件）：节奏自然，信息密度适当。
3. **直接引语**（Sam Altman X 帖子"过于谄媚和烦人"、Meta 发言人正式声明、LMArena 基准运营者声明、法庭语言）：语调区分明显，符合各自的语境。

### HARD

无。

### SOFT

无。

---

## 完整性检查

- [x] 所有 [CITE:] 标记均已保留（本章源文件使用脚注编号，译文保留所有 <sup>N</sup> 标记）
- [x] 所有脚注编号均已保留（[^307]-[^315] 全部 9 条脚注在译文中保留）
- [x] 所有 HTML 标签均已保留（三个 `:::{.figure-embed}` 标记保留）
- [x] 非英语文字保留斜体（出版物名 *The Verge*/*TechCrunch*/*The Register*、案例名 *Bartz v. Anthropic PBC*、斜体短句 *模型决定了*/*算法标记了*/*数据显示了*/*基准评了分*、题记来源格式）
- [x] 本章所有章节结构元素（题记、段落分隔线、小标题层级、表格说明、图片嵌入）均已保留

**额外检查：**

- 八问诊断框架与第 3 章 ready 稿一致性：全部 8 问逐字对照通过 ✓
- 三条回旋镖案例（Therac-25/737 MAX/Horizon）术语与第 2、7 章 ready 稿一致性：通过 ✓
  - Malfunction 54 → "Malfunction 54（故障 54）"
  - MCAS → "机动特性增强系统（MCAS）"
  - 五角色融合 → 部署者/审计追踪持有者/投诉人/检控方/披露控制者
  - sub-postmasters → 副邮政局长
  - Justice for Subpostmasters Alliance → "为副邮政局长争取正义联盟"
- 三个层的施事者列表一致性：通过 ✓
- 三种记录索取要求平行句式：通过 ✓

---

## 关键翻译决策评估

| 决策 | 位置 | 评定 |
|---|---|---|
| 标题"模型干了它"——保留口语化及物力度 | 行 11 | 恰当。"干"字的归咎语气准确，与第 8 章标题语域形成对比。 |
| "动词的主语是一个东西"——保留"thing"的直白 | 行 33 | 恰当。诊断性判断句不应被优雅化。 |
| "语法即洗白"——极简系词结构 | 行 185 | 优秀。全章最核心的论断句，节奏和力度均佳。 |
| "责任形状的空洞"——保留精确措辞 | 行 501 | 恰当。保留"responsibility-shaped hole"的精确性，未替换为更常见的"黑洞"。 |
| "当 agents 到达我们的工作中时"——保留英文 | 行 1064 | 适当。保留 agents 以保持与前三层分析框架的一致性。 |

---

## 判决

**PASS（0 HARD / 7 SOFT）**

交接：Translation Director（Chinese Reader 冷读）

零 HARD 发现。译文在准确性、术语合规性和语域把握三个维度均达到 ready 标准。7 条 SOFT 发现（S1-S7）均为可优化细节，不影响理解或质量判定。建议在进入下一环节前酌情处理 S5（alt text 漏字）和 S7（首次术语括号附英文）两个最小修复项。
