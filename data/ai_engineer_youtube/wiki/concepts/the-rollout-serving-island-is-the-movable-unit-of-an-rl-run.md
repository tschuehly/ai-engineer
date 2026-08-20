# The Rollout Serving Island Is the Movable Unit of an RL Run

Summary: When splitting an RL post-training loop across locations, the boundary to cut on is the absence of a global all-reduce, not the label "training versus inference." Back-propagation stays in one RDMA-connected cluster because every step has collectives; rollout can leave in units of a *serving island* — a coherent endpoint or local group of endpoints serving one policy version — because islands never talk to each other.

Use when:
- Deciding which components of a training system may run outside the trainer's cluster.
- Designing an RL system whose rollout capacity must scale independently of the trainer.
- Reasoning about what an "async RL" architecture actually decouples.
- Choosing the granularity at which rollout capacity is added and removed.

Details:
- What must stay, and why: "training is one tightly coupled job. Every step has collectives, all-reduce and the model parallel communication. That part actually wants one fast fabric, an RDMA-connected [cluster]." The requirement belongs to the collective, not to training as a category. ([Modal](../sources/20260810_maRzp4kImJ4.md), 03:25-03:37)
- What may leave: "rollout is a fleet of serving jobs. It generates trajectories, calls environments or maybe tools… across rollout jobs there's no global all-reduce. So the thing I want to move here is not back propagation. Back propagation should stay in the cluster. The rollout fleet is the one that can leave." (03:37-03:59)
- **The unit is the island, not the GPU and not the fleet.** "The movable unit is the rollout serving island, a coherent endpoint or maybe a local group of endpoints that can be serving one policy version inside [the] island. A large model may still be having local parallelism. They can do PD disaggregation. They can have local serving constraints." Tight coupling is permitted *within* an island — tensor parallelism, prefill/decode disaggregation — because those collectives are local; the island is exactly the largest scope over which fast interconnect is still required. (03:59-04:18)
- The payoff is a very narrow global interface: "across islands the dependency is much lighter right now: policy version in and the trajectory and the metadata out," restated as "the global interface is very simple: the trainer sends policy weight version out and the rollout sends trajectory and the metadata back." Two directions, both coarse-grained, neither latency-critical at collective timescales. (04:18-04:25, 04:48-05:03)
- **Cutting on the collective, rather than on the workload name, is what makes the boundary usable.** It says precisely why a rollout island can sit in another region (no cross-island collective) *and* why it cannot be shattered into individual GPUs (intra-island collectives are real). Systems that split on "training vs. inference" get the first half of that and have no principled answer for the second.
- Having removed the collective, exactly one dependency remains and it becomes the whole engineering problem: "at this point the architecture depends on one remaining link, the weight update." The rest of the talk is about making that link small enough to cross a commodity network — see [Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint](synchronize-rollout-weights-with-a-bitwise-lossless-patch.md). (05:03-05:16)
- Relation to existing decoupled-rollout designs in this wiki: [Use hybrid RL system design for agent trajectories](use-hybrid-rl-system-design-for-agent-trajectories.md) decouples rollout workers from the trainer to stop slow agent tasks from blocking the pipeline — a *scheduling* motivation, with the workers still inside the cluster. This page decouples for a *placement* reason, and the unit it names is what lets the same split cross a region boundary. The two are compatible and address different costs.
- Limits: the argument assumes the model fits inside one island's local parallelism. Jiang allows that "a large model may still be having local parallelism," but gives no guidance on what happens when a policy is too large to serve within any single island available in the bazaar, and no measurement of how island size interacts with trajectory throughput. ([Modal](../sources/20260810_maRzp4kImJ4.md), 03:59-04:18)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)
- [Inference](../topics/inference.md)

Related concepts:
- [RL Post-Training Demands Four Scarce Compute Properties at Once](rl-post-training-demands-four-scarce-compute-properties-at-once.md)
- [Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint](synchronize-rollout-weights-with-a-bitwise-lossless-patch.md)
- [Publish Immutable Weight Versions to a Bulletin Board](publish-immutable-weight-versions-to-a-bulletin-board.md)
- [Use hybrid RL system design for agent trajectories](use-hybrid-rl-system-design-for-agent-trajectories.md)
- [Pipeline RL Trades Policy Staleness for GPU Throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md)
- [Inference Tolerates Degraded GPUs That Training Cannot](inference-tolerates-degraded-gpus-that-training-cannot.md)

Sources:
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 03:22-05:16
