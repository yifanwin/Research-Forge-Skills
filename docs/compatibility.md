# 跨 Agent 兼容性

Research Forge Skills 遵循通用 Agent Skills 规范，可由 Codex、Claude Code、Kilo、Cursor 及其他兼容宿主加载。核心 Skill 不依赖特定运行时；宿主能力不足时按 Skill 中的 capability ladder 降级，并明确披露证据限制。

旧项目可使用 `scripts/migrate-kilo-to-research.py` 将 `.kilo/` 状态迁移为 `.research/`。
