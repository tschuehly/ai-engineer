# Choose HybridRAG When Relationship Structure Matters

Summary: HybridRAG combines vector retrieval with knowledge-graph retrieval when semantic similarity alone misses important entity relationships. It is most useful when questions require traversing explicit relationships rather than only finding similar text chunks.

Use when:
- Deciding whether a corpus needs vector RAG, GraphRAG, or a hybrid retrieval architecture.
- Answering questions where entity relationships, business objects, or multi-source relationships matter more than nearest-neighbor text similarity.

Details:
- Knowledge graphs encode entity-relationship-entity structure, while vector databases encode semantic similarity over chunks; HybridRAG keeps both retrieval paths available for the same application. 01:28-03:11, 03:23-04:38
- Structured domains such as retail, financial services, and employee databases are strong graph candidates because their objects and relationships are already well-defined. 18:36-18:54
- Unstructured corpora can still justify GraphRAG when the team can reliably extract a useful knowledge graph and the use case requires complex relationship understanding. 18:56-19:25
- Graph systems are compute-heavy, so relationship-aware retrieval should be justified by the question set rather than added by default. 19:23-19:31
- GraphRAG can add domain facts, relationships, nodes, community grouping, and inspectable evidence to an LLM answer, making it stronger than vector similarity when the answer depends on connected structure. 09:23-10:30

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [RAG stacks need modular baselines instead of one fixed recipe](rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md)
- [Hybrid retrieval should support filters and embedding migration](hybrid-retrieval-should-support-filters-and-embedding-migration.md)
- [Knowledge graphs make agent memory traversable and explainable](knowledge-graphs-make-agent-memory-traversable-and-explainable.md)

Sources:
- [HybridRAG: A Fusion of Graph and Vector Retrieval  - Mitesh Patel, NVIDIA](../sources/20250722_-tgQa8Fzf80.md), 01:28-04:38, 18:07-19:31
- [Context Engineering: Connecting the Dots with Graphs - Stephen Chin, Neo4j](../sources/20251124_LLuKshphGOE.md), 09:23-10:30
