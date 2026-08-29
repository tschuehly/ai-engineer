# Push Agent Benchmarks on Environment Complexity, Autonomy Horizon, and Output Complexity

Summary: Snorkel's bet on where the next generation of agent benchmarks must go is three under-covered axes: environment complexity (how realistic and dynamic the operating world is), autonomy horizon (how long an agent runs before reliability breaks down), and output complexity (work and reward signals beyond plain text). Today's benchmarks capture only a fraction of each.

Use when:
- Designing an agent benchmark and choosing which dimension to push beyond current sets.
- Explaining why a high benchmark score doesn't predict real deployment readiness.
- Mapping the gap between toy agent tasks and real enterprise/professional work.

Details:
- Environment complexity: how complex, realistic, and dynamic is the operating environment, and is it representative of what a professional would actually use? A real codebase has org-specific policies, lots of Slack context, screenshots, flaky toolchains, distributed CI, human reviewers with preferences in their heads, and many parallel contributors — "benchmarks today capture a fraction of this complexity," and this gap is where agents fail. (18:55-20:47)
- Autonomy horizon: how long an agent can operate before reliability breaks down, and whether the benchmark intentionally captures different points on the co-pilot↔fully-autonomous slider. A customer-experience agent may lose track of context delivered weeks ago, see integrations/specs change the requirements, or have a reorg shift priorities midstream — long-horizon, continual-learning settings with changing state and environment. (18:49-21:37)
- Output complexity beyond plain text: produce more complex, representative work and *nuanced* signals usable for both evaluation and reward during training. It is subjective and non-trivial to define what is verifiable about a good strategic recommendation, proposal, or roadmap — it needs organizational context and real human judgment. A related target is "trustworthy outputs": agents that capture their own uncertainty and stop or ask for more information rather than always emitting a plain-text answer, plus new artifact form factors for how agents interact with humans and each other. (18:58-22:35)
- These three are framed as degrees of freedom for creativity, not a rigid spec — "areas where we think there's a lot of room to push complexity and realism in benchmarks." (18:17-18:43)
- **An output-complexity axis realized concretely: grade on speed, not on text.** ParallelKernelBench's reward signal is not a string comparison — the artifact must compile, run correctly across ranks, and beat a runnable PyTorch+NCCL reference on wall-clock, which is captured in a second metric (`fast_1@k`) alongside plain correctness. It also carries an environment-complexity element that is cheap to copy: each task ships "a system topology that specifies the number of ranks and intra-node hardware configuration," making the correct answer depend on the deployment environment rather than on the prompt alone. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 22:07-22:33, 24:00-24:30)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Design Benchmarks as Forward Bets That Shape the Field](design-benchmarks-as-forward-bets-that-shape-the-field.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Benchmark saturation pushes capability evals toward human time horizons](benchmark-saturation-pushes-capability-evals-toward-human-time-horizons.md)
- [Coding-Agent Capability Tiers Change the Bottleneck](coding-agent-capability-tiers-change-the-bottleneck.md)
- [Evaluate whether models reject impossible or nonsensical premises](evaluate-whether-models-reject-impossible-or-nonsensical-premises.md)
- [Specify a Generation Task as a Reference Implementation Plus a Topology Spec](specify-a-generation-task-as-a-reference-implementation-plus-a-topology-spec.md)

Sources:
- [The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI](../sources/20260604_iNkFlCiij0U.md), 18:17-22:35
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 22:07-22:33, 24:00-24:30
