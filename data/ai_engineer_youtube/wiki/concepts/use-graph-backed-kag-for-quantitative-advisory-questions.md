# Use Graph-Backed KAG For Quantitative Advisory Questions

Summary: Knowledge-Augmented Generation is useful when an advisory answer needs structured relationships, exact values, calculations, and evidence-backed recommendations. Vector retrieval can find relevant passages, but graph-backed retrieval can select structured facts and route them through deterministic computation.

Use when:
- A RAG system must answer competitive, financial, or operational questions that depend on exact numbers and multi-hop relationships.
- Debugging why vector RAG returns plausible passages but fails to produce a precise quantitative answer.

Details:
- The talk argues that vector stores are strong at semantic similarity but weak for complex numerical reasoning and calculations, which matters when marketing or competitive analysis depends on numbers. 14:03-14:28
- In the Apple revenue example, the desired flow is not passage retrieval; the query engine should select structured revenue figures from the graph and use a function call to compute the requested value. 14:29-15:16
- The speaker frames the resulting answer as evidence-based decision making because the recommendation is grounded in structured data, not only retrieved prose. 15:16-15:28
- For simpler product-information lookup, a Chroma-style vector database plus an LLM agent may be enough; graph DB, Cypher queries, and multi-hop loops become justified when questions ask how to beat a competitor based on current market share. 15:31-16:35

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Choose HybridRAG when relationship structure matters](choose-hybridrag-when-relationship-structure-matters.md)
- [Balance GraphRAG hop depth against production latency](balance-graphrag-hop-depth-against-production-latency.md)

Sources:
- [Wisdom-Driven Knowledge Augmented Generation at Scale - Chin Keong Lam, Patho AI](../sources/20250822_9AQOvT8LnMI.md), 11:38-16:35
