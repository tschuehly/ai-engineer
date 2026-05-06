# Models

## Overview

Model work in this wiki covers how AI engineers choose, train, adapt, and deploy model architectures under real constraints. The current sources show two complementary views: small or edge models make deployment practical when memory, latency, privacy, and accelerator access matter, while from-scratch local training exposes the tokenizer, architecture, training-loop, and inference choices that are often hidden behind high-level APIs. Tiny models add a third pattern: specialize and fine-tune narrow components, then compose them into a product workflow.

## Key Concepts

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

## Sources

- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Training an LLM from Scratch, Locally - Angelos Perivolaropoulos, ElevenLabs](../sources/20260504_UsB70Tf5zcE.md)
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md)
