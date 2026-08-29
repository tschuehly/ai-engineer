# Build coding benchmarks around construct validity

Summary: A coding benchmark should measure the real capability it claims to measure, not only produce a high or low leaderboard score. Construct-valid code evals pair natural task distributions with grading that captures correctness, equivalence, and the intended engineering outcome.

Use when:
- Turning repository-scale engineering work into benchmark tasks.
- Evaluating whether a benchmark score predicts real-world coding-agent usefulness.

Details:
- High benchmark scores can fail to translate to real-world gains when the measurement does not reflect the underlying capability being claimed. (07:41-08:04)
- Construct validity for code optimization requires tasks sourced from real code and reliable grading for the actual intended outcome. (08:07-08:17)
- The optimization benchmark described crawls real commits, selects performance-related changes, generates performance workloads, and asks agents to make the code run faster. (08:23-09:09)
- Grading includes whether the patch remains correct, whether it is equivalent to the human patch, and whether it improves runtime over the human reference. (09:19-09:36)
- High-performance code tasks mix algorithmic reasoning, repository editing, low-level implementation detail, and runtime measurement, making them a bridge between programming-problem evals and SWE-bench-style repository evals. (07:07-07:35)
- **A construct-validity test you can run after the fact: are the solutions worth having?** ParallelKernelBench's problems were drawn from GitHub repositories, optimized library implementations, and existing multi-GPU DSL kernels, with the explicit design goal that solving it "would lead to net new useful production kernels rather than artificial or useless kernels." The check is that it produced some — a NeMo vocab-parallel filtering kernel, a Hyena context-parallelism kernel, and an IoU-suppression kernel for SAM 3 — in cases "where people have not invested a bunch of time to hand write a multi-GPU kernel." A benchmark whose outputs nobody would deploy is measuring something other than the capability it names. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 23:15-23:49, 28:00-28:51)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Evaluate generated kernels for correctness, performance, and benchmark gaming](evaluate-generated-kernels-for-correctness-performance-and-benchmark-gaming.md)
- [Benchmark narrow slices separately from real expert work](benchmark-narrow-slices-separately-from-real-expert-work.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Specify a Generation Task as a Reference Implementation Plus a Topology Spec](specify-a-generation-task-as-a-reference-implementation-plus-a-topology-spec.md)

Sources:
- [Coding Evals: From Code Snippets to Codebases - Naman Jain, Cursor](../sources/20251215_tHN44yJoeS8.md), 07:07-10:18
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 23:15-23:49, 28:00-28:51
