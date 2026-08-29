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

- **Inside an RL loop, precision acquires a third axis beyond memory and throughput: how much of the model changes per training step.** For a fixed float format the visibility floor is roughly θ/2^(mantissa+1), so a coarser serving dtype rounds away more of each optimizer step and fewer served weights differ between versions — "in even lower precision there will be less weight changed" — which shrinks the trainer→rollout sync payload ([Lower Serving Precision Shrinks the Weight-Sync Patch](lower-serving-precision-shrinks-the-weight-sync-patch.md)). The accuracy cost is unchanged and this argument says nothing about it. ([Modal](../sources/20260810_maRzp4kImJ4.md), 13:25-13:42)
- The group-scaled formats this page benchmarks (NVFP4) behave differently under that lens than plain floats do: "plain floats are easy to reason about — each element has its own rounding," whereas with a shared group scale the same rationale is asserted to apply but the encoding and decoding differ, and a scale-factor change re-encodes a whole group at once. The talk works through neither, and its one measured run is FP8. ([Modal](../sources/20260810_maRzp4kImJ4.md), 13:42-14:43)
- **A counterexample worth measuring before assuming the quantized path is faster: KV-cache precision.** From a GLM 5.2 deployment on H200s, offered as a days-old finding and explicitly still under investigation, BF16 KV cache "actually is faster than using FP8 KV cache for longer prefill." Nothing accompanies it — no workload definition, no measurement, no explanation — so its only use is as a prompt: KV-cache precision is a separate dial from weight precision, it is exercised hardest during prefill rather than decode, and this page's memory-bandwidth argument does not obviously predict its sign on a prefill-bound workload. ([Fama](../sources/20260827_YXowceUKYJI.md), 19:28-19:52)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Lower Serving Precision Shrinks the Weight-Sync Patch](lower-serving-precision-shrinks-the-weight-sync-patch.md)
- [Profile small-model architectures on target hardware](profile-small-model-architectures-on-target-hardware.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Treat edge models as their own architecture class](treat-edge-models-as-their-own-architecture-class.md)
- [Text Diffusion Trades Serving Throughput for Low Latency](text-diffusion-trades-serving-throughput-for-low-latency.md)
- [Set the Prefill-to-Decode Ratio From the Workload's Input-to-Output Ratio](set-the-prefill-to-decode-ratio-from-the-workloads-input-output-ratio.md)

Sources:
- [Running LLMs locally: Practical LLM Performance on DGX Spark - Mozhgan Kabiri chimeh, NVIDIA](../sources/20260410_c5-kx2bwoCk.md), 05:34-09:18
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 13:25-14:43
- [KV Cache-Aware Routing and P/D Disaggregation on Kubernetes — Yuchen Fama & Ashish Kamra, Red Hat](../sources/20260827_YXowceUKYJI.md), 19:28-19:52
