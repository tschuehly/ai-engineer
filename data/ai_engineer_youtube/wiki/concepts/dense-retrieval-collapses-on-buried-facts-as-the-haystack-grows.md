# Dense Retrieval Collapses on Buried Facts as the Haystack Grows

Summary: Semantic retrieval degrades non-linearly with haystack size on facts buried in the middle. Measured on the same probe at increasing scale, dense retrieval held around 80% recall from 50k to 200k tokens and then fell to 0% at 400k, while BM25 returned the fact 100% of the time at every size — which is a scale-dependent argument for hybrid search, not just a query-shape one.

Use when:
- A RAG system that tested well on a small corpus starts missing facts users know are in there.
- Justifying keyword retrieval alongside vectors to a team that considers BM25 legacy.
- Sizing how far a semantic-only index can be pushed before it needs a lexical partner.

Details:
- The measurement: dense (semantic) retrieval scored roughly 80% recall from 50k to 200k tokens, but at 400k it "was not able to [find] facts that were buried in the middle and it started giving us 0% recall," where BM25 "still got 100% every time." ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 58:31-59:30)
- The failure mode is a cliff, not a slope: 80% at 200k to 0% at 400k means a system validated at one corpus size gives no warning before it stops working at another. Recall against corpus size is a curve worth measuring, not a single number.
- The distinguishing property is the same one that separates surviving from degrading facts in long context — distinctiveness. A fact with a rare exact term is what BM25 is built to find; a fact expressed only semantically is what has no lexical anchor to fall back on when the embedding space gets crowded. (53:16-54:33, 58:31-59:30)
- This is why the production tutor runs hybrid search rather than semantic search alone: a Cohere embedding model plus a BM25 keyword index to top 30 each, merged, then reranked to top 5. The presenters draw the causal line explicitly — "semantic search on its own is not enough and that's why we're actually using a hybrid search." (25:30-27:05, 59:15-59:30)
- The existing query-shape argument for hybrid retrieval (exact names and IDs need lexical, paraphrase needs dense) is orthogonal to this one and stacks with it: even for queries where dense is the right mechanism, dense stops working past a corpus scale where lexical does not.
- Practical caveat: the source reports the recall numbers and the sizes but not the embedding model used for the long-context probe, the chunking scheme, or whether reranking was applied, so treat 400k as "there is a cliff and you should find yours" rather than as a portable threshold.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Hybrid Retrieval Combines Lexical, Sparse, Dense, and Reranking Signals](hybrid-retrieval-combines-lexical-sparse-dense-and-reranking-signals.md)
- [Choose Lexical, Vector, and Reranking Retrieval by Query Shape](choose-lexical-vector-and-reranking-retrieval-by-query-shape.md)
- [BM25 Scores Lexical Retrieval With Frequency, Rarity, and Field Length](bm25-scores-lexical-retrieval-with-frequency-rarity-and-field-length.md)
- [Full History Recalls Details That Summaries Delete](full-history-recalls-details-that-summaries-delete.md)
- [Local Deployment Inverts the Keep-Everything Context Strategy](local-deployment-inverts-the-keep-everything-context-strategy.md)

Sources:
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 25:30-27:05, 53:16-54:33, 58:31-59:30
