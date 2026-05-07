# Update coding eval sets dynamically as model capability changes

Summary: Static coding benchmarks lose signal when models have seen similar problems, tests are too weak, or task difficulty no longer matches current capability. Dynamic eval sets can use release time, fresh tasks, and changing difficulty distributions to preserve useful comparisons.

Use when:
- Designing a coding benchmark that should remain useful across model generations.
- Investigating whether a high code-benchmark score reflects contamination or benchmark saturation.

Details:
- Programming problems are often available on Stack Overflow, GitHub, and similar public sources, so internet-trained models can appear strong because of contamination rather than fresh problem solving. (02:23-02:45)
- Weak test suites can accept semantically wrong solutions, such as returning a set without preserving a required sorted output. (02:46-03:12)
- Benchmarks with scores clustered near 80-90% or near 1% provide little hill-climbing signal; useful evals need task difficulty near the model frontier. (03:15-03:55)
- LiveCodeBench-style updates can evaluate models on problems released after a model's training window and adjust difficulty distributions as models improve. (03:55-04:35)
- Time-based slices can reveal contamination: performance may drop sharply after a model release date when evaluated on newer problem months. (04:53-05:28)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Benchmark saturation pushes capability evals toward human time horizons](benchmark-saturation-pushes-capability-evals-toward-human-time-horizons.md)
- [Evaluate agent trajectories with backtests and smell metrics](evaluate-agent-trajectories-with-backtests-and-smell-metrics.md)

Sources:
- [Coding Evals: From Code Snippets to Codebases - Naman Jain, Cursor](../sources/20251215_tHN44yJoeS8.md), 02:23-06:47
