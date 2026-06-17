#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# AI Crew Runtime 模板 — 初始化脚本（中文版）
# ============================================================
#
# 将通用 7 层模板适配到你的具体项目。
# 替换所有 {{占位符}} 标记为你的项目值。

# ---- 默认值 ----
PROJECT_NAME=""
PROJECT_DESC=""
DOMAIN="general"
LANG="zh"

# Agent 名称（可自定义）
ORCHESTRATOR_NAME="orchestrator"
ORCHESTRATOR_DISPLAY="编排者"
PRODUCER_NAME="producer"
PRODUCER_DISPLAY="执行者"
REVIEWER_NAME="reviewer"
REVIEWER_DISPLAY="审查员"
RED_TEAM_NAME="red-team"
RED_TEAM_DISPLAY="对抗性审查员"

# 核心原则（可自定义）
VALUE_1="证据先于优雅。不为了产出干净而弱化证据。"
VALUE_2="责任跟随控制权、利益、知情和可预防性。不停止在最可见的行为者。"
VALUE_3="保持分类完整。区分不同类别，不为叙事便利而混为一谈。"
VALUE_4="最强反方论证先于判断。每个重要断言必须先面对它的最强反方论证。"
VALUE_5="清晰交接。每个产出必须声明假设、证据等级、开放问题和下一个负责人。"

STATUS_FILE="STATUS.md"

# ---- 解析参数 ----
while [[ $# -gt 0 ]]; do
  case "$1" in
    --name)
      PROJECT_NAME="$2"; shift 2 ;;
    --description)
      PROJECT_DESC="$2"; shift 2 ;;
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
用法：./init.sh [选项]

初始化 AI Crew Runtime 模板到你的项目。

必填：
  --name NAME              项目名称
  --description DESC       一行项目描述

可选：
  --domain DOMAIN          项目领域（默认：general）
  --lang LANG              语言代码（默认：zh）
  --orchestrator NAME      编排者 agent 名称（默认：orchestrator）
  --producer NAME          执行者 agent 名称（默认：producer）
  --reviewer NAME          审查员 agent 名称（默认：reviewer）
  --red-team NAME          对抗性审查员名称（默认：red-team）
  --value1 "..."            覆盖核心原则 1
  --value2 "..."            覆盖核心原则 2
  --value3 "..."            覆盖核心原则 3
  --value4 "..."            覆盖核心原则 4
  --value5 "..."            覆盖核心原则 5
  --status-file FILENAME   项目状态文件（默认：STATUS.md）
  --help, -h               显示此帮助

示例：
  ./init.sh --name "我的书" --description "一本关于系统运作的非虚构书" --domain book
  ./init.sh --name "代码审查系统" --description "自动化代码审查流水线" --domain code-review --producer developer --reviewer code-auditor
EOF
      exit 0 ;;
    *)
      echo "未知选项：$1（使用 --help 查看用法）"
      exit 1 ;;
  esac
done

# ---- 验证 ----
if [[ -z "$PROJECT_NAME" ]]; then
  echo "错误：--name 是必填项。使用 --help 查看用法。"
  exit 1
fi

if [[ -z "$PROJECT_DESC" ]]; then
  echo "错误：--description 是必填项。使用 --help 查看用法。"
  exit 1
fi

# ---- 确认 ----
echo "════════════════════════════════════════════"
echo "  AI Crew Runtime — 初始化"
echo "════════════════════════════════════════════"
echo ""
echo "  项目：       $PROJECT_NAME"
echo "  描述：       $PROJECT_DESC"
echo "  领域：       $DOMAIN"
echo "  语言：       $LANG"
echo ""
echo "  编排者：     $ORCHESTRATOR_NAME"
echo "  执行者：     $PRODUCER_NAME"
echo "  审查员：     $REVIEWER_NAME"
echo "  红队：       $RED_TEAM_NAME"
echo ""
echo "  目标目录：   $(pwd)"
echo ""

if [[ ! -d ".claude" ]]; then
  echo "错误：当前目录找不到 .claude/ 目录。"
  echo "请在复制模板文件后从项目根目录运行此脚本。"
  exit 1
fi

read -rp "确认初始化？[y/N] " confirm
if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
  echo "已取消。"
  exit 0
fi

# ---- 标记替换函数 ----
replace_tokens() {
  local file="$1"

  # macOS sed 需要备份扩展名；使用 '' 进行就地编辑
  local sed_inplace=(-i '')
  if [[ "$(uname)" != "Darwin" ]]; then
    sed_inplace=(-i)
  fi

  sed "${sed_inplace[@]}" \
    -e "s|{{项目名称}}|${PROJECT_NAME}|g" \
    -e "s|{{项目描述}}|${PROJECT_DESC}|g" \
    -e "s|{{领域}}|${DOMAIN}|g" \
    -e "s|{{语言}}|${LANG}|g" \
    -e "s|{{编排者名称}}|${ORCHESTRATOR_NAME}|g" \
    -e "s|{{编排者显示名}}|${ORCHESTRATOR_DISPLAY}|g" \
    -e "s|{{执行者名称}}|${PRODUCER_NAME}|g" \
    -e "s|{{执行者显示名}}|${PRODUCER_DISPLAY}|g" \
    -e "s|{{审查员名称}}|${REVIEWER_NAME}|g" \
    -e "s|{{审查员显示名}}|${REVIEWER_DISPLAY}|g" \
    -e "s|{{红队名称}}|${RED_TEAM_NAME}|g" \
    -e "s|{{红队显示名}}|${RED_TEAM_DISPLAY}|g" \
    -e "s|{{状态文件}}|${STATUS_FILE}|g" \
    -e "s|{{原则_1}}|${VALUE_1}|g" \
    -e "s|{{原则_2}}|${VALUE_2}|g" \
    -e "s|{{原则_3}}|${VALUE_3}|g" \
    -e "s|{{原则_4}}|${VALUE_4}|g" \
    -e "s|{{原则_5}}|${VALUE_5}|g" \
    "$file"
}

# ---- 第一阶段：替换标记 ----
echo ""
echo "第一阶段：替换 {{占位符}} 标记..."

FILES_TO_PROCESS=(
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
for file in "${FILES_TO_PROCESS[@]}"; do
  if [[ -f "$file" ]]; then
    replace_tokens "$file"
    count=$((count + 1))
    echo "  ✓ $file"
  else
    echo "  ⚠ $file（不存在，已跳过）"
  fi
done
echo "  → 已处理 $count 个文件。"

# ---- 第二阶段：同步核心原则 ----
echo ""
echo "第二阶段：同步核心原则到所有目标文件..."

if [[ -f "scripts/sync_core_values.py" ]]; then
  python3 scripts/sync_core_values.py || echo "  ⚠ sync_core_values.py 遇到问题 — 请检查上方输出"
else
  echo "  ⚠ sync_core_values.py 不存在 — 跳过自动同步"
fi

# ---- 第三阶段：使 hooks 可执行 ----
echo ""
echo "第三阶段：使 hooks 可执行..."
chmod +x .claude/hooks/*.py 2>/dev/null || true
echo "  ✓ Hooks 现在可执行"

# ---- 第四阶段：初始化状态 ----
echo ""
echo "第四阶段：初始化项目状态..."

TODAY=$(date +%Y-%m-%d)

cat > .claude/state/current-focus.md <<STATEFILE
# 当前焦点

**Sprint:** 初始设置 — 项目于 ${TODAY} 初始化。

## 进行中的工作

- [ ] 定义第一个交付物并创建其 STATUS.md 行
- [ ] 执行者：创建第一个交付物
- [ ] 编排者：建立 sprint 节奏

## 近期完成

- 模板已为 **${PROJECT_NAME}** 初始化

## 阻塞 / 等待中

暂无。

## 即将到来的截止日期

暂无。

---

> 此文件由 \`session-context.py\` 在 SessionStart 读取，并注入为每个新会话的 \`additionalContext\`。保持简短——一屏。在 sprint 开始和交接时更新。
STATEFILE
echo "  ✓ state/current-focus.md 已初始化"

# ---- 第五阶段：验证 ----
echo ""
echo "第五阶段：运行工作区验证..."

if [[ -f "scripts/validate_workspace.py" ]]; then
  python3 scripts/validate_workspace.py --quick || echo "  ⚠ 验证发现问题 — 请检查上方输出"
else
  echo "  ⚠ validate_workspace.py 不存在 — 跳过验证"
fi

# ---- 完成 ----
echo ""
echo "════════════════════════════════════════════"
echo "  初始化完成！"
echo "════════════════════════════════════════════"
echo ""
echo "  项目：     $PROJECT_NAME"
echo "  领域：     $DOMAIN"
echo "  Agent：    $ORCHESTRATOR_NAME, $PRODUCER_NAME, $REVIEWER_NAME, $RED_TEAM_NAME"
echo "  状态文件： $STATUS_FILE"
echo ""
echo "下一步："
echo "  1. 检查 .claude/agents/ — 按需自定义角色描述"
echo "  2. 检查 .claude/rules/00-core-values.md — 使原则与项目匹配"
echo "  3. 在 $STATUS_FILE 中定义你的第一个交付物"
echo "  4. 启动新的 Claude Code 会话 — SessionStart hook 将注入状态"
echo "  5. 尝试 /status 查看你的项目状态"
echo ""
