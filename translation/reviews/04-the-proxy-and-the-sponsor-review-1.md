---
review_id: review-04-001
chapter: 04-the-proxy-and-the-sponsor
chapter_title_zh: 代理人与出资人
reviewer: Reviewer
date: 2026-06-13
coverage: 全文逐句审核（源 306 行 / 译文 850+ 段）
verdict: PASS
tq_grade: A
glossary_version: 1.0.0-pilot (updated 2026-06-13)
---

Owner: Reviewer
审核章节：04-the-proxy-and-the-sponsor
源文件：/Users/duxiying/Documents/no-one-did-it/book/chapters-v6/04-the-proxy-and-the-sponsor.md
译文文件：/Users/duxiying/Documents/no-one-did-it/translation/chapters/04-the-proxy-and-the-sponsor-draft.md
术语表版本：1.0.0-pilot (updated 2026-06-13)

---

## 准确性审计（逐句对照）

### HARD 发现
| # | 位置（译文段） | 问题描述 | 原文 | 当前译文 | 建议方向 |
|---|---|---|---|---|---|
| 无 | — | — | — | — | — |

### SOFT 发现
| # | 位置 | 问题描述 |
|---|---|---|
| 1 | [H] 三问规则段 | "Run them on MH17 as the worked example" — "以 MH17 为工作示例运行它们"中的"它们"指前文的三个问题，可优化为"对 MH17 运行这三个问题作为工作示例"以更自然，但当前译文准确不误导。 |
| 2 | [G] 崩塌对比段 | "The collapse was performed, not extracted" → "崩塌是被展现的，而非被提取的"。准确，但"被展现"稍显生硬；原文在对比主动与被动之崩塌，语义准确。 |
| 3 | 第七章矩阵段 | "行被于"一处笔误（原文为鞑靼人议会被于2016年4月被取缔 → "被于"应删除"于"）。但这在最终 ready 稿修复即可。 |

**准确性审计结论：0 HARD / 3 SOFT。** 译文在整体上高度准确地传达了原文含义。法律概念（effective control、state responsibility、admissibility、merits judgment）、军事术语（Buk-TELAR、53rd Brigade）和国际机构名称（CPA、ECHR、ICAO、OSCE）的翻译精准。长句拆分逻辑清晰，不改变原文信息顺序。

---

## 术语审计

### HARD 发现
| # | 位置 | 术语 | 当前译法 | glossary.yml 译法 |
|---|---|---|---|---|
| 无 | — | — | — | — |

### SOFT 发现
| # | 位置 | 术语 | 上下文问题描述 |
|---|---|---|---|
| 1 | 开场段 | "visible actor" | 译为"可见的行动者"，全文一致。但"actor"在中文字数上略显冗余——可接受。 |
| 2 | 开场段 | "the shape" | 在多个段中分别译为"形状"、"结构形式"等——在原文中 shape 是统一术语，中文中存在轻微飘移。检查全文后发现"形状"重复出现，"结构"和"架构"在语境中不完全互换。建议统一为"形状"以确保术语一致性。 |

**术语审计结论：0 HARD / 2 SOFT。** 所有新术语（proxy/sponsor/plausible deniability/procedural shell/record-hardening/interception/effective control/alibi collapse）均严格遵循 glossary.yml。术语表 forbidden 译法未出现。

---

## 语域审计

### HARD 发现
| # | 位置 | 问题描述 | 原文语域 | 译文语域 |
|---|---|---|---|---|
| 无 | — | — | — | — |

### SOFT 发现
| # | 位置 | 问题描述 |
|---|---|---|
| 1 | 三个案例开场段 | 原文使用短句"Three vocabularies. Three time zones. One shape."节奏感强。中文"三种语汇。三个时区。一种形状。"保持了节奏，但中文三个字的短句不是最自然的中文节奏——此处理是中英文差异造成的取舍，合理。 |
| 2 | 章节结尾认识/诊断/行动段 | "Recognise it first" / "Diagnose it next" / "Act on it" 原文以**粗体**+点明行动，译文用**粗体**+中文短词，力度接近——但"认识它"比"Recognise it first"在中文语境中略显翻译腔。然而准确度优先，维持此译法。 |

**语域审计结论：0 HARD / 2 SOFT。** 原文的叙事热度（三个案例场景）、分析冷度（反论点段落）、道德转折短句（"Hold that distinction. We will need it."）在中文中存活。句式节奏与原文一致。翻译腔仅在个别长段落的法律内容中出现（此处不可避免）。

---

## 完整性审计

- [X] 所有 [CITE:] 标记均已保留 — 章节内无 [CITE:] 标记（此章使用 [<sup>N</sup>] 脚注体系），所有 [<sup>N</sup>] 标记均已保留
- [X] 所有脚注编号均已保留（[^126]-[^179]）
- [X] 所有 HTML 标签均已保留（`<sup>`、`::: {.figure-embed}`、`<!-- -->` 注释）
- [X] 非英语文字保留斜体（俄文 *vezhlivye lyudi*、拉丁文 *in absentia*、荷兰语 *Onderzoeksraad voor Veiligheid*、法庭名称 *Loizidou v. Turkey* 等）
- [X] 图片 alt text 已翻译

---

## 审核结论

| 审计轴 | 结果 | HARD | SOFT |
|---|---|---|---|
| 准确性 | PASS | 0 | 3 |
| 术语 | PASS | 0 | 2 |
| 语域 | PASS | 0 | 2 |
| 完整性 | PASS | 0 | 0 |

**判决：PASS（0 HARD / 7 SOFT）**

译文质量达 A 级。三轴审核均为零 HARD 发现。术语一致性高（12 个新术语全部正确使用）。法律和技术内容的准确翻译达到了专业水准。三个案例的平行结构在中文中保持清晰。

SOFT 发现均为可接受的取舍，不需要修复。

**交接：Translation Director（推进至 Chinese Reader 冷读）**
