# Structure-Aware Document Parsing Improves RAG Chunk Quality

Summary: RAG ingestion should preserve document structure before chunking when the source material includes PDFs, tables, images, slides, spreadsheets, audio, or video. Hierarchy-aware intermediate representations give downstream chunkers and retrievers cleaner units than plain extracted text.

Use when:
- Ingesting PDFs or mixed-format corpora into retrieval systems.
- Debugging poor answers caused by lost headings, table structure, scanned text, images, or document hierarchy.

Details:
- Docling uses different pipelines for file types including HTML, Markdown, Word, slides, spreadsheets, audio, video, and PDFs; audio/video use ASR, while PDFs can use standard extraction pipelines or a vision-language-model pipeline.
- The PDF standard pipeline combines focused models for text, table, and image extraction and can choose OCR backends for scanned documents.
- Docling emits an intermediate document structure in DocTags that can be converted to Markdown, HTML, or JSON, and its chunker (the Hybrid Chunker) uses that hierarchy to create structurally informed chunks.
- Optional table structure, OCR, and picture-description extraction can improve context but add extra model work and latency.
- The parsed output is a Pydantic `DoclingDocument`, so extraction can be programmatic: tables export to DataFrames, images map to picture→caption→embedded-text elements, and structured field extraction can pull only chosen fields (e.g. an invoice's bill number, total, sender) instead of the whole document. (Clyburn 09:10-12:42)
- The same layout model that draws bounding boxes over section headers, text, and pictures can be used to strip PII from a document before extraction; a vision-language model (e.g. a local Granite served through Ollama's OpenAI-compatible endpoint) can enrich images/diagrams with descriptions that become retrievable context. (Clyburn 12:42-13:26)
- Deployment surface for scale: `docling serve` runs a REST microservice (container/Kubernetes) taking per-request options (OCR, backend, image annotation) for thousands of documents, and a Docling MCP server (run via `uvx`) exposes conversion/generation/manipulation tools so coding agents (Claude Code, Cursor, Codex, Continue) can drive extraction without knowing the arguments. (Clyburn 16:50-19:16)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Use omnimodal embeddings for cross-modal retrieval and comparison](use-omnimodal-embeddings-for-cross-modal-retrieval-and-comparison.md)
- [Choose a document-extraction tier by cost, determinism, and scale](choose-document-extraction-tier-by-cost-determinism-and-scale.md)
- [Use a document outline as the retrieval index for chunkless agentic RAG](use-a-document-outline-as-the-retrieval-index-for-chunkless-agentic-rag.md)

Sources:
- [OpenRAG: An open-source stack for RAG - Phil Nash](../sources/20260408_4TxOBhDRRCM.md), 02:51-05:11, 11:24-11:51
- [Structuring the Unstructured - Cedric Clyburn, Red Hat](../sources/20260628_-x5GEVnkuRw.md), 05:44-19:52
