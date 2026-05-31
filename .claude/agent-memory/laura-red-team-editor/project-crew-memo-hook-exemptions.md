---
name: project-crew-memo-hook-exemptions
description: rule-14 pronoun/meta-frame and overclaim hooks fire on intra-crew review memos; these are expected false positives per rule-14 edge-case 12
metadata:
  type: project
---

When I (or any crew agent) write a review memo under `process/review-memos/`, the PostToolUse hooks (`scan-pronoun-discipline`, `scan-overclaim`) will flag meta-frame language ("the chapter", "the book") and sometimes overclaim verbs.

**Why:** these hooks scope to `process/review-memos/` by path, but rule-14 edge-case 12 explicitly exempts intra-crew metadata — a review memo instructs about the chapter as an object under construction, so naming "the chapter"/"the book" is correct and required there. Rule 14 binds reader-facing chapter prose, not crew memos. Alan's al-Aulaqi memo (2026-05-28) carries the same exemption and noted it explicitly. The overclaim hook also matches verbs inside quoted findings / open questions (e.g. "deliberately" appearing in a quoted question), which are not claims about named persons.

**How to apply:** do not edit a review memo to satisfy these specific flags. They are warn-mode (never block). The deny path is only the chapter-promotion gate. If a flag is on actual reader-facing prose I'm quoting *to fix*, that's the chapter's problem to fix, not the memo's.
