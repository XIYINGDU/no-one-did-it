---
review_id: R02-002
chapter: 02-the-four-goats
reviewer: Reviewer
date: 2026-06-12
coverage: 全章（621 行译文）— 15 项修复验证
verdict: PASS
grade: A
---

Owner: Reviewer
审核章节：02 — The Four Goats / 四种山羊
源文件：book/chapters-v6/02-the-four-goats.md
译文文件：translation/chapters/02-the-four-goats-draft.md
术语表版本：1.0.0-pilot（含新增 doctrine/doctrinal 条目）
修复记录：translation/decision-log/02-the-four-goats/resolutions.yml（15 项：1 HARD + 14 SOFT，全部 fixed）

---

## 修复验证总表

本章共 15 项审核发现（1 HARD + 14 SOFT），全部已在 `resolutions.yml` 中记录修复方案并在译文文件中实施。本报告对每项修复进行逐项验证。

### HARD 修复验证

| 发现 | 问题 | 修复方向 | 验证结果 |
|---|---|---|---|
| HARD-01 | "doctrine/doctrinal" 系统性地误译为「教条」（dogma 贬义），全章至少10处 | 军事语境→「条令」/ 法律/制度语境→「原则」 | **PASS** — 零「教条」残留 |

### SOFT 修复验证

| 发现 | 位置 | 修复方向 | 验证结果 |
|---|---|---|---|
| SOFT-01 | 开场 Therac-25 段 | "named" → 同位语结构 | **PASS** |
| SOFT-02 | 「托辞登上层级阶梯」段 | 语序重构 | **PASS** |
| SOFT-03 | 同段 "shift" | 「变化」→「递变」 | **PASS** |
| SOFT-04 | 「戴德姆，1921年」段 "turned on itself" | 「对自己发起了攻击」→「反噬了自身」 | **PASS** |
| SOFT-05 | 同段 "close the public record" | 「了结」→「关闭」 | **PASS** |
| SOFT-06 | "proximate cause" | 统一为「近因」 | **PASS** |
| SOFT-07 | "on its own terms" | 「条件」→「逻辑」 | **PASS** |
| SOFT-08 | "bright lines" | 「亮线」→「明确界线」 | **PASS** |
| SOFT-09 | "removal policy" | 删除无原文依据的「强行」 | **PASS** |
| SOFT-10 | 「辨认它」段长句（60+字） | 破折号拆分 | **PASS** |
| SOFT-11 | 「行动」段三重平行结构 | 「对于身处...的我们中的那些人」精简 | **PASS** |
| SOFT-12 | "Redress Scheme" | 「补救计划」→「赔偿计划」 | **PASS** |
| SOFT-13 | 图注 "blame is moved off" | 「移开」→「转移」 | **PASS** |
| SOFT-14 | "from the start" | 「从一开始」→「从第1章」 | **PASS** |

**15/15 全部修复验证通过，零残留。**

---

## 准确性审核

### HARD

无。

### SOFT

无（全部原 SOFT 发现已修复）。

---

## 术语审核

### HARD

无。

### SOFT

无。

**术语合规清单（glossary.yml 对照）：**

| glossary 条目 | 译文中使用 | 合规 |
|---|---|---|
| scapegoat → 替罪羊 | ✓ | PASS |
| responsibility laundering → 责任洗白 | ✓ | PASS |
| pure scapegoat → 纯粹替罪羊 | ✓ | PASS |
| partial scapegoat → 部分替罪羊 | ✓ | PASS |
| system/object alibi → 系统/对象托辞 | ✓ | PASS |
| cost-bearing goat → 承担代价的山羊 | ✓ | PASS |
| alibi → 托辞 | ✓ | PASS（forbidden 译法零出现） |
| substitution → 替代 | ✓ | PASS |
| cost → 代价 | ✓ | PASS（未使用 prohibited「成本」） |
| bearing → 承担 | ✓ | PASS |
| responsibility chain → 责任链 | ✓ | PASS（未使用 forbidden「责任链条」） |
| doctrine → 条令/原则 | ✓ | PASS（新增术语，严格区分语境） |
| 所有 forbidden 译法 | — | 零违规 |

---

## 语域审核

### HARD

无（原 HARD 发现与准确性 HARD-01 同源，已随其修复）。

### SOFT

无。

**语域整体评估：**
修复后的译文在三个语域维度均保持原文质量：
- **叙事热度：** 开场场景短句重量存活（"他于九月去世"）
- **分析冷度：** doctrine 系列修复后，原文的制度性分析语域完全恢复，不再被贬义干扰
- **道德转折：** 「反噬了自身」保留了原文的内省重量；「认证流程不是一个人」的锤击句完整

---

## 完整性检查

- [x] 所有 `[CITE:]` 标记均已保留
- [x] 所有脚注编号均已保留（[^22]～[^87]）
- [x] 所有 `<sup>` HTML 标签均已保留
- [x] 非英语文字保留斜体
- [x] 引用块正确翻译
- [x] 图片 embed 标签保留，alt text 已翻译
- [x] 题记格式保留
- [x] References 脚注定义保留英语原文（按规范）
- [x] Frontmatter 完整且已更新（tq_grade: A）
- [x] glossary.yml 已更新（doctrine/doctrinal 条目）

---

## 等级判定

根据 SCORING.md：

| 条件 | 结果 |
|---|---|
| HARD = 0 | ✓ |
| SOFT ≤ 3 | ✓（0 SOFT） |
| **最终等级** | **A — 精良** |

### 判决

**PASS — 0 HARD / 0 SOFT**

**等级：A**

译文在精确性、术语一致性和语域保留方面均已达到可出版标准。所有审核发现均已修复，无残留问题。

**后续建议：** 按 SCORING.md 完整流程，建议安排 Chinese Reader 冷读以确认信任轴无发现。如 Chinese Reader 报告零 HARD，可正式确认 A 级；如有发现，由 Reviewer 和 Translation Director 共同判断是否影响等级。

---

**交接：** Translation Director — 确认 A 级判定，更新状态表。
