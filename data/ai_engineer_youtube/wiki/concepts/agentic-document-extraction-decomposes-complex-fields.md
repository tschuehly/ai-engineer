# Agentic Document Extraction Decomposes Complex Fields

Summary: Complex enterprise extraction works better as an agentic workflow than as one large prompt when documents, fields, OCR quality, and validation needs exceed what one model call can track.

Use when:
- Designing extraction over long contracts, leases, proposals, or mixed enterprise documents.
- A single LLM call works on simple examples but fails on many fields, pages, languages, or document-quality variants.

Details:
- Box found that generic LLM extraction worked well for simple documents, but struggled when customers asked for hundreds of fields across long documents, risk assessments, complex digital assets, languages, and noisy OCR.
- The agentic workflow keeps the same product contract of document in and fields out, but decomposes the work into field preparation, intelligent field grouping, multiple document queries, tool checks, page-image verification, model voting, and judge feedback.
- Field grouping matters because related values such as contract parties and their addresses need to be extracted together; splitting them independently can produce mismatched structured data.
- OCR is a first-stage dependency, not a solved detail: scans, handwriting, strikeouts, PDFs, file formats, and languages can corrupt the context passed into the model.

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Route heterogeneous documents through multimodal LLM pipelines](route-heterogeneous-documents-through-multimodal-llm-pipelines.md)
- [Structure-aware document parsing improves RAG chunk quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)
- [Stage complex AI applications into inspectable deterministic and agentic steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)

Sources:
- [Building an Agentic Platform - Ben Kus, CTO Box](../sources/20250824_12v5S1n1eOY.md), 05:34-12:23
