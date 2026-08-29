# Scale Test-Time Search Through Parallel Verifier-Checked Branches

Summary: Test-time scaling for agents can run many branched attempts from a shared starting workspace, evaluate them with verifiers, and promote the branch that satisfies the condition. The pattern converts more wall-clock compute into broader solution-space search without requiring every branch to succeed.

Use when:
- Evaluating agent architectures that use parallel attempts, subagents, or branch-and-bound style search.
- Designing verification conditions for test-time compute over stateful environments.

Details:
- Han frames the cloud-for-agents requirement as declaratively specifying workspaces, passing them among humans and agents, and scaling test-time search against verifiers to find the best answer. 07:23-07:50
- The server demo starts from a prepared snapshot, hands the same environment to multiple parallel agents, lets them try different methods for starting a server on port 8000, and keeps the successful solution when another branch fails. 07:54-09:28
- In the chess demo, a tool-using reasoning agent interacts with a restricted chess engine treated as a verifier; reasoning-time branching then lets it explore more of the solution space and escape a local minimum. 11:35-13:38
- The talk identifies the infrastructure bottleneck as creating branchable environments that support large-scale reinforcement learning and multi-agent coordination with less wall-clock time. 13:44-14:36
- **The search is only as good as what the verifier can see.** On multi-GPU kernel generation, parallel sampling lifted correct solutions from 28 to 36 of 87 while the share that was both correct and faster than baseline "plateaus out at roughly 31%." The asymmetry has a clean cause: a verifier that runs the code can detect compile and correctness failures, and "if you do multiple sampling or have the model kind of look at its errors and correct them, it can often compile the kernels" — but a slow-yet-correct kernel returns no error to branch away from. Where a quality dimension is not part of the verifier's signal, expect branch-and-promote to plateau on it. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 24:45-25:11, 26:28-26:44)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Build RL Environments as Software Artifacts](build-rl-environments-as-software-artifacts.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Prefer outcome verifiers over ground-truth path checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md)
- [More Samples Buy Correctness, Not Speedups](more-samples-buy-correctness-not-speedups.md)

Sources:
- [Infrastructure for the Singularity - Jesse Han, Morph](../sources/20250801_2goSS66XRBk.md), 07:23-14:36
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 24:45-25:11, 26:28-26:44
