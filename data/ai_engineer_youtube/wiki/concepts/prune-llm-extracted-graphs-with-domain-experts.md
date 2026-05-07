# Prune LLM-Extracted Graphs With Domain Experts

Summary: LLM graph extraction should be treated as a draft graph, not the final knowledge model. Domain experts still need to shape the taxonomy and remove noisy relationships before the graph supports reliable retrieval or advisory decisions.

Use when:
- Building a knowledge graph from unstructured text with LLM graph transformers.
- Evaluating whether a graph-backed RAG or KAG system is reliable enough for expert-facing decisions.

Details:
- The talk contrasts fully automated LLM graph-transformer extraction with a manual path, then recommends a hybrid model: extract the graph with an LLM and ask experts to build the taxonomy and prune the graph. 16:46-17:12
- Pruning means removing relationships that do not belong in the expert decision model before they pollute downstream retrieval and recommendations. 17:03-17:12
- The reported benchmark dimensions for the graph-backed system include accuracy, flexibility, deterministic reproducibility, traceability, and scalability, which are useful evaluation axes for graph construction quality. 17:14-17:39

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Treat ontology and triplet quality as GraphRAG bottlenecks](treat-ontology-and-triplet-quality-as-graphrag-bottlenecks.md)
- [Continuously reconcile eval datasets with user reality](continuously-reconcile-eval-datasets-with-user-reality.md)

Sources:
- [Wisdom-Driven Knowledge Augmented Generation at Scale - Chin Keong Lam, Patho AI](../sources/20250822_9AQOvT8LnMI.md), 16:46-17:39
