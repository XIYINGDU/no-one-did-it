---
name: quality-gate
description: Generic multi-dimensional quality review framework. Use when verifying any deliverable against declared standards — evidence grading, claim checking, overreach detection, schema compliance.
---

# Quality Gate — Decision Framework

## Purpose

Provide a repeatable, falsifiable quality-review method that any Reviewer or Adversarial Reviewer agent can apply to any deliverable. The framework produces findings with explicit severity (HARD/SOFT), each traceable to a specific standard.

## When to use

- Reviewer: before signing off on a deliverable as promotion-ready
- Adversarial Reviewer: before concluding a red-team pass
- Producer: during self-review before handoff

## When NOT to use

- When the deliverable is still in early draft and the Producer explicitly requests "rough feedback, not formal review"
- When no quality standards have been declared for the project — define standards first

## The five review dimensions

For each dimension, the reviewer checks every load-bearing element of the deliverable:

### 1. Evidence / source support

- Does every load-bearing claim cite a source?
- Is the source's grade (A/B/C/D) appropriate to the claim's weight?
- If the claim is C-grade, is the uncertainty visible in the deliverable?
- **HARD if:** a load-bearing claim has no source, or the source contradicts the claim.

### 2. Overclaim / overreach

- Does any verb assert knowledge, intent, causation, or guilt without citation?
- Does structural placement (sentence sequence, paragraph adjacency, focalization) imply what the sources don't support?
- **HARD if:** a load-bearing claim overstates its evidence grade. **SOFT if:** a non-load-bearing sentence could be tighter.

### 3. Counterargument presence

- Does every major claim acknowledge its strongest counterargument?
- Is the counterargument stated fairly (steelmanned) before being addressed?
- **HARD if:** a major claim has no counterargument and one obviously exists. **SOFT if:** the counterargument is present but could be stronger.

### 4. Schema / structure compliance

- Does the deliverable include all required schema fields?
- Is the `Handoff:` field populated with a named next owner?
- Are evidence grades, assumptions, and open questions declared?
- **HARD if:** required schema fields are missing or the handoff is unnamed.

### 5. Internal consistency

- Does the deliverable contradict itself?
- Does it contradict other deliverables in the same project?
- Are taxonomy categories or classifications used consistently?
- **HARD if:** a contradiction affects a load-bearing claim. **SOFT if:** a minor inconsistency exists in non-load-bearing framing.

## Severity classification

```text
HARD = claim unsupported by cited source
     | required citation missing
     | quality standard violated
     | core-value regression
     | overreach surface on load-bearing claim
     | internal contradiction on load-bearing claim

SOFT = stylistic issue
     | non-load-bearing claim could be tighter
     | citation form inconsistency
     | counterargument present but could be stronger
     | minor inconsistency in non-load-bearing framing
```

## Decision tree

```
For each load-bearing element:
  1. What is the claim?
  2. What is the cited source? (If none → HARD)
  3. What is the source's evidence grade (A/B/C/D)?
  4. Does the claim's certainty match the evidence grade? (If overclaim → HARD)
  5. Is the strongest counterargument named? (If missing → HARD or SOFT depending on claim weight)
  6. Is the schema complete? (If missing required field → HARD)
  7. Is the element internally consistent? (If contradiction → HARD or SOFT depending on weight)

Output: finding list with severity per finding.
```

## Promotion recommendation

```text
go        = zero HARD findings
no-go     = one or more HARD findings
conditional = zero HARD, but SOFT findings exist that should be addressed in the next cycle
```

## Escalation

If Reviewer and Producer disagree on a HARD finding, escalate to Orchestrator. The Orchestrator decides or escalates to the project owner. No agent may silently overrule another agent's HARD finding.

## Edge cases

- **Deliverable references an external source not in the project's source ledger:** SOFT — flag for inclusion; do not block promotion unless the claim is load-bearing and the source is unverifiable.
- **Producer self-reviews and claims zero findings:** Reviewer must independently verify at least a sample of claims. Self-review is a gate, not a substitute for independent review.
- **Adversarial Reviewer and Reviewer disagree on severity:** Orchestrator consolidates. If the disagreement is on a HARD finding, the more severe classification wins.
