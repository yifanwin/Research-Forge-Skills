# 检索策略与 Retrieval Brief

系统调研先冻结 brief：`topic`、`research decision`、RQ1…、scope、time horizon、anchor papers、required evidence depth。每个 query 必须映射至少一个 RQ。

默认 3–5 个独立 perspective：mainstream、competing paradigm、critical/negative、adjacent、survey/benchmark；至少一条 anchor-independent。每个 perspective 先宽后窄一轮，独立候选集，再对各 seed 做 reference-of 与 cited-by 扩展。检索单位是 Research Question，而非模糊主题。

`00-query-log.md` 字段：RQ、perspective、query、seed、discovery path、source、date、result count、new notes、cache status。默认缓存 7 天；latest/recent 刷新时间窗，快速变化主题增量刷新，citation graph 仅拉取 newer-than-last-search。

## Benchmark / leaderboard search

查询某 benchmark 的工作时，不得只搜 benchmark 名称：以 benchmark 原论文作 seed 扩展 references/cited-by；检查官方 leaderboard、网站、model zoo 或 evaluation repository；执行一个相邻宽查询和一个上位任务/能力查询；再反查命中论文或模型的 evaluation section。

## Citation expansion rules

优先筛选明确批评、扩展、复现或修正 seed 的后继；citation count 不是相关性指标，排序为 directness > evidence value > recency > citation count。尽量检查正文引用上下文，bibliography 单次出现不构成实质关系。仅当候选成为新关键 seed 或揭示未覆盖 branch 时继续下一跳；当前跳只剩重复/背景工作即停止。
