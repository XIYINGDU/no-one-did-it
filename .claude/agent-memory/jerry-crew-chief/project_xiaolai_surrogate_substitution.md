---
name: project-xiaolai-surrogate-substitution
description: Under the goal-hook "finish all chapters" (set 2026-05-26), the xiaolai-surrogate agent substituted for the human principal at chapter-ready beat-10 sanity sign-off; the human read remains a separate gate.
metadata:
  type: project
---

# xiaolai-surrogate substitution pattern (goal-hook era)

**Decision:** when the user set `/goal "finish all chapters"` on 2026-05-26, the chapter-promotion flow's final-gate substitution rule was: xiaolai-surrogate stands in for the human principal at the beat-10-sanity / reversal-sentence-coherence sign-off step, so Jerry can promote a chapter to `status: ready` without blocking on the human's calendar.

**Why:** the goal hook was a session-scoped Stop hook that blocked Jerry from stopping until all 13 chapters reached `status: ready`. The human-principal final-read step would have blocked every chapter and broken the goal. The surrogate carries the principal's reasoning frame (Six Values-Over-Rules: independence; first-principles; AI-leverage calibration; evidence-over-elegance; steelman; responsibility-chain check) and audits the chapter against them. It does not substitute for authority over commits, pushes, scope expansions, or strategic pivots — those still surface to the principal.

**How to apply:**

1. **`status: ready` under surrogate** is a structural-soundness claim, not a publication claim. The chapter has cleared the four agent gates (Stephen / Alan / Laura / Nancy) and the surrogate's beat-10 sanity. It has NOT cleared the human principal's final read.
2. **STATUS.md marks `✓ (surrogate)`** in the Principal column when surrogate cleared; `✓` without parens means the human read cleared too. ch-02 is the only chapter in the book with a human-read sign-off (Wave 1, before the goal hook). The other 12 are surrogate-cleared.
3. **Pre-publication discipline:** human principal final read is item 4 in `.claude/state/current-focus.md` post-chapter sprint. The book is not "done" by `book/STATUS.md` exit condition until that read clears.
4. **What the surrogate cannot do:** authorize a deviation from the chapter card or brief; authorize a counter-case insertion that the brief did not call for; authorize a scope change to the book's spine; authorize a commit message that claims more than the surrogate-cleared scope.
5. **What the surrogate did do, across Waves 2–4:** confirm each chapter's reversal-sentence is intact and italicized; confirm beat 9 and beat 10 are present and not generic; confirm the chapter does not break the book's voice; confirm the chapter's pure-scapegoat anchor (where load-bearing) meets the Dreyfus-shaped gate per `[[project_downstream_pure_scapegoat_gate]]`.

**Tested against:** Waves 2, 3, 4 — 11 chapters total promoted under surrogate substitution. Zero rollbacks; zero principal-overruled promotions to date.

**Risk:** if the human principal disagrees with a surrogate sign-off on a chapter, the chapter reverts to `status: draft` for re-work; this has not happened but the flow is built to absorb it (STATUS.md is the state board; the chapter's frontmatter is the operative gate).
