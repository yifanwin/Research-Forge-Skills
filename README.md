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

安装脚本为每个 Skill 创建符号链接，因此仓库更新后无需重复复制。目标目录中已有同名条目时会跳过；可先用 `--dry-run` 检查将执行的操作。

## 使用指南

### 1. 准备项目目录

可以用脚本一条命令生成完整项目骨架（脚本不会覆盖已有的 `AGENTS.md` 或 `.research/`）：

```bash
./scripts/init-research-project.sh /path/to/my-research
```

脚本会创建 `AGENTS.md`、`.research/` 及其 `proposal/`、`project/`、`archive/`、`reports/`、`knowledge/` 子目录，并复制索引与待办模板。完成后请编辑 `AGENTS.md`，填写项目目标、成功判据和工具链。

如果不使用脚本，也可以手动准备：

```bash
cp /path/to/Research-Forge-Skills/templates/AGENTS.md ./AGENTS.md
mkdir -p .research/{proposal,project,archive,reports,knowledge/{papers,reviews,pdfs}}
cp /path/to/Research-Forge-Skills/templates/research-root/global.md .research/global.md
cp /path/to/Research-Forge-Skills/templates/research-root/TODO.md .research/TODO.md
```

按模板填写目标、非目标、成功判据和工具链；`.research/global.md` 只做索引，不写研究结论。若宿主支持项目级上下文文件，也可将 `templates/CLAUDE.md` 作为相应入口进行适配。

### 2. 在宿主中调用 Skill

安装后，直接用自然语言描述任务即可；在不确定时可明确点名 Skill。例如：

```text
请用 research-progress 评估“<研究想法>”，先检查价值、相关工作和实现链。
请用 knowledge-keeper 查找 <主题/论文 DOI>，核实后写入 .research/knowledge/papers/。
请用 experiment-manager 开始 ENN 实验，绑定当前主假设并生成运行报告。
请用 result-analysis 分析这次实验，说明哪条因果链成立以及下一步决定。
请用 result-visualization 根据已批准的数据生成可复现图表。
请用 write-md 检查报告可读性并生成 HTML 版。
请用 academic-paper-writing 润色论文 Introduction；请用 slide-deck 生成 HTML 幻灯片。
```

Skill 之间按职责交接：不要让写作 Skill 代替实验或统计判断，也不要绕过 `research-manager` 直接移动方向目录。长报告通常由 `experiment-manager → result-analysis → result-visualization → write-md` 协作完成。

### 3. 推荐的研究流程

1. **收敛想法**：在 `proposal/NN-slug/` 中让 `research-progress` 检查价值、直接竞争工作、硬门槛和可实现性。
2. **建立知识**：用 `knowledge-keeper` 处理本地或外部论文；每篇实际依赖的论文都要有可追溯笔记。
3. **开始实验**：用户确认后，由 `experiment-manager` 创建 `exp/NN-slug` 分支，在运行前冻结 baseline、预期和停手/做成标准。
4. **运行与分析**：每次运行使用 `ENN` 编号，绑定一个主要假设；运行后先分析证据和收敛，再决定继续、转向或停止。
5. **表达与归档**：用 `write-md`、`result-visualization` 整理报告，结束方向时由 `research-manager` 归档并保留 `REPORT.md`。

状态目录约定为：评估中 `proposal/`、进行中 `project/`、已结束 `archive/YYYY-MM-DD-NN-slug/`。新想法先放入当前方向的暂存清单，不自动开启实验。

### 4. 更新、卸载与排错

- **更新**：拉取本仓库最新内容；符号链接会自动指向新文件。
- **卸载**：删除宿主 Skills 目录中指向本仓库的符号链接，不要删除仓库源文件。
- **检查安装**：`ls -l ~/.codex/skills`（或对应宿主目录），确认链接指向本仓库的 `skills/`。
- **宿主未加载 Skill**：确认目标目录和宿主配置一致，重新启动宿主后再试；可用 `--dry-run` 检查路径。
- **校验失败**：在仓库根目录运行下方校验命令，根据报错修复 frontmatter、名称或引用文件。

## 研究生命周期

`research-progress` 评估方向与关键不确定性 → `knowledge-keeper` 捕获文献证据 → `experiment-manager` 执行决策驱动实验 → `result-analysis` 解释证据 → `result-visualization` 生成图表；`research-manager` 统一状态和归档。缺少兄弟 Skill 或工具时，按能力阶梯降级并披露限制，不编造证据。

## 开发与校验

```bash
python scripts/lint-skills.py
python scripts/check-shared-sync.py
git diff --check
```

## 迁移已有 Kilo 项目

先预览，再执行迁移；脚本不会删除源目录，目标 `.research/` 已存在时会拒绝覆盖：

```bash
python scripts/migrate-kilo-to-research.py /path/to/project --dry-run
python scripts/migrate-kilo-to-research.py /path/to/project
```

迁移只复制 `.kilo/` 内容，并将 Markdown 中的 `.kilo/` 路径替换为 `.research/`。
