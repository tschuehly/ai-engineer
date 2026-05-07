# Hybrid Retrieval Combines Lexical, Sparse, Dense, and Reranking Signals

Summary: Hybrid retrieval combines more than one retrieval mechanism for the same search, such as keyword, learned sparse, dense vector, or multiple dense models. RRF and rerankers are practical ways to merge and reorder those candidate sets when raw scores are not directly comparable.

Use when:
- Building RAG over mixed query shapes where exact names and semantic paraphrases both matter.
- Deciding how to combine keyword search, vector search, filters, RRF, and reranking.

Details:
- Krenn defines hybrid search broadly: combining more than one search type for a single search, including sparse plus dense, dense plus keyword, or multiple dense-vector searches. 01:21:30-01:22:35
- Reciprocal rank fusion blends results by each mechanism's rank position instead of assuming lexical, sparse, and dense scores are on the same scale. 01:22:37-01:23:07
- The source challenges vector-only RAG: if users search for a specific brand or known term, vector retrieval may miss text that keyword search would return, creating a visibly bad experience. 01:27:30-01:28:08
- Query shape can route retrieval strategy; one- or two-word queries may fit keyword search, while longer contextual queries may benefit from vector retrieval. 01:28:32-01:29:00
- Rerankers can rescore candidates from lexical or hybrid retrieval, not only vector retrieval, and can improve eval scores when applied to existing customer datasets. 01:37:30-01:38:55

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [BM25 Scores Lexical Retrieval With Frequency, Rarity, and Field Length](bm25-scores-lexical-retrieval-with-frequency-rarity-and-field-length.md)
- [Choose Lexical, Vector, and Reranking Retrieval by Query Shape](choose-lexical-vector-and-reranking-retrieval-by-query-shape.md)
- [Hybrid Retrieval Should Support Filters And Embedding Migration](hybrid-retrieval-should-support-filters-and-embedding-migration.md)

Sources:
- [Information Retrieval from the Ground Up - Philipp Krenn, Elastic](../sources/20250727_4Xe_iMYxBQc.md), 01:21:30-01:23:07, 01:27:30-01:29:00, 01:37:30-01:38:55
