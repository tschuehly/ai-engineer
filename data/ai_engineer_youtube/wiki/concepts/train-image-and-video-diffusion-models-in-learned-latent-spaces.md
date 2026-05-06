# Train Image and Video Diffusion Models in Learned Latent Spaces

Summary: Modern image and video diffusion models usually train over learned autoencoder latents rather than raw pixels. The latent representation reduces memory and compute while preserving enough spatial or temporal structure for media-oriented neural architectures.

Use when:
- Designing a diffusion training pipeline for high-resolution images or video.
- Comparing raw pixel, conventional codec, and learned latent representations.

Details:
- Raw pixel tensors grow quickly with image resolution and video duration; the source gives 30 seconds of 1080p video at 30 fps as too large to treat as a convenient single training example in memory (04:02-04:59).
- Conventional codecs such as JPEG or H.265 optimize for compact storage but can obscure structure in ways that make generative modeling harder (05:01-05:23, 08:21-08:31).
- Learned autoencoders compress inputs through an encoder bottleneck, train the diffusion model over the latent grid, and decode sampled latents back into pixels (05:25-06:50).
- Useful latents preserve the original grid topology at a coarser resolution, often adding channels to retain information that simple resizing would lose (07:16-07:59).
- Video latents exploit temporal redundancy and can reduce tensor sizes by orders of magnitude, which can be the difference between fitting data in memory and being unable to train (08:00-08:16).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Tokenizer size must match data and compute budget](tokenizer-size-must-match-data-and-compute-budget.md)
- [Tune multimodal token budgets by visual or audio task](tune-multimodal-token-budgets-by-visual-or-audio-task.md)

Sources:
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md), 04:02-08:56
