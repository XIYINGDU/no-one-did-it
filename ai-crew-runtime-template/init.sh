#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# AI Crew Runtime Template — Initialization Script
# ============================================================
#
# Adapts the generic 7-layer template to your specific project.
# Replaces all {{PLACEHOLDER}} tokens with your project's values.

# ---- Defaults ----
PROJECT_NAME=""
PROJECT_DESCRIPTION=""
DOMAIN="general"
LANG="en"

# Agent names (customizable)
ORCHESTRATOR_NAME="orchestrator"
ORCHESTRATOR_DISPLAY_NAME="Orchestrator"
PRODUCER_NAME="producer"
PRODUCER_DISPLAY_NAME="Producer"
REVIEWER_NAME="reviewer"
REVIEWER_DISPLAY_NAME="Reviewer"
RED_TEAM_NAME="red-team"
RED_TEAM_DISPLAY_NAME="Adversarial Reviewer"

# Core values (customizable)
VALUE_1="Evidence before elegance. Never improve the output by weakening the evidence."
VALUE_2="Responsibility follows control, benefit, knowledge, and preventability. Do not stop at the most visible actor."
VALUE_3="Keep the taxonomy intact. Distinguish categories; do not collapse them for narrative convenience."
VALUE_4="Steelman before judgment. Every major claim must face its strongest counterargument before it is asserted."
VALUE_5="Handoff cleanly. Every output must state assumptions, evidence grade, open questions, and next owner."

STATUS_FILE="STATUS.md"

# ---- Parse arguments ----
while [[ $# -gt 0 ]]; do
  case "$1" in
    --name)
      PROJECT_NAME="$2"; shift 2 ;;
    --description)
      PROJECT_DESCRIPTION="$2"; shift 2 ;;
    --domain)
      DOMAIN="$2"; shift 2 ;;
    --lang)
      LANG="$2"; shift 2 ;;
    --orchestrator)
      ORCHESTRATOR_NAME="$2"; shift 2 ;;
    --producer)
      PRODUCER_NAME="$2"; shift 2 ;;
    --reviewer)
      REVIEWER_NAME="$2"; shift 2 ;;
    --red-team)
      RED_TEAM_NAME="$2"; shift 2 ;;
    --value1)
      VALUE_1="$2"; shift 2 ;;
    --value2)
      VALUE_2="$2"; shift 2 ;;
    --value3)
      VALUE_3="$2"; shift 2 ;;
    --value4)
      VALUE_4="$2"; shift 2 ;;
    --value5)
      VALUE_5="$2"; shift 2 ;;
    --status-file)
      STATUS_FILE="$2"; shift 2 ;;
    --help|-h)
      cat <<EOF
Usage: ./init.sh [OPTIONS]

Initialize the AI Crew Runtime template for your project.

Required:
  --name NAME              Project name
  --description DESC       One-line project description

Optional:
  --domain DOMAIN          Project domain (default: general)
  --lang LANG              Language code (default: en)
  --orchestrator NAME      Orchestrator agent name (default: orchestrator)
  --producer NAME          Producer agent name (default: producer)
  --reviewer NAME          Reviewer agent name (default: reviewer)
  --red-team NAME          Adversarial reviewer name (default: red-team)
  --value1 "..."            Override core value 1
  --value2 "..."            Override core value 2
  --value3 "..."            Override core value 3
  --value4 "..."            Override core value 4
  --value5 "..."            Override core value 5
  --status-file FILENAME   Project status file (default: STATUS.md)
  --help, -h               Show this help

Examples:
  ./init.sh --name "My Book" --description "A nonfiction book about systems" --domain book
  ./init.sh --name "Code Review System" --description "Automated code review pipeline" --domain code-review --producer developer --reviewer code-auditor
EOF
      exit 0 ;;
    *)
      echo "Unknown option: $1 (use --help for usage)"
      exit 1 ;;
  esac
done

# ---- Validate ----
if [[ -z "$PROJECT_NAME" ]]; then
  echo "ERROR: --name is required. Use --help for usage."
  exit 1
fi

if [[ -z "$PROJECT_DESCRIPTION" ]]; then
  echo "ERROR: --description is required. Use --help for usage."
  exit 1
fi

# ---- Confirm ----
echo "════════════════════════════════════════════"
echo "  AI Crew Runtime — Initialization"
echo "════════════════════════════════════════════"
echo ""
echo "  Project:       $PROJECT_NAME"
echo "  Description:   $PROJECT_DESCRIPTION"
echo "  Domain:        $DOMAIN"
echo "  Language:      $LANG"
echo ""
echo "  Orchestrator:  $ORCHESTRATOR_NAME"
echo "  Producer:      $PRODUCER_NAME"
echo "  Reviewer:      $REVIEWER_NAME"
echo "  Red Team:      $RED_TEAM_NAME"
echo ""
echo "  Target dir:    $(pwd)"
echo ""

if [[ ! -d ".claude" ]]; then
  echo "ERROR: .claude/ directory not found in current directory."
  echo "Run this script from your project root after copying the template files."
  exit 1
fi

read -rp "Proceed with initialization? [y/N] " confirm
if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
  echo "Aborted."
  exit 0
fi

# ---- Token replacement function ----
replace_tokens() {
  local file="$1"

  # macOS sed requires a backup extension; use '' for in-place
  local sed_inplace=(-i '')
  if [[ "$(uname)" != "Darwin" ]]; then
    sed_inplace=(-i)
  fi

  sed "${sed_inplace[@]}" \
    -e "s|{{PROJECT_NAME}}|${PROJECT_NAME}|g" \
    -e "s|{{PROJECT_DESCRIPTION}}|${PROJECT_DESCRIPTION}|g" \
    -e "s|{{DOMAIN}}|${DOMAIN}|g" \
    -e "s|{{LANG}}|${LANG}|g" \
    -e "s|{{ORCHESTRATOR_NAME}}|${ORCHESTRATOR_NAME}|g" \
    -e "s|{{ORCHESTRATOR_DISPLAY_NAME}}|${ORCHESTRATOR_DISPLAY_NAME}|g" \
    -e "s|{{PRODUCER_NAME}}|${PRODUCER_NAME}|g" \
    -e "s|{{PRODUCER_DISPLAY_NAME}}|${PRODUCER_DISPLAY_NAME}|g" \
    -e "s|{{REVIEWER_NAME}}|${REVIEWER_NAME}|g" \
    -e "s|{{REVIEWER_DISPLAY_NAME}}|${REVIEWER_DISPLAY_NAME}|g" \
    -e "s|{{RED_TEAM_NAME}}|${RED_TEAM_NAME}|g" \
    -e "s|{{RED_TEAM_DISPLAY_NAME}}|${RED_TEAM_DISPLAY_NAME}|g" \
    -e "s|{{STATUS_FILE}}|${STATUS_FILE}|g" \
    -e "s|{{VALUE_1}}|${VALUE_1}|g" \
    -e "s|{{VALUE_2}}|${VALUE_2}|g" \
    -e "s|{{VALUE_3}}|${VALUE_3}|g" \
    -e "s|{{VALUE_4}}|${VALUE_4}|g" \
    -e "s|{{VALUE_5}}|${VALUE_5}|g" \
    "$file"
}

# ---- Phase 1: Replace tokens ----
echo ""
echo "Phase 1: Replacing {{PLACEHOLDER}} tokens..."

files_to_process=(
  "AGENTS.md"
  ".claude/agents/orchestrator.md"
  ".claude/agents/producer.md"
  ".claude/agents/reviewer.md"
  ".claude/agents/red-team.md"
  ".claude/commands/status.md"
  ".claude/commands/quality-gate.md"
  ".claude/rules/00-core-values.md"
  ".claude/state/current-focus.md"
  ".claude/docs/architecture.md"
  ".claude/docs/role-map.md"
  ".claude/docs/workflow.md"
  "templates/STATUS.md"
  "templates/DELIVERABLE.md"
  "templates/DECISION_LOG.md"
)

count=0
for file in "${files_to_process[@]}"; do
  if [[ -f "$file" ]]; then
    replace_tokens "$file"
    count=$((count + 1))
    echo "  ✓ $file"
  else
    echo "  ⚠ $file (not found, skipped)"
  fi
done
echo "  → Processed $count files."

# ---- Phase 2: Sync core values ----
echo ""
echo "Phase 2: Syncing core values to all target files..."

if [[ -f "scripts/sync_core_values.py" ]]; then
  python3 scripts/sync_core_values.py || echo "  ⚠ sync_core_values.py encountered issues — check output above"
else
  echo "  ⚠ sync_core_values.py not found — skipping auto-sync"
fi

# ---- Phase 3: Make hooks executable ----
echo ""
echo "Phase 3: Making hooks executable..."
chmod +x .claude/hooks/*.py 2>/dev/null || true
echo "  ✓ Hooks are now executable"

# ---- Phase 4: Initialize state ----
echo ""
echo "Phase 4: Initializing project state..."

# Set current date
TODAY=$(date +%Y-%m-%d)

# Update current-focus.md with real values
cat > .claude/state/current-focus.md <<STATEFILE
# Current Focus

**Sprint:** Initial setup — project just initialized on ${TODAY}.

## Active work

- [ ] Define the first deliverable and create its STATUS.md row
- [ ] Producer: create the first deliverable
- [ ] Orchestrator: establish sprint cadence

## Recent completions

- Template initialized for **${PROJECT_NAME}**

## Blocked / waiting

None yet.

## Upcoming deadlines

None yet.

---

> This file is read by \`session-context.py\` at SessionStart and injected as \`additionalContext\` into every fresh session. Keep it short — one screen. Update at sprint start and at handoffs.
STATEFILE
echo "  ✓ state/current-focus.md initialized"

# ---- Phase 5: Validate ----
echo ""
echo "Phase 5: Running workspace validation..."

if [[ -f "scripts/validate_workspace.py" ]]; then
  python3 scripts/validate_workspace.py --quick || echo "  ⚠ Validation found issues — review output above"
else
  echo "  ⚠ validate_workspace.py not found — skipping validation"
fi

# ---- Done ----
echo ""
echo "════════════════════════════════════════════"
echo "  Initialization complete!"
echo "════════════════════════════════════════════"
echo ""
echo "  Project:    $PROJECT_NAME"
echo "  Domain:     $DOMAIN"
echo "  Agents:     $ORCHESTRATOR_NAME, $PRODUCER_NAME, $REVIEWER_NAME, $RED_TEAM_NAME"
echo "  State file: $STATUS_FILE"
echo ""
echo "Next steps:"
echo "  1. Review .claude/agents/ — customize role descriptions if needed"
echo "  2. Review .claude/rules/00-core-values.md — make values project-specific"
echo "  3. Define your first deliverable in $STATUS_FILE"
echo "  4. Start a new Claude Code session — SessionStart hook will inject state"
echo "  5. Try /status to see your project state"
echo ""
