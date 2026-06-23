# Decide Open-Model Ownership by Capability, Hardware, Latency, and Cost Thresholds

Summary: Deciding whether to own or offload a workload to an open model is a threshold decision across four axes — is the model capable of the task, does it fit the target hardware, can it meet the latency budget, and does the cost (energy on-device, capex/opex on a GPU) beat the hosted alternative — and rising agentic token-generation volume is what tips that calculation toward ownership.

Use when:
- Choosing whether a specific task should run on a hosted frontier API, a single owned GPU, or local/edge hardware.
- Sizing an on-device or single-GPU deployment and reasoning about its real cost.
- Explaining why high-token-generation agentic workloads change the ownership math.

Details:
- The driver is the agentic shift: as work moves from single calls to multi-step agentic tasks, token generation rises, and owning the model lets a team control that cost or amortize sunken hardware. The OpenRouter "State of AI" report is cited showing programming among the highest tasks in combined input+output token generation. (09:41-10:46)
- The decision is framed as a set of thresholds that must all hold: the model is capable of the task, it fits the right hardware, it meets the latency budget, and the cost is acceptable. Each is task-specific. (11:39-12:37)
- Latency splits by interaction class: a user-facing task may need a response in a couple of seconds, while a batch-processing task tolerates a looser threshold. (11:55-12:10)
- Cost has two shapes: a sunken infrastructure cost you already own (or are prepared to outlay) and operate on, versus leasing GPU time — the right answer depends on which you have. (12:10-12:37)
- On-device, the unit of cost shifts from tokens to energy: you pay in GPU/NPU utilization, so scheduling matters — does the user need a response now (taking a picture) or can the task run offline as a background job when the phone is plugged in at night. (14:00-14:50)
- Fit the model to where it can run: effective 2B/4B models on a phone, the 26B/31B on a desktop or single GPU, and enterprise workloads scaling down from a 300B-class multi-GPU model to a single H100/A100 or even an L4. Match the workload (refactoring, analysis, small modular code generation) to the smaller owned model rather than reserving it for full systems-architecture redesign. (10:46-11:35, 14:53-15:30)
- Serving tradeoffs to price in: running your own GPU means controlling uptime but carrying maintenance, ongoing, and upfront capex costs; mobile offload means checking device accelerators and RAM; the payoff is offline operation and private data that never leaves the device. (19:00-20:10)

Related topics:
- [Edge Inference](../topics/edge-inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Use edge inference when latency, privacy, offline access, or token cost dominate](use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md)
- [Own Open Models for Sovereignty and Permissionless Adoption](own-open-models-for-sovereignty-and-permissionless-adoption.md)
- [Enterprise Open-Model Adoption Follows Task Pressure](enterprise-open-model-adoption-follows-task-pressure.md)
- [Route Gemma 4 model variants by deployment and workflow shape](route-gemma-4-model-variants-by-deployment-and-workflow-shape.md)
- [Use local AI workstations when iteration, privacy, or latency dominate](use-local-ai-workstations-when-iteration-privacy-or-latency-dominate.md)

Sources:
- [Sovereign Escape Velocity: Ownership w Open Models — Gus Martins, & Ian Ballantyne, Google DeepMind](../sources/20260610_SS-A8sE7hkw.md), 09:41-20:10
