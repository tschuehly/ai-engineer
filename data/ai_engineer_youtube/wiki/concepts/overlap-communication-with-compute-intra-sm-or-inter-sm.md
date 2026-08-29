# Overlap Communication With Compute Intra-SM or Inter-SM by Data Alignment

Summary: Overlapping communication with compute inside a multi-GPU kernel has exactly two schedules. Specialize warps within one SM when the communication and the computation consume the same data; specialize whole SMs when they do not, when they would contend for registers or shared memory, or when a single SM cannot saturate the link.

Use when:
- Fusing a collective into a compute kernel and deciding how to hide the transfer.
- A fused GEMM-plus-collective kernel overlaps in principle but does not reach link bandwidth in practice.
- Reviewing generated or hand-written distributed kernels for whether the schedule matches the data dependency.

Details:
- **Intra-SM: warp specialization inside one processor.** "We'll have different warps or threads within that processor specialized to handle either compute or one specialized for communication concurrently. We can dedicate different warps to each of these." ([Arora](../sources/20260827_pOvWgX7IJsc.md), 18:28-18:52)
- **The condition that makes intra-SM work — and it is a data condition, not a performance one.** "The challenge with this intra-SM overlapping is that the communication and computation pattern really need to align and jive with one another. They need to use the same data as inputs for the computation and communication." If the warps are operating on different tiles, the co-location buys nothing and costs contention. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 18:52-19:07)
- **Inter-SM: specialize whole processors.** "Each of the different rainbow colored dots on our GPUs, those different processors, specialized to compute, communication and memory." Two reasons to prefer it: when the kernel "would otherwise need to split across resources like the register file or shared memory in misaligned ways" across the different steps, and when "it's hard to maximize NVLink traversal with intra-SM overlapping." The second reason is a bandwidth argument — one SM's issue rate may not be enough to keep the link busy. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 19:09-19:47)
- **The worked pair, which is the fastest way to internalize the rule.** On GEMM plus reduce-scatter, "the intra-SM overlapping schedule is very effective." On GEMM plus all-reduce, "the inter-SM, which again leverages the in-network reductions of NVSwitch, is very effective." The all-reduce case couples to the transfer-mechanism decision: reaching NVSwitch reductions requires register-level `multimem` instructions, which are expensive enough in registers to want their own SMs. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 19:50-20:22)
- **The two decisions are not independent.** Transfer mechanism and overlap schedule interact through the register file and the SM budget: TMA's low register and SM cost is what makes it "a nice useful tool for fine grain overlapping" at the intra-SM level, while the in-network-reduction path pushes toward inter-SM. Choosing one constrains the other. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 17:30-18:08)
- **This is a named model failure mode.** "Thinking about intra versus inter-SM scheduling" is listed among the tradeoffs frontier models cannot reason through even when the principles are supplied in context — a kernel that compiles and is correct can still have the wrong schedule, and nothing in the compile-run-fix loop surfaces that. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 26:44-26:56)
- **Limits.** The GEMM-plus-reduce-scatter / GEMM-plus-all-reduce comparison is shown as a chart and characterized qualitatively ("very effective"); no speedup ratio, problem size, or GPU count is stated for either. Treat the pair as a worked illustration of the rule rather than as calibrated evidence. ([Arora](../sources/20260827_pOvWgX7IJsc.md), Provenance and Limits)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Choose the Inter-GPU Transfer Mechanism by Message Size and Resource Cost](choose-the-inter-gpu-transfer-mechanism-by-message-size-and-resource-cost.md)
- [Add Multi-GPU Primitives to a Single-GPU Kernel Instead of Orchestrating Bulk Collectives](add-multi-gpu-primitives-to-a-single-gpu-kernel.md)
- [GPU Utilization Is a Lie: Instrument Tensor Cores and the Fabric](measure-tensor-core-utilization-not-gpu-utilization.md)
- [Derive the Principles by Hand Before Testing Whether Models Can Apply Them](derive-the-principles-by-hand-before-testing-whether-models-can-apply-them.md)

Sources:
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 17:30-20:22, 26:44-26:56
