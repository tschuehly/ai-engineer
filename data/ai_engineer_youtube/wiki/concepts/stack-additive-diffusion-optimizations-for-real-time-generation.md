# Stack Additive Diffusion Optimizations for Real-Time Generation

Summary: Image and video diffusion latency comes mainly from running 20-50 denoising steps, and the way to attack it is to stack independent, additive optimizations — quantization, caching, and step distillation — rather than picking one. Each lever helps on its own and they compose, so teams can start cheap and add complexity only until the quality/latency target is met.

Use when:
- Planning how to make a diffusion image/video model fast enough for developer, enterprise, or real-time use.
- Deciding which optimization to try first and when to stop adding more.
- Estimating how far speedups can go before reaching real-time generation.

Details:
- Diffusion defaults to 20-50 denoising steps and, unlike autoregressive LLMs, does not emit a token per pass; that iterative trajectory is the latency cost, and the diffusion serving ecosystem is less mature than the LLM/VLM stack, so NVIDIA borrows LLM optimization ideas and adapts them (01:23-02:30).
- The three levers are quantization (easiest, lowest-hanging fruit), caching (skip recomputing near-identical denoising work), and step distillation (most impactful). They are explicitly described as incremental: "you can use this plus this plus this," not an either/or choice (03:17-03:43, 15:17-15:52).
- Suggested escalation: start with quantization; if it is good enough, stop. Otherwise move to multi-GPU / context parallelism, add caching, and finally distillation as the last and most impactful step. Quantization alone can be enough on its own (15:17-15:52).
- Stacking the levers can reach the 10x-200x speedup real-time generation requires; the GTC demo produced near-real-time video on a single Blackwell B200 using two distillation techniques (10:13-10:35, 14:03-14:35).
- FastGen (NVIDIA NV Research, open source) is the framework that structures the heaviest lever: it packages the post-training and GPU scale-sharding work distillation needs for large video diffusion models (20/30/40B params today, heading to hundreds of billions) so teams focus on quality and recipe tuning rather than infrastructure (12:44-14:03).
- Speedups show up in both wall-clock time and compute used, and the levers are all open source with support for model families such as Flux 2 and LTX 2 (14:03-14:35, 16:01-16:28).
- Pruna (Bertrand Charpentier) corroborates the stacking recipe from the efficiency-company side and adds two levers: quantization applied per module (a different quantization for each module of the model, "super important") and pruning (removing components that are not important), on top of attacking the same 20–50 denoiser steps via distillation or caching to reach ~20x or even ~4x fewer steps depending on aggressiveness. Pruna ships open-source caching algorithms (plus internal ones for served models) and likewise works on Flux 2 / Flux with Black Forest Labs (hqHC6Z_lXyo, 17:52-19:15, 15:26-16:02).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Quantize Diffusion Models for Memory and Throughput Despite Attention Heaviness](quantize-diffusion-models-for-memory-and-throughput-despite-attention-heaviness.md)
- [Cache Unchanged Computation Between Diffusion Denoising Steps](cache-unchanged-computation-between-diffusion-denoising-steps.md)
- [Distill diffusion models to reduce sampling steps](distill-diffusion-models-to-reduce-sampling-steps.md)
- [Tune inference to the application Pareto point](tune-inference-to-the-application-pareto-point.md)

Sources:
- [You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia](../sources/20260616_gHs5ZiY80PM.md), 01:23-02:30, 03:17-03:43, 10:13-10:35, 12:44-14:35, 15:17-16:28
- [20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna](../sources/20260601_hqHC6Z_lXyo.md), 15:26-16:02, 17:52-19:15
