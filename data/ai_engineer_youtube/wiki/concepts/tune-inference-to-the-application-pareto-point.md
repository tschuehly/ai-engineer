# Tune inference to the application Pareto point

Summary: Production inference should be optimized for the application's required operating point across quality, latency, and cost rather than for one generic model-serving metric.

Use when:
- Choosing model, runtime, retrieval, reasoning, quantization, or batching strategy for a product workload.
- Explaining why the same model deployment shape may be wrong for tab completion, robotics, async coding agents, or high-value scientific work.

Details:
- Kranen frames deployability as whether the model plus surrounding system can meet quality, latency, and per-request cost constraints for the target application (01:31-02:08).
- The desired Pareto point is application-specific: personal cancer-cure research may tolerate high latency and cost for quality, tab completion depends on fast response, and async code-commit agents can trade latency for quality and cost (03:04-04:32).
- Frontier-shifting techniques compose: RAG can raise quality while increasing latency and cost, reasoning spends more tokens for quality, and quantization can recover latency and cost by allowing higher batch sizes (04:35-06:01).

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Treat quantization as a memory-bandwidth lever](treat-quantization-as-a-memory-bandwidth-lever.md)
- [Plan AI products for a multimodel market](plan-ai-products-for-a-multimodel-market.md)

Sources:
- [Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA](../sources/20250801_Y2qc0UhDSnc.md), 01:31-06:01
