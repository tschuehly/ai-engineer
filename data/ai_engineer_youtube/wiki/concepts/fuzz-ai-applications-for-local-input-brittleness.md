# Fuzz AI applications for local input brittleness

Summary: GenAI applications can pass a static golden set while failing on nearby natural-language variants. Fuzzing adds coverage by generating many semantically or syntactically varied stimuli and looking for cases where small input changes produce unacceptable output changes.

Use when:
- A prototype looks good on curated examples but needs production-readiness testing.
- Static evals do not cover user wording variance, edge cases, policy boundaries, or prompt-injection-adjacent behavior.

Details:
- The source distinguishes ordinary nondeterminism from brittleness: even mostly deterministic workflows can produce sharply different outputs from ostensibly similar inputs. 02:47-03:56
- Static golden data sets measure performance only on the listed examples; nearby perturbations can tell a different story about behavior in the wild. 04:29-05:08
- AI-specific fuzzing simulates large-scale stimuli, scores responses, and uses the results to guide further search for corner cases before deployment. 06:10-06:49
- Regulated and customer-facing applications benefit from this because unexpected policy and code-of-conduct gaps can block production release even when happy-path demos work. 16:23-17:06

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Build AI app benchmarks before optimization](build-ai-app-benchmarks-before-optimization.md)
- [Continuously reconcile eval datasets with user reality](continuously-reconcile-eval-datasets-with-user-reality.md)
- [Search natural-language input space as an optimization problem](search-natural-language-input-space-as-an-optimization-problem.md)

Sources:
- [Fuzzing in the GenAI Era — Leonard Tang, Haize Labs](../sources/20250822_OMGPvW8TBHc.md), 02:47-06:49, 16:23-17:06
