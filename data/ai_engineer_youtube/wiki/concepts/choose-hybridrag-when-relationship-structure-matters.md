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
- A negative datapoint that supports the "justify it by the question set" rule: Towards AI compared GraphRAG against plain RAG for their AI tutor and found it "way costlier to set up and just [a] tie on the results" on evaluations built from real user questions, so they did not adopt it. They keep the same caveat this page states — a very large dataset with genuinely interconnected topics might change the answer, so it is still worth testing rather than assuming either way. ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 11:55-12:58)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [RAG stacks need modular baselines instead of one fixed recipe](rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md)
- [Hybrid retrieval should support filters and embedding migration](hybrid-retrieval-should-support-filters-and-embedding-migration.md)
- [Knowledge graphs make agent memory traversable and explainable](knowledge-graphs-make-agent-memory-traversable-and-explainable.md)
- [Measure Agentic Knowledge-Base Browsing Before Adding It](measure-agentic-knowledge-base-browsing-before-adding-it.md)

Sources:
- [HybridRAG: A Fusion of Graph and Vector Retrieval  - Mitesh Patel, NVIDIA](../sources/20250722_-tgQa8Fzf80.md), 01:28-04:38, 18:07-19:31
- [Context Engineering: Connecting the Dots with Graphs - Stephen Chin, Neo4j](../sources/20251124_LLuKshphGOE.md), 09:23-10:30
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 11:55-12:58
