# Workflow Lifecycle — Workflow Layer

**Every deliverable entering a review cycle transitions through declared states; prior review reports archive before new reviews run.**

## Status flow

A deliverable's status follows this state machine:

```text
draft
  └─→ in-self-review   (Producer completes self-review checklist)
        └─→ in-peer-review (handed off to Reviewer)
              └─→ in-adversarial-review (handed off to Adversarial Reviewer)
                    └─→ ready (promoted only after all HARD findings resolved)
                    └─→ in-self-review (re-opened if any HARD finding)
```

Transitions:

- `draft → in-self-review`: Producer completes the quality checklist and flips the self-review flag.
- `in-self-review → in-peer-review`: Producer hands off to Reviewer.
- `in-peer-review → in-adversarial-review`: Reviewer returns no HARD findings; hands off to Adversarial Reviewer.
- `in-adversarial-review → ready`: Adversarial Reviewer returns no HARD findings; Orchestrator promotes.
- Any stage → `in-self-review`: Reverted on any HARD finding, with recorded reason.

## Review archive

Before any new review pass overwrites a prior review report on the same deliverable, the prior report is archived. Archives are never deleted during a review cycle — they are the rollback unit.

## Promotion gate

A deliverable cannot return to `ready` if:

1. Any HARD finding from Reviewer remains unresolved
2. Any HARD finding from Adversarial Reviewer remains unresolved
3. The deliverable's last-edit date is newer than its most recent review report
4. Required schema fields are incomplete

## Why this rule exists

Without declared states and archival, a review cycle silently overwrites prior review work and breaks the chain of custody on quality decisions. With declared states, every step is recoverable and every downstream artifact knows whether it is current or stale.
