# Use a Document Outline as the Retrieval Index for Chunkless Agentic RAG

Summary: For a single structured document, the parsed Markdown/section outline can serve as the entire retrieval index — an agent iterates over section summaries, picks the relevant section, and pulls its full text — removing the chunker, embedding model, and vector database from the RAG stack.

Use when:
- Answering questions over one large but well-structured document (report, filing, manual) rather than a huge heterogeneous corpus.
- You want to avoid standing up a chunking/embedding/vector-database pipeline for document-scoped Q&A.
- The document already has clean hierarchy (headings/sections) from a structure-aware parser.

Details:
- "Chunkless" / agentic RAG treats the document's Markdown outline (each section with a summary) as the whole retrieval index; there is no semantic-similarity search over thousands of vectors in a database. (14:09)
- Retrieval becomes an agentic loop: the LLM reads the outline, judges whether a section is relevant to the question, and pulls that section's full text from the parsed document; it can iterate several times (~5) when one section is insufficient. (14:09-16:33)
- The demo answered "what are the main AI models used in Docling?" in a single iteration by searching the document structure for the relevant section instead of querying a vector store; it scaled to the IBM 2025 annual report with 418 sections. (16:13)
- Prerequisite: a structure-aware parse that yields a faithful section hierarchy (e.g. Docling's Pydantic document → Markdown outline); poor structure extraction would degrade the outline that this pattern relies on.
- This is a document-scoped specialization of agentic retrieval: the "index" is generated fresh per document, trading a persistent vector index for per-run agent iteration — appropriate when query volume per document is low.

Related topics:
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Structure-aware document parsing improves RAG chunk quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)
- [Choose a document-extraction tier by cost, determinism, and scale](choose-document-extraction-tier-by-cost-determinism-and-scale.md)
- [Agentic retrieval lets models plan search steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Redefine RAG as iterative multi-tool retrieval, not vector search](redefine-rag-as-iterative-multi-tool-retrieval.md)
- [Treat embeddings as cached compute decided by query volume](treat-embeddings-as-cached-compute-decided-by-query-volume.md)

Sources:
- [Structuring the Unstructured - Cedric Clyburn, Red Hat](../sources/20260628_-x5GEVnkuRw.md), 14:09-16:33
