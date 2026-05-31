---
name: feedback-installing-chapter-rule
description: Rule for placing hybrid taxonomy cases — installing chapters get clean labels, pattern chapters get hybrids
metadata:
  type: feedback
---

# Installing-chapter rule for hybrid cases

**Rule.** When a chapter's load-bearing job is to *install* a taxonomy (ch-2 in this book), anchor cases must be single-category. Hybrid cases — cases that legitimately read as more than one category at different chain levels — belong in *pattern* chapters (Part II), not installing chapters.

**Why:** Readers learn categories by contrast first, then meet ambiguity. If the installing chapter teaches "the categories are fuzzy", every downstream pattern chapter inherits the fuzziness and the diagnostic loses its bite. Rule 01 (case-taxonomy) explicitly permits hybrids when "named as such" — but the *permission* is about not silently mixing; it is not a recommendation to put hybrids in load-bearing installing slots.

**How to apply:**
- For ch-2 ("The Four Goats") and any future installing chapter: anchor candidates with `secondary_case_type:` set in frontmatter are flagged for review. Either (a) demote to echo, (b) move to a pattern chapter where the secondary layer is on-thesis, or (c) keep with explicit "we use this as primary-category teaching example; here's the secondary reading we set aside" framing in rhythm slot 3.
- For Part II pattern chapters (ch-4 through ch-7): hybrid cases are welcome and often stronger than single-layer cases, because they show the diagnostic running across chain levels.
- Russell-on-Sacco-Vanzetti is a *within-case* counterargument, not a re-classification — it belongs in rhythm slot 6 of the chapter using the case, not in the architectural decision.

**Tested against:** 2026-05-25 anchor decision for ch-2 — kept Sacco/Vanzetti as pure-scapegoat anchor (Russell → counterargument slot), moved Bhopal to ch-5 because the Anderson partial-scapegoat layer is on-thesis there.
