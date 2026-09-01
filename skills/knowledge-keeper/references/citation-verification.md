# 引用验证协议

分离 bibliographic verification（`verified|partial|unverifiable|local-file`）与 assessment depth（`metadata|abstract|full|code|reproduced`）。前者确认论文身份（作者、标题、年份、DOI/arXiv），后者记录实际阅读深度。`verified + abstract` 只能支持“值得进一步阅读”，不能支持实验扎实、实现可行或 gap 成立；本地 PDF 可为 `local-file`，正式引用仍需确认身份。

## Retrieval failure

API、网页、PDF parser 或 metadata source 失败时必须暴露失败；验证响应内容，不能只看 HTTP 状态码。记录失败的 query、seed、source，依赖失败来源的候选标为 `partial`/`unverifiable`。禁止用模型记忆补齐论文、引用关系、数字或正文内容。
