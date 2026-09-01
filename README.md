# Research Forge Skills

面向 Codex、Claude Code、Kilo、Cursor 及其他 Agent Skills 宿主的**厂商中立科研 Skill 套件**。

**One skill source. Multiple agent hosts. No per-platform forks.**

## 架构

- `skills/`：可移植、可独立复制的科研 Skill。
- `AGENTS.md`：项目级研究目标与约束（模板见 `templates/AGENTS.md`）。
- `.research/`：项目动态研究状态，由 `research-manager` 维护。
- `scripts/`：安装、迁移与校验工具。

## Skills

`research-manager`、`research-progress`、`knowledge-keeper`、`experiment-manager`、`result-analysis`、`result-visualization`、`write-md`、`academic-paper-writing`、`slide-deck`、`skill-rsi`。

## 安装

从本仓库的 `skills/` 安装到宿主用户级 Skills 目录；脚本仅创建符号链接，不复制内容：

```bash
./scripts/install-skills.sh --dry-run codex
./scripts/install-skills.sh claude
./scripts/install-skills.sh --target ~/.some-agent/skills
```

## 研究生命周期

`research-progress` 评估方向与关键不确定性 → `knowledge-keeper` 捕获文献证据 → `experiment-manager` 执行决策驱动实验 → `result-analysis` 解释证据 → `result-visualization` 生成图表；`research-manager` 统一状态和归档。缺少兄弟 Skill 或工具时，按能力阶梯降级并披露限制，不编造证据。

## 迁移旧项目

```bash
python scripts/migrate-kilo-to-research.py /path/to/project --dry-run
python scripts/migrate-kilo-to-research.py /path/to/project
```

目标已存在时脚本拒绝覆盖，失败会安全退出且保留源目录。

## 开发与校验

```bash
python scripts/lint-skills.py
python scripts/check-shared-sync.py
git diff --check
```
