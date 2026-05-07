# BM25 Scores Lexical Retrieval With Frequency, Rarity, and Field Length

Summary: BM25 is a lexical relevance function that scores exact-term retrieval with term frequency saturation, inverse document frequency, and field-length normalization. It remains useful for RAG because exact names, brands, identifiers, and short keyword queries can be poorly served by vector similarity alone.

Use when:
- Diagnosing why keyword search ranked one chunk above another.
- Deciding whether exact-term retrieval should remain in a RAG stack alongside embeddings.

Details:
- Krenn describes BM25 as the current "best match" implementation in the TF-IDF family. 39:05-39:17
- Term frequency helps when the query term appears more often, but BM25 saturates the benefit so a document does not become indefinitely more relevant just by repeating the same word. 39:20-39:53
- Inverse document frequency boosts rare terms and demotes very common terms because rarity is treated as a relevance signal. 39:56-40:23
- Field-length normalization makes a match in a shorter field, such as a title, more relevant than the same match buried in a long body field. 40:29-40:49
- The workshop warns that some storage layers with vector extensions may not implement full BM25 because they may not keep the needed lexical statistics. 01:27:11-01:27:19

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Choose Lexical, Vector, and Reranking Retrieval by Query Shape](choose-lexical-vector-and-reranking-retrieval-by-query-shape.md)
- [Hybrid Retrieval Combines Lexical, Sparse, Dense, and Reranking Signals](hybrid-retrieval-combines-lexical-sparse-dense-and-reranking-signals.md)

Sources:
- [Information Retrieval from the Ground Up - Philipp Krenn, Elastic](../sources/20250727_4Xe_iMYxBQc.md), 39:05-40:49, 01:27:11-01:27:19
