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

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Benchmark inference with use-case-shaped token loads](benchmark-inference-with-use-case-shaped-token-loads.md)
- [Tune inference to the application Pareto point](tune-inference-to-the-application-pareto-point.md)
- [Disaggregate prefill and decode workers by workload shape](disaggregate-prefill-and-decode-workers-by-workload-shape.md)

Sources:
- [Introduction to LLM serving with SGLang - Philip Kiely and Yineng Zhang, Baseten](../sources/20250726_Ahtaha9fEM0.md), 15:14-20:18
