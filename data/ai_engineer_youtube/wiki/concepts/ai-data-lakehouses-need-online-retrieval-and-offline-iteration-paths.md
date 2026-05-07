# AI Data Lakehouses Need Online Retrieval and Offline Iteration Paths

Summary: Large-scale AI data infrastructure should support low-latency retrieval, large offline ingestion, experimentation, analytics, and training from a shared data substrate. Separating compute, memory, and storage over object storage can reduce duplicate AI-data copies while preserving online and offline workloads.

Use when:
- Choosing storage and indexing architecture for large multimodal RAG systems.
- Planning how retrieval, analytics, preprocessing, and training should share AI data.

Details:
- LanceDB describes a lakehouse-style architecture where data on object storage can support search and retrieval workloads, analytical workloads, training, preprocessing, and feature engineering.
- Online serving needs low-latency querying, while offline work needs ingestion, reingestion, and ML experiments across variations; large legal corpora can reach tens of millions of large documents.
- LanceDB's distributed architecture is presented as combining multiple vector columns, vector search, full-text search, and reranking behind Python or TypeScript APIs, with compute/memory/storage separation for cloud object storage.
- The underlying Lance format is positioned as an AI-data format for mixed blobs and scalars: images, video, audio, embeddings, text, tabular, and time-series data can stay in one table instead of being copied across disconnected systems.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Hybrid Retrieval Should Support Filters And Embedding Migration](hybrid-retrieval-should-support-filters-and-embedding-migration.md)
- [Use omnimodal embeddings for cross-modal retrieval and comparison](use-omnimodal-embeddings-for-cross-modal-retrieval-and-comparison.md)

Sources:
- [Scaling Enterprise-Grade RAG: Lessons from Legal Frontier - Calvin Qi (Harvey), Chang She (Lance)](../sources/20250729_W1MiZChnkfA.md), 06:11-07:10, 09:58-14:55
