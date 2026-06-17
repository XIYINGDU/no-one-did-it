# Production Workflow

## Deliverable lifecycle

Every deliverable walks through these stages:

```
Draft → Self-Review → Peer Review → Adversarial Review → Final Gate → Ready
```

### Stage descriptions

| Stage | Owner | Action |
|-------|-------|--------|
| **Draft** | Producer | Creates initial deliverable following quality standards |
| **Self-Review** | Producer | Checks own work against the quality checklist; fixes mechanical issues |
| **Peer Review** | Reviewer | Verifies quality against standards; assigns evidence/source grades; flags issues |
| **Adversarial Review** | Adversarial Reviewer | Attacks the deliverable to find weaknesses; constructs strongest counterargument; checks for overreach |
| **Final Gate** | Orchestrator | Verifies all review findings resolved; checks state consistency; promotes to `ready` |

### Promotion gates

A deliverable cannot advance to `ready` while:

1. Any unresolved HARD finding from Reviewer
2. Any unresolved HARD finding from Adversarial Reviewer
3. State file shows stale review memo dates
4. Required schema fields are incomplete

### Halt and override

The Reviewer and Adversarial Reviewer can halt promotion independently of the dispatch chain. Only the project owner can override a halt. Overrides are recorded with reason.

## State tracking

`STATUS.md` is the single orchestration status board. Each deliverable has a row with stage columns. The orchestrator reads it to determine the next incomplete stage. Cross-session recoverable: the board is the truth source, not in-memory state.

`state/current-focus.md` is the sprint-level snapshot — active work, blocked items, upcoming deadlines. `session-context.py` hook injects it as additional context at SessionStart.

## Handoff protocol

Every deliverable ends with:

```text
Handoff: <next-owner> — <next-action>
```

Cross-cell handoffs are explicit and recorded. No implicit handoff. No unowned intermediate state.
