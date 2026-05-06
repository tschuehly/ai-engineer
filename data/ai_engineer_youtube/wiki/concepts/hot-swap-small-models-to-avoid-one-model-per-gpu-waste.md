# Hot-Swap Small Models to Avoid One-Model-Per-GPU Waste

Summary: Small-model inference infrastructure should dynamically load, unload, and hot-swap models rather than pinning each model to a dedicated GPU. This raises utilization when embeddings, rerankers, NER models, and other small models each occupy only a small amount of memory.

Use when:
- Many small task-specific models share a fleet but individual model traffic is bursty or uneven.
- GPU memory is underused because each model is deployed in its own container or on its own accelerator.

Details:
- The talk names Stella embeddings, rerankers, and the GLiNER NER model as examples of models that may occupy only a few gigabytes each. (07:20-07:38)
- A one-model-per-GPU deployment leaves idle GPU capacity; swapping several models on one GPU can improve utilization and reduce cost. (07:39-08:05)
- Least-recently-used eviction is presented as a policy for quickly switching between models when workflows need different tools such as rerankers or other small models. (08:05-08:21)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)

Sources:
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md), 07:20-08:21
