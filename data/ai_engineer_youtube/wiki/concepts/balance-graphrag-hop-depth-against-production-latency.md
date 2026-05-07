# Balance GraphRAG Hop Depth Against Production Latency

Summary: Graph retrieval can use deeper multi-hop traversal to expose indirect entity relationships, but each added hop can increase retrieval latency. Production GraphRAG systems need an explicit relevance-latency tradeoff rather than unbounded traversal.

Use when:
- Choosing graph traversal depth for GraphRAG or HybridRAG retrieval.
- Optimizing a graph-backed retrieval system for production latency.

Details:
- Single-hop graph retrieval can miss the main value of a graph: relationships that emerge through multiple connected nodes. 09:05-09:44
- Deeper traversal can provide better context, but it also increases retrieval time, so teams need a hop-depth sweet spot for the application latency budget. 09:46-10:31
- Graph acceleration can widen that budget. The talk cites cuGraph and its NetworkX integration as ways to accelerate graph algorithms over large graphs so systems can traverse more deeply with lower latency. 10:33-11:00, 16:56-18:00
- Evaluation should inspect both retrieval and response quality. The source names Ragas metrics such as faithfulness, answer relevancy, precision, and recall, and notes that Ragas evaluates the response, retrieval, and query path end to end. 11:16-12:29

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Build AI app benchmarks before optimization](build-ai-app-benchmarks-before-optimization.md)
- [Use local AI workstations when iteration, privacy, or latency dominate](use-local-ai-workstations-when-iteration-privacy-or-latency-dominate.md)

Sources:
- [HybridRAG: A Fusion of Graph and Vector Retrieval  - Mitesh Patel, NVIDIA](../sources/20250722_-tgQa8Fzf80.md), 09:05-12:29, 16:56-18:00
