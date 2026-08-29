# Models Solve the Parallelism Patterns the Internet Already Contains

Summary: On multi-GPU kernel generation, frontier-model successes concentrate in exactly the patterns that are heavily represented in public code — collective primitives, tensor-parallel GEMMs, Ulysses-style context parallelism — while the underlying design tradeoffs stay unapplied even when the principles are supplied in context. Retrieval of familiar shapes, not reasoning about the hardware, is doing the work.

Use when:
- Estimating whether a model will transfer to a specialist engineering task with little public code.
- Interpreting strong benchmark scores on a task whose examples are abundant online.
- Deciding whether the next intervention is more context, a better harness, or training.

Details:
- **Where the wins are.** "The success patterns here are really concentrated into familiar patterns. So collective primitives, tensor parallel GEMMs and Ulysses style context parallelism. So in other words, patterns that we see heavily represented on the internet rather than necessarily patterns that the model has used its reasoning abilities to think through." ([Arora](../sources/20260827_pOvWgX7IJsc.md), 25:24-25:47)
- **The framing question the benchmark was built to answer.** "Do they generalize well to these problems, or are we benchmaxed on benchmarks of the past which are more single GPU centric?" Models "are showing really promising results on single GPU benchmarks. So it's a ripe time to extend it." The multi-GPU setting is a natural held-out split: same language, same tooling, sparser public corpus. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 21:42-22:05)
- **The failures are not language mechanics.** "We found that there's deeper issues than CUDA syntax." Given multiple samples or an error-correction loop, models "can often compile the kernels. But the models really struggle to reason through the tradeoffs" — collective ordering, data partitioning, intra- versus inter-SM scheduling, and the choice among transfer mechanisms. Concretely, "they often do not use things like the register transfer instructions or tensor memory acceleration when writing the kernels": the less-common mechanisms are the ones that go unused. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 26:28-27:06)
- **The strongest form of the result: context did not fix it.** "Models do not currently understand how to reason through these trade-offs even when we provide them in context." The principle set had been distilled by hand into a small primitive vocabulary and handed to the model; the gap survived. This rules out the easiest explanation — that the model simply had not been told — and pushes the problem toward training or method. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 29:11-29:17)
- **Even the successes are one move.** "Once correctness is established, speedups naturally come from eliminating NCCL staging overhead in favor of direct NVLink loads and stores." The speedups that exist come from a single well-known substitution, not from a search over the design space — which is consistent with the retrieval reading and explains why the speedup-threshold curve drops off so fast. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 25:12-25:22, 25:50-26:24)
- **The practical test this suggests before adopting a model for specialist work.** Split candidate tasks by how much public code exists for them, and score both halves. A model that scores well only on the well-represented half will look competent in a demo and fail on the long tail of your actual workload — which is usually where the unwritten optimizations are, and therefore where the value is.
- **The corollary that is good news.** The same distributional effect means the benchmark's *unsolved* problems are a map of where public code is thin, and those are precisely the kernels nobody has hand-written — the reason the effort produced net-new kernels for NeMo vocab-parallel filtering, Hyena context parallelism, and SAM 3 IoU suppression. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 28:00-28:51)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [More Samples Buy Correctness, Not Speedups](more-samples-buy-correctness-not-speedups.md)
- [Match Agent Tooling to the Model's Training Distribution](match-agent-tooling-to-the-models-training-distribution.md)
- [Use AI Kernel Generation For Known Optimization Patterns, Not Expert-Level Breakthroughs](use-ai-kernel-generation-for-known-optimization-patterns-not-expert-level-breakthroughs.md)
- [Choose the Inter-GPU Transfer Mechanism by Message Size and Resource Cost](choose-the-inter-gpu-transfer-mechanism-by-message-size-and-resource-cost.md)
- [Derive the Principles by Hand Before Testing Whether Models Can Apply Them](derive-the-principles-by-hand-before-testing-whether-models-can-apply-them.md)

Sources:
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 21:42-22:05, 25:12-27:06, 28:00-28:51, 29:11-29:17
