# Treat Ontology And Triplet Quality As GraphRAG Bottlenecks

Summary: GraphRAG quality depends on how well the system extracts domain entities, relationship labels, and entity-relationship-entity triplets from source data. A weak ontology or noisy triplets make the downstream graph retrieval noisy even if the graph database and LLM are strong.

Use when:
- Building a knowledge graph from unstructured documents for retrieval.
- Debugging GraphRAG systems whose answers miss relationships or retrieve noisy graph paths.

Details:
- The talk frames triplet extraction as difficult enough to justify LLM-based extraction, but only when the prompt is tightly defined around the use case and ontology. 05:18-07:07
- The ontology should be domain-specific and included in the extraction prompt so the LLM structures outputs into useful triplets rather than generic text summaries. 06:41-07:07
- Patel warns that if the ontology or triplets are wrong or noisy, retrieval will be noisy; he expects teams to iterate heavily on this step. 07:09-07:41
- Practical optimization knobs include cleaning irrelevant characters, constraining overly long outputs, and fine-tuning the extraction model; in the reported experiment, LoRA fine-tuning improved Llama-based extraction from about 71% to 87% accuracy on a 100-document test. 14:21-16:47

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Structure-aware document parsing improves RAG chunk quality](structure-aware-document-parsing-improves-rag-chunk-quality.md)

Sources:
- [HybridRAG: A Fusion of Graph and Vector Retrieval  - Mitesh Patel, NVIDIA](../sources/20250722_-tgQa8Fzf80.md), 05:18-07:41, 14:21-16:47
