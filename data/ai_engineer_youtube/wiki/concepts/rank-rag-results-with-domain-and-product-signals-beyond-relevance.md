# Rank RAG Results With Domain and Product Signals Beyond Relevance

Summary: Semantic relevance is only a proxy for the result an application should rank first. Production RAG ranking may need domain vocabulary, structured attributes, corpus prominence, popularity, price, merchant quality, and user-preference signals in addition to embedding or reranker relevance.

Use when:
- Search or RAG results are relevant but ordered poorly for the product task.
- A vertical domain has terms, constraints, or business signals that generic relevance models miss.

Details:
- Standard embeddings and rerankers mostly measure semantic similarity; the application may need information needs that are not captured by relevance alone (07:02-07:21).
- Domain-specific vocabulary can make generic relevance fail: legal meanings of words such as "moot" or "material" can differ from general-language semantics, so query sets should expose whether the vocabulary is out of distribution (08:13-08:49).
- Product ranking can require signals that are not semantic, such as price thresholds, merchant signals, podcast listens, popularity, or PageRank-style prominence from the structure of the corpus (09:43-10:35).
- User behavior adds another layer: clicks and other preference signals can change ranking after the system already understands relevance and domain signals (11:05-12:17).

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Decompose Domain RAG by Query Structure and Corpus Scale](decompose-domain-rag-by-query-structure-and-corpus-scale.md)
- [Build Scoring Systems From Inspectable Quality Signals](build-scoring-systems-from-inspectable-quality-signals.md)

Sources:
- [Layering every technique in RAG, one query at a time - David Karam, Pi Labs (fmr. Google Search)](../sources/20250729_w9u11ioHGA0.md), 07:02-12:17
