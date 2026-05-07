# Route inference requests by KV locality and worker load

Summary: Distributed inference routers should consider both KV-cache locality and current worker load; maximizing prefix cache match alone can overload the workers that happen to hold useful KV state.

Use when:
- Building routing for prefill/decode disaggregated inference or KV-cache-aware serving.
- Diagnosing why cache-friendly routing still produces high queue depth or poor latency.

Details:
- Prefill/decode disaggregation requires transferring KV state between machines, and previous requests can leave useful KV state on GPU, host memory, or external storage (11:03-11:33).
- Naive random routing ignores this locality, while KV-only routing can bias too strongly toward machines with the best match and create queueing when those machines are already loaded (11:35-12:18).
- A smarter routing cost function should maximize prefix match from work already done on the node while also accounting for the node's existing load (12:18-12:36).
- As deployments scale, the amount of KV space represented locally across the fleet grows, making KV-cache hit rate a scale lever that reduces repeated prefill work over time (12:38-13:01).

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [KV-cache hit rate is a production agent SLO](kv-cache-hit-rate-is-a-production-agent-slo.md)
- [Size KV-cache memory tiers with workload-shaped benchmarks](size-kv-cache-memory-tiers-with-workload-shaped-benchmarks.md)
- [Disaggregate prefill and decode workers by workload shape](disaggregate-prefill-and-decode-workers-by-workload-shape.md)

Sources:
- [Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA](../sources/20250801_Y2qc0UhDSnc.md), 11:03-13:01
