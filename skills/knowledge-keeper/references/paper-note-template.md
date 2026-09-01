# 标题 — 作者 (年份)

link: <canonical URL>   pdf: <pdfs/... 或 not cached>
added: <YYYY-MM-DD>   source-query: "<查询>"
discovered-via: <关键词 | reference-of:<id> | cited-by:<id>>
origin: user-upload | external-search | existing-library
priority: anchor | normal
local-pdf: <relative-or-absolute path | none>   sha256: <hash | unknown>
bibliographic-id:
  arxiv: <id | none>
  doi: <id | none>
verification: local-file | verified | partial | unverifiable
assessment-depth: metadata | abstract | full | code | reproduced
publication: <venue>   review-status: published | preprint | unknown
quality: strong | usable | weak | unassessed   quality-updated: <YYYY-MM-DD>
parse-status: success | partial | failed | not-applicable

## 结论
一句话说明论文是否值得作为参照、竞争或背景，以及最有价值点和最大风险。结论必须受 verification 与 assessment-depth 限制。

## 摘要
用 3–5 句独立描述论文的问题、方法、核心结论和证据强度；不围绕当前临时问题重写。

## 关键细节
- 输入/输出、方法模块、数据集、标签、训练目标、推理路径。
- 主要数字、实验设置、基线、评测协议与资源/算力。
- 代码实现与论文是否一致；作者报告的失败消融和负结果。

## 外部信号
会议/期刊、作者在该问题上的履历、采用情况及查询日期。仅作辅助，不压过正文证据。

## 局限
- 论文明确承认的局限、未验证声明和解析失败原因；推测标 `[speculation]`。

## 相关记录
- <YYYY-MM-DD> <方向/提案>：角色（参照 | 竞争 | 相邻 | 背景）及使用方式。
- Anchor 追加用户指定原因；注意 priority of attention != strength of evidence。

> 内容目标：让带着不同问题的后来读者几乎无需重新打开原文；metadata 不能替代正文证据。
