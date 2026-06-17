# 翻译质量等级 — A/B/C/D 四级评分系统

**每条译文在其获得 ready 状态之前，必须被 Reviewer 评定翻译质量等级。**

## 翻译质量等级（TQ-Grade）

### A — 精良
Reviewer 三轴零 HARD，SOFT 合计 ≤ 3，Chinese Reader 零 HARD 且信任轴无任何发现。

- 译文在精确性、术语一致性和语域保留方面均达到可出版标准
- 剩余的 SOFT 发现为语感层面的微调，不构成理解和信任障碍

### B — 合格
Reviewer 三轴零 HARD，SOFT 合计 ≤ 10，Chinese Reader 零 HARD。

- 译文准确、术语合规、语域存活
- 存在记录在案的取舍——每次 SOFT 发现即是一个声明过的取舍
- 这是 ready 的标准等级

### C — 需返工
Reviewer 零 HARD 但 SOFT > 10，或 Chinese Reader 报告 HARD 发现。

- 累积的微小摩擦达到了需要返工的门槛
- 或：中文读者在冷读中遇到了理解障碍
- 不可进入 ready

### D — 阻断
Reviewer 任一轴存在 ≥ 1 HARD 发现。

- 译文存在意义错误、术语使用禁止译法、或语域严重漂移
- 章节被阻断，不可推进

## 等级判定流程

```
Reviewer 审核完成
  → HARD > 0? → D（阻断）
  → HARD = 0?
    → SOFT > 10? → C（需返工）
    → SOFT ≤ 10?
      → Chinese Reader 冷读
        → Reader HARD > 0? → C
        → Reader HARD = 0?
          → 信任轴有发现? → 检查
          → SOFT ≤ 3 + 信任轴无发现? → A
          → SOFT 4-10? → B
```

## 等级与 ready 的对应

| 等级 | ready | 含义 |
|---|---|---|
| A | ✓ | 可出版，优先合稿 |
| B | ✓ | 合格，可合稿 |
| C | ✗ | 需返工 |
| D | ✗ | 阻断 |

## 判定者

等级由 **Reviewer** 在所有审核轴完成后判定，记录在审核报告的判决栏中。判定者署名——这是追责链的一部分。
