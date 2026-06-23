# Route Gemma 4 Model Variants By Deployment And Workflow Shape

Summary: Gemma 4 is useful as a deployment menu rather than one model choice: effective 2B/4B models target on-device multimodal input, while 26B MoE and 31B dense models target heavier reasoning, coding, function calling, and agentic workflows.

Use when:
- Selecting a Gemma model for local, edge, hosted, coding, or agentic work.
- Deciding whether a workload needs on-device efficiency, sparse active parameters, or dense long-context reasoning.

Details:
- The family is presented as four sizes: smaller effective models for on-device applications and two larger models, including a 26B MoE and a 31B dense model. (00:51-01:29)
- The 26B MoE is described as requiring only about 3.8-3.9B active parameters during a forward pass, which makes it a sparse-efficiency option rather than a fully dense 26B runtime. (01:13-01:25, 03:03-03:24)
- The 31B dense model is positioned for advanced reasoning with a 256K context length plus native thinking, function calling, and structured JSON outputs for autonomous workflows. (02:25-02:56)
- The effective 2B and 4B models support vision, text, and audio inputs with text output while being optimized for phones and laptops rather than remote API-only deployment. (03:30-03:47, 08:11-08:24)
- The suggested adoption paths are self-hosting through Hugging Face, Kaggle, and Ollama for downloadable models, or hosted access through AI Studio and Vertex for the larger models. (18:06-18:34)
- A second Gemma overview presents the same routing pattern as a product menu: the smallest variants target Android, iOS, Raspberry Pi, and on-device agentic workflows; the MoE variant targets low latency; and the 31B dense model targets the highest raw capability while still fitting a consumer GPU. (01:26-02:25)
- Local demos included airplane-mode phone execution with no API calls, parallel llama.cpp instances on a laptop, and offline coding or Android development examples, reinforcing that deployment target should shape model choice. (02:38-03:35, 10:07-10:40)
- A third Gemma talk reinforces the efficiency-per-size argument: the 31B dense ranks ~4th/7th among open models on LM Arena while running on a single GPU, where comparable-quality competitors need ~200 GB of memory (≈4-5 GPUs); the 26B MoE was demonstrated running in LM Studio on an M4 Mac (~26 GB RAM with context) driving a parallel multi-agent translation that compiled results into a generated web page. (Sovereign Escape Velocity, 04:18-06:00, 16:05-18:25)
- The same talk frames AI.dev (AI Studio) as the zero-setup way to try the 26B/31B variants free, including vision + thinking + code execution in one call, before committing to a self-hosted path. (06:00-06:30)

Related topics:
- [Agents](../topics/agents.md)
- [Edge Inference](../topics/edge-inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Match Gemma edge model size to device memory and interaction class](match-gemma-edge-model-size-to-device-memory-and-interaction-class.md)
- [Open Model Families Need Ecosystem-Compatible Tooling](open-model-families-need-ecosystem-compatible-tooling.md)
- [Use hosted model playgrounds to prototype before owning infrastructure](use-hosted-model-playgrounds-to-prototype-before-owning-infrastructure.md)
- [Decide open-model ownership by capability, hardware, latency, and cost thresholds](decide-open-model-ownership-by-capability-hardware-latency-and-cost-thresholds.md)

Sources:
- [Gemma 4 Deep Dive - Cassidy Hardin, Researcher, Google DeepMind](../sources/20260427__A367W_qvc8.md), 00:51-03:47, 18:06-18:34
- [Gemma, DeepMind's Family of Open Models - Omar Sanseviero, Google DeepMind](../sources/20260420__gVFUEdhCyI.md), 01:26-03:35, 10:07-10:40
- [Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind](../sources/20260610_SS-A8sE7hkw.md), 04:18-06:30, 16:05-18:25
