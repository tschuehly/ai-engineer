# Add Multi-GPU Primitives to a Single-GPU Kernel Instead of Orchestrating Bulk Collectives

Summary: The three standard routes to multi-GPU performance each fail in a different way — collective libraries are tuned for bulk contiguous transfers, distributed DSLs cannot track networking hardware changes, and hand-tuned operators do not scale across precisions. The alternative that worked in production was a small primitive set inserted directly into an existing single-GPU kernel, at a cost of roughly a dozen lines.

Use when:
- Deciding whether to reach for NCCL, a distributed DSL, a hand-written operator, or in-kernel communication primitives.
- A fused collective (GEMM plus all-reduce, GEMM plus reduce-scatter) is on the critical path and the library version stages through buffers.
- Evaluating whether a distributed-kernel abstraction will survive the next hardware generation.

Details:
- **Where collective libraries stop.** NCCL, and RCCL on AMD, get heavy vendor investment but "they're not very flexible. So they're tuned for bulk transfers for large contiguous chunks of data transfers. And the design really breaks down when you care about peak performance, fine grain communication, and sort of non-trivial collectives that you want to fuse together." ([Arora](../sources/20260827_pOvWgX7IJsc.md), 11:33-11:53)
- **The framework layer inherits the constraint rather than fixing it.** Megatron-LM, FlexFlow, and NanoFlow are "primarily orchestrating bulk collectives via NCCL and require synchronization before and after data transfers" — the synchronization boundary is what forecloses overlap, and it is structural to the layering. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 12:33-12:52)
- **Distributed DSLs have a portability half-life.** "It's very difficult to support the rapid pace of networking improvements within these frameworks," and the concrete instance is Triton-distributed, "originally tuned around 8 H800 GPUs," failing "to adapt efficiently to other architectures like H100s." A compiler for a moving hardware target inherits the target's churn. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 12:56-13:27)
- **Hand-tuning reaches peak and does not scale.** Per-operator kernels (the talk lists a set that includes Ring Attention and distributed GEMM kernels from CUTLASS) "achieve peak performance but… some of these methods have been designed in one precision and it takes five or six months to scale it to another precision." Precision migration is a routine event; a five-to-six-month port per operator is not a maintainable practice. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 13:27-14:07)
- **The alternative, and its cost.** ParallelKittens is "a simple set of programming primitives and templates for these multi-GPU kernels" where "we usually add roughly a dozen lines of code over a single GPU kernel to insert these multi-GPU primitives." It is in production at Together AI and at Cursor, with state-of-the-art results claimed across data, sequence, and expert parallelism against strong reference baselines. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 14:50-15:12, 20:41-21:26)
- **The abstraction's fourth requirement, easy to miss.** Beyond transfer mechanism and overlap schedule, "abstraction should allow the developer flexibility to control how they're buffering and synchronizing between data senders and receivers." That control is precisely what the library and framework routes take away. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 20:29-20:41)
- **Independent corroboration of where the win comes from.** When models generate kernels for these problems, "once correctness is established, speedups naturally come from eliminating NCCL staging overhead in favor of direct NVLink loads and stores" — the same mechanism, arrived at by a different method. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 25:12-25:22)
- **What is not shown.** No absolute performance numbers for ParallelKittens appear in the talk; the comparison chart is referenced rather than read out, and the "dozen lines" figure is the only quantified claim about the abstraction itself. Cross-vendor portability is also unproven here — the group's own point that networking stacks differ sharply across vendors applies to their abstraction too. ([Arora](../sources/20260827_pOvWgX7IJsc.md), Provenance and Limits)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Measure Multi-GPU Headroom Against a Communication-Aware Roofline](measure-multi-gpu-headroom-against-a-communication-aware-roofline.md)
- [Choose the Inter-GPU Transfer Mechanism by Message Size and Resource Cost](choose-the-inter-gpu-transfer-mechanism-by-message-size-and-resource-cost.md)
- [Overlap Communication With Compute Intra-SM or Inter-SM by Data Alignment](overlap-communication-with-compute-intra-sm-or-inter-sm.md)
- [Use LLMs to generate compiler lowerings under verification](use-llms-to-generate-compiler-lowerings-under-verification.md)
- [Use AI Kernel Generation For Known Optimization Patterns, Not Expert-Level Breakthroughs](use-ai-kernel-generation-for-known-optimization-patterns-not-expert-level-breakthroughs.md)

Sources:
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 11:33-11:53, 12:33-14:07, 14:50-15:12, 20:29-21:26, 25:12-25:22
