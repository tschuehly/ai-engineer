# Hybrid Retrieval Should Support Filters And Embedding Migration

Summary: Production RAG retrieval should combine semantic, lexical, metadata, and operational indexing choices rather than depending only on one vector index. Supporting multiple embedding models, filters, and disk-backed vector indexes helps teams tune relevance, scope retrieval, and migrate models without freezing the system.

Use when:
- Choosing retrieval infrastructure for a RAG application with changing embeddings or scoped knowledge collections.
- Designing search controls for users who need to query specific document sets.

Details:
- OpenRAG uses OpenSearch for hybrid vector and keyword search, configurable filtering, and aggregation instead of treating vector search as the whole retrieval layer.
- It supports vector search across multiple embedding models; the talk notes this can slow search, but helps when migrating embedding models within a running system.
- OpenRAG uses the JVector KNN plugin by default. JVector supports live indexing and disk-KNN architecture so the whole index does not need to fit in memory.
- The demo exposes knowledge filters in the UI so chat queries can target selected documents or document groups.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Adapt embedding dimensions with Matryoshka representation learning](adapt-embedding-dimensions-with-matryoshka-representation-learning.md)
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)

Sources:
- [OpenRAG: An open-source stack for RAG - Phil Nash](../sources/20260408_4TxOBhDRRCM.md), 05:39-06:48, 09:29-10:14
