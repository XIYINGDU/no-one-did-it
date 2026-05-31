# Example Counter-Case Card — Fill Before Drafting

Counter-case: UK sub-postmasters / Horizon convictions overturned
Paired scapegoat case: post-office-horizon
Domain: public administration / software / legal process
Interception type: system/object alibi pierced
Evidence grade: A

Use this as a formatting example only. Do not treat it as a completed counter-case file. The `Evidence grade: A` shown above is illustrative — a real counter-case earns its grade through Stephen's verification gate against the documented record (court judgments, public-inquiry findings, audited technical reports for grade A).

## Directory and naming convention

Counter-case files live alongside their paired scapegoat case file in `book/evidence/case-files/`. The naming convention is paired by slug:

- Scapegoat case file: `book/evidence/case-files/<slug>.md`
- Counter-case file:   `book/evidence/case-files/<slug>-counter.md`

Example:

- `book/evidence/case-files/post-office-horizon.md`           (scapegoat case)
- `book/evidence/case-files/post-office-horizon-counter.md`   (paired counter-case — UK convictions overturned)

This co-location is deliberate: every chapter that consumes a scapegoat case must also consume its counter-case for beat 9 ("the escape"). Pairing them in one directory means the chapter brief author cannot forget the counter-case exists.

## Counter-case file structure

```text
Counter-case name:
Paired scapegoat case:
Domain:
Dates and place:

Laundering attempt:
  Pattern (from Cross_Pattern_Matrix.md):
  Goat-candidate:
  Alibi being constructed:

Interception mechanism:
  Type: whistleblower / inquiry / independent technical verification / journalism / court / civil-society pressure / record durability / jurisdictional persistence
  Named institutional actor:
  Key act of interception:
  Date of interception:

Amplifiers (supporting mechanisms, not load-bearing):

Cost of escape:
  Time from laundering to interception:
  Reputational, financial, or career cost to the goat-candidate during the laundering:
  Cost absorbed by cost-bearers who could not wait:
  Cost to the intercepting actor:

Outcome:
  Full reversal / partial reversal / recognition without remedy / accountability for some / accountability for none:

Transferable lesson (one sentence, diagnostic not motivational):
Limits of the lesson (where this counter-case does NOT generalise):
Best counterargument:
Evidence grade:
Sources:
Handoff:
```

## Absence findings

If after a focused search no counter-case exists for the paired scapegoat pattern, the file still gets written — as an **absence finding**. Naming convention is the same (`<slug>-counter.md`), but the body documents the search:

```text
Counter-case name: [Absence finding for <pattern>]
Paired scapegoat case:
Status: no qualifying counter-case found
Search scope (domains and periods examined):
Closest analogues considered (and why each was rejected):
Implication for the chapter (what beat 9 says when the answer is "nobody escaped this pattern"):
Handoff:
```

Absence is itself a finding the book uses. A chapter whose pattern has no documented escape says so explicitly — that absence becomes part of beat 9, not a reason to skip the beat.

## Rules

- The counter-case must come from the **same laundering pattern** as its paired scapegoat case. A proxy-deniability counter-case for a proxy-deniability scapegoat case; a record-control counter-case for a record-control scapegoat case. A counter-case from a different pattern teaches the wrong lesson.
- Do not romanticise the intercepting actor. The mechanism is the lesson, not the heroism.
- Do not claim a counter-case where the reversal happened through luck, regime change unrelated to the laundering, or the death of the original blamers.
- See `.claude/skills/counter-case-method/SKILL.md` for the full method, evidence rubric, escalation conditions, and worked examples.
