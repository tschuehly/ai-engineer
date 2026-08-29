# Derive the Principles by Hand Before Testing Whether Models Can Apply Them

Summary: Before asking whether a model can do a hard technical job, do the job manually until you can state the small set of decisions it reduces to. That hand-derived principle set becomes three things at once: the in-context material you give the model, the rubric that explains its failures, and the proof that the task is learnable at all.

Use when:
- Scoping an "can an LLM do X" investigation in a domain where you are not already the expert.
- A model is failing at a specialist task and the error reports are unactionable ("the output was bad").
- Deciding whether to build the benchmark first or the system first.

Details:
- **The stance, stated directly.** "We think it's important to build our own fundamental understanding and to manually do the work to understand it rather than just throwing say an LLM at the problem." The group spent the time to build ParallelKittens — a minimal primitive set for multi-GPU kernels — specifically "to understand the trade-offs of multi-GPU kernels" and to write a large collection of peak-performance kernels across parallelism schemes. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 14:38-15:12)
- **The order is explicit and conditional.** "Once we found that there is indeed a small set of trade-offs governing this landscape, we were curious whether models… could reason about these trade-offs when we provide them in context to actually generate a bunch of net new multi-GPU kernels for us." The model question is only well-posed after the manual work establishes that a small governing set exists. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 15:19-15:41)
- **The payoff is diagnostic resolution.** Because the tradeoffs were enumerated by hand first — transfer mechanism, overlap schedule, collective ordering, data partitioning — the failure report is specific rather than a score: models "really struggle to reason through the tradeoffs that we talked about in the prior section," and "often do not use things like the register transfer instructions or tensor memory acceleration." A benchmark built without the manual phase would have produced the same pass rate and none of that. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 26:41-27:06)
- **It also lets you rule out the easy explanation.** The manual understanding is what supports the claim that "there's deeper issues than CUDA syntax" — the group knew what a good answer looks like, so they could see that the compiling-but-slow kernels were failing on decisions rather than on language mechanics. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 26:28-26:44)
- **The strongest form of the negative result depends on it.** "Models do not currently understand how to reason through these trade-offs *even when we provide them in context*" is a much sharper claim than "models score 32% on our benchmark," and it is only available because there was a hand-derived principle set to put in the context window. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 29:11-29:17)
- **Cost and applicability.** This is expensive: it means building a production system (here, one deployed at Together AI and Cursor) before you have any evidence about the model question. It is worth it when the domain has a plausibly small governing decision set and when the manual artifact has standalone value — both true here. It is a poor fit when the space is genuinely open-ended, where the manual phase would produce a rubric that is itself a guess.
- **The companion practice.** Note that this is the opposite ordering from the common "let the agent try and see where it breaks" approach the wiki records elsewhere; both are legitimate, and the discriminator is whether you can recognize a good answer when you see one. Where you cannot, watching an agent fail teaches you little.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Specify a Generation Task as a Reference Implementation Plus a Topology Spec](specify-a-generation-task-as-a-reference-implementation-plus-a-topology-spec.md)
- [Models Solve the Parallelism Patterns the Internet Already Contains](models-solve-the-parallelism-patterns-the-internet-already-contains.md)
- [Overlap Communication With Compute Intra-SM or Inter-SM by Data Alignment](overlap-communication-with-compute-intra-sm-or-inter-sm.md)
- [Evaluate Generated Kernels For Correctness, Performance, And Benchmark Gaming](evaluate-generated-kernels-for-correctness-performance-and-benchmark-gaming.md)

Sources:
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 14:38-15:41, 26:28-27:06, 29:11-29:17
