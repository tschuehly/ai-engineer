# Treat Quantization as a Memory-Bandwidth Lever

Summary: Quantization is not only a model-fit technique; it can be the difference between a model that merely fits in local memory and one that feels responsive. Memory capacity determines whether a model can load, while memory bandwidth and precision format strongly shape throughput and time to first token.

Use when:
- Choosing precision formats for local or self-hosted LLM serving.
- Explaining why a model that fits in unified memory may still be too slow for interactive use.

Details:
- In the reported local vLLM benchmark, a 1.5B instruct model delivered 61.73 tokens per second, while a 14B NVFP4/NVFB4 model still delivered 20.19 tokens per second despite being nearly ten times larger. (05:34-06:16)
- The unoptimized 14B base model dropped to 8.40 tokens per second, which the talk uses to argue that quantization format can be as important as hardware selection on Blackwell-class local systems. (06:38-07:27)
- The 14B NVFP4/NVFB4 model was reported as 3.4 times faster to first token than the unoptimized 14B base model, reinforcing that precision choices affect perceived latency as well as throughput. (07:31-08:37)
- A system with 128 GB unified memory can fit very large models, but throughput is governed by how efficiently data moves through the system; the talk describes quantization as increasing "intelligence per byte." (08:37-09:18)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Profile small-model architectures on target hardware](profile-small-model-architectures-on-target-hardware.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Treat edge models as their own architecture class](treat-edge-models-as-their-own-architecture-class.md)
- [Text Diffusion Trades Serving Throughput for Low Latency](text-diffusion-trades-serving-throughput-for-low-latency.md)

Sources:
- [Running LLMs locally: Practical LLM Performance on DGX Spark - Mozhgan Kabiri chimeh, NVIDIA](../sources/20260410_c5-kx2bwoCk.md), 05:34-09:18
