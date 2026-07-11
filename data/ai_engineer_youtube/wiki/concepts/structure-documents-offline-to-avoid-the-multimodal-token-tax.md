# Structure Documents Offline to Avoid the Multimodal Token Tax

Summary: Drag-and-dropping raw PDFs, Word docs, or images into a cloud chatbot spends tokens on document processing before any question is asked and hides how the file was chunked and read. Pre-parsing files to structured Markdown offline (locally on CPU) turns ingestion into a one-time, controllable, cheaper-or-free step and makes retrieved chunks visible and traceable.

Use when:
- Deciding whether to upload documents into a chatbot at query time versus ingesting them into your own store ahead of time.
- Debugging why a document-upload chatbot is expensive, slow, or hallucinating on tables and long files.
- Building a knowledge-base chatbot where the same documents are queried repeatedly by many users.

Details:
- Two costs of naive upload: you pay tokens just to process the document before asking anything, and you lose visibility into how it was chunked — if a table is read badly you cannot see it, so accuracy drops and hallucination rises. (Matini 01:07-02:35, 08:14-09:40)
- The structure-first alternative runs on local CPU: Docling converts the file to Markdown, you choose a known chunking strategy, embeddings are written to a Postgres vector store, and the resulting prompt is cheap — or free when the whole pipeline is local. (Matini 09:06-10:16)
- The cost gap scales with volume: 1-2 pages is negligible, but a 200-page handbook re-queried by many employees makes per-upload ingestion expensive, so amortizing it into a one-time offline ingest wins. (Matini 10:16-10:29)
- Structuring offline also buys traceability: every answer can cite the exact source chunk it was generated from, so a wrong answer is debuggable (you can inspect which chunk was or wasn't retrieved) instead of an untrackable blob from a whole-file upload. (Matini 14:46-17:57)
- This is the ingestion half of the same principle behind structure-aware parsing: convert non-text/binary material into structured Markdown before chunking and embedding rather than handing raw files to the model at request time. (Matini 44:31-44:48)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Structure-aware document parsing improves RAG chunk quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)
- [Parse Multimodal Business Sources Into Structured Markdown](parse-multimodal-business-sources-into-structured-markdown.md)
- [Match Chunking Strategy to Document Type](match-chunking-strategy-to-document-type.md)
- [Choose a document-extraction tier by cost, determinism, and scale](choose-document-extraction-tier-by-cost-determinism-and-scale.md)

Sources:
- [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy](../sources/20260628_Akm1sqvWG4A.md), 01:07-10:29, 44:31-44:48
