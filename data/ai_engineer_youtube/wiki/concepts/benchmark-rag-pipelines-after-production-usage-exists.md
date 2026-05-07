# Benchmark RAG Pipelines After Production Usage Exists

Summary: Early RAG builds can prioritize a product-requirement-satisfying baseline, then benchmark and optimize once real usage reveals source types, queries, hallucinations, cost shape, and failure modes. This is a pragmatic sequencing rule, not an excuse to ignore accuracy once users depend on the system.

Use when:
- Building a RAG feature before realistic production usage and query distribution are known.
- Deciding when to benchmark parsing vendors, chunking strategies, vector stores, hybrid search, and cost.
- Planning post-launch improvement loops for hallucinations, parser quality, graph/vector retrieval, and pipeline cost.

Details:
- 11x initially selected parsing vendors for resource support, Markdown output, and webhooks, while not considering accuracy, comprehensiveness, or cost deeply because the system was pre-production and usage was unknown. (09:48-10:56)
- The talk explicitly calls this gap out: accuracy means extracted output matching the original resource, while comprehensiveness means how much source information is available in the parsed output. (10:12-10:39)
- The recommended sequence is to get something into production that satisfies product requirements, then establish real benchmarks for iteration and improvement. (21:08-21:27)
- Planned follow-up work included tracking email hallucinations, evaluating parsing vendors on accuracy and completeness, experimenting with hybrid RAG by adding a graph database beside the vector database, and reducing pipeline cost. (21:42-22:00)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [RAG stacks need modular baselines instead of one fixed recipe](rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md)
- [Use fast query-document evals for retrieval changes](use-fast-query-document-evals-for-retrieval-changes.md)
- [Hybrid retrieval should support filters and embedding migration](hybrid-retrieval-should-support-filters-and-embedding-migration.md)

Sources:
- [Building Alice's Brain: an AI Sales Rep that Learns Like a Human - Sherwood & Satwik, 11x](../sources/20250729_KWmkMV0FNwQ.md), 09:48-10:56, 21:08-22:00
