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
- **A shipped implementation of exactly this cost function, with the scoring inputs named.** llm-d's router carries pluggable *endpoint picker* (EP) plugins that "continuously probe each pod's vLLM metrics to score each pod on running and waiting requests, the KV cache utilization, also prefix cache availability," then "schedule requests to the optimal pod with the lowest load and also highest possibility of a cache hit" — the load term and the locality term this page argues for, made concrete as four probe signals. A four-turn demo shows the resulting behaviour: the cold first request takes "roughly 3 seconds"; a second turn with the same system prompt lands on "exactly the same" pod address and takes "about one second"; a third turn with a *different* system prompt goes to a different pod and pays the full 3 seconds; changing only the user prompt returns to the cached pod and ~1 second. Routing is therefore pod affinity, not just cache lookup — the request follows the state. Unquantified: the probe overhead, the staleness window, and what the scorer does when the cache-richest pod is also the busiest. ([Fama](../sources/20260827_YXowceUKYJI.md), 06:28-07:12, 07:44-08:53)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [KV-cache hit rate is a production agent SLO](kv-cache-hit-rate-is-a-production-agent-slo.md)
- [Size KV-cache memory tiers with workload-shaped benchmarks](size-kv-cache-memory-tiers-with-workload-shaped-benchmarks.md)
- [Disaggregate prefill and decode workers by workload shape](disaggregate-prefill-and-decode-workers-by-workload-shape.md)
- [Match the Inference Lever to the Latency Metric It Moves](match-the-inference-lever-to-the-latency-metric-it-moves.md)

Sources:
- [Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA](../sources/20250801_Y2qc0UhDSnc.md), 11:03-13:01
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 06:28-07:12, 07:44-08:53
