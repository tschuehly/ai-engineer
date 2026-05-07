# Use Eagle 3 Speculative Decoding With Matched Draft Models

Summary: Eagle 3 is a speculative decoding path in SGLang that uses both a target model and a matched draft model. Its draft model is built from the target model, so it should not be treated as interchangeable with any smaller model from the same family.

Use when:
- Evaluating speculative decoding as an SGLang latency or throughput lever.
- Configuring target and draft model paths for a serving experiment.
- Avoiding invalid assumptions about arbitrary small-model draft pairing.

Details:
- The workshop introduces Eagle 3 as a speculative decoding algorithm supported by SGLang that can improve serving performance. (13:19-13:25, 24:19-24:36)
- Configuration requires specifying the speculative decoding algorithm plus separate target model and draft model paths. (25:26-25:54)
- The speaker distinguishes Eagle-family draft models from simply pairing a large model with an unrelated smaller model, explaining that Eagle builds a draft model from the target model. (25:59-26:25)
- The demo treats batch size as a parameter to sweep when evaluating the target/draft setup, using batch sizes such as 1, 2, 4, 8, and 16 before deciding which parameter belongs in online serving. (27:42-28:47)

Related topics:
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Tune inference to the application Pareto point](tune-inference-to-the-application-pareto-point.md)
- [Benchmark inference with use-case-shaped token loads](benchmark-inference-with-use-case-shaped-token-loads.md)

Sources:
- [Introduction to LLM serving with SGLang - Philip Kiely and Yineng Zhang, Baseten](../sources/20250726_Ahtaha9fEM0.md), 13:19-13:25, 24:19-28:47
