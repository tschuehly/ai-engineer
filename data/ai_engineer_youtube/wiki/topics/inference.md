# Inference

## Overview

Inference is the production discipline of turning trained models into reliable, efficient services. For small models, the main constraint is often not raw compute alone but orchestration across many specialized models: dynamic loading, routing, batching, model-specific runtime support, observability, and autoscaling determine whether the system wastes GPU capacity or becomes a reusable agent and retrieval substrate.

## Key Concepts

- [Profile small-model architectures on target hardware](../concepts/profile-small-model-architectures-on-target-hardware.md) - local inference performance should be measured on the intended hardware, not inferred from architecture alone.
- [Hot-swap small models to avoid one-model-per-GPU waste](../concepts/hot-swap-small-models-to-avoid-one-model-per-gpu-waste.md) - many small models can share accelerator capacity when the runtime supports dynamic loading and eviction.
- [Production inference combines model support with cluster operations](../concepts/production-inference-combines-model-support-with-cluster-operations.md) - serving many model families requires both architecture-specific adaptation and production operations.
- [Use small models as context-management tools before agent reasoning](../concepts/use-small-models-as-context-management-tools-before-agent-reasoning.md) - inference infrastructure can expose narrow models as preprocessing and retrieval tools for agent workflows.

## Open Questions

- How should teams evaluate the latency and quality tradeoff between preprocessing with small models and sending broader raw context to a larger agent model?

## Sources

- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md)
