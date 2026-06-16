# .claude-zh/ — 中文翻译工作区

将 `.claude/` 下所有文件翻译为中文的存放目录。目录结构与 `.claude/` 完全镜像。

## 状态

**当前阶段：** 目录骨架已建立，翻译尚未开始。

## 目录对照

| 源（`.claude/`） | 翻译（`.claude-zh/`） | 文件数 | 状态 |
|-------------------|------------------------|--------|------|
| `agents/` | `agents/` | 15 | 待翻译 |
| `commands/` | `commands/` | 10 | 待翻译 |
| `skills/` | `skills/` | 29 | 待翻译 |
| `rules/` | `rules/` | 15 | 待翻译 |
| `hooks/` | `hooks/` | 9 | 待翻译 |
| `docs/` | `docs/` | 12 | 待翻译 |
| `agent-memory/` | `agent-memory/` | 13 子目录 | 待翻译 |
| `state/` | `state/` | 1 | 待翻译 |
| `output-styles/` | `output-styles/` | 1 | 待翻译 |
| `settings.json` | `settings.json` | 1 | 待翻译 |
| `settings.local.json` | `settings.local.json` | 1 | 待翻译 |

## 翻译约定（待确定）

- [ ] 自然语言正文：翻译
- [ ] YAML frontmatter 字段名：保持英文
- [ ] 文件路径 / slug：保持原样
- [ ] Python 代码 / docstring：待定
- [ ] 五大原则生成块 `<!-- GENERATED:five-over-rules -->`：翻译成中文
- [ ] 文件命名：保持原样（文件名不翻译）

## 工作方式

1. 从 `TRANSLATION_MANIFEST.md` 选取一个文件
2. 读取 `.claude/` 下的对应源文件
3. 翻译后写入 `.claude-zh/` 下的对应路径
4. 在 `TRANSLATION_MANIFEST.md` 中标记完成
