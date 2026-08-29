# Tune CUDA Graph Batch Capture to Real Decode Concurrency

Summary: CUDA graph acceleration only helps SGLang decode when the active decode batch fits within the captured graph sizes. The max CUDA graph batch setting should be validated against realistic concurrency, because a default that is too low can silently fall back during the decode phase.

Use when:
- Tuning decode throughput for an SGLang deployment.
- Interpreting server logs that show CUDA graph disabled during decode.
- Designing serving benchmarks that represent actual concurrent request load.

Details:
- In the workshop demo, CUDA graph is enabled by default, but the default maximum CUDA graph batch size for the L4/model setup is eight. (15:14-15:29)
- When the decode batch reaches ten running requests, the server log reports CUDA graph as false because the active running request count exceeds the max captured graph size. (15:46-16:11)
- That fallback corresponds to roughly 155 generation tokens per second in the demo, or around fifteen tokens per second per user at ten concurrent requests. (16:12-16:29)
- Raising the max CUDA graph batch size to 32 allows a decode batch with thirteen running requests to keep CUDA graph true. (16:42-19:13)
- The speaker emphasizes that CUDA graph should remain true during decode because it is important for decoding performance, and that the setting should handle the realistic batch observed during benchmarking. (19:43-20:18)
- **The other way a realistic decode batch changes behaviour, at the pod level rather than the graph level.** Decode concurrency is not only a capture-size question: on a pod serving both phases, prefill and decode contend, and "a sudden influx of a long prefill prompt… will completely stall the ongoing decode token generation process causing massive problems and jitter in user streaming latency." That means a benchmark holding concurrency steady can miss both failures at once — the silent CUDA-graph fallback this page describes, and phase interference — because both only appear when the running-request count moves. Validate decode settings against a load pattern with bursty long prompts in it, not a fixed batch. ([Kamra](../sources/20260827_YXowceUKYJI.md), 10:20-11:56)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Benchmark inference with use-case-shaped token loads](benchmark-inference-with-use-case-shaped-token-loads.md)
- [Tune inference to the application Pareto point](tune-inference-to-the-application-pareto-point.md)
- [Disaggregate prefill and decode workers by workload shape](disaggregate-prefill-and-decode-workers-by-workload-shape.md)
- [Disaggregate prefill and decode workers by workload shape](disaggregate-prefill-and-decode-workers-by-workload-shape.md)

Sources:
- [Introduction to LLM serving with SGLang - Philip Kiely and Yineng Zhang, Baseten](../sources/20250726_Ahtaha9fEM0.md), 15:14-20:18
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 10:20-11:56
