# Edge Inference

## Overview

Edge inference is most useful when latency, privacy, offline access, or cloud-token cost dominate the product constraint. The practical design pattern is hybrid: push suitable workloads onto the device, size the model to the target hardware, and keep cloud calls for tasks that exceed local capability. Whether to own or offload a given workload is best treated as a threshold decision across four axes — is the model capable, does it fit the hardware, does it meet the latency budget, and does the cost beat the alternative — where on-device the unit of cost shifts from tokens to energy (GPU/NPU utilization), so scheduling a job as a realtime response versus an offline background task is itself a design lever. Edge models are not just smaller cloud models: memory-bound architectures, embedding-layer overhead, operator choice, quantization, and post-training targets all need to be optimized against local hardware and narrow product jobs. Gemma 4's effective models add concrete examples of this pressure: per-layer embeddings trade flash storage for lower VRAM pressure, and multimodal token budgets let developers spend image/audio context only where the task needs it. Local demos in airplane mode, through llama.cpp, and through MLX on iPhone reinforce that the target runtime, device class, offline requirement, download size, and streaming UX should drive model selection. For agentic edge workflows, the context and tool surface must also be compressed: expose skill descriptions first, load details on demand, and use runtime constraints when small models generate tool calls.

Physical robotics is a sharper edge-inference case because deployment means running action-producing models on the robot itself. GR00T N1's lifecycle separates simulation/data generation, training, and edge deployment, with the deployed model needing to be efficient enough for AGX-like robot hardware while still translating perception and language into continuous motion.

Generation paradigm is itself an edge lever. Text diffusion is much lower latency per request than autoregressive decoding but loses big-batch throughput, so its natural first home is on-device serving (phones, robotics in the Alphabet ecosystem) where you serve batch-of-1 and throughput is a non-issue — and since a diffusion model's quality is "the same basically" as a frontier autoregressive model, you pick the lowest-latency option. This is the same latency-dominant logic as the four-axis ownership decision, applied to how a model generates rather than where it runs.

Deciding *which* workload goes on device is itself a measurement discipline, not a reflex. RL Nabors sharpens the four-axis ownership call with a concrete cost taxonomy for one-size-fits-all cloud inference — security costs trust, latency costs UX (a ~4-second believability limit that many frontier calls blow through), third-party inference cost is uncontrollable and compounds under agentic token growth, remote models fail offline, and an SLM burns ~25% of an LLM's per-task energy (a task-specific model half of that again, with the battery cost shifted to the consumer). Her right-sizing framework — "prototype big, deploy small" — turns the switch into an eval: prove the task is possible on the largest model, freeze a golden dataset of success criteria, benchmark from the smallest model up, and select the SAGE ("small and good enough") model, then close any remaining gap with per-variant prompt engineering and deterministic harness post-processing rather than reaching back for the frontier model. In her summarization case a Llama 3.2 3B beat both a slower Gemma 4 and a peer recommendation on the accuracy-vs-latency tradeoff, and on-device APIs are already available to ship into (Chrome's prompt API exposes Gemini Nano; the Pixel 10 Pro ships an SLM). This reinforces the topic's core lesson that edge models are not just smaller cloud models — the decision to move a call on device is made by measuring your own task, not by the leaderboard or by which model your friends like.

## Key Concepts

- [Use edge inference when latency, privacy, offline access, or token cost dominate](../concepts/use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md) - local execution is strongest when responsiveness, data locality, connectivity, or cost matter more than maximum model capability.
- [Right-size models with prototype-big, deploy-small](../concepts/right-size-models-with-prototype-big-deploy-small.md) - prove the task on the largest model, freeze success criteria as a golden dataset, benchmark small-to-large, and select the SAGE (small-and-good-enough) model instead of guessing.
- [Close the small-model gap with prompt variants and harness post-processing](../concepts/close-the-small-model-gap-with-prompt-variants-and-harness-post-processing.md) - lift a near-baseline small model with one-variable-per-variant prompt testing (few-shot beat strict rules) plus deterministic post-processing, without swapping the model.
- [Decide open-model ownership by capability, hardware, latency, and cost thresholds](../concepts/decide-open-model-ownership-by-capability-hardware-latency-and-cost-thresholds.md) - on-device offload is a four-axis threshold decision where cost is measured in energy, not tokens.
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
- [Text Diffusion Trades Serving Throughput for Low Latency](../concepts/text-diffusion-trades-serving-throughput-for-low-latency.md) - low-latency, low-throughput text diffusion fits on-device serving where batch-of-1 makes throughput a non-issue.

## Open Questions

- How should teams decide the cutoff where local quality is good enough and cloud fallback becomes unnecessary?
- Which edge skills should be available by default, and which should stay disabled until the user or product context opts in?
- Which architecture changes produce measurable user-facing gains across the oldest supported edge devices?
- Which multimodal token budgets preserve enough OCR, object-recognition, or speech quality on the oldest devices in the supported fleet?

## Sources

- [Frontier results, on device - RL Nabors, Arize](../sources/20260629_fWXJM-J0ZB8.md)
- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md)
- [Gemma 4 Deep Dive - Cassidy Hardin, Researcher, Google DeepMind](../sources/20260427__A367W_qvc8.md)
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md)
- [Gemma, DeepMind's Family of Open Models - Omar Sanseviero, Google DeepMind](../sources/20260420__gVFUEdhCyI.md)
- [Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind](../sources/20260610_SS-A8sE7hkw.md)
- [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX - Adrien Grondin, Locally AI](../sources/20260420_a2muGkT4WD4.md)
- [What Is a Humanoid Foundation Model? An Introduction to GR00T N1 - Annika & Aastha](../sources/20250728_mWKYvT9Lc50.md)
- [Text Diffusion — Brendan O'Donoghue, Google DeepMind](../sources/20260604_r305-aQTaU0.md)
