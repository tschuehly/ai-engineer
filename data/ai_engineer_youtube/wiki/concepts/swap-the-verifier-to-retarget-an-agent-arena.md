# Swap the Verifier to Retarget an Agent Arena

Summary: In a well-built agent arena the only domain-specific component is the verifier. Together AI pointed the same environment — same leaderboard, same forum, same competition and collaboration mechanics — at GPU kernel optimization by replacing the mathematics checker with a compile-benchmark-test backend, and the agents produced kernels reported at over 2x, now running in production.

Use when:
- You have built an eval harness or agent environment for one domain and are asking what part of it transfers.
- Scoping how much work a new agent-optimization problem actually costs: a verifier, or a whole platform.
- Judging whether a demonstrated environment design generalizes or was tuned to its showcase problem.
- Deciding where to spend engineering effort inside an environment.

Details:
- The retarget, stated as a substitution: "we use the same environment, right? Where the agents can compete and they also can collaborate and they see these leaderboards. And we basically change the back end instead of trying to verify the solutions to this mathematics problem, here we're basically trying to… compile and benchmark and test and verify the quality and the speed of the individual kernels… and then we'll provide a feedback to the agents in real time in the form of these leaderboards." (08:57-09:41)
- **What this says about where the engineering is.** Everything that made the arena work for an open mathematics problem — the entry gate, the problem pages, the discussion forum, the downloadable submissions, the live scoring loop — is domain-neutral infrastructure. The domain-specific part is a function from submission to score. That is a useful cost model: a new problem class costs a verifier, provided the outcome is mechanically checkable at all.
- **The kernel verifier is heavier than the mathematics one, and this is the real constraint.** Checking a sphere packing is a geometric predicate; scoring a kernel means compiling it, running it on the target hardware, checking numerical correctness, and timing it reliably. The wiki's [kernel evaluation page](evaluate-generated-kernels-for-correctness-performance-and-benchmark-gaming.md) enumerates what that backend has to get right — tolerance policy, representative shapes, warmups, cache clearing, ordering effects — none of which the talk describes. "Swap the verifier" understates the work when the verifier is a hardware-in-the-loop measurement rig.
- Reported outcome: "sometimes over two-fold speed ups in some of these production kernels," shown "for things like page attention… for specific shapes, but we also have generalized this to many different shapes and different hardware types," and "these improved kernels… are actually already used in production at Together AI." (10:14-10:54)
- **This is the same organization that measured the ceiling of the alternative approach.** Simran Arora's ParallelKernelBench work, also at Together AI, found that a standard multi-turn coding harness lifted a frontier model from 24 to 35 of 87 multi-GPU kernel problems and then flatly plateaued: "as we scaled the amount of time the performance plateaued, and additional techniques would be required to continue seeing the scaling there," with the diagnosis that compile and correctness errors produce a signal the loop can act on while performance decisions produce no error to act on. An arena is a candidate answer to exactly that gap — the leaderboard makes speed a visible, comparable, refinable signal rather than a silent property of a passing kernel, and rival submissions supply the counterfactual a self-correcting loop never sees. The two talks do not reference each other, so read this as a coherence between two results from one company rather than as a claimed causal fix. See [Use Hardware-In-The-Loop Search For AI Kernel Generation](use-hardware-in-the-loop-search-for-ai-kernel-generation.md).
- **The evidence quality is deployment, not measurement.** "Over 2x" names no baseline, no tolerance, no timing protocol, no hardware, and no aggregate. "Already used in production at Together AI" is a different and in some ways better kind of claim — someone accepted the kernels into a serving path — but it reports adoption rather than a margin, and it comes from the group that both produced and adopted them.
- **The corollary is the constraint on the whole pattern.** An arena can only be pointed at problems where a verifier can be written. That is the same admission filter the arena applies to its mathematics problems ([Curate Tasks by Live Human Demand and a Deterministic Verifier](curate-tasks-by-live-human-demand-and-a-deterministic-verifier.md)) and the same boundary the wiki draws around [verifiable-reward RL](use-verifiable-rewards-for-language-model-rl.md). Domains without a mechanical scorer do not become arena-shaped by adding a leaderboard; they need [a high-fidelity engine built first](build-high-fidelity-engines-to-create-verification-loops-in-non-code-domains.md).

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Design the Environment, Not the Workflow](design-the-environment-not-the-workflow.md)
- [Open Agent Arenas Reach Solutions No Single Agent Reaches](open-agent-arenas-reach-solutions-no-single-agent-reaches.md)
- [Give Parallel Agents Complementary Optimization Personas](give-parallel-agents-complementary-optimization-personas.md)
- [Use Hardware-In-The-Loop Search For AI Kernel Generation](use-hardware-in-the-loop-search-for-ai-kernel-generation.md)
- [Evaluate Generated Kernels For Correctness, Performance, And Benchmark Gaming](evaluate-generated-kernels-for-correctness-performance-and-benchmark-gaming.md)
- [Use AI Kernel Generation For Known Optimization Patterns, Not Expert-Level Breakthroughs](use-ai-kernel-generation-for-known-optimization-patterns-not-expert-level-breakthroughs.md)
- [Use Verifiable Rewards for Language-Model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Build High-Fidelity Engines to Create Verification Loops in Non-Code Domains](build-high-fidelity-engines-to-create-verification-loops-in-non-code-domains.md)
- [Build RL Environments as Software Artifacts](build-rl-environments-as-software-artifacts.md)

Sources:
- [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../sources/20260825_mMNkdYnIVC4.md), 08:57-10:54
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 27:07-27:56
