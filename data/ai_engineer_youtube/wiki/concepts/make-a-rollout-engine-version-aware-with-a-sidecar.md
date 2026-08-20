# Make a Rollout Engine Version-Aware With a Sidecar

Summary: An ordinary serving engine has no concept of "which policy version am I." Putting a sidecar in front of it adds exactly that, with three cases: if the engine is already at an acceptable version, proxy the request; if it is behind but can catch up, apply the missing transitions first; if it cannot get there, return "not ready." That single piece of state is what turns any idle GPU running an unmodified engine into a usable RL rollout worker.

Use when:
- Adding RL rollout capacity from serving infrastructure you did not build for training.
- Avoiding a fork of vLLM, SGLang, or another engine to add version semantics.
- Handling a fleet whose members are at different policy versions at the same moment.
- Deciding what to do with a request that arrives at a stale worker.

Details:
- The role, in one sentence: "the sidecar is basically what makes a normal rollout engine version aware." Everything version-related lives beside the engine rather than inside it, so the engine stays stock. ([Modal](../sources/20260810_maRzp4kImJ4.md), 16:43-16:46)
- The three cases: "if the version is already at [an] acceptable commit version, the sidecar just prox[ies] the request. If the engine is behind but they can catch up, the sidecar just appl[ies] the missing transition[s]. If they cannot get there, the sidecar just simply return[s] not ready." (16:46-17:04)
- **The third case is the one that makes the design honest.** A worker that cannot reach the requested version refuses rather than serving a wrong-version completion. In a loop where trajectories are training data, silently answering from a stale policy corrupts the update; a refusal costs one request. Explicit unavailability is cheaper than undetected staleness — which is the same argument the rest of the wiki makes about [Pipeline RL Trades Policy Staleness for GPU Throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md), except that here staleness is *enforced* per request rather than tolerated in aggregate.
- The middle case is where cheap sync pays off. "Applying the missing transitions" is only viable because each transition is a small lossless patch rather than a checkpoint reload — see [Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint](synchronize-rollout-weights-with-a-bitwise-lossless-patch.md) — and because prior versions remain addressable on the board.
- **Why the sidecar shape rather than an engine feature.** The version logic is small, changes independently of the engine, and must work identically across engines a team does not control. Putting it in a proxy keeps the serving stack replaceable: any engine that can load Hugging Face safetensors participates without modification, which is the compatibility argument on [Publish Immutable Weight Versions to a Bulletin Board](publish-immutable-weight-versions-to-a-bulletin-board.md).
- The elasticity claim that follows: "this will be supporting elasticity [in] rollout, and any idle GPU can just be used with this design to support this [disaggregated] rollout," summarized later as "rollout engines autoscale globally. Each one self-syncs its weights, serves, accepts version, and returns rollout metadata. That means scattered inference capacity became one elastic rollout fleet… inference capacity can now become RL capacity." (17:04-17:13, 18:17-18:43)
- That last line is the economically interesting one and should be read as a claim about *fungibility*: it argues serving hardware and RL rollout hardware are the same tier, which is the same asymmetry [Inference Tolerates Degraded GPUs That Training Cannot](inference-tolerates-degraded-gpus-that-training-cannot.md) reaches from the hardware-health side. Both say the training tier is the narrow one and everything else can be pooled.
- **Costs and gaps.** The sidecar adds a hop on every rollout request, unmeasured in the talk. No policy is given for how long an engine may spend catching up before a request is failed, how "not ready" interacts with the caller's retry behavior, or how the fleet avoids a thundering herd when a new version lands. No latency, overhead, or failure-rate numbers appear anywhere. ([Modal](../sources/20260810_maRzp4kImJ4.md), 16:43-17:13)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Publish Immutable Weight Versions to a Bulletin Board](publish-immutable-weight-versions-to-a-bulletin-board.md)
- [Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint](synchronize-rollout-weights-with-a-bitwise-lossless-patch.md)
- [The Rollout Serving Island Is the Movable Unit of an RL Run](the-rollout-serving-island-is-the-movable-unit-of-an-rl-run.md)
- [Pipeline RL Trades Policy Staleness for GPU Throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md)
- [Inference Tolerates Degraded GPUs That Training Cannot](inference-tolerates-degraded-gpus-that-training-cannot.md)
- [Evict Inference Off-Cluster Through a Virtual-Kubelet Node](evict-inference-off-cluster-through-a-virtual-kubelet-node.md)

Sources:
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 16:43-17:13, 18:17-18:43
