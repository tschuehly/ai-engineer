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
- Standardized benchmarks visibly age out: Cline cites OpenAI stating SWE-bench Verified "no longer measures frontier coding capabilities," because its tasks (e.g. solve the Fibonacci sequence, do matrix multiplication) don't reflect real-world software engineering — so look for *very new and very precise* evals, and treat long, agentic, multi-minute tasks (Terminal Bench tasks run up to 30-40 minutes) as a legitimacy signal. ([Evals Are Broken](../sources/20260606_QuuIywMG4s8.md), 05:26-06:18, 10:55-11:07)
- Model-adoption discipline for *interpreting* others' evals: don't believe a lab's launch number (they are approximations), and stay current without being the earliest adopter — let a new model "settle for a couple weeks" and switch only if it stands the test of time. ([Evals Are Broken](../sources/20260606_QuuIywMG4s8.md), 03:38-05:23)
- A production instance of the time-split discipline: Nebius's SWE-rebench leaderboard rebuilds *every month* from fresh real-world GitHub issues of the previous month and evaluates ~30 models with the same simple harness, on the premise that benchmarks release questions *and* solutions, which become next-generation pretraining data — so "time splits are the only way" to a truly decontaminated benchmark. ([SWE-rebench](../sources/20260604_wcUJWP6WpGM.md), 02:13-03:51)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Benchmark saturation pushes capability evals toward human time horizons](benchmark-saturation-pushes-capability-evals-toward-human-time-horizons.md)
- [Evaluate agent trajectories with backtests and smell metrics](evaluate-agent-trajectories-with-backtests-and-smell-metrics.md)
- [Portfolio-Allocate Eval Failures With a Triage Agent](portfolio-allocate-eval-failures-with-a-triage-agent.md)
- [Seal Eval Environments Against Agents That Read the Leaked Answer](seal-eval-environments-against-answer-leaking-agents.md)
- [Run Agentic Coding Evals as an Infrastructure-Reliability Problem](run-agentic-coding-evals-as-an-infrastructure-problem.md)

Sources:
- [Coding Evals: From Code Snippets to Codebases - Naman Jain, Cursor](../sources/20251215_tHN44yJoeS8.md), 02:23-06:47
- [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](../sources/20260606_QuuIywMG4s8.md), 03:38-06:18, 10:55-11:07
- [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](../sources/20260604_wcUJWP6WpGM.md), 02:13-03:51
