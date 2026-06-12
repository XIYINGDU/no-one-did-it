---
name: ch-03-promotion
description: "Chapter 3 (Who Could Have Stopped It?) promoted to ready A on 2026-06-12"
metadata:
  type: project
---

Chapter 3 promoted to **ready A** on 2026-06-12.

Pipeline: Translator → Review-1 (B, 0H/3S) → Chinese Reader (4 HARD) → fixes → Review-2 (A, 0H/0S) → ready.

Key fix events:
- Review-1 H1 (CAFEE "受雇于" → "受委托于") -- fixed, verified in review-1
- Chinese Reader 4 HARD (pronoun reference, nested "的" clauses, "充分性容器" context, "系统/对象托辞" readability) -- all fixed, verified by review-2 regression check
- Review-2 cleared 3 SOFT from review-1 (对应记录→对抗记录, 操作层面的重量→操作分量, 跨越了→经受住了)

Files:
- Draft: `translation/chapters/03-who-could-have-stopped-it-draft.md` (status: ready, tq_grade: A)
- Ready: `translation/ready/03-who-could-have-stopped-it.md`
- Reviews: `translation/reviews/03-who-could-have-stopped-it-review-1.md`, `translation/reviews/03-who-could-have-stopped-it-review-2.md`
- Decisions: `translation/decision-log/03-who-could-have-stopped-it/decisions.yml`
- Resolutions: `translation/decision-log/03-who-could-have-stopped-it/resolutions.yml`
