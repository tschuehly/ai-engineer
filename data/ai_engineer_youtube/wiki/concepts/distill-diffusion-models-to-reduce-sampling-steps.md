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

- A shipped instance of the technique, with numbers attached to the outcome rather than the method: Helios, the real-time video model uRun serves, "is a distill of [Wan] 2.1 14B" — an open 14-billion-parameter video model — and reached production in March. Its output is "about at the same quality as the frontier models were last year" and costs roughly a hundredth of a minutes-long generation, with the residual gap showing up as motion quality (Xln-On3syJk 01:16-02:48). Two things generalize: the base can be someone else's open weights rather than your own teacher, and the achievable position is a one-year quality lag at two orders of magnitude less cost, which is the trade a product team is actually deciding on.
- A second shipped instance, at the aggressive end of the step-count range and in a harder setting: LemonSlice reduces its video model from "let's say 30 steps" of denoising to one — "you basically just in a single step go from like pure noise to a pure video" — as the single biggest lever for making a real-time avatar (z1dqv74SpUs 11:11-11:44). Two things distinguish it from the batch case. The model is already constrained to attend only backward, so single-step generation runs on top of causal conditioning rather than on a full bidirectional view; and the output is not one clip but an eight-hour continuous session, so whatever quality the distilled sampler gives up is compounded by error accumulation rather than paid once. Step distillation is the standard lever here, but its quality cost is measured over a session, not over a sample.
- Field-wide adoption rather than one vendor's trick: "at least 40 models with real-time capabilities and long horizon generation capabilities released this year," and "these are techniques that are being applied all over the place, not just the one model" (Xln-On3syJk 02:42-03:23).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Use guidance to trade diffusion sample diversity for conditional quality](use-guidance-to-trade-diffusion-sample-diversity-for-conditional-quality.md)
- [Stack Additive Diffusion Optimizations for Real-Time Generation](stack-additive-diffusion-optimizations-for-real-time-generation.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)
- [Scale Text-Diffusion Quality With More Denoising Steps](scale-text-diffusion-quality-with-more-denoising-steps.md) - the same denoising-step lever in the text modality, where more steps trade latency for quality.
- [Track the Efficiency Axis in Generative Video, Not Only Quality](track-the-efficiency-axis-in-generative-video-not-only-quality.md) - what a distilled real-time video model is worth in cost and quality terms.
- [Make a Video Model Interactive With a Causal Attention Mask, Then Budget for Error Accumulation](make-video-models-causal-and-budget-for-error-accumulation.md) - the other conversion a real-time video model needs, and why step reduction is judged over a session.

Sources:
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md), 02:17-02:27, 28:04-29:50
- [You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia](../sources/20260616_gHs5ZiY80PM.md), 09:22-12:44, 16:50-17:48
- [Generative Video at the Speed of Light — Keegan McCallum, uRun](../sources/20260818_Xln-On3syJk.md), 01:16-03:23
- [Voice agents with Realtime Video — Sidney Primas, LemonSlice](../sources/20260818_z1dqv74SpUs.md), 11:11-11:44
