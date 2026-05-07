# Decompose Domain RAG by Query Structure and Corpus Scale

Summary: Expert-domain RAG should model the corpus shape, query structure, and domain vocabulary before choosing retrieval components. Legal RAG can involve uploads, project vaults, and global corpora whose queries mix date filters, named regulations, multiple provisions, and domain jargon.

Use when:
- Designing retrieval for legal, tax, compliance, or other expert corpora.
- Deciding whether a generic vector search recipe is too shallow for the query patterns.

Details:
- Harvey frames legal retrieval across three scales: small on-demand uploads, project vaults such as deal rooms or litigation collections, and large corpora such as legislation, case law, tax, and regulation sources; each scale changes retrieval and filtering requirements.
- Domain-specific queries may combine semantic intent with hard constraints such as jurisdiction, applicability date, named directive IDs, multiple articles or regulations, and abbreviations that only domain experts recognize.
- Engineers should work with domain experts to translate legal structure into representation, indexing, querying, preprocessing, categorization, and heuristics rather than treating dense retrieval as the whole solution.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Structure-Aware Document Parsing Improves RAG Chunk Quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)
- [Hybrid Retrieval Should Support Filters And Embedding Migration](hybrid-retrieval-should-support-filters-and-embedding-migration.md)

Sources:
- [Scaling Enterprise-Grade RAG: Lessons from Legal Frontier - Calvin Qi (Harvey), Chang She (Lance)](../sources/20250729_W1MiZChnkfA.md), 01:23-04:37
