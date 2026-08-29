# Production Inference Combines Model Support With Cluster Operations

Summary: Production inference is a combined model-support and infrastructure problem. It must handle architecture-specific model behavior while also providing routing, queueing, autoscaling, monitoring, GPU provisioning, and deployable packaging.

Use when:
- An inference system needs to serve many open-source or task-specific models rather than one fixed model.
- A prototype built with a model runtime or API wrapper must become observable, autoscaled, and resource-efficient in production.

Details:
- Model support is necessary because open-source small models are numerous, improving quickly, and can outperform managed services on narrow tasks. (09:45-11:07)
- BERT, Qwen, ModernBERT, ColBERT, cross-encoders, and rerankers may differ in attention implementation, positional embeddings, normalization, output shape, and score-vs-vector outputs. (11:18-13:35)
- Efficient support may require adapting the forward pass, variable-length flash attention, padding strategy, query/key/value fusion, and model-specific positional encoding behavior. (11:56-14:20)
- Infrastructure support includes API primitives such as `encode`, `score`, and `extract`, plus routing, queueing, GPU pools, spot instances, Prometheus metrics, Grafana, KEDA autoscaling, Terraform, Helm charts, and Docker images. (14:47-16:09)
- **The cluster-operations half, in Kubernetes primitives.** llm-d expresses the same combination as custom workload APIs rather than generic deployments: LeaderWorkerSet and DisaggregatedSet orchestrate multi-node model execution, autoscalers watch "capacity bounds and real-time traffic mixes" to scale pools independently, and a router with endpoint-picker plugins probes each vLLM pod's metrics to place requests. The framework is CNCF-hosted and Kubernetes-native but now runs off-Kubernetes too — evidence that the operations layer, not the scheduler, is the durable part. ([Kamra](../sources/20260827_YXowceUKYJI.md), 09:28-10:20)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Hot-swap small models to avoid one-model-per-GPU waste](hot-swap-small-models-to-avoid-one-model-per-gpu-waste.md)
- [Route inference requests by KV locality and worker load](route-inference-requests-by-kv-locality-and-worker-load.md)

Sources:
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md), 09:45-16:09
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 09:28-10:20
