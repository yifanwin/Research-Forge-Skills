---
name: knowledge-keeper
description: Literature retrieval, local-PDF ingestion, citation expansion, verification, paper notes and corpus reviews. Owns all literature search and synthesis; research-progress consumes its evidence.
---

## Output Contract

- 先说结论，再给必要依据和下一步。
- 默认短句和常用词；术语只在更准确时用，首次出现直接解释。
- 内部状态、流程和检查表默认不展示；只有影响决定或用户明确要求时才展开。
- 外部事实、论文结论和数字附来源；不确定的直接写“尚未验证”或“我推测”。
- 一段能说清就不用表格；不写套话、廉价肯定、重复总结和固定收尾。

## Ownership and invariants

- `.research/knowledge/papers/` 保存一篇论文一份永久知识；`reviews/` 保存围绕 Research Question 的综合；`pdfs/` 仅为可选原始缓存。不要新建 deep-research skill。
- 用户显式提供/上传 PDF 默认 `origin: user-upload`、`priority: anchor`；先处理再外搜。Anchor 决定注意力和 search seed，不决定可信度。
- 不移动用户文件；记录 `local-pdf`、`sha256`（可用时），同 hash 去重。写文件前遵循宿主授权策略。
- 任何用到的论文必须 capture；不要把临时问题写进 paper-centric note。

## Mode selection

- **lookup**：local → exact retrieval → verification → 阅读 → capture，适合单篇查询/总结。
- **scan**：local anchors → retrieval brief → keywords/seeds → references + cited-by → direct competitors/implementation facts → capture，适合 related work。
- **survey**：冻结 RQ → 读取 anchors → multi-perspective search → query/citation expansion → corpus → blind-spot/coverage gate → verification、extraction、taxonomy、冲突分析、adversarial pass → review artifact。不要把两篇查询升级为 survey。

## 主流程

1. **本地优先**：先处理本轮用户显式提供的 PDF、论文名、DOI 或 URL；再查 `.research/knowledge/papers/`、已有 `local-pdf`、`knowledge/pdfs` 与 `papers/00-query-log.md`。仅当当前模式所需证据未被本地材料充分覆盖时才外部检索（lookup、scan、survey 标准不同）。
2. 建立 Retrieval Brief（`references/search-strategy.md`），每个 query 映射 RQ；默认 mainstream、competing、critical、adjacent、survey/benchmark 视角，至少一个 anchor-independent。
3. 用户显式给出的论文名、DOI、arXiv、URL 或 PDF 优先解析为 seed；要求重点参照或上传的 PDF 另标为 anchor（anchor ⊆ seeds，seed 不一定是 anchor）。已有可靠 seed 时不先做宽泛关键词摸索。多 seed 检索；每个 seed 同时扩展 `reference-of` 与 `cited-by`，保留 discovery path。关键词至少迭代一轮。
4. 按 `references/citation-verification.md` 分离书目验证与阅读深度。直接工作尽量达到 `full`/`code`，并用 `impl-facts-template.md` 记录实现事实。
5. 对核心 claim 运行 `self-adversarial.md`；synthesis 前执行 `coverage-gates.md`，不通过则 targeted supplementary search。
6. 按 `synthesis-framework.md` 做 taxonomy、evidence graph（supports/challenges/extends/replicates/contradicts）与条件化冲突分析；产出 `reviews/<topic-slug>.md`（模板见 `review-template.md`）。

## Paper note schema（最小字段）

```yaml
origin: user-upload | external-search | existing-library
priority: anchor | normal
local-pdf: <path | none>
sha256: <hash | unknown>
bibliographic-id: {arxiv: <id>, doi: <id>}
verification: local-file | verified | partial | unverifiable
assessment-depth: metadata | abstract | full | code | reproduced
```

继续保留 `quality`、`role`、`discovered-via`、`source-query`、`publication`、`review-status`。Paper note 的正文结构和内容质量由 `references/paper-note-template.md` 定义；metadata 不能替代论文结论、方法/数据/实验关键细节、局限和项目相关记录。Anchor 原因追加到“相关记录”。`priority of attention != strength of evidence`。

## Indexing

`papers/` 超过 5 篇后维护 `00-overview.md`，每篇记录 citation/title、priority、role、quality、assessment-depth、要点和关联方向；`reviews/` 超过 5 篇同样维护 overview（RQ、scope、更新时间、judgment）。

## Cache and handoff

维护 `papers/00-query-log.md`（默认 7 天；latest/recent 刷新，fast-moving 增量，citation graph 拉取新结果），字段含 RQ、perspective、query、seed、discovery path、source、date、result count、new notes、cache status。向 `research-progress` 交付 anchors、RQ、direct competitors、验证/深度、coverage gate 与 counter-query 状态；不自行判断 gap。

## Capability

按宿主能力阶梯选择 PDF 读取：原生 reader/附件 → `pdftotext` → Python parser → metadata fallback。任何 fallback 必须更新 assessment-depth 和 parse-status；保持平台无关，不写 Codex/Claude/Kilo 专属调用。

## References

- `references/local-paper-ingestion.md`
- `references/search-strategy.md`
- `references/citation-verification.md`
- `references/coverage-gates.md`
- `references/self-adversarial.md`
- `references/synthesis-framework.md`
- `references/review-template.md`
- `references/paper-note-template.md`、`references/impl-facts-template.md`、`paper-quality.md`
