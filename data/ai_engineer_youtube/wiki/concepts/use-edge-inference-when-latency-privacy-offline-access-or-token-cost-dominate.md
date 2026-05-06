# Use Edge Inference When Latency, Privacy, Offline Access, Or Token Cost Dominate

Summary: On-device inference is most compelling when a workflow needs real-time latency, local handling of sensitive data, offline operation, or lower cloud token spend. A hybrid design can shift suitable work to the device while keeping cloud calls for tasks that need them.

Use when:
- Deciding whether an AI feature should run locally, in the cloud, or as a hybrid.
- Designing camera, voice, summarization, or sensitive-document workflows.

Details:
- Real-time camera features, video-call filters, and background replacement are examples where local latency can matter more than raw model capability.
- Local execution also helps with sensitive summarization, poor-connectivity use cases, and cost control by reducing token-heavy cloud calls.
- The talk frames edge-vs-cloud as a balance rather than a strict replacement: on-device inference can offset cloud work where the device is good enough.

Related topics:
- [Edge Inference](../topics/edge-inference.md)

Related concepts:
- [Match Gemma edge model size to device memory and interaction class](match-gemma-edge-model-size-to-device-memory-and-interaction-class.md)

Sources:
- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md), 02:13-03:06
