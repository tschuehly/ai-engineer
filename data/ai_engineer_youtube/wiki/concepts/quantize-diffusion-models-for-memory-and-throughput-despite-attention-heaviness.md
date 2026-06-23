# Quantize Diffusion Models for Memory and Throughput Despite Attention Heaviness

Summary: Quantization is the easiest first lever for diffusion serving — it cuts memory so models run on lower-end GPUs and improves throughput — but it pays off less than in LLMs because diffusion models are attention-heavy. It is still worthwhile, especially to exploit modern low-precision hardware features, and can often be adopted by loading a pre-quantized checkpoint rather than quantizing yourself.

Use when:
- Choosing the first, lowest-effort optimization for an image/video diffusion model.
- Deciding between post-training quantization and quantization-aware training for media models.
- Picking static vs dynamic quantization, or whether to fine-tune after quantizing.

Details:
- Two approaches exist: post-training quantization (PTQ) and quantization-aware training (QAT). PTQ is the simpler choice teams reach for first, but maintaining image/video quality under quantization is harder for diffusion than for LLMs (03:53-04:15).
- Diffusion models are more attention-heavy, so quantization is "not as impactful as the LLMs VLMs," but it remains a low-hanging fruit — particularly for taking advantage of advanced Blackwell features and more modern compute (04:15-04:39).
- Static quantization precomputes all parameter ranges up front and deploys a fixed range; dynamic quantization computes some ranges on the fly so they match the data distribution seen at run time. The Black Forest Labs work on Flux 2 used dynamic quantization (04:39-05:13).
- Adoption paths: quantize yourself with NVIDIA's open-source TensorRT-LLM visual-gen repository, or load a partner's pre-quantized checkpoint from Hugging Face and run directly — handy when you do not need to fine-tune or add LoRA adapters afterward (05:13-05:46).
- Impact is on both memory (less memory means running on lower-end consumer or data-center GPUs) and performance/throughput (05:46-06:06).
- Because attention dominates these models, recent research bringing FP4 to attention is being pulled into the toolkit to push quantization further (06:13-06:31).

Related topics:
- [Inference](../topics/inference.md)
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)

Related concepts:
- [Stack Additive Diffusion Optimizations for Real-Time Generation](stack-additive-diffusion-optimizations-for-real-time-generation.md)
- [Treat quantization as a memory-bandwidth lever](treat-quantization-as-a-memory-bandwidth-lever.md)
- [Cache Unchanged Computation Between Diffusion Denoising Steps](cache-unchanged-computation-between-diffusion-denoising-steps.md)

Sources:
- [You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia](../sources/20260616_gHs5ZiY80PM.md), 03:53-06:31
