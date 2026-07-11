# Shard Cache-Augmented Generation Into Parallel Buckets With a Supervisor

Summary: Extended Cache Augmented Generation (ECAG) answers global questions over an all-relevant, fast-churning corpus by sharding documents across many parallel cached-context "buckets" and letting a supervisor model interrogate the buckets and synthesize. It fits the gap where top-k RAG cannot select a subset, GraphRAG is too expensive to recompute, and a single CAG context window overfills and degrades.

Use when:
- Every document in a collection is relevant to a set of global questions, so top-k similarity retrieval cannot pick a useful subset.
- The corpus is deeply interconnected and gets fully replaced very fast, so recomputing a knowledge graph on each update is too expensive.
- A single large-context (CAG) load degrades answer quality because the context window is overfilled.

Details:
- The problem shape is specific: all documents relevant to a global question, deeply interconnected, and obsolete/replaced very fast. Match the retrieval strategy to those corpus dynamics rather than defaulting to one recipe. 00:24-00:44
- Simple RAG (vector DB + embedding model) inserts fast, so replacing an obsolete collection is cheap — but when *all* documents matter, similarity-threshold retrieval cannot select a subset and you cannot dump the whole collection into the LLM either. 00:46-01:54
- GraphRAG (LLM extracts entities/relationships → knowledge graph → navigate to synthesize a cross-collection answer) is excellent for rarely-changing corpora, but recomputing the graph on every replacement is computationally very expensive and slow. 01:55-03:08
- CAG (Cache Augmented Generation) loads all documents into a large-context model and caches the context by storing the model's KV matrix, avoiding re-reading; but a limited context window means overfilling degrades answer quality. 03:08-03:46
- ECAG shards documents across multiple CAG caches ("context buckets") run in parallel; each cache answers questions about its own content, and a smarter supervisor model asks the right questions to the right buckets, explores them to progressively build understanding, asks follow-up questions when something looks interesting, and synthesizes the final answer. 03:46-05:00
- Because the caches load in parallel, ECAG's knowledge-building is significantly faster than GraphRAG while providing more accurate answers than simple RAG. 04:52-05:06
- KV cache is expensive; cost is reduced by optimizing how long each cache lives (cache lifetime/TTL), and there is no one-size-fits-all — every retrieval strategy trades compute, cost, and speed. 05:06-05:34

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Distribute Documents Across Cache Buckets in No Particular Order](distribute-documents-across-cache-buckets-in-no-particular-order.md)
- [Choose HybridRAG when relationship structure matters](choose-hybridrag-when-relationship-structure-matters.md)
- [Balance GraphRAG hop depth against production latency](balance-graphrag-hop-depth-against-production-latency.md)
- [RAG stacks need modular baselines instead of one fixed recipe](rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md)

Sources:
- [When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis](../sources/20260628_XovaGv4f39A.md), 00:24-05:34
