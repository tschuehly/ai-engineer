# Inference Tolerates Degraded GPUs That Training Cannot

Summary: A GPU that must be pulled from a training cluster is often still perfectly good for serving. Synchronous multi-node training runs at the speed of its slowest participant, so one warm or flaky card destabilizes the whole run; single-node inference has no collective to hold up, so it keeps working on hardware that is thermally marginal or intermittently faulty. Treating "training-grade" and "inference-grade" as different hardware tiers is what lets the same fleet absorb degraded cards instead of idling them.

Use when:
- Deciding what to do with GPUs that failed a training-cluster health threshold.
- Planning where evicted, spillover, or burst inference can safely run.
- Negotiating for cheaper external capacity whose hardware quality is unknown or variable.
- Explaining why one workload demands homogeneous healthy hardware and another does not.

Details:
- The claim, from Krea's infra lead, at the end of a talk about a cluster shared between training and serving: "if you're doing like diffusion transformers, they're not huge like LLMs that need like multi-node inference. Something that we learned: whatever GPU works. The GPU can be hot, falling out of the bus. It can be exploding. Inference still going to run. It is very interesting. So, like you can have very very bad GPUs for inference and everyone's going to be happy." ([Menezes](../sources/20260818_byn9PURoBNY.md), 16:02-16:22)
- The stated precondition is model size: their diffusion transformer fits on one node. The tolerance follows from the absence of cross-node collectives, not from diffusion being intrinsically robust — so the asymmetry weakens exactly where inference itself becomes distributed, as it is for large LLMs requiring multi-node serving.
- The contrast is drawn against the same talk's training rule, which is unusually strict: any GPU above 78 °C is pulled without investigation, because a single warmer card throttles, slows, and makes "the training… unstable." Same fleet, same hardware population, opposite tolerance — the difference is entirely the workload's coupling. (04:46-05:17)
- The economic consequence is that hardware quality becomes a routing parameter rather than a pass/fail gate. Cards that would be quarantined for training remain revenue-generating on the serving tier, which is also what makes it viable to send evicted inference to cheap external providers whose hardware you do not control — see [Evict Inference Off-Cluster Through a Virtual-Kubelet Node](evict-inference-off-cluster-through-a-virtual-kubelet-node.md).
- Failure semantics differ too, and Kubernetes already exploits this: an inference pod that dies is marked failed and replaced, losing one request's work, while a training crash rolls back to the last checkpoint. Cheap-to-restart workloads can accept hardware that expensive-to-restart workloads cannot. (12:53-13:41)
- Caveats the talk does not address: it says nothing about *silent* degradation — a card producing wrong results rather than crashing — which inference would not notice and which no checkpoint would catch, nor about tail-latency effects when a throttling GPU serves user-facing traffic. The claim as given is about availability, not about quality or latency SLOs.

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Generative Media](../topics/generative-media.md)

Related concepts:
- [Evict Inference Off-Cluster Through a Virtual-Kubelet Node](evict-inference-off-cluster-through-a-virtual-kubelet-node.md)
- [Give Training Priority Over Production on a Shared GPU Cluster](give-training-priority-over-production-on-a-shared-gpu-cluster.md)
- [Let Training Crash and Checkpoint Against a Fast Filesystem](let-training-crash-and-checkpoint-against-a-fast-filesystem.md)
- [Benchmark And Rate Heterogeneous GPU Providers](benchmark-and-rate-heterogeneous-gpu-providers.md)
- [Aggregate Idle GPU Supply Through Compute Marketplaces](aggregate-idle-gpu-supply-through-compute-marketplaces.md)
- [Hot-swap small models to avoid one-model-per-GPU waste](hot-swap-small-models-to-avoid-one-model-per-gpu-waste.md)

Sources:
- [Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai](../sources/20260818_byn9PURoBNY.md), 04:46-05:17, 12:53-13:41, 16:02-16:22
