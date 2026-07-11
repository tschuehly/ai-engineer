# Evaluate Coding Agents on Project-Scale, Billion-Token Tasks

Summary: The next rung of coding-agent evaluation is whole-project ownership at long horizons — building an entire product, library, or compiler from scratch over multi-hour, tens-to-hundreds-of-millions-of-tokens rollouts — rather than fixing an isolated bug or GitHub issue. At this scale the best agents still resolve only a quarter of tasks, and the agent scaffold matters as much as the model.

Use when:
- Deciding what to measure once bug-fix benchmarks (SWE-bench-style) start to saturate and you want a signal for autonomous, long-running project work.
- Turning "Frontier Labs case studies" (a team of agents building a C compiler, rebuilding a framework hands-off) into reproducible eval tasks.
- Reading a headline agent resolution rate and needing to know whether the model or the harness/scaffold drove it.

Details:
- SWE-Marathon (Abundant AI) asks whether coding agents "can stay coherent over a billion token budget," building whole projects end-to-end — build Slack from scratch, rewrite an entire JAX codebase in PyTorch, build a C compiler in Rust — the shift "from fixing bugs to owning entire projects." (00:11-00:40)
- It extends the SWE benchmark lineage: HumanEval (write individual Python functions) → SWE-bench (real GitHub issues: inspect a repo, make a patch, patch unit tests) → Terminal-bench (each task is a full environment with a verifier, terminal, bash, files, and a final container state) → SWE-Marathon, which "stretches the horizon to project scale work" — multi-hour trajectories and coordinated changes across many components, "hundreds of hours of human work compressed into a single agent rollout." (01:32-02:28)
- 20 project-scale tasks across four families — library clones, full-stack product clones, ML engineering, algorithmic — some using external APIs (a post-train task that must post-train a language model via the *tinker* API). Expert contributors propose tasks and reference solutions, standardized into executable environments with multi-layer verifier suites in the harbor format. (05:09-06:07)
- The best configuration (Claude Opus 4.8 + Claude Code) resolves only 26% — "one in four tasks" with the strongest setup evaluated — so "end-to-end project ownership is still very far from being solved." These are not shallow failures: the average trial used 31 million tokens and the longest rollout consumed 877 million tokens. (06:15-07:03)
- The scaffold matters as much as the model: on a cost-vs-resolution plot, Opus 4.8 tops out at 26% but is one of the most expensive, while a cheaper Codex-based config gets 12% — "the model isn't just the full picture. The agent scaffold makes a huge difference" (how it plans, uses tools, summarizes context, decides when to test). (07:10-07:54)
- A single rollout is a long engineering loop, not a coding task: one run (GLM 5.2 on a Next.js→Vite rewrite) spanned 356 million tokens, 9 hours, and 800+ trajectory steps, starting from a full test suite at 0/325 passing and pushing for hours through routing, hydration, server actions, middleware, and cache behavior — "lots of reading and searching early, then huge waves of editing, building, testing, and debugging." (08:00-09:03)
- All tasks, code, paper, logs, and 320 GB of trajectories are public (swe-bench.org), released so the benchmark is "fully inspectable and transparent"; it is a community-driven effort across task contributors and advisors. (12:20-12:54)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [At Long Horizons a Weak Verifier Becomes an Attack Surface](at-long-horizons-a-weak-verifier-becomes-an-attack-surface.md)
- [Benchmark saturation pushes capability evals toward human time horizons](benchmark-saturation-pushes-capability-evals-toward-human-time-horizons.md)
- [Push Agent Benchmarks on Environment Complexity, Autonomy Horizon, and Output Complexity](push-agent-benchmarks-on-environment-autonomy-and-output-complexity.md)
- [Use intermediate progress signals for long-horizon code evals](use-intermediate-progress-signals-for-long-horizon-code-evals.md)
- [Coding-Agent Capability Tiers Change the Bottleneck](coding-agent-capability-tiers-change-the-bottleneck.md)

Sources:
- [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](../sources/20260707_Rx8f05JI_WA.md), 00:11-02:28, 05:09-09:03, 12:20-12:54
