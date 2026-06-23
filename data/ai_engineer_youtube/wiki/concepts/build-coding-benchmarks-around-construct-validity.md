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

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Evaluate generated kernels for correctness, performance, and benchmark gaming](evaluate-generated-kernels-for-correctness-performance-and-benchmark-gaming.md)
- [Benchmark narrow slices separately from real expert work](benchmark-narrow-slices-separately-from-real-expert-work.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)

Sources:
- [Coding Evals: From Code Snippets to Codebases - Naman Jain, Cursor](../sources/20251215_tHN44yJoeS8.md), 07:07-10:18
