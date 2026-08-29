# Size KV-cache memory tiers with workload-shaped benchmarks

Summary: KV-cache infrastructure should be sized with load tests that match agent working sets, cache TTLs, prefill/decode behavior, concurrency ramps, and memory-tier throughput instead of relying on raw storage capacity alone.

Use when:
- Comparing HBM, DRAM, NVMe-backed, or offloaded KV-cache tiers for agent workloads.
- Designing benchmarks for context-platform capacity, latency, and throughput SLOs.

Details:
- Cache TTL affects both hit rate and memory footprint: one-minute TTLs can thrash when request gaps exceed a minute, while longer TTLs improve hits but require holding more tokens in cache (11:07-12:49).
- Working-set and cache-hit curves are not linear; they vary with context length, accelerator choice, prefill/decode architecture, and memory-tier behavior (14:23-14:53).
- Useful token storage needs enough capacity plus fast writes and reads; otherwise the system drops KVs before they are stored, blocks GPUs, or cannot fetch cached tokens fast enough to affect inference (16:05-17:00).
- WEKA's benchmark framing ramps coding-agent user pools, compares memory-tier configurations, and measures whether systems maintain output tokens and concurrency as HBM advantages fade and lower tiers carry more of the working set (18:46-22:58).
- Agent tool waits create a concrete tiering case: if the runtime knows a tool call will take about 30 seconds, it can move KV state from GPU memory to host memory and restore it before the next LLM call instead of losing the cached prefill work (16:14-17:40).
- **The tier stack and the eviction policies a second vendor converged on.** Beneath llm-d's router, the cache-management layer treats agentic sessions as hot/warm/cold and offloads to NVMe SSD and the XFS filesystem alongside KV-centric stores such as Mooncake, with "smarter and session-aware eviction policies such as priority and also session pinning to ensure this really important context persists exactly when and where it's needed." Session pinning is the policy that TTL tuning approximates: rather than guessing a lifetime, it names the session whose state must survive. The tiering exists for the same reason this page's TTL analysis does — the client owns the prompt lifecycle, so the server cannot predict which prefix returns. ([Fama](../sources/20260827_YXowceUKYJI.md), 07:12-07:44)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [KV-cache hit rate is a production agent SLO](kv-cache-hit-rate-is-a-production-agent-slo.md)
- [Make local inference benchmarks reproducible artifacts](make-local-inference-benchmarks-reproducible-artifacts.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)
- [Client-Controlled Context Makes the Server's KV Cache Volatile](client-controlled-context-makes-the-servers-kv-cache-volatile.md)

Sources:
- [Context Platform Engineering to Reduce Token Anxiety - Val Bercovici, WEKA](../sources/20251124_NTBX-wxUhHs.md), 11:07-12:49, 14:23-17:00, 18:46-22:58
- [Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA](../sources/20250801_Y2qc0UhDSnc.md), 16:14-17:40
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 07:12-07:44
