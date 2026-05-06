# Models

## Overview

Model work in this wiki covers how AI engineers choose, train, adapt, and deploy model architectures under real constraints. The current sources show two complementary views: small or edge models make deployment practical when memory, latency, privacy, and accelerator access matter, while from-scratch local training exposes the tokenizer, architecture, training-loop, and inference choices that are often hidden behind high-level APIs. Edge-scale models should be treated as their own architecture class, profiled on target hardware, and post-trained for narrow capabilities rather than judged as miniature general-purpose chatbots. Model choice should also account for behavioral reliability: some models improve on public leaderboards while still accepting nonsensical premises, overusing reasoning, or underperforming on fuzzy expert work. Gemma 4 adds a concrete routing pattern inside one open-weight family: effective on-device variants, sparse MoE efficiency, and dense long-context reasoning variants serve different deployment and workflow shapes. Tiny models add a third pattern: specialize and fine-tune narrow components, then compose them into a product workflow.

## Key Concepts

- [Compare models by task, thinking budget, cost, and latency](../concepts/compare-models-by-task-thinking-budget-cost-and-latency.md) - model choice should be routed by workload constraints rather than by size alone.
- [Evaluate whether models reject impossible or nonsensical premises](../concepts/evaluate-whether-models-reject-impossible-or-nonsensical-premises.md) - model reliability includes knowing when not to answer a malformed request.
- [Benchmark narrow slices separately from real expert work](../concepts/benchmark-narrow-slices-separately-from-real-expert-work.md) - public benchmark progress should be interpreted alongside real prompt distributions and expert dissatisfaction.
- [Route Gemma 4 model variants by deployment and workflow shape](../concepts/route-gemma-4-model-variants-by-deployment-and-workflow-shape.md) - Gemma 4's effective, MoE, and dense variants map to different local, hosted, reasoning, coding, and agentic workloads.
- [Treat edge models as their own architecture class](../concepts/treat-edge-models-as-their-own-architecture-class.md) - memory-bound edge models need architecture and training choices optimized for local latency and limited effective parameters.
- [Interleave local and global attention to trade context for efficiency](../concepts/interleave-local-and-global-attention-to-trade-context-for-efficiency.md) - attention placement and grouped query attention can reduce context cost without removing global context flow.
- [Per-layer embeddings move effective-model capacity out of VRAM](../concepts/per-layer-embeddings-move-effective-model-capacity-out-of-vram.md) - PLE shows one way to add representational depth while respecting on-device memory constraints.
- [Tune multimodal token budgets by visual or audio task](../concepts/tune-multimodal-token-budgets-by-visual-or-audio-task.md) - image and audio inputs should spend tokens according to the modality's actual task value.
- [Profile small-model architectures on target hardware](../concepts/profile-small-model-architectures-on-target-hardware.md) - operator choices should be validated on the CPUs, phones, GPUs, and accelerators that will run the model.
- [Post-train small models for narrow capabilities](../concepts/post-train-small-models-for-narrow-capabilities.md) - data extraction, tool use, and other focused tasks are better targets than average performance across every benchmark.
- [Mitigate small-model doom loops during preference alignment and RL](../concepts/mitigate-small-model-doom-loops-during-preference-alignment-and-rl.md) - tiny reasoning models need post-training checks for repetitive loops that SFT may not remove.
- [Match Gemma edge model size to device memory and interaction class](../concepts/match-gemma-edge-model-size-to-device-memory-and-interaction-class.md) - model size is an engineering decision tied to device capability and product interaction.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - specialized small models can prepare context before a larger reasoning model is invoked.
- [Local LLM training exposes the core model-building stack](../concepts/local-llm-training-exposes-the-core-model-building-stack.md) - local from-scratch training clarifies the core pieces behind model behavior.
- [Tokenizer size must match data and compute budget](../concepts/tokenizer-size-must-match-data-and-compute-budget.md) - tokenizer capacity should fit the data, domain, modality, and training budget.
- [Use loss curves to debug local model training](../concepts/use-loss-curves-to-debug-local-model-training.md) - train and validation loss patterns reveal learning, overfitting, and instability.
- [Modular tiny-model pipelines reuse specialized models across mobile app workflows](../concepts/modular-tiny-model-pipelines-reuse-specialized-models-across-mobile-app-workflows.md) - narrow fine-tuned models can be composed into mobile app pipelines and reused across features.

## Open Questions

- How should tokenizer decisions change when a model must support mixed modalities or mixed domains rather than a single constrained corpus?
- Which lightweight generated-sample checks complement train/validation loss for tiny local model runs?
- When is a modular set of fine-tuned tiny models preferable to one larger model with prompting or skills?
- Which small-model failures should be fixed with architecture, post-training data, runtime tools, or product task narrowing?
- How should teams evaluate sparse MoE, effective on-device, and dense long-context models against the same agent workflow without hiding deployment cost differences?
- When does adding reasoning effort improve model judgment, and when does it simply make accommodation of a bad premise longer?

## Sources

- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md)
- [Gemma 4 Deep Dive - Cassidy Hardin, Researcher, Google DeepMind](../sources/20260427__A367W_qvc8.md)
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md)
- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Training an LLM from Scratch, Locally - Angelos Perivolaropoulos, ElevenLabs](../sources/20260504_UsB70Tf5zcE.md)
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md)
- [What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench](../sources/20260424_R7A8rX-09Zw.md)
