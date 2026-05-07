# Route LoRA Voice Clones With Sticky GPU Affinity

Summary: Voice-clone serving needs routing that accounts for LoRA residency and session continuity, not only generic request balancing. Sticky GPU affinity and consistent hashing can keep a realtime voice session on a server that already has the required adapter while still allowing gradual scaling.

Use when:
- Serving many voice clones or task adapters over a shared GPU fleet.
- Designing load balancing for streaming inference sessions that should stay on the same accelerator.

Details:
- Gabber needed batch inference with multiple LoRAs on the same GPU, multiple language-specific models, and one load balancer in front of the fleet rather than separate bespoke serving paths. (10:55-11:33)
- LoRAs are described as roughly 100-200 MB depending on hyperparameters, so a request should preferably land on a server where the required adapter is already resident in memory. (12:31-12:48)
- Gabber used a consistent hash ring with virtual nodes so a generation request maps to a stable server; the same strategy limits traffic movement when a server is removed. (13:13-13:54)
- Popular voice clones can be replicated by adding their LoRA to more servers, which lets the system scale that clone up and down without a large routing redesign. (13:56-14:13)

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Hot-swap small models to avoid one-model-per-GPU waste](hot-swap-small-models-to-avoid-one-model-per-gpu-waste.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)
- [Serve Realtime TTS By Audio-Token Throughput](serve-realtime-tts-by-audio-token-throughput.md)

Sources:
- [Serving Voice AI at $1/hr: Open-source, LoRAs, Latency, Load Balancing - Neil Dwyer, Gabber](../sources/20250731_rD23-VZZHOo.md), 10:55-14:13
