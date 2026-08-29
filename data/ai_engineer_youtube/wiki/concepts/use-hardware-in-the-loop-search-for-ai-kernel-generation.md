# Use Hardware-In-The-Loop Search For AI Kernel Generation

Summary: AI kernel generation works best as a search loop that proposes optimization variants, runs them on the target hardware, and feeds correctness and profiling results back into the next attempt.

Use when:
- Porting PyTorch workloads or existing kernels to a new accelerator, vendor framework, or device generation.
- Building agents that optimize low-level inference code where static inspection cannot reliably predict performance.

Details:
- The talk frames agentic inference as heterogeneous pipelines of models, stages, and tool calls, which makes hardware-specific kernel porting part of inference infrastructure. (00:34-01:17)
- The human workflow is iterative: try an implementation, check compilation, execution, and correctness, then use profiling data to attack the next bottleneck. The agentic workflow should preserve that same loop. (03:39-04:45)
- Gimlet's described architecture uses a supervisor agent that takes input code, target hardware, and human prompting, then dispatches a synthesis swarm to propose optimization ideas and a verification agent to run them on actual hardware. (14:17-15:05)
- Hardware-in-the-loop profiling is necessary because low-level code behavior depends on hardware features such as cache size and device-specific execution properties. (02:39-03:34, 13:43-13:56)
- Generated kernels can be packaged as API-compatible PyTorch replacements, including inline low-level code loaded and called from the original model path. (16:22-16:39)
- **The loop's ceiling, measured on a harder task class.** A bare multi-turn harness — mini-SWE-agent, Gemini 3 Pro, and a local bash environment "to sort of mimic the standard Claude Code setup" — moved that model from 24 to 35 of 87 multi-GPU kernel problems, with 26 beating the reference. Then it stopped: "as we scaled the amount of time the performance plateaued, and additional techniques would be required to continue seeing the scaling there." The compile-run-fix loop reliably converts failures into correct kernels, because compile and correctness errors produce a signal it can act on; performance decisions produce no error, so more iterations re-sample the same choices. Budget hardware-in-the-loop search for correctness recovery, and expect a separate mechanism to be needed for quality. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 26:28-27:56)

- **One candidate for the "additional technique" the plateau demands, from the same company.** Together AI pointed a multi-agent arena at kernel optimization — a live leaderboard scored by a compile-benchmark-test backend, a discussion forum, and downloadable rival submissions — and reports "sometimes over two-fold speed ups in some of these production kernels," including for page attention, "already used in production at Together AI." The structural difference from a single hardware-in-the-loop loop is what makes it a plausible answer to the plateau: a self-correcting loop sees no error when a kernel is correct but slow, whereas a leaderboard makes speed a visible, ranked, refinable signal and a rival's faster submission is the counterfactual the solo loop never gets. Zou adds persona differentiation on top — separate agents biased toward profiling, memory consumption, and precision/tensor computations. The two talks do not cite each other and the arena result carries no evaluation methodology, so read this as a coherence between two results from one organization, not as a demonstrated fix. See [Swap the Verifier to Retarget an Agent Arena](swap-the-verifier-to-retarget-an-agent-arena.md) and [Give Parallel Agents Complementary Optimization Personas](give-parallel-agents-complementary-optimization-personas.md). ([Einstein Arena — James Zou, Together AI](../sources/20260825_mMNkdYnIVC4.md), 08:57-10:54)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Make Local Inference Benchmarks Reproducible Artifacts](make-local-inference-benchmarks-reproducible-artifacts.md)
- [Profile Small-Model Architectures On Target Hardware](profile-small-model-architectures-on-target-hardware.md)
- [Production Inference Combines Model Support With Cluster Operations](production-inference-combines-model-support-with-cluster-operations.md)
- [More Samples Buy Correctness, Not Speedups](more-samples-buy-correctness-not-speedups.md)
- [Swap the Verifier to Retarget an Agent Arena](swap-the-verifier-to-retarget-an-agent-arena.md)
- [Give Parallel Agents Complementary Optimization Personas](give-parallel-agents-complementary-optimization-personas.md)

Sources:
- [AI Kernel Generation: What's working, what's not, what's next - Natalie Serrino, Gimlet Labs](../sources/20251217_6guQG_tGt0o.md), 00:34-01:17, 02:39-04:45, 13:43-15:05, 16:22-16:39
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 26:28-27:56
- [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../sources/20260825_mMNkdYnIVC4.md), 08:57-10:54
