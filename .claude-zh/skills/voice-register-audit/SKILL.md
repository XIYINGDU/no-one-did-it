---
name: voice-register-audit
description: 审计章节的三种声音语域分布——R-primary（一手文件以完整力度引用）、R-frame（新闻室风格释义）、R-analytic（书籍的分析性声音）。验证段落级语域标签存在、分布处于可调阈值内、语域转换被标记而非无声。
version: 1.0.0
---

# 声音语域审计

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## 三种语域

| 语域 | 标签 | 权威来源 |
|---|---|---|
| **R-primary** | `<!-- voice: R-primary -->` | 所引用的文件本身 |
| **R-frame** | `<!-- voice: R-frame -->` | 其发现被释义的报道者/调查/法院 |
| **R-analytic** | `<!-- voice: R-analytic -->` | 作者的分析框架 |

## 决策标准

一章通过当：(1) ≥90% 实质性段落携带语域标签；(2) 无语域低于 10% 或高于 70%；(3) 相邻不同语域段以显式转换提示分隔；(4) R-primary 内容通过 rule 06；(5) R-frame 内容通过 rule 05；(6) R-analytic 内容通过 rule 12 V8。

## 关键规则

章节开头语域选择信号章节声音意图——R-primary 开头（以文档开场）是偏好默认。Beat 10 必须是 R-analytic。Beat 8 必须是 R-analytic。识别节拍必须在 R-analytic 中。段内语域混合是硬失败。双标签段落是硬失败。
