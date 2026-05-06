# Edge Inference

## Overview

Edge inference is most useful when latency, privacy, offline access, or cloud-token cost dominate the product constraint. The practical design pattern is hybrid: push suitable workloads onto the device, size the model to the target hardware, and keep cloud calls for tasks that exceed local capability. Edge models are not just smaller cloud models: memory-bound architectures, embedding-layer overhead, operator choice, and post-training targets all need to be optimized against local hardware and narrow product jobs. For agentic edge workflows, the context and tool surface must also be compressed: expose skill descriptions first, load details on demand, and use runtime constraints when small models generate tool calls.

## Key Concepts

- [Use edge inference when latency, privacy, offline access, or token cost dominate](../concepts/use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md) - local execution is strongest when responsiveness, data locality, connectivity, or cost matter more than maximum model capability.
- [Treat edge models as their own architecture class](../concepts/treat-edge-models-as-their-own-architecture-class.md) - edge models should be designed around local memory, latency, and narrow capability instead of scaled-down large-model defaults.
- [Profile small-model architectures on target hardware](../concepts/profile-small-model-architectures-on-target-hardware.md) - target-device profiling validates whether architecture choices actually reduce latency and memory use.
- [Match Gemma edge model size to device memory and interaction class](../concepts/match-gemma-edge-model-size-to-device-memory-and-interaction-class.md) - model choice should account for quantized memory footprint and the interaction class being served.
- [Benchmark edge models across the device fleet before shipping](../concepts/benchmark-edge-models-across-the-device-fleet-before-shipping.md) - deployment quality depends on the full fleet, not a current development device.
- [Edge agent skills need progressive disclosure to preserve small-model reliability](../concepts/edge-agent-skills-need-progressive-disclosure-to-preserve-small-model-reliability.md) - edge agents should see only lightweight skill metadata until a task requires deeper instructions.
- [Constrained decoding makes small-model tool calls production-usable](../concepts/constrained-decoding-makes-small-model-tool-calls-production-usable.md) - narrowing generation to valid tool-call shapes improves reliability for small local models.
- [Modular tiny-model pipelines reuse specialized models across mobile app workflows](../concepts/modular-tiny-model-pipelines-reuse-specialized-models-across-mobile-app-workflows.md) - mobile apps can compose specialized tiny models for speech, personalization, and text generation.

## Open Questions

- How should teams decide the cutoff where local quality is good enough and cloud fallback becomes unnecessary?
- Which edge skills should be available by default, and which should stay disabled until the user or product context opts in?
- Which architecture changes produce measurable user-facing gains across the oldest supported edge devices?

## Sources

- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md)
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md)
