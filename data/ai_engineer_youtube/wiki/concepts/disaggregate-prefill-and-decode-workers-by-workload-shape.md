# Disaggregate prefill and decode workers by workload shape

Summary: LLM inference can split prefill and decode onto separate worker pools because prefill and decode stress hardware differently and create scheduling conflicts when mixed on the same GPUs.

Use when:
- Designing a distributed inference deployment for long-context, interactive, or high-throughput workloads.
- Deciding whether prefill/decode disaggregation is worth the configuration complexity.

Details:
- KV caching creates two generation phases: prefill fills the cache for the prompt context, while decode generates new tokens and extends the cache during autoregressive output (06:23-07:06).
- Disaggregation moves those phases from the same GPUs onto different workers, allowing load matching because prefill is compute-bound while decode can be memory-bound depending on the model and application (07:06-08:09).
- Mixed prefill and decode on the same machine creates scheduling conflicts; separating them simplifies scheduling compared with in-flight batching or chunked prefill approaches, but worker counts must be tuned (08:10-10:30).
- The payoff depends on workload shape: low-input-length cases may see little speedup, interactive applications often fit the useful region, and the prefill/decode worker balance can starve decode workers or create queue depth when misconfigured (09:16-10:58).

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)
- [Size KV-cache memory tiers with workload-shaped benchmarks](size-kv-cache-memory-tiers-with-workload-shaped-benchmarks.md)
- [Autoscale specialized inference workers as traffic mix changes](autoscale-specialized-inference-workers-as-traffic-mix-changes.md)

Sources:
- [Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA](../sources/20250801_Y2qc0UhDSnc.md), 06:23-10:58
