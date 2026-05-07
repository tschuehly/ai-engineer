# Benchmark inference with use-case-shaped token loads

Summary: Inference benchmarks should model the request shape the application will actually serve. Request rate, input tokens, output tokens, time to first token, inter-token latency, throughput, P99, hardware, and runtime configuration all change whether a model is production-usable.

Use when:
- Comparing inference runtimes, hardware setups, or model sizes for a chatbot, copilot, or RAG application.
- Turning latency and throughput tests into deployment evidence instead of generic benchmark numbers.

Details:
- Smith argues that no matter how good the model is, production serving fails if it is not fast, reliable, and affordable under concurrent traffic. (05:01-05:59)
- The workshop uses GuideLLM with a vLLM-served IBM Granite model to benchmark latency, throughput, inter-token latency, time to first token, and request-rate sweeps. (14:53-15:33, 20:51-22:15)
- GuideLLM benchmarks should be configured with input and output token levels that match the use case, such as chatbot or RAG traffic profiles. (15:45-16:07)
- Benchmark interpretation is use-case-dependent: mean, median, and P99 matter differently by SLO, hardware, concurrency, model size, and production deployment target. (22:21-23:08)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Make local inference benchmarks reproducible artifacts](make-local-inference-benchmarks-reproducible-artifacts.md)
- [Tune inference to the application Pareto point](tune-inference-to-the-application-pareto-point.md)
- [Size KV-cache memory tiers with workload-shaped benchmarks](size-kv-cache-memory-tiers-with-workload-shaped-benchmarks.md)

Sources:
- [Strategies for LLM Evals (GuideLLM, lm-eval-harness, OpenAI Evals Workshop) - Taylor Jordan Smith](../sources/20250727_89NuzmKokIk.md), 05:01-05:59, 14:53-16:07, 20:51-23:08
