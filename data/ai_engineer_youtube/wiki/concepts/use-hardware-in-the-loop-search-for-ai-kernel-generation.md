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

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Make Local Inference Benchmarks Reproducible Artifacts](make-local-inference-benchmarks-reproducible-artifacts.md)
- [Profile Small-Model Architectures On Target Hardware](profile-small-model-architectures-on-target-hardware.md)
- [Production Inference Combines Model Support With Cluster Operations](production-inference-combines-model-support-with-cluster-operations.md)

Sources:
- [AI Kernel Generation: What's working, what's not, what's next - Natalie Serrino, Gimlet Labs](../sources/20251217_6guQG_tGt0o.md), 00:34-01:17, 02:39-04:45, 13:43-15:05, 16:22-16:39
