# Enterprise Deep Research Needs Trustworthy Retrieval and Governance Controls

Summary: Private-corpus deep research needs enterprise-grade retrieval quality and governance because its outputs are only useful when factual accuracy, citations, data access, deployment boundaries, and observability are reliable.

Use when:
- Designing deep research over internal data rather than public web pages.
- Evaluating whether an enterprise RAG or agent platform is ready for document-heavy business workflows.

Details:
- The talk lists multimodal ingestion for images and tables, hybrid retrieval, metadata, and reranking as retrieval capabilities needed to make internal documents findable and usable in RAG or agentic RAG workflows. (00:43-01:05)
- Mendelevitch connects enterprise deep research quality to hallucination detection and correction, arguing that factual accuracy remains a top challenge for LLM applications and that research outputs should be based on robust information. (01:08-02:16)
- Enterprise deployment requirements include security, role-based access controls, bring-your-own-model, custom prompts, observability, monitoring, and the ability to run as SaaS, in a customer VPC, or on premises. (00:31-00:37, 01:25-01:41)
- Corpus understanding is presented as a planning aid: the system should plan properly based on the available private data, not only run blind top-k retrieval. (03:42-03:47)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Hybrid retrieval should support filters and embedding migration](hybrid-retrieval-should-support-filters-and-embedding-migration.md)
- [Structure-aware document parsing improves RAG chunk quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)
- [Evaluate retrieval and MCP layers by task value, not only response availability](evaluate-retrieval-and-mcp-layers-by-task-value.md)

Sources:
- [Enterprise Deep Research: The Next Killer App for Enterprise AI — Ofer Mendelevitch, Vectara](../sources/20251124_fh9LgKXBGnQ.md), 00:31-02:16, 03:42-03:47
