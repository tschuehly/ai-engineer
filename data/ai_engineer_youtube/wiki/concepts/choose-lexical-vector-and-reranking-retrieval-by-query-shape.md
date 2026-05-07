# Choose Lexical, Vector, and Reranking Retrieval by Query Shape

Summary: Lexical retrieval, vector retrieval, and reranking solve different query and candidate-set failures. BM25 fits explicit term matching, vector retrieval fits semantic paraphrase and nuance, and cross-encoder reranking helps resolve conflicted candidate sets when the smaller pool is worth rescoring.

Use when:
- Choosing an initial retrieval stack for a new RAG product.
- Diagnosing whether poor retrieval comes from missing exact terms, paraphrase mismatch, or poor ordering among plausible candidates.

Details:
- In-memory retrieval is the simplest baseline when the corpus fits in the context window, but it fails when documents are too numerous or the model fails to attend to the right document (04:10-04:49).
- BM25 uses query terms, term frequency, document length, and term rarity; it is easy to try and can work well when production queries contain explicit names or keywords (04:51-05:11).
- Vector retrieval helps when user intent is expressed indirectly, such as asking how long a phone lasts before charging rather than using the exact phrase "battery life" (05:18-06:08).
- Cross-encoder rerankers take the query and document together and score them jointly, which is more powerful than comparing separate embedding vectors, but their cost usually limits them to reranking a smaller retrieved set (06:12-06:55).

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Hybrid Retrieval Should Support Filters And Embedding Migration](hybrid-retrieval-should-support-filters-and-embedding-migration.md)
- [Use Small Models as Context-Management Tools Before Agent Reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)

Sources:
- [Layering every technique in RAG, one query at a time - David Karam, Pi Labs (fmr. Google Search)](../sources/20250729_w9u11ioHGA0.md), 04:10-06:55
