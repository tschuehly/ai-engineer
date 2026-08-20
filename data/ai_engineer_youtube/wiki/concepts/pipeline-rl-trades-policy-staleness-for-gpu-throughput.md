# Pipeline RL Trades Policy Staleness for GPU Throughput

Summary: Asynchronous pipeline RL improves accelerator utilization by letting sampling and training run concurrently, but it introduces stale-policy tokens that can destabilize learning if staleness is too high. The systems win is only useful when the ML algorithm can tolerate the resulting off-policy data.

Use when:
- Optimizing RL training throughput for language models or agent policies.
- Diagnosing idle GPUs, straggler samples, or unstable async RL runs.

Details:
- Synchronous RL waits for all samples in a batch before training, so the slowest sample determines step time and leaves GPUs idle near the tail of the batch. (04:06-05:23)
- Pipeline RL dedicates some GPUs to sampling and some to training; samplers continuously run high-batch inference, completed samples enter a training queue, and trainers propagate new weights back through in-flight updates. (05:27-06:24)
- In-flight updates can make one trajectory contain tokens from multiple policy versions, so later training may use samples whose earliest tokens came from policies several steps behind the current one. (06:27-07:35)
- Higher tolerated staleness usually reduces idle time, but the importance-ratio variance grows with staleness and can make learning unstable or divergent. (07:42-08:37)
- The practical tradeoff is not simply "async is faster"; teams need a staleness threshold that their algorithm can tolerate before they can turn the systems gain into useful learning. (08:19-08:53)

- **The same company later treats staleness as partly purchasable back, in a different loop.** For distillation over stored production traces — which are days stale by construction — Applied Compute replays the prefix and has the current policy generate exactly one step, "without actually having to interact with the environment," then writes the teacher's hint against that step ([Buy On-Policyness With a Single Rollout Step](buy-on-policyness-with-a-single-rollout-step.md)). Staleness there is not a throughput tradeoff but a supervision-quality one, and the reported fix costs one forward pass rather than an environment. Different loop, same underlying quantity — how far the data is from the policy being updated. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 06:28-07:15, 13:38-14:17)
- The endpoint both talks point at is the same: Denton names "this sort of unified engine of putting inference and training together" as "the holy grail of continual learning," which is the zero-staleness limit of the pipeline this page describes and the reason he expects ceilings to rise "as the infra collapses between serving and training" ([Place a Continual-Learning Setup on Two Axes](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)). ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 01:58-02:48, 10:18-10:36)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Buy On-Policyness With a Single Rollout Step on an Offline Trace](buy-on-policyness-with-a-single-rollout-step.md)
- [Place a Continual-Learning Setup on Two Axes: Trace Policyness and Hint Provenance](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Control environment noise for group-based RL](control-environment-noise-for-group-based-rl.md)
- [Simulate RL run layouts before spending GPU budget](simulate-rl-run-layouts-before-spending-gpu-budget.md)

Sources:
- [Efficient Reinforcement Learning - Rhythm Garg & Linden Li, Applied Compute](../sources/20251209_o15AaYl7Wu0.md), 04:06-08:53
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 01:58-02:48, 06:28-07:15, 10:18-10:36, 13:38-14:17
