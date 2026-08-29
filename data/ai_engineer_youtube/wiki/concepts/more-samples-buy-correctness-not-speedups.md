# More Samples Buy Correctness, Not Speedups

Summary: On a task graded for both correctness and quality, test-time sampling improves the two at very different rates. Drawing more parallel generations raised correct multi-GPU kernels from 28 to 36 of 87, while the share that was both correct and faster than baseline stalled near 31% — so a pass@k curve reported alone would have shown healthy scaling that the quality metric does not have.

Use when:
- Deciding whether to spend more test-time compute on a generation task, or to change method.
- Choosing which metrics to report for a code-generation or optimization eval.
- Reading a paper or vendor claim that shows only pass@k on a task where correctness is the easy half.

Details:
- **The two metrics, kept separate on purpose.** ParallelKernelBench reports "pass at k, which is the number of correct kernels generated after k attempts," and "fast one at k, which counts solutions that are both correct and outperform the speed of the PyTorch plus NCCL baseline" — that is, "whether you're getting a 1x or higher speed up over the reference." ([Arora](../sources/20260827_pOvWgX7IJsc.md), 24:00-24:30)
- **The divergence.** Zero-shot, the best frontier model solves 28 of 87 with 22 faster than baseline. With more samples, "we can get that number to 36 correct solutions, but the fast one performance still plateaus out at roughly 31%. So we don't see much room from continuing to scale there as we increase the number of parallel generations." ([Arora](../sources/20260827_pOvWgX7IJsc.md), 24:32-25:11)
- **The distribution of speedups matters as much as the count.** The best model benchmarked, GPT 5.5, "drops off very quickly as the speed up threshold increases" when the x-axis sweeps the required multiple over baseline; DeepSeek V4 Pro sits below it. A single 1x-threshold number hides how thin the margin is — most passing solutions are barely faster. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 25:50-26:24)
- **Why the curves diverge.** Sampling and self-correction attack the failure mode they can observe. "If you do multiple sampling or have the model kind of look at its errors and correct them, it can often compile the kernels" — compile errors and correctness failures produce a signal the loop can act on. Performance decisions produce no error to correct, so repeated draws re-sample from the same distribution of choices. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 26:28-26:44)
- **A multi-turn agent harness moves the same needle, and then stops.** mini-SWE-agent plus Gemini 3 Pro with a local bash environment took that model from 24 to 35 of 87 solved, with 26 over 1x — but "as we scaled the amount of time the performance plateaued, and additional techniques would be required to continue seeing the scaling there." A harness is another way to spend test-time compute on the observable failure mode, and it hits the same wall. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 27:07-27:56)
- **The generalizable rule.** When a task has a cheap-to-verify component and an expensive-to-verify component, expect test-time scaling to lift the first and not the second, and report both curves. Any eval whose grader can only see correctness will report scaling that the deployed artifact does not have.
- **Comparison caveat.** The 28-problem zero-shot figure belongs to the best model tried; the 24-to-35 harness gain is measured within Gemini 3 Pro. The harness result is therefore an improvement over that model's own zero-shot score, not over the best zero-shot result, and no token or wall-clock budget is given for either condition. ([Arora](../sources/20260827_pOvWgX7IJsc.md), Provenance and Limits)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Models Solve the Parallelism Patterns the Internet Already Contains](models-solve-the-parallelism-patterns-the-internet-already-contains.md)
- [Specify a Generation Task as a Reference Implementation Plus a Topology Spec](specify-a-generation-task-as-a-reference-implementation-plus-a-topology-spec.md)
- [Scale Test-Time Search Through Parallel Verifier-Checked Branches](scale-test-time-search-through-parallel-verifier-checked-branches.md)
- [Evaluate Generated Kernels For Correctness, Performance, And Benchmark Gaming](evaluate-generated-kernels-for-correctness-performance-and-benchmark-gaming.md)
- [Raise the Floor Before Maxing the Benchmark](raise-the-floor-before-maxing-the-benchmark.md)

Sources:
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 24:00-26:44, 27:07-27:56
