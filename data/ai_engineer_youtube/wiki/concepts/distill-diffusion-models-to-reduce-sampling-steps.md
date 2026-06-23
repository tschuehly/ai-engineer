# Distill Diffusion Models to Reduce Sampling Steps

Summary: In diffusion systems, distillation is often about reducing the number of denoising steps needed for a good sample. This turns a slow iterative sampler into a lower-latency generator while trying to preserve output quality. The student keeps the teacher's parameter count; what shrinks is the number of sampling steps.

Use when:
- Optimizing image or video generation latency.
- Comparing model-size reduction with sampler-step reduction as deployment levers.
- Choosing between trajectory-based and distribution-based step distillation.

Details:
- The source explicitly distinguishes diffusion distillation from the common meaning of making a model smaller; here the target is reducing the number of sampling steps needed for good results (02:17-02:27, 28:04-28:19).
- Sampling ordinarily moves through a multi-step denoising trajectory, which gives quality but costs latency (12:24-15:18).
- Distillation can be understood as teaching a model or sampler to cover larger intervals of the sampling path, reducing the amount of iterative work needed at inference time (28:04-29:50).
- NVIDIA frames it as step distillation: train a same-size student to match teacher-quality images/videos in far fewer steps — 50 down to 4, 8, or even one shot — where holding quality at low step counts is the hard part. Success yields 10x-200x speedup and is currently the only path to good-quality real-time generation (gHs5ZiY80PM 09:22-10:35).
- Two main approaches: trajectory-based distillation teaches the student to follow the teacher's exact denoising path step by step, while distribution-based distillation only requires the student to land on the same output distribution and lets it find its own path. Distribution-based is now the more common and higher-quality technique, and the two can be combined (gHs5ZiY80PM 11:09-11:53).
- It is a post-training technique, so it needs data and must converge well ("garbage in, garbage out") and costs more compute, time, and proficiency than enabling caching or quantization; FastGen's hybrid distillation recipe held quality while stabilizing training (gHs5ZiY80PM 11:53-12:44).
- Hardware bar is moderate: distillation does not need top-tier GB200 — it runs on Hopper (H100/H200) and Blackwell (B200/B300) and costs far less than pre-training, scaling with model size (small 2-4B video models need much less) (gHs5ZiY80PM 16:50-17:48).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Use guidance to trade diffusion sample diversity for conditional quality](use-guidance-to-trade-diffusion-sample-diversity-for-conditional-quality.md)
- [Stack Additive Diffusion Optimizations for Real-Time Generation](stack-additive-diffusion-optimizations-for-real-time-generation.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)
- [Scale Text-Diffusion Quality With More Denoising Steps](scale-text-diffusion-quality-with-more-denoising-steps.md) - the same denoising-step lever in the text modality, where more steps trade latency for quality.

Sources:
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md), 02:17-02:27, 28:04-29:50
- [You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia](../sources/20260616_gHs5ZiY80PM.md), 09:22-12:44, 16:50-17:48
