# Generative Media

## Overview

Generative media covers the model and product patterns behind image, video, and other audiovisual generation. The current sources frame large-scale media systems as more than a diffusion backbone: data curation, learned latent representations, denoising architecture, sampling procedure, step distillation, explicit controls, and interactive state all shape whether the model is practical and steerable. Compared with language models, media diffusion can exploit spatial or temporal topology, bidirectional attention, perceptual frequency weighting, and coarse-to-fine generation instead of strict token-by-token causality. Media evaluation has the same perceptual constraint: codecs, internet artifacts, FID-style scores, and object-count metrics may not match what humans notice or what a creative user values. Media products also need retrieval over their own outputs: once a studio or campaign generates many personalized variants, finding the right asset and preserving provenance can become as important as creating another image. World models add a different bar from passive generation: when users act inside generated environments, the system needs memory, consistency, controllability, and live prompting so the world remains coherent under interaction.

Serving cost is its own discipline once a media model is good enough to use. NVIDIA's view is that diffusion latency comes mainly from the default 20-50 denoising steps and that the diffusion serving stack is less mature than the autoregressive LLM/VLM stack, so optimization ideas are borrowed from LLMs and adapted. Three levers are presented as additive and stackable rather than mutually exclusive: quantization is the easiest lever but pays off less than in LLMs because diffusion is attention-heavy; caching skips recomputing latent regions that barely change between denoising steps; and step distillation trains a same-size student to match teacher quality in far fewer steps (50 down to 4, 8, or one), the most impactful lever and currently the only path to good-quality real-time generation. Teams are advised to start with quantization, add caching and multi-GPU/context parallelism if needed, and finish with distillation, which together can reach the 10x-200x speedup that produced near-real-time video on a single Blackwell B200.

Generative media also includes music: Google DeepMind's Lyria 3 now generates full songs with lyrics and ships as two variants — a clip model and a Pro full-length-song model. How media generation is invoked is itself a product pattern: rather than a single static prompt, a real-time conversational model can expose the media generator as a tool, gather the creative brief through dialogue, and then call it — demonstrated by a "jukebox" where Gemini Live calls Lyria on request. This composes a native sound-to-sound interaction model with a dedicated media-generation model through ordinary tool use, and generalizes to image and video endpoints behind an agent.

## Key Concepts

- [Stack Additive Diffusion Optimizations for Real-Time Generation](../concepts/stack-additive-diffusion-optimizations-for-real-time-generation.md) - quantization, caching, and step distillation are incremental, combinable levers ordered from easy to most impactful.
- [Quantize Diffusion Models for Memory and Throughput Despite Attention Heaviness](../concepts/quantize-diffusion-models-for-memory-and-throughput-despite-attention-heaviness.md) - the cheapest serving lever, with PTQ/QAT, static/dynamic, and pre-quantized-checkpoint choices.
- [Cache Unchanged Computation Between Diffusion Denoising Steps](../concepts/cache-unchanged-computation-between-diffusion-denoising-steps.md) - inter-step similarity, not per-token reuse, is the cacheable signal in diffusion.
- [Curate generative-media data before tuning model internals](../concepts/curate-generative-media-data-before-tuning-model-internals.md) - data quality can dominate model and optimizer tweaks for large-scale media generation.
- [Train image and video diffusion models in learned latent spaces](../concepts/train-image-and-video-diffusion-models-in-learned-latent-spaces.md) - autoencoder latents make high-resolution and video diffusion tractable while preserving useful topology.
- [Use guidance to trade diffusion sample diversity for conditional quality](../concepts/use-guidance-to-trade-diffusion-sample-diversity-for-conditional-quality.md) - guidance is a sampling-time lever for prompt adherence, quality, diversity, and artifact risk.
- [Distill diffusion models to reduce sampling steps](../concepts/distill-diffusion-models-to-reduce-sampling-steps.md) - diffusion distillation primarily reduces iterative denoising latency.
- [Expose explicit control signals for generative media models](../concepts/expose-explicit-control-signals-for-generative-media-models.md) - media products need controls beyond text, such as camera motion, masks, and depth.
- [Ground generated media with current search context](../concepts/ground-generated-media-with-current-search-context.md) - retrieval can make generated images depend on current facts and public context.
- [Evaluate generative media with perceptual metrics](../concepts/evaluate-generative-media-with-perceptual-metrics.md) - media scores should account for human-visible quality, not only easy embedding or object checks.
- [Account for compression artifacts in media model data and evals](../concepts/account-for-compression-artifacts-in-media-model-data-and-evals.md) - compressed internet media can shape both training data and metric behavior.
- [Personalize aesthetic evals with preference classifiers](../concepts/personalize-aesthetic-evals-with-preference-classifiers.md) - creative products may need user-specific taste models rather than one universal aesthetic score.
- [Design AI creative systems for generated-asset retrieval](../concepts/design-ai-creative-systems-for-generated-asset-retrieval.md) - generated-media products need indexing and search when output volume grows with personalization.
- [Interactive world models need memory, control, and live prompting](../concepts/interactive-world-models-need-memory-control-and-live-prompting.md) - generated environments need state and action consistency when users navigate inside them.
- [Orchestrate Generative Media From a Real-Time Voice Agent via Tool Use](../concepts/orchestrate-generative-media-from-a-realtime-voice-agent.md) - a conversational model can gather a creative brief and invoke a media generator (e.g. Lyria 3 music) as a tool.

## Open Questions

- Which data-curation checks best predict downstream image and video generation quality before expensive training runs?
- How should teams choose the compression ratio and topology of image or video latents for a target product and serving budget?
- Which controls should be trained into the base model, exposed through adapters, or handled by external editing workflows?
- Which generated-world failures should be evaluated as media quality problems, interaction-control problems, or long-horizon memory problems?
- How should perceptual media evals combine universal human-visible defects with user-specific aesthetic preferences?
- What retrieval and provenance metadata should generated-media tools attach before personalized asset volume becomes unmanageable?
- How should diffusion serving teams measure quality regression as they stack quantization, caching, and step distillation toward a real-time target?

## Sources

- [You Might Not Need 50 Diffusion Steps — Ziv Ilan, Nvidia](../sources/20260616_gHs5ZiY80PM.md)
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md)
- [How Google DeepMind is researching the next Frontier of AI for Gemini - Raia Hadsell, VP of Research](../sources/20260418_zZsTVBXcbow.md)
- [Building in the Gemini Era - Kat Kampf & Ammaar Reshi, Google DeepMind](../sources/20251215_fgkXEIbZpGc.md)
- [Perceptual Evaluations: Evals for Aesthetics - Diego Rodriguez, Krea.ai](../sources/20250823_h5ItAJuB3Fc.md)
- [The Next Unicorns: 7 Top AI startups from the HF0 Residency](../sources/20250821_L8-5ezsoI5A.md)
- [From Transcription to Live Music: Gemini's Audio Stack — Thor Schaeff, Google DeepMind](../sources/20260609_Bc6Ojl2XS1w.md)
