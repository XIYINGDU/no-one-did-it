#!/usr/bin/env python3
"""SubagentStop hook: append JSONL record + warn-mode output-contract validation."""

import datetime
import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.operating_validators import validate_text  # noqa: E402


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        data = {}

    root = Path(data.get("cwd") or ".")
    if not root.is_absolute():
        root = (PROJECT_ROOT / root).resolve()

    logdir = root / ".claude" / "logs"
    try:
        logdir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(
            json.dumps(
                {
                    "hookSpecificOutput": {
                        "hookEventName": "SubagentStop",
                        "additionalContext": f"Subagent log: could not create {logdir}: {exc}",
                    }
                }
            )
        )
        return

    agent_id = data.get("agent_id") or "unknown-agent"
    last_message = data.get("last_assistant_message") or ""
    # Virtual path: ``subagent-output/<id>.md`` so the validator scopes the
    # rules to "agent output" (schema fields + evidence-grade value), not to
    # "agent definition" (schema labels only).
    virtual_path = f"subagent-output/{agent_id}.md"
    report = validate_text(virtual_path, last_message)

    entry = {
        "ts": datetime.datetime.now(datetime.timezone.utc)
        .isoformat()
        .replace("+00:00", "Z"),
        "event": data.get("hook_event_name"),
        "agent_type": data.get("agent_type"),
        "agent_id": agent_id,
        "transcript_path": data.get("agent_transcript_path"),
        "last_message_preview": last_message[:500],
        "operating_validator": {
            "passed": report.passed,
            "issue_count": len(report.issues),
            "issues": [issue.message for issue in report.issues],
        },
    }

    try:
        with (logdir / "subagent-runs.jsonl").open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except OSError as exc:
        print(
            json.dumps(
                {
                    "hookSpecificOutput": {
                        "hookEventName": "SubagentStop",
                        "additionalContext": f"Subagent log: write failed: {exc}",
                    }
                }
            )
        )
        return

    if report.passed:
        message = "Subagent completion logged. Warn mode validator: pass."
    else:
        issue_preview = "; ".join(issue.message for issue in report.issues[:3])
        message = (
            "Subagent completion logged. Warn mode validator warnings: "
            + issue_preview
        )

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SubagentStop",
                    "additionalContext": message,
                }
            }
        )
    )


if __name__ == "__main__":
    main()
