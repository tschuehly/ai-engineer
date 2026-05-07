# Patch-level visual embeddings trade ingest cost for query-time retrieval

Summary: ColPali-style retrieval embeds document-page image patches, so retrieval operates over many patch vectors rather than one vector per text chunk. The tradeoff is heavier ingestion and larger vector indexes, while query-time search can still use standard approximate-nearest-neighbor indexing.

Use when:
- Estimating storage, indexing, and latency costs for page-image retrieval.
- Explaining why visual retrieval over many page patches is not a brute-force scan over every image.

Details:
- The workshop describes each PDF page as an image that is split into patches before embedding, with one vector generated per patch, 20:56-21:44.
- Vector count grows with pages and patches: in the example, 15 patches on a page means 150 vectors for a 10-page document, 21:47-22:12.
- Debnath identifies model heaviness as the main ColPali drawback he has seen, especially during data ingestion when embeddings are created, 01:12:47-01:13:09.
- Query-time retrieval does not need to scan every page image directly; the vector database can use indexing techniques such as hierarchical navigable small-world style indexes, with vectors representing patches instead of text chunks, 01:13:13-01:14:10.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Treat PDF pages as visual retrieval units](treat-pdf-pages-as-visual-retrieval-units.md)
- [Hybrid retrieval should support filters and embedding migration](hybrid-retrieval-should-support-filters-and-embedding-migration.md)

Sources:
- [VoiceVision RAG - Integrating Visual Document Intelligence with Voice Response - Suman Debnath, AWS](../sources/20251206_hwCmfThIiS4.md), 20:56-22:12, 01:12:47-01:14:10
