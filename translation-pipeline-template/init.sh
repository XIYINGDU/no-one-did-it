#!/usr/bin/env bash
# 翻译流水线初始化脚本
# 用法:
#   ./init.sh --source book/chapters/ --target translation/ --lang zh
#   ./init.sh --source src/ --target i18n/zh/ --lang zh --project "我的书"

set -euo pipefail

SOURCE_DIR="book/chapters"
TRANSLATION_DIR="translation"
TARGET_LANG="zh"
SOURCE_LANG="en"
PROJECT_NAME=""

usage() {
    cat <<EOF
用法: ./init.sh [选项]

  翻译流水线初始化 — 在任意书籍项目中一键部署完整的翻译流水线。

选项:
  --source DIR      英文源文件目录    (默认: book/chapters)
  --target DIR      翻译产出目录      (默认: translation)
  --source-lang LANG  源语言代码      (默认: en)
  --target-lang LANG  目标语言代码    (默认: zh)
  --project NAME    项目名称（可选）

示例:
  ./init.sh --source book/chapters-v6/ --target i18n/zh/
  ./init.sh --source content/en/ --target content/zh/ --project "My Book"

完成后的流水线:
  Translator → Reviewer → Glossary Master → Chinese Reader → Translation Director
EOF
    exit 0
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --source) SOURCE_DIR="$2"; shift 2 ;;
        --target) TRANSLATION_DIR="$2"; shift 2 ;;
        --source-lang) SOURCE_LANG="$2"; shift 2 ;;
        --target-lang) TARGET_LANG="$2"; shift 2 ;;
        --project) PROJECT_NAME="$2"; shift 2 ;;
        --help|-h) usage ;;
        *) echo "未知选项: $1"; usage ;;
    esac
done

TEMPLATE_DIR="$(cd "$(dirname "$0")" && pwd)"
GLOSSARY_PATH="${TRANSLATION_DIR}/glossary.yml"
SCORING_PATH="${TRANSLATION_DIR}/SCORING.md"

echo "╔══════════════════════════════════════════════╗"
echo "║  翻译流水线初始化                             ║"
echo "║  Translator → Reviewer → Glossary Master     ║"
echo "║  → Chinese Reader → Translation Director     ║"
echo "╚══════════════════════════════════════════════╝"
echo ""
echo "  源文件:    ${SOURCE_DIR}"
echo "  翻译产出:  ${TRANSLATION_DIR}"
echo "  源语言:    ${SOURCE_LANG} → 目标语言: ${TARGET_LANG}"
echo ""

# --- 1. Create directory structure ---
echo "→ 创建目录结构..."
mkdir -p "${TRANSLATION_DIR}"/{chapters,ready,reviews,decision-log}
mkdir -p .claude/agents
mkdir -p .claude/agent-memory/{translator,reviewer,glossary-master,translation-director}

# --- 2. Copy and parameterize agent definitions ---
echo "→ 安装翻译 agent..."
for agent in translator reviewer glossary-master translation-director; do
    if [ "$agent" = "chinese-reader" ]; then
        continue  # handled below
    fi
    cp "${TEMPLATE_DIR}/.claude/agents/${agent}.md" ".claude/agents/${agent}.md"
done

# Chinese Reader: no memory (cold read)
cp "${TEMPLATE_DIR}/.claude/agents/chinese-reader.md" ".claude/agents/chinese-reader.md"

# Replace placeholders in agent files
for agent in translator reviewer glossary-master translation-director; do
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s|{{GLOSSARY_PATH}}|${GLOSSARY_PATH}|g" ".claude/agents/${agent}.md"
        sed -i '' "s|{{SCORING_PATH}}|${SCORING_PATH}|g" ".claude/agents/${agent}.md"
    else
        sed -i "s|{{GLOSSARY_PATH}}|${GLOSSARY_PATH}|g" ".claude/agents/${agent}.md"
        sed -i "s|{{SCORING_PATH}}|${SCORING_PATH}|g" ".claude/agents/${agent}.md"
    fi
done

# --- 3. Copy templates and parameterize ---
echo "→ 安装配置模板..."
cp "${TEMPLATE_DIR}/templates/glossary.yml" "${GLOSSARY_PATH}"
cp "${TEMPLATE_DIR}/templates/SCORING.md" "${SCORING_PATH}"

# TRANSLATION.md with full parameterization
cp "${TEMPLATE_DIR}/templates/TRANSLATION.md" "${TRANSLATION_DIR}/TRANSLATION.md"
if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i '' "s|{{SOURCE_LANG}}|${SOURCE_LANG}|g" "${TRANSLATION_DIR}/TRANSLATION.md"
    sed -i '' "s|{{TARGET_LANG}}|${TARGET_LANG}|g" "${TRANSLATION_DIR}/TRANSLATION.md"
    sed -i '' "s|{{SOURCE_DIR}}|${SOURCE_DIR}|g" "${TRANSLATION_DIR}/TRANSLATION.md"
    sed -i '' "s|{{TRANSLATION_DIR}}|${TRANSLATION_DIR}|g" "${TRANSLATION_DIR}/TRANSLATION.md"
    sed -i '' "s|{{GLOSSARY_PATH}}|${GLOSSARY_PATH}|g" "${TRANSLATION_DIR}/TRANSLATION.md"
    sed -i '' "s|{{SCORING_PATH}}|${SCORING_PATH}|g" "${TRANSLATION_DIR}/TRANSLATION.md"
else
    sed -i "s|{{SOURCE_LANG}}|${SOURCE_LANG}|g" "${TRANSLATION_DIR}/TRANSLATION.md"
    sed -i "s|{{TARGET_LANG}}|${TARGET_LANG}|g" "${TRANSLATION_DIR}/TRANSLATION.md"
    sed -i "s|{{SOURCE_DIR}}|${SOURCE_DIR}|g" "${TRANSLATION_DIR}/TRANSLATION.md"
    sed -i "s|{{TRANSLATION_DIR}}|${TRANSLATION_DIR}|g" "${TRANSLATION_DIR}/TRANSLATION.md"
    sed -i "s|{{GLOSSARY_PATH}}|${GLOSSARY_PATH}|g" "${TRANSLATION_DIR}/TRANSLATION.md"
    sed -i "s|{{SCORING_PATH}}|${SCORING_PATH}|g" "${TRANSLATION_DIR}/TRANSLATION.md"
fi

# --- 4. Copy scripts and parameterize ---
echo "→ 安装脚本..."
cp "${TEMPLATE_DIR}/scripts/extract_ready.py" "scripts/extract_ready.py"
chmod +x "scripts/extract_ready.py"
if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i '' "s|{{TRANSLATION_DIR}}|${TRANSLATION_DIR}|g" "scripts/extract_ready.py"
else
    sed -i "s|{{TRANSLATION_DIR}}|${TRANSLATION_DIR}|g" "scripts/extract_ready.py"
fi

# --- 5. Copy decision-log templates ---
cp "${TEMPLATE_DIR}/templates/../templates/TEMPLATE-decisions.yml" "${TRANSLATION_DIR}/decision-log/" 2>/dev/null || true
cp "${TEMPLATE_DIR}/templates/../templates/TEMPLATE-resolutions.yml" "${TRANSLATION_DIR}/decision-log/" 2>/dev/null || true

# --- 6. Initialize agent memory ---
for agent in translator reviewer glossary-master translation-director; do
    cat > ".claude/agent-memory/${agent}/memory.md" <<MEMEOF
# ${agent} 记忆

## 项目: ${PROJECT_NAME:-未命名}

初始化日期: $(date +%Y-%m-%d)
MEMEOF
done

echo ""
echo "✓ 翻译流水线初始化完成。"
echo ""
echo "已创建:"
echo "  .claude/agents/          — 5 个翻译 agent"
echo "  .claude/agent-memory/    — 角色独立记忆"
echo "  ${TRANSLATION_DIR}/       — 翻译产出目录"
echo "  ${TRANSLATION_DIR}/TRANSLATION.md — 翻译宪法"
echo "  ${TRANSLATION_DIR}/SCORING.md     — 评分标准"
echo "  ${GLOSSARY_PATH}         — 术语表（空模板）"
echo "  scripts/extract_ready.py — 纯文本剥离脚本"
echo ""
echo "下一步:"
echo "  1. 编辑 ${GLOSSARY_PATH} 添加项目专属术语"
echo "  2. 启动翻译流水线: 让 Translator 翻译第一章"
