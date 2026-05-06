# OpenRAG: An open-source stack for RAG - Phil Nash

Source: [OpenRAG: An open-source stack for RAG - Phil Nash](https://www.youtube.com/watch?v=4TxOBhDRRCM)
Uploaded: 2026-04-08
Transcript: `raw/20260408_4TxOBhDRRCM/4TxOBhDRRCM.en-orig.vtt`

## Summary

Phil Nash presents OpenRAG as an opinionated but customizable open-source RAG baseline that combines Docling for document processing, OpenSearch plus JVector for hybrid and scalable indexing, and LangFlow for visual orchestration, agentic retrieval, guardrail insertion, APIs, and MCP exposure.

## Extracted Concepts

- [RAG stacks need modular baselines instead of one fixed recipe](../concepts/rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md) - the source frames RAG as project-specific despite reusable core components.
- [Structure-aware document parsing improves RAG chunk quality](../concepts/structure-aware-document-parsing-improves-rag-chunk-quality.md) - Docling preserves document hierarchy, tables, images, OCR output, and modality-specific extraction before chunking.
- [Hybrid retrieval should support filters and embedding migration](../concepts/hybrid-retrieval-should-support-filters-and-embedding-migration.md) - OpenRAG uses OpenSearch for vector, keyword, filter, aggregation, and multiple-embedding-model retrieval.
- [Agentic retrieval lets models plan search steps](../concepts/agentic-retrieval-lets-models-plan-search-steps.md) - OpenRAG hands the user query to an agent with retrieval tools instead of always using one embedded top-k query.

## Topic Links

- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

## Notes

- Large context windows do not eliminate RAG when businesses have more data than fits cheaply or usefully into every prompt; RAG remains hard because PDFs, chunking, embeddings, search techniques, users, questions, and expectations vary by project (00:20-02:08).
- OpenRAG combines Docling, OpenSearch, and LangFlow as a reusable baseline that stays customizable rather than prescribing one permanent RAG pipeline (02:11-02:40, 14:17-14:46).
- Docling handles PDFs, HTML, Markdown, Word, slides, spreadsheets, audio, video, OCR, table extraction, image extraction, and a Granite Docling VLM path, then emits a structured Docling document that can become Markdown, HTML, JSON, or hierarchy-aware chunks (02:51-05:11).
- OpenRAG can run offline with local models through Ollama, while also supporting external embedding and generation providers (05:14-05:36, 10:55-11:24).
- OpenSearch provides hybrid vector and keyword search, configurable filtering and aggregation, multiple embedding-model support for migration, and JVector KNN for live indexing without requiring the full vector index to fit in memory (05:39-06:48).
- Agentic retrieval gives an agent instructions and retrieval tools so it can decide what searches to perform and what to do with results, rather than relying on one top-k nearest-neighbor query (07:24-08:15).
- LangFlow exposes OpenRAG internals as editable flows, making it possible to add prompt templates, knowledge filters, guardrails, parsers, MCP URL ingestion, calculator tools, and OpenSearch retrieval tools (12:11-14:08).
- OpenRAG exposes API keys and an MCP server so its search or agent can be embedded into other applications and handed to other agents (11:52-12:03, 14:04-14:13).
