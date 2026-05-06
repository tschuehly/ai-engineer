# Inference

## Overview

Inference is the production discipline of turning trained models into reliable, efficient services. For small models, the main constraint is often not raw compute alone but orchestration across many specialized models: dynamic loading, routing, batching, model-specific runtime support, observability, and autoscaling determine whether the system wastes GPU capacity or becomes a reusable agent and retrieval substrate. At the architecture level, inference cost is also shaped by attention and memory choices: sparse expert activation, local/global attention mixes, grouped query attention, and flash-backed embedding tables can change the practical serving envelope before cluster operations even begin. For image and video diffusion, inference behavior is also the sampler: guidance, denoising step count, and distillation affect quality, diversity, artifacts, and latency.

## Key Concepts

- [Profile small-model architectures on target hardware](../concepts/profile-small-model-architectures-on-target-hardware.md) - local inference performance should be measured on the intended hardware, not inferred from architecture alone.
- [Interleave local and global attention to trade context for efficiency](../concepts/interleave-local-and-global-attention-to-trade-context-for-efficiency.md) - local windows, periodic global layers, and grouped query attention shape memory and serving cost.
- [Per-layer embeddings move effective-model capacity out of VRAM](../concepts/per-layer-embeddings-move-effective-model-capacity-out-of-vram.md) - flash-backed PLE changes the memory profile of effective on-device models.
- [Hot-swap small models to avoid one-model-per-GPU waste](../concepts/hot-swap-small-models-to-avoid-one-model-per-gpu-waste.md) - many small models can share accelerator capacity when the runtime supports dynamic loading and eviction.
- [Production inference combines model support with cluster operations](../concepts/production-inference-combines-model-support-with-cluster-operations.md) - serving many model families requires both architecture-specific adaptation and production operations.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - inference infrastructure can expose narrow models as preprocessing and retrieval tools for agent workflows.
- [Train image and video diffusion models in learned latent spaces](../concepts/train-image-and-video-diffusion-models-in-learned-latent-spaces.md) - latent media representations shrink inference tensors while keeping useful topology.
- [Use guidance to trade diffusion sample diversity for conditional quality](../concepts/use-guidance-to-trade-diffusion-sample-diversity-for-conditional-quality.md) - sampling parameters shape output quality and failure modes.
- [Distill diffusion models to reduce sampling steps](../concepts/distill-diffusion-models-to-reduce-sampling-steps.md) - step reduction is a direct latency lever for diffusion serving.

## Open Questions

- How should teams evaluate the latency and quality tradeoff between preprocessing with small models and sending broader raw context to a larger agent model?
- When do local/global attention and grouped query attention provide enough serving efficiency to justify architecture-specific runtime support?
- How should diffusion serving expose guidance, step count, and distillation choices without letting users create predictable artifacts or unacceptable latency?

## Sources

- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Gemma 4 Deep Dive - Cassidy Hardin, Researcher, Google DeepMind](../sources/20260427__A367W_qvc8.md)
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md)
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md)
