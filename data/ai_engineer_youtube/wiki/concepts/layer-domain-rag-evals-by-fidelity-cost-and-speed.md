# Layer Domain RAG Evals by Fidelity, Cost, and Speed

Summary: Enterprise RAG evaluation should combine expensive expert review, curated expert criteria, and fast automated retrieval metrics. No single eval is enough when domain correctness depends on specialized knowledge and complex corpus structure.

Use when:
- Building an eval strategy for high-accuracy domain RAG.
- Balancing expert review capacity against fast iteration on retrievers, rerankers, and preprocessing.

Details:
- Harvey reports spending substantial effort on validation, not only on algorithms or agentic techniques, because engineers may not personally know the expert domain being retrieved.
- High-fidelity expert reviews of outputs and reports are expensive but provide quality signals that automated metrics cannot replace.
- Mid-cost evals can encode expert-labeled criteria for synthetic or automated checks, while fast quantitative metrics such as precision, recall, right-folder retrieval, right-section retrieval, and keyword presence support rapid retriever iteration.
- Good evaluation sets and procedures create the signal needed to move quickly as tools, model context windows, and retrieval paradigms change.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Use Fast Query-Document Evals for Retrieval Changes](use-fast-query-document-evals-for-retrieval-changes.md)
- [Domain evals need expert-built environments](domain-evals-need-expert-built-environments.md)

Sources:
- [Scaling Enterprise-Grade RAG: Lessons from Legal Frontier - Calvin Qi (Harvey), Chang She (Lance)](../sources/20250729_W1MiZChnkfA.md), 04:39-06:08, 15:36-16:05
