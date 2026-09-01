# Repository Guidelines

## 项目结构

- `skills/`：可移植的 Agent Skill；每个子目录以 kebab-case 命名，并包含入口 `SKILL.md`，较长示例放在同级 `references/`。
- `scripts/`：项目维护工具（安装、初始化、迁移及校验），包括 Bash 脚本和 Python 工具。
- `templates/`：下游研究项目的 `AGENTS.md`、`CLAUDE.md` 及 `.research/` 初始模板。
- `docs/`：架构、兼容性和维护说明；`README.md` 是用户安装与使用入口。`.research/` 为运行时目录，默认不提交。

## 构建、测试与本地开发

本仓库无编译步骤或包管理器。提交前在仓库根目录运行：

```bash
python scripts/lint-skills.py       # 校验 frontmatter、命名、引用和文件长度
python scripts/check-shared-sync.py # 检查跨 Skill 共享内容同步
git diff --check                    # 检查空白和补丁格式
```

可用 `./scripts/install-skills.sh --dry-run codex` 预览安装链接，或用
`./scripts/init-research-project.sh /path/to/project` 验证项目骨架初始化。修改脚本后，至少在临时目录执行一次正向流程及重复执行（幂等/拒绝覆盖）流程。

## 编码风格与命名

Shell 使用 Bash、`set -euo pipefail`、双引号包裹变量并保持可执行权限；Python 使用 Python 3、4 空格缩进、`snake_case` 函数/变量和清晰的非零退出码。Skill 目录及 `name` frontmatter 必须使用小写 kebab-case（如 `result-analysis`）；Markdown 标题层级清晰，文件名使用小写或约定的大写入口名（`SKILL.md`、`TODO.md`）。避免提交宿主专属路径（`.kilo/`、`my_skills/`）。

## 测试指南

当前没有独立测试框架或覆盖率门槛；上述校验脚本是必需的回归检查。新增校验时使用 `test_*.py` 命名，并覆盖成功、参数错误和目标已存在等边界情形。对 Markdown/模板变更，检查相对链接存在且运行相关脚本生成结果符合预期。

## 提交与 Pull Request

沿用历史中的 Conventional Commit 风格：`feat: ...`、`docs: ...`、`refactor: ...`、`chore: ...`；主题简短、使用祈使语气，必要时加范围（如 `feat(skills): ...`）。PR 应说明动机、影响范围和验证命令，关联 issue（如有），并列出兼容性或迁移影响；涉及文档渲染或用户界面时附前后截图。不要提交密钥、个人路径或生成的 `.research/` 数据。
