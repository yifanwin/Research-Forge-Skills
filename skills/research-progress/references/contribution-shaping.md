# Contribution Shaping

## Contribution shape

轻量标记核心形态：`New Problem`（新问题）、`New Method`（新方法）、`New Setting`（新设定）或 `Unclear`。它用于选择 related work、baseline 和 claim，不是评分器。多重声称触发 scope 检查；Unclear 不进入实验设计。

## Contribution Vector

对 Higher（效果）、Faster（速度）、Stronger（鲁棒/泛化）、Cheaper（成本）、Broader（范围）记录当前依据、证据状态和是否为主张。状态只能是 `已证据支持`、`机制假设`、`未验证`、`非主张`。确定 Primary 与 Secondary，通常最多两个，不把五维全写成贡献。

## Minimal Claim Test

删除非核心模块后，剩余最小系统若仍能验证 claim，则保留最小系统，其余暂存。若 claim 依赖多个未经验证机制，判定 scope 过大，先缩范围。

## Reframing probe

按需询问一两个真正能改变方向的问题：领域默认假设是什么？被绕开的真实问题是什么？为何现在值得做？成功改变 benchmark 数字还是研究/部署方式？这些问题只用于升华，不是强制 gate；增量工作可正常通过。
