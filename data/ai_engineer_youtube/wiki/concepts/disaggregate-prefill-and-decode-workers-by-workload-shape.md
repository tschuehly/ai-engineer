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
- **The mechanism named, and the metric it defends.** Red Hat calls colocation *phase interference* and derives it from hardware: prefill "wants high compute… is highly bursty… utilizes GPUs at high FLOPs and thrives on large batch parallelism," while decode "is generating one token at a time and it's more memory bandwidth hungry… highly latency sensitive and requires heavy cache residency." The concrete failure is a tail-latency one: "if there's a sudden influx of a long prefill prompt, it will completely stall the ongoing decode token generation process causing massive problems and jitter in user streaming latency." So the metric disaggregation defends is inter-token latency, not time-to-first-token — measured at P99 ITL falling from ~900 ms aggregated to ~100 ms disaggregated, and visibly smoother, on gpt-oss across 16 H100s (4 replicas at TP4 versus 2 prefill + 2 decode at TP4) with a 10,000-token prefix and 128 tokens per turn. ([Kamra](../sources/20260827_YXowceUKYJI.md), 10:20-11:56, 12:59-13:52)
- **The trend line past prefill/decode: disaggregation across different hardware backends.** Arora describes the direction of travel as inference systems that "increasingly disaggregate different steps of inference across different hardware backends. So you could run speculative decoding on some hardware, decode on different hardware, prefill on different hardware," alongside KV cache memory that is "forked across GPU, CPU, disk and remote machines." That generalizes this page's two-pool split into an n-way placement problem, and it raises the interconnect stakes correspondingly — every additional split is another state transfer over the fabric. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 08:19-09:02)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)
- [Size KV-cache memory tiers with workload-shaped benchmarks](size-kv-cache-memory-tiers-with-workload-shaped-benchmarks.md)
- [Autoscale specialized inference workers as traffic mix changes](autoscale-specialized-inference-workers-as-traffic-mix-changes.md)
- [Disaggregation Needs a Fabric, and Pays Off in the Middle Concurrency Band](disaggregation-needs-a-fabric-and-pays-off-in-the-middle-band.md)
- [Measure Multi-GPU Headroom Against a Communication-Aware Roofline](measure-multi-gpu-headroom-against-a-communication-aware-roofline.md)

Sources:
- [Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA](../sources/20250801_Y2qc0UhDSnc.md), 06:23-10:58
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 10:20-11:56, 12:59-13:52
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 08:19-09:02
