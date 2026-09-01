# Idea Hard Gates

## Hard contradiction

若高质量直接工作已完整解决核心问题、可靠数据反驳机制、创新仅剩措辞/组合，或 claim 在评测中原则上不可验证，判定为 hard contradiction：否决、证伪或转向，不进入实验设计。

已有证据使核心机制不优于 baseline、简单控制或隔离消融时，原机制视为被直接挑战。不得靠外围模块续命；新解释必须作为新 hypothesis，并产生可证伪预测。`未验证` 不等于 `已被反驳`。

## Repairable blocker

数据、接口、最强 baseline、资源、实现链或 scope 尚未确认时，状态为卡住，先查事实或缩小范围。

## Research risk

跨场景泛化、机制适用边界或评测隔离风险可进入猜想清单，不自动否决。

## Attribution discipline

同时改变机制、backbone、数据、采样、routing、预算或评测时，正向结果只能归因于完整系统；核心机制须经 isolating ablation 或 controlled comparison。不能隔离时写“观察到系统提升，核心机制贡献尚未隔离”。`experiment-manager` 冻结归因风险，`result-analysis` 在判定时复核。

## Technique is not a problem

方法名、模型名或热门技术不是研究问题。删除方法名后仍须说明谁在何种情况下失败、现有方案为何不够、失败造成何种影响及解决后改变什么能力；否则属于 solution hunting，继续收敛问题。

## Project fit

动态检查 skills、compute/hardware、data、time、collaboration dependency，并比较 estimated execution time 与 research half-life。结果仅为 `fit`、`tight`、`mismatch`、`unknown`；缺事实即 unknown/blocker，不猜固定月份。
