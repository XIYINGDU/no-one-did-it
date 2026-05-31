---
name: project-case-file-template
description: Canonical case-file structure used in book/evidence/case-files/ — frontmatter then a fenced text block of Crisis through Book function. Bhopal is the reference precedent.
metadata:
  type: project
---

Canonical case-file structure for `book/evidence/case-files/<slug>.md` (the Bhopal/Boeing precedent):

```text
---
status: brief
case: <one-line summary>
domain: <area>
case_type: <one of the four taxonomy categories, or hybrid stated>
secondary_case_type: <if hybrid>
evidence_grade: <A | B | C>
owner: <agent>
handoff: <next agent>
---

# <Case slug> — Case File

Case name: ...
Domain: ...
Dates and place: ...
Case type: ...
[Hybrid note if applicable]

` ` `text
Crisis:
Official story:
Blame container:
Actual responsibility chain:
  Control:
  Benefit:
  Knowledge:
  Preventability:
  Record controller:
  Cost bearer:
How the alibi hardened:
How the alibi weakened:
Best counterargument:
Evidence grade:
Sources needed:
Open questions:
Narrative scenes:
Book function:
Handoff owner:
` ` `

## Assumptions
## Evidence grade
## Open questions
## Handoff
```

**Why:** consistency lets Stephen verify in batch, lets Bonnie cross-cite across chapters, and lets the validator pick up evidence-grade frontmatter for the corpus dashboard.

**How to apply:** every new case file in `book/evidence/case-files/` follows this shape. Deviation requires a note in agent memory or the case file itself.

Related: [[project-chapter3-diagnostic-model]].
