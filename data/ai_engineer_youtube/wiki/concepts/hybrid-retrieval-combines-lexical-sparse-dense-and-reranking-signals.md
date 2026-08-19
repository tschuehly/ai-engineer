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
- A framework-free build confirms the pattern end to end: pgvector nearest-neighbor semantic search returns "close" meanings while BM25 keyword search returns "exact" matches (product name, SKU, brand, medication, ID, language filter), so medical/product chatbots need both; RRF fuses the two candidate sets in SQL and a reranker rescores to the final top-N. (Matini 29:22-34:25)
- A production education assistant runs the same shape and adds a scale argument for it: a user-selected source filter, then a Cohere embedding model plus a BM25 keyword index to top 30 each, merged and reranked to top 5, with a hard 100,000-token cap that drops trailing chunks — over an 8-million-token corpus of course lessons and public library docs. The configuration "is not random"; it came from a separate sweep optimized on recall (did it retrieve the correct page). Their reason for keeping BM25 is measured, not stylistic: dense retrieval fell to 0% recall on facts buried at 400k tokens where BM25 held 100%. ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 24:43-27:05, 58:31-59:30)
- Top-K should be tuned by use case, not fixed: product catalogs retrieve more (else same-brand products never surface or sell) while medical retrieves fewer for accuracy and liability; too many results (e.g. top-20) confuse the user. (Matini 30:37-33:46)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [BM25 Scores Lexical Retrieval With Frequency, Rarity, and Field Length](bm25-scores-lexical-retrieval-with-frequency-rarity-and-field-length.md)
- [Choose Lexical, Vector, and Reranking Retrieval by Query Shape](choose-lexical-vector-and-reranking-retrieval-by-query-shape.md)
- [Hybrid Retrieval Should Support Filters And Embedding Migration](hybrid-retrieval-should-support-filters-and-embedding-migration.md)
- [Dense Retrieval Collapses on Buried Facts as the Haystack Grows](dense-retrieval-collapses-on-buried-facts-as-the-haystack-grows.md)

Sources:
- [Information Retrieval from the Ground Up - Philipp Krenn, Elastic](../sources/20250727_4Xe_iMYxBQc.md), 01:21:30-01:23:07, 01:27:30-01:29:00, 01:37:30-01:38:55
- [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry - Abed Matini, Ogilvy](../sources/20260628_Akm1sqvWG4A.md), 29:22-34:25
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 24:43-27:05, 58:31-59:30
