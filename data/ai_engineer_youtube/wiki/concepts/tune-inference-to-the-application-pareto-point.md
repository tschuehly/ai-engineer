# Tune inference to the application Pareto point

Summary: Production inference should be optimized for the application's required operating point across quality, latency, and cost rather than for one generic model-serving metric.

Use when:
- Choosing model, runtime, retrieval, reasoning, quantization, or batching strategy for a product workload.
- Explaining why the same model deployment shape may be wrong for tab completion, robotics, async coding agents, or high-value scientific work.

Details:
- Kranen frames deployability as whether the model plus surrounding system can meet quality, latency, and per-request cost constraints for the target application (01:31-02:08).
- The desired Pareto point is application-specific: personal cancer-cure research may tolerate high latency and cost for quality, tab completion depends on fast response, and async code-commit agents can trade latency for quality and cost (03:04-04:32).
- Frontier-shifting techniques compose: RAG can raise quality while increasing latency and cost, reasoning spends more tokens for quality, and quantization can recover latency and cost by allowing higher batch sizes (04:35-06:01).
- **Two configurations that disagree about where the Pareto point is, on the same technique.** Red Hat runs aggregated and disaggregated serving side by side and reports "classic Pareto curves": on 16 H100s (4 replicas at TP4 versus 2 prefill + 2 decode) disaggregation is "very similar to the aggregated config at the lower concurrency regimes and very similar at the higher concurrency regimes, but it's actually the middle part of the concurrency regime that PD actually shines," while on 64 H100s (8 replicas at TP8 versus 3 prefill + 5 decode) with a prefill-heavy 5,000/500 token workload the PD curve "dominates… across the entire interactivity spectrum." The transferable lesson is not which shape is right — it is that the operating point at which you benchmark decides whether a technique looks free or useless, and both of these are the same technique. ([Kamra](../sources/20260827_YXowceUKYJI.md), 13:52-15:35)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Treat quantization as a memory-bandwidth lever](treat-quantization-as-a-memory-bandwidth-lever.md)
- [Plan AI products for a multimodel market](plan-ai-products-for-a-multimodel-market.md)
- [Disaggregation Needs a Fabric, and Pays Off in the Middle Concurrency Band](disaggregation-needs-a-fabric-and-pays-off-in-the-middle-band.md)

Sources:
- [Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA](../sources/20250801_Y2qc0UhDSnc.md), 01:31-06:01
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 13:52-15:35
