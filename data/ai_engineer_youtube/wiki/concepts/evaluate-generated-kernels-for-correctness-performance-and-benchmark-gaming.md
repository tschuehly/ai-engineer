# Evaluate Generated Kernels For Correctness, Performance, And Benchmark Gaming

Summary: Generated kernels need evaluation that checks numerical correctness, representative workload shape, reliable timing, and whether the agent exploited benchmark assumptions instead of producing a generally valid optimization.

Use when:
- Scoring an AI kernel-generation agent or comparing prompt, context, and harness changes.
- Reviewing large reported speedups from generated low-level code.

Details:
- Floating-point correctness requires an explicit tolerance policy, and benchmark inputs must be large and representative enough that the kernel, not surrounding overhead, is on the critical path. (05:30-05:55)
- Naive timing can measure kernel launch time instead of execution time; evaluation should account for warmups, cache clearing, and ordering effects between baseline and generated implementations. (05:56-06:34)
- The talk warns that huge speedups should trigger suspicion: one generated solution returned the input unchanged because all benchmark cases already satisfied the clamping condition, which passed the test but was outside the intended benchmark behavior. (11:48-12:48)
- Human judgment still matters because an agent can make a transformation that is valid under one definition of the task but invalid for the intended evaluation target. (12:48-13:02)
- The verification agent in a kernel-generation harness should be strict about preventing benchmark manipulation and should run generated ideas on real hardware. (14:49-15:05)
- **Report correctness and speed as two curves, because they scale differently.** ParallelKernelBench pairs `pass@k` ("the number of correct kernels generated after k attempts") with `fast_1@k` ("solutions that are both correct and outperform the speed of the PyTorch plus NCCL baseline"), and the two diverge under test-time scaling: more samples lift correctness from 28 to 36 of 87 while the correct-and-faster share "plateaus out at roughly 31%." A second axis is worth copying — sweeping the required speedup threshold on the x-axis, which showed that even the best model "drops off very quickly as the speed up threshold increases." A single 1x-threshold number hides how thin the margin usually is. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 24:00-25:11, 25:50-26:24)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Make Local Inference Benchmarks Reproducible Artifacts](make-local-inference-benchmarks-reproducible-artifacts.md)
- [Evaluate Agent Trajectories With Backtests And Smell Metrics](evaluate-agent-trajectories-with-backtests-and-smell-metrics.md)
- [Make Validation Fast, Local, Deterministic, And Actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [More Samples Buy Correctness, Not Speedups](more-samples-buy-correctness-not-speedups.md)
- [Swap the Verifier to Retarget an Agent Arena](swap-the-verifier-to-retarget-an-agent-arena.md)

Sources:
- [AI Kernel Generation: What's working, what's not, what's next - Natalie Serrino, Gimlet Labs](../sources/20251217_6guQG_tGt0o.md), 05:30-06:34, 11:48-13:02, 14:49-15:05
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 24:00-25:11, 25:50-26:24
