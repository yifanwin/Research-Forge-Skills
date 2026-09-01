# 本地论文摄取协议

在外部搜索前执行 preflight：检查用户显式 PDF、任务指向路径、`.research/knowledge/pdfs/`、paper note 的 `local-pdf`。用户提供的 PDF 记录 `origin: user-upload`、`priority: anchor`，不移动原文件；仅用户要求缓存时复制到 `pdfs/`，默认不入 Git。

流程：识别书目信息 → 尽可能完整阅读 → 建/更新 paper note → 标记 anchor → 提取术语、references 与 search seeds → 外部扩展。按路径、可用 hash 去重；同 sha256 只保留一个 note。

解析能力阶梯：宿主原生阅读器、附件能力、`pdftotext`、Python parser、metadata fallback。失败时记录 `assessment-depth: metadata|partial`、`parse-status` 与原因，绝不伪称 full。Anchor 优先级只是注意力，不是证据强度（priority of attention != strength of evidence）。
