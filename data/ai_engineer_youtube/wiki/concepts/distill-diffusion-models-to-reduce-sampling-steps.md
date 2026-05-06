# Distill Diffusion Models to Reduce Sampling Steps

Summary: In diffusion systems, distillation is often about reducing the number of denoising steps needed for a good sample. This turns a slow iterative sampler into a lower-latency generator while trying to preserve output quality.

Use when:
- Optimizing image or video generation latency.
- Comparing model-size reduction with sampler-step reduction as deployment levers.

Details:
- The source explicitly distinguishes diffusion distillation from the common meaning of making a model smaller; here the target is reducing the number of sampling steps needed for good results (02:17-02:27, 28:04-28:19).
- Sampling ordinarily moves through a multi-step denoising trajectory, which gives quality but costs latency (12:24-15:18).
- Distillation can be understood as teaching a model or sampler to cover larger intervals of the sampling path, reducing the amount of iterative work needed at inference time (28:04-29:50).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Use guidance to trade diffusion sample diversity for conditional quality](use-guidance-to-trade-diffusion-sample-diversity-for-conditional-quality.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)

Sources:
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md), 02:17-02:27, 28:04-29:50
