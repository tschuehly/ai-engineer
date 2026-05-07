# Search Engines Shift Retrieval Work to Ingestion

Summary: Search engines make retrieval fast by analyzing documents when they are indexed, not by waiting until query time to parse every document. Tokenization, offsets, positions, and inverted-index postings become reusable retrieval metadata for highlighting, phrase search, and fast candidate lookup.

Use when:
- Designing a retrieval system that needs explainable matches, snippets, or phrase queries.
- Comparing search-engine indexing with database-style storage for RAG infrastructure.

Details:
- Krenn distinguishes search engines from ordinary databases by saying search engines do much of the work at ingestion: they break text into tokens, compute offsets, and store positions so long documents do not need to be reanalyzed for every match. 07:17-08:41
- Offsets support hit highlighting because the engine can point back to where a matched token appeared in the original text. 07:39-08:08
- Token positions support phrase-style retrieval because the engine can check whether one word follows another. 08:41-09:04
- The inverted index stores analyzed tokens with pointers to document IDs, occurrence counts, and positions; retrieval then jumps from query token to matching documents instead of scanning the whole corpus. 22:14-23:24

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [BM25 Scores Lexical Retrieval With Frequency, Rarity, and Field Length](bm25-scores-lexical-retrieval-with-frequency-rarity-and-field-length.md)
- [Structure-Aware Document Parsing Improves RAG Chunk Quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)

Sources:
- [Information Retrieval from the Ground Up - Philipp Krenn, Elastic](../sources/20250727_4Xe_iMYxBQc.md), 07:17-08:41, 22:14-23:24
