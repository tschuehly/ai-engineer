# Specify a Generation Task as a Reference Implementation Plus a Topology Spec

Summary: A code-generation benchmark task is better specified as a working-but-unoptimized reference implementation plus a machine-readable description of the hardware it must run on than as a prose problem statement. The reference pins correctness and supplies the baseline to beat; the topology spec pins the decisions the model is actually being tested on.

Use when:
- Building an eval for optimization work, where the output is judged on speed rather than on whether it exists.
- Designing tasks whose correct answer depends on the deployment environment.
- Deciding how to sample problems so a benchmark covers a combinatorial space rather than whatever was easy to collect.

Details:
- **The task format.** Each ParallelKernelBench task "presents the model with an unoptimized reference implementation written in PyTorch with torch.distributed NCCL operations, and then a system topology that specifies the number of ranks and intra-node hardware configuration. And the model needs to rewrite the reference into a performant CUDA kernel that uses unified virtual addressing." Three parts: semantics, environment, and an output contract. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 22:07-22:33)
- **The reference doubles as the baseline.** Because the reference is a runnable PyTorch+NCCL implementation, the same artifact defines correct output and defines the speed threshold — the `fast_1@k` metric counts solutions "that are both correct and outperform the speed of the PyTorch plus NCCL baseline." No separate baseline construction, and no ambiguity about what 1x means. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 24:00-24:30)
- **Why the topology spec is load-bearing rather than decoration.** The decisions the benchmark tests — transfer mechanism, overlap schedule, data partitioning — have different right answers on different rank counts and intra-node configurations. Withholding the topology would make the task underdetermined; supplying it in prose would make it unparseable. The existing failure of a distributed DSL "originally tuned around 8 H800 GPUs" to "adapt efficiently to other architectures like H100s" is the concrete evidence that topology changes the answer. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 12:56-13:27, 22:16-22:26)
- **Sample from a taxonomy, not from convenience.** "A standard transformer layer can be parallelized across data, sequence, tensor, context, layer, pipeline and expert dimensions, and each composition induces a different communication pattern." Because the space "expands combinatorially beyond single GPU cases," the group "created this taxonomy… and then picked representative problems for each part of the taxonomy" to get coverage. Taxonomy-first sampling is what lets a fixed 87-problem set claim coverage of a combinatorial space. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 22:37-23:12)
- **Draw the problems from code that already exists in production.** The 87 problems come from "GitHub repositories that we found to be very informative," optimized library implementations, and existing multi-GPU DSL kernels, with the stated intent that "solving PKB would lead to net new useful production kernels rather than artificial or useless kernels." The patterns "arise in real AI workloads from inference to RL to post-training." ([Arora](../sources/20260827_pOvWgX7IJsc.md), 23:15-23:49)
- **The construct-validity test the design passes.** A benchmark of this shape can be checked by asking whether its solutions are worth having independently of the score, and here they were: the effort produced a NeMo vocab-parallel filtering kernel, a Hyena-architecture context-parallelism kernel, and an IoU-suppression kernel for SAM 3 video segmentation — "net new interesting ones… where people have not invested a bunch of time to hand write a multi-GPU kernel." (None of the three is benchmarked in the talk.) ([Arora](../sources/20260827_pOvWgX7IJsc.md), 28:00-28:51)
- **Headroom is a design property here, not an accident.** The best zero-shot result is 28 of 87 and the agent condition reaches 35 of 87, so the benchmark is far from saturated at introduction — which is the condition under which a score change means something. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 24:32-24:44, 27:29-27:41)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [More Samples Buy Correctness, Not Speedups](more-samples-buy-correctness-not-speedups.md)
- [Build coding benchmarks around construct validity](build-coding-benchmarks-around-construct-validity.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Evaluate Generated Kernels For Correctness, Performance, And Benchmark Gaming](evaluate-generated-kernels-for-correctness-performance-and-benchmark-gaming.md)
- [Derive the Principles by Hand Before Testing Whether Models Can Apply Them](derive-the-principles-by-hand-before-testing-whether-models-can-apply-them.md)

Sources:
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 12:56-13:27, 22:07-23:49, 24:00-24:44, 27:29-27:41, 28:00-28:51
