# Generative Media

## Overview

Generative media covers the model and product patterns behind image, video, and other audiovisual generation. The current sources frame large-scale media systems as more than a diffusion backbone: data curation, learned latent representations, denoising architecture, sampling procedure, step distillation, explicit controls, and interactive state all shape whether the model is practical and steerable. Compared with language models, media diffusion can exploit spatial or temporal topology, bidirectional attention, perceptual frequency weighting, and coarse-to-fine generation instead of strict token-by-token causality. Media evaluation has the same perceptual constraint: codecs, internet artifacts, FID-style scores, and object-count metrics may not match what humans notice or what a creative user values. World models add a different bar from passive generation: when users act inside generated environments, the system needs memory, consistency, controllability, and live prompting so the world remains coherent under interaction.

## Key Concepts

- [Curate generative-media data before tuning model internals](../concepts/curate-generative-media-data-before-tuning-model-internals.md) - data quality can dominate model and optimizer tweaks for large-scale media generation.
- [Train image and video diffusion models in learned latent spaces](../concepts/train-image-and-video-diffusion-models-in-learned-latent-spaces.md) - autoencoder latents make high-resolution and video diffusion tractable while preserving useful topology.
- [Use guidance to trade diffusion sample diversity for conditional quality](../concepts/use-guidance-to-trade-diffusion-sample-diversity-for-conditional-quality.md) - guidance is a sampling-time lever for prompt adherence, quality, diversity, and artifact risk.
- [Distill diffusion models to reduce sampling steps](../concepts/distill-diffusion-models-to-reduce-sampling-steps.md) - diffusion distillation primarily reduces iterative denoising latency.
- [Expose explicit control signals for generative media models](../concepts/expose-explicit-control-signals-for-generative-media-models.md) - media products need controls beyond text, such as camera motion, masks, and depth.
- [Ground generated media with current search context](../concepts/ground-generated-media-with-current-search-context.md) - retrieval can make generated images depend on current facts and public context.
- [Evaluate generative media with perceptual metrics](../concepts/evaluate-generative-media-with-perceptual-metrics.md) - media scores should account for human-visible quality, not only easy embedding or object checks.
- [Account for compression artifacts in media model data and evals](../concepts/account-for-compression-artifacts-in-media-model-data-and-evals.md) - compressed internet media can shape both training data and metric behavior.
- [Personalize aesthetic evals with preference classifiers](../concepts/personalize-aesthetic-evals-with-preference-classifiers.md) - creative products may need user-specific taste models rather than one universal aesthetic score.
- [Interactive world models need memory, control, and live prompting](../concepts/interactive-world-models-need-memory-control-and-live-prompting.md) - generated environments need state and action consistency when users navigate inside them.

## Open Questions

- Which data-curation checks best predict downstream image and video generation quality before expensive training runs?
- How should teams choose the compression ratio and topology of image or video latents for a target product and serving budget?
- Which controls should be trained into the base model, exposed through adapters, or handled by external editing workflows?
- Which generated-world failures should be evaluated as media quality problems, interaction-control problems, or long-horizon memory problems?
- How should perceptual media evals combine universal human-visible defects with user-specific aesthetic preferences?

## Sources

- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md)
- [How Google DeepMind is researching the next Frontier of AI for Gemini - Raia Hadsell, VP of Research](../sources/20260418_zZsTVBXcbow.md)
- [Building in the Gemini Era - Kat Kampf & Ammaar Reshi, Google DeepMind](../sources/20251215_fgkXEIbZpGc.md)
- [Perceptual Evaluations: Evals for Aesthetics - Diego Rodriguez, Krea.ai](../sources/20250823_h5ItAJuB3Fc.md)
