# Cache Unchanged Computation Between Diffusion Denoising Steps

Summary: Across a diffusion sampler's 20-50 denoising steps, many regions of the latent change very little from one step to the next, so a serving layer can detect near-identical computation and skip recomputing it. This is the diffusion analogue of LLM KV caching, but it keys on inter-step similarity rather than reusing per-token attention state.

Use when:
- Cutting diffusion image/video latency without retraining the model.
- Deciding a similarity threshold that trades speedup against output quality.
- Explaining why LLM KV-cache intuition does not transfer directly to diffusion.

Details:
- KV caching is well understood for autoregressive models, but diffusion does not generate a token each pass; the reusable signal is computation that barely changes between denoising steps, which makes the technique harder to apply directly (06:33-07:18).
- TeaCache is the illustrative method: it compares consecutive denoising steps and, when the change is below a threshold, decides it does not need to recompute the next step; in its basic form it does this over the entire pixel/latent space (07:18-07:58).
- More modern caching is chunk-based: isolate only the chunks of the latent that actually change between steps and recompute just those, leaving static chunks cached (classroom analogy: most of the audience is unchanged, so only the moving part is recomputed) (07:58-08:26).
- The similarity threshold is the main knob and the technique makes a large impact, but done wrong it significantly degrades image quality, so validate that quality holds while taking the speedup (08:26-09:18).
- It ships as an enable-and-set-threshold flag in NVIDIA's TensorRT-LLM visual-gen repository and other serving libraries, so it can be experimented with at the serving layer rather than in the model (09:00-09:18).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Stack Additive Diffusion Optimizations for Real-Time Generation](stack-additive-diffusion-optimizations-for-real-time-generation.md)
- [Distill diffusion models to reduce sampling steps](distill-diffusion-models-to-reduce-sampling-steps.md)
- [KV-cache hit rate is a production agent SLO](kv-cache-hit-rate-is-a-production-agent-slo.md)

Sources:
- [You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia](../sources/20260616_gHs5ZiY80PM.md), 06:33-09:18
