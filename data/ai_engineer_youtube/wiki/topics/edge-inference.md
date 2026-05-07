# Edge Inference

## Overview

Edge inference is most useful when latency, privacy, offline access, or cloud-token cost dominate the product constraint. The practical design pattern is hybrid: push suitable workloads onto the device, size the model to the target hardware, and keep cloud calls for tasks that exceed local capability. Edge models are not just smaller cloud models: memory-bound architectures, embedding-layer overhead, operator choice, quantization, and post-training targets all need to be optimized against local hardware and narrow product jobs. Gemma 4's effective models add concrete examples of this pressure: per-layer embeddings trade flash storage for lower VRAM pressure, and multimodal token budgets let developers spend image/audio context only where the task needs it. Local demos in airplane mode, through llama.cpp, and through MLX on iPhone reinforce that the target runtime, device class, offline requirement, download size, and streaming UX should drive model selection. For agentic edge workflows, the context and tool surface must also be compressed: expose skill descriptions first, load details on demand, and use runtime constraints when small models generate tool calls.

Physical robotics is a sharper edge-inference case because deployment means running action-producing models on the robot itself. GR00T N1's lifecycle separates simulation/data generation, training, and edge deployment, with the deployed model needing to be efficient enough for AGX-like robot hardware while still translating perception and language into continuous motion.

## Key Concepts

- [Use edge inference when latency, privacy, offline access, or token cost dominate](../concepts/use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md) - local execution is strongest when responsiveness, data locality, connectivity, or cost matter more than maximum model capability.
- [Treat edge models as their own architecture class](../concepts/treat-edge-models-as-their-own-architecture-class.md) - edge models should be designed around local memory, latency, and narrow capability instead of scaled-down large-model defaults.
- [Route Gemma 4 model variants by deployment and workflow shape](../concepts/route-gemma-4-model-variants-by-deployment-and-workflow-shape.md) - effective Gemma variants target local multimodal work while larger variants serve heavier reasoning and hosted workflows.
- [Per-layer embeddings move effective-model capacity out of VRAM](../concepts/per-layer-embeddings-move-effective-model-capacity-out-of-vram.md) - PLE uses flash-backed layer embeddings to reduce VRAM pressure on phones and laptops.
- [Tune multimodal token budgets by visual or audio task](../concepts/tune-multimodal-token-budgets-by-visual-or-audio-task.md) - local multimodal workloads should allocate image and audio tokens according to task detail needs.
- [Profile small-model architectures on target hardware](../concepts/profile-small-model-architectures-on-target-hardware.md) - target-device profiling validates whether architecture choices actually reduce latency and memory use.
- [Use MLX Swift LM for Apple local model integration](../concepts/use-mlx-swift-lm-for-apple-local-model-integration.md) - native Apple apps can run local MLX-compatible models by pulling curated Hugging Face weights through MLX Swift LM.
- [Match Gemma edge model size to device memory and interaction class](../concepts/match-gemma-edge-model-size-to-device-memory-and-interaction-class.md) - model choice should account for quantized memory footprint and the interaction class being served.
- [Benchmark edge models across the device fleet before shipping](../concepts/benchmark-edge-models-across-the-device-fleet-before-shipping.md) - deployment quality depends on the full fleet, not a current development device.
- [Edge agent skills need progressive disclosure to preserve small-model reliability](../concepts/edge-agent-skills-need-progressive-disclosure-to-preserve-small-model-reliability.md) - edge agents should see only lightweight skill metadata until a task requires deeper instructions.
- [Constrained decoding makes small-model tool calls production-usable](../concepts/constrained-decoding-makes-small-model-tool-calls-production-usable.md) - narrowing generation to valid tool-call shapes improves reliability for small local models.
- [Modular tiny-model pipelines reuse specialized models across mobile app workflows](../concepts/modular-tiny-model-pipelines-reuse-specialized-models-across-mobile-app-workflows.md) - mobile apps can compose specialized tiny models for speech, personalization, and text generation.
- [Physical AI Has a Three-Stage Compute Lifecycle](../concepts/physical-ai-has-a-three-stage-compute-lifecycle.md) - robot foundation models need edge deployment planned alongside simulation and training.

## Open Questions

- How should teams decide the cutoff where local quality is good enough and cloud fallback becomes unnecessary?
- Which edge skills should be available by default, and which should stay disabled until the user or product context opts in?
- Which architecture changes produce measurable user-facing gains across the oldest supported edge devices?
- Which multimodal token budgets preserve enough OCR, object-recognition, or speech quality on the oldest devices in the supported fleet?

## Sources

- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md)
- [Gemma 4 Deep Dive - Cassidy Hardin, Researcher, Google DeepMind](../sources/20260427__A367W_qvc8.md)
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md)
- [Gemma, DeepMind's Family of Open Models - Omar Sanseviero, Google DeepMind](../sources/20260420__gVFUEdhCyI.md)
- [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX - Adrien Grondin, Locally AI](../sources/20260420_a2muGkT4WD4.md)
- [What Is a Humanoid Foundation Model? An Introduction to GR00T N1 - Annika & Aastha](../sources/20250728_mWKYvT9Lc50.md)
