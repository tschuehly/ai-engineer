# Use AI Kernel Generation For Known Optimization Patterns, Not Expert-Level Breakthroughs

Summary: Current AI kernel generation is strongest at rapidly exploring known optimization patterns and hardware ports, not at inventing the next expert-level primitive or beating heavily hand-optimized kernels.

Use when:
- Deciding where AI-generated low-level optimization is worth applying.
- Separating useful automated search from unrealistic claims about replacing kernel experts.

Details:
- The talk reports useful cases such as fusing multiple operations into one kernel, rewriting average pool 1D as a faster Metal convolution, and specializing six fused kernels for an audio encoder on RTX 6000 Blackwell. (08:03-10:40, 16:02-16:39)
- Kernel fusion is not new, and `torch.compile` already does it well, but agents can still customize fused implementations to a specific workload. (08:12-08:53)
- AI kernel generation is a poor fit for outperforming deeply hand-optimized primitives such as matrix multiplication, where expert libraries already embody extensive optimization work. (11:15-11:44)
- The best current applications are searching across known tricks such as fusion and tiling, porting existing implementations to new hardware, and adapting optimizations to changes such as model quantization. (16:43-17:35)
- The strategic value is freeing scarce kernel experts to focus on the most interesting optimization problems while agents improve the long tail of workloads experts do not have time to hand-tune. (17:38-18:06)
- **The same conclusion, measured, on multi-GPU kernels.** ParallelKernelBench gives this page's claim a number and a mechanism. The best frontier model solves 28 of 87 problems zero-shot with 22 faster than a PyTorch+NCCL baseline, and "the success patterns here are really concentrated into familiar patterns — collective primitives, tensor parallel GEMMs and Ulysses style context parallelism… patterns that we see heavily represented on the internet rather than necessarily patterns that the model has used its reasoning abilities to think through." The speedups also come from a single known substitution: "eliminating NCCL staging overhead in favor of direct NVLink loads and stores." ([Arora](../sources/20260827_pOvWgX7IJsc.md), 24:32-25:47)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use Hardware-In-The-Loop Search For AI Kernel Generation](use-hardware-in-the-loop-search-for-ai-kernel-generation.md)
- [Treat Quantization As A Memory-Bandwidth Lever](treat-quantization-as-a-memory-bandwidth-lever.md)
- [Compare Models By Task, Thinking Budget, Cost, And Latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Models Solve the Parallelism Patterns the Internet Already Contains](models-solve-the-parallelism-patterns-the-internet-already-contains.md)

Sources:
- [AI Kernel Generation: What's working, what's not, what's next - Natalie Serrino, Gimlet Labs](../sources/20251217_6guQG_tGt0o.md), 08:03-11:44, 16:02-18:06
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 24:32-25:47
