# Structure-Aware Document Parsing Improves RAG Chunk Quality

Summary: RAG ingestion should preserve document structure before chunking when the source material includes PDFs, tables, images, slides, spreadsheets, audio, or video. Hierarchy-aware intermediate representations give downstream chunkers and retrievers cleaner units than plain extracted text.

Use when:
- Ingesting PDFs or mixed-format corpora into retrieval systems.
- Debugging poor answers caused by lost headings, table structure, scanned text, images, or document hierarchy.

Details:
- Docling uses different pipelines for file types including HTML, Markdown, Word, slides, spreadsheets, audio, video, and PDFs; audio/video use ASR, while PDFs can use standard extraction pipelines or a vision-language-model pipeline.
- The PDF standard pipeline combines focused models for text, table, and image extraction and can choose OCR backends for scanned documents.
- Docling emits an intermediate document structure in DocTags that can be converted to Markdown, HTML, or JSON, and its chunker uses that hierarchy to create structurally informed chunks.
- Optional table structure, OCR, and picture-description extraction can improve context but add extra model work and latency.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Use omnimodal embeddings for cross-modal retrieval and comparison](use-omnimodal-embeddings-for-cross-modal-retrieval-and-comparison.md)

Sources:
- [OpenRAG: An open-source stack for RAG - Phil Nash](../sources/20260408_4TxOBhDRRCM.md), 02:51-05:11, 11:24-11:51
