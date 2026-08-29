# Choose the Inter-GPU Transfer Mechanism by Message Size and Resource Cost

Summary: There are three ways to move data between GPUs, and they are not interchangeable: the host-initiated copy engine, device-initiated TMA transfers, and register-level `multimem` PTX instructions. They differ in the message size at which they reach peak bandwidth, in how many registers and SMs they consume, and in whether they can reach the switch's in-network reduction hardware.

Use when:
- Writing or reviewing a multi-GPU kernel and deciding how a tile actually crosses NVLink.
- Diagnosing why a fine-grained communication pattern fails to saturate the link.
- Explaining to a code-generating model or a new engineer why "just use the copy engine" is not a default.

Details:
- **Copy engine — host-initiated, bulk, resource-free.** The per-GPU copy engine "is host or CPU initiated work. It's really good for large message transfers… when the amount of data being transferred is really big" and can reach peak bandwidth on the communication side. Its distinguishing virtue is what it does not spend: it "doesn't take away or waste a lot of our precious registers" and "doesn't use any of those rainbow colored dots" — the SMs — "allowing us to repurpose those for memory or computation on our other parts of the AI pipeline." ([Arora](../sources/20260827_pOvWgX7IJsc.md), 15:56-16:22, 17:02-17:30)
- **TMA — device-initiated, fine-grained, cheap in registers and SMs.** Tensor memory acceleration performs "asynchronous network transfers from the device side" and can "saturate our NVLink bandwidth using relatively small message sizes," which is what makes it "really nice when we're trying to do fine grain communication rather than sending bulk amounts of data over the links all at once coarsely." It "consumes very few registers" and "can achieve high utilization using very few of our processors. So it's a nice useful tool for fine grain overlapping." ([Arora](../sources/20260827_pOvWgX7IJsc.md), 09:17-09:39, 16:22-16:59, 17:30-17:44)
- **The limitation that decides the third case.** "TMA does have limitations. It can't effectively take advantage of these in-network computations that… are feasible with technologies like NVSwitch." Register-level PTX instructions — `ld`/`st`/`red` with `multimem` — "are really nice for being able to take advantage of those in-network reductions that NVSwitch offers." If the collective is a reduction and the fabric can do reductions, the transfer mechanism is what determines whether you get to use that hardware. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 16:32-16:39, 17:44-18:08)
- **Why the switch matters at all.** NVSwitch "connects all NVLink endpoints into a non-blocking fabric for full GPU-GPU communication," and is notable because "it also provides support for in-network off-device acceleration for communication primitives like multicast and reductions." The in-network reduction is compute that happens in the fabric rather than on any GPU; reaching it is a kernel-level decision, not a topology-level one. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 05:12-05:36)
- **Read the choice as a three-column ledger,** not a ranking: message size at peak (large / small / small), register cost (none / very few / high), SM cost (none / very few / high), in-network reductions (no / no / yes). No column dominates, which is why the decision has to be made per kernel.
- **This is one of the four decisions frontier models measurably do not make.** Models generating multi-GPU kernels "often do not use things like the register transfer instructions or tensor memory acceleration when writing the kernels," defaulting instead to the coarse path — which is also why their generated kernels compile and then run slowly. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 26:56-27:06)
- **Scope.** Everything concrete here is NVIDIA-specific (NVLink, NVSwitch, TMA, PTX `multimem`). The equivalent ledger on AMD xGMI or a TPU 3D torus is not given, and the talk's own observation that networking stacks "really differ across vendors" is a warning against assuming the same three-way choice exists elsewhere. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 11:04-11:07)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Overlap Communication With Compute Intra-SM or Inter-SM by Data Alignment](overlap-communication-with-compute-intra-sm-or-inter-sm.md)
- [Add Multi-GPU Primitives to a Single-GPU Kernel Instead of Orchestrating Bulk Collectives](add-multi-gpu-primitives-to-a-single-gpu-kernel.md)
- [Measure Multi-GPU Headroom Against a Communication-Aware Roofline](measure-multi-gpu-headroom-against-a-communication-aware-roofline.md)
- [Models Solve the Parallelism Patterns the Internet Already Contains](models-solve-the-parallelism-patterns-the-internet-already-contains.md)

Sources:
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 05:12-05:36, 09:17-09:39, 15:56-18:08, 26:56-27:06
