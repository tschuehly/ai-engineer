# Use Edge Inference When Latency, Privacy, Offline Access, Or Token Cost Dominate

Summary: On-device inference is most compelling when a workflow needs real-time latency, local handling of sensitive data, offline operation, or lower cloud token spend. A hybrid design can shift suitable work to the device while keeping cloud calls for tasks that need them.

Use when:
- Deciding whether an AI feature should run locally, in the cloud, or as a hybrid.
- Designing camera, voice, summarization, or sensitive-document workflows.

Details:
- Real-time camera features, video-call filters, and background replacement are examples where local latency can matter more than raw model capability.
- Local execution also helps with sensitive summarization, poor-connectivity use cases, and cost control by reducing token-heavy cloud calls.
- The talk frames edge-vs-cloud as a balance rather than a strict replacement: on-device inference can offset cloud work where the device is good enough.
- Nabors gives a five-part cost taxonomy for one-size-fits-all cloud inference: security costs trust (data leaves the stack, risking exposure/interception/retention/breach), latency costs UX (research puts ~4 seconds as the believability limit and many frontier calls exceed it), third-party inference cost is uncontrollable and compounds as agentic reasoning burns tokens faster than prices fall, remote models fail offline, and outages cost productivity. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 01:17-02:48)
- The energy case is concrete: an SLM uses ~25% of an LLM's per-task energy and a task-specific model ~half of that again, and moving inference on device shifts the unit cost from your token bill to the consumer's battery — Nvidia's 2025 paper called SLMs "the future of agentic AI." ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 05:59-06:48, 14:38-15:02)
- On-device APIs already ship: Chrome's prompt API exposes Gemini Nano natively (no model to download for browser users) and the Pixel 10 Pro ships with an SLM. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 05:48-05:51, 28:55-29:20)

Related topics:
- [Edge Inference](../topics/edge-inference.md)

Related concepts:
- [Match Gemma edge model size to device memory and interaction class](match-gemma-edge-model-size-to-device-memory-and-interaction-class.md)
- [Right-size models with prototype-big, deploy-small](right-size-models-with-prototype-big-deploy-small.md)
- [Browser-native AI APIs bring local models into web apps](browser-native-ai-apis-bring-local-models-into-web-apps.md)

Sources:
- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md), 02:13-03:06
- [Frontier results, on device - RL Nabors, Arize](../sources/20260629_fWXJM-J0ZB8.md), 01:17-06:48
