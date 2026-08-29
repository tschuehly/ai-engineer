# Measure Multi-GPU Headroom Against a Communication-Aware Roofline

Summary: Hardware generations have widened the gap between arithmetic throughput and interconnect bandwidth far enough that communication now consumes the majority of runtime on many production distributed workloads. Before optimizing anything, compute a communication-aware roofline for the problem and measure the default stack against it — on a benchmark of 87 real multi-GPU problems, PyTorch plus NCCL sat below 50% of that bound on the majority of them.

Use when:
- A distributed training or inference workload shows low model FLOP utilization and you need to decide whether the fix is compute-side or link-side.
- Justifying investment in custom communication kernels over the default collective library.
- Setting a target for a multi-GPU optimization effort, so "we got 15% faster" can be judged against how much was available.

Details:
- **The generational numbers that moved the bottleneck.** From NVIDIA's A100 in 2020 to the B200 in 2024, "BF16 tensor core speeds improved by 7.2x, while intra node communication by just 3x and inter node communication by just 2x." Compute outran links by roughly 2.4x within a scale-up domain and 3.6x across nodes in four years, and the divergence is cumulative across generations rather than a one-off. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 10:30-10:46)
- **What it does at the top of the stack.** "On many production distributed training and inference workloads, communication is increasingly consuming the majority of the runtime and yields low model FLOP utilization at scale." This is the same quantity teams report as MFU; the page's claim is that a low MFU number at scale is usually a communication result, not a kernel result. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 06:45-07:04)
- **The measured headroom.** Across the 87 problems in ParallelKernelBench, a naive baseline "representative of very popular libraries in machine learning stacking PyTorch with NCCL" falls "below 50% of their communication aware roofline bound" on the majority of problems. That is the number that converts the trend into a decision: more than half the analytically available performance is unclaimed on the default stack. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 12:03-12:32)
- **A useful asymmetry for portability planning.** "Things like tensor cores that run matmuls and our memory hierarchies are pretty consistent and resemble one another across diverse AI vendors and multi-silicon. But the networking stack is something that is really different across vendors still" — AMD xGMI point-to-point links, the TPU's 3D torus with optical wraparound links, and NVIDIA's NVLink/NVSwitch are genuinely different topologies. Compute-side optimizations port; communication-side optimizations may not. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 07:08-07:45, 10:49-11:07)
- **The trend is not flattening.** Scale-up domains are growing — 72 GPUs in "the coming chips," and "Nvidia planning on a single system in 2027 with 576 GPUs" — which enlarges the region where these kernels apply rather than shrinking it. The forward bet named at the end of the talk is "architectures that can grow with the trends of how networking stacks are evolving… larger scale up domains, shift away from scale out, and massive on-chip memory structures." (These figures are forward-looking and unattributed.) ([Arora](../sources/20260827_pOvWgX7IJsc.md), 09:02-09:15, 29:19-29:35)
- **What the roofline number does and does not license.** The bound is computed by the group that also built the benchmark and the competing abstraction, and the talk does not define how the communication-aware roofline is calculated per problem. Treat the 50% figure as a claim about the size of the opportunity on their problem set, and re-derive the bound for your own workload before using it as an acceptance criterion. ([Arora](../sources/20260827_pOvWgX7IJsc.md), Provenance and Limits)
- **The measurement gap this implies at the observability layer.** A communication-aware roofline needs fabric counters to be checked against reality, and those are exactly the metrics no vendor exporter ships by default — see the InfiniBand and NVLink argument on the utilization page below.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Add Multi-GPU Primitives to a Single-GPU Kernel Instead of Orchestrating Bulk Collectives](add-multi-gpu-primitives-to-a-single-gpu-kernel.md)
- [GPU Utilization Is a Lie: Instrument Tensor Cores and the Fabric](measure-tensor-core-utilization-not-gpu-utilization.md)
- [Fast Inference Moves the Agent Bottleneck to the Network](fast-inference-moves-the-agent-bottleneck-to-the-network.md)
- [Choose the Inter-GPU Transfer Mechanism by Message Size and Resource Cost](choose-the-inter-gpu-transfer-mechanism-by-message-size-and-resource-cost.md)
- [Treat Quantization as a Memory-Bandwidth Lever](treat-quantization-as-a-memory-bandwidth-lever.md)

Sources:
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 06:45-07:04, 07:08-07:45, 09:02-09:15, 10:30-11:07, 12:03-12:32, 29:19-29:35
