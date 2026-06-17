---
owner: orchestrator
argument-hint: <deliverable-id>
description: Run the full quality gate on a deliverable — reviewer pass + adversarial pass + promotion decision.
example: |
  /quality-gate deliverable-03
---

For the specified deliverable:

1. Dispatch `reviewer` to run a full quality-verification pass — claim-by-claim evidence grading, source checking, standards compliance.
2. Dispatch `red-team` to run an adversarial pass — strongest counterargument, overreach detection, gap exposure.
3. Consolidate findings. If both Reviewer and Adversarial Reviewer return no HARD findings, promote to `ready`. If either returns a HARD finding, return to Producer with findings and record the halt.
4. Update `STATUS.md`.
