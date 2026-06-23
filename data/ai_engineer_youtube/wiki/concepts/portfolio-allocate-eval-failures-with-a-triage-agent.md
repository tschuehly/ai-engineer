# Portfolio-Allocate Eval Failures With a Triage Agent

Summary: After an agent-eval run, don't read a single score — send a second agent through the traces of every failure to categorize *why* each task failed, which surfaces the small levers that actually move the score; then sort fixes into three zones (obvious harness bugs, nuance/model-specific tuning, and the overfitting danger zone), remembering that every run tests three things at once: the model, the harness, and the problem set.

Use when:
- A coding-agent eval suite returns a score with many failures and you need to decide what to change next.
- You are tempted to "fix" a low eval score by swapping in a bigger/newer model instead of diagnosing the failures.
- Triaging long agent traces (every LLM call) by hand is too slow to be done across dozens of failed tasks.

Details:
- The method: run the suite (e.g. Terminal Bench's 89 tasks) → get a score → say 50 failures → run *another agent* over the failure traces and have it allocate each failure to a cause ("this failed because it didn't pass tests," "this failed because the retry tool was broken"). A trace is a massive file containing every LLM call the agent made, which is why an agent, not a human, reads them. Proper allocation reveals the small levers; pulling them makes massive improvements. (13:03-13:51)
- An eval run is testing three things simultaneously, and the triage must separate them: (1) the **model** — a strong model can overshoot and score well even on a horrible harness; (2) the **harness** — is it leveraging the best of the model (the same model often works much better with one coding agent than another)?; (3) the **problem set** — scoring 100% on stupid problems is worthless, so the tasks must be legit. (13:53-15:00)
- Three zones of improvement after an original score: **Zone 1 — obvious flaws/bugs** (a bug that crashes the harness, rate limits): fix them, that's fine. **Zone 2 — nuance improvements** (the most critical, the essence of hill-climbing): model-family-specific prompt engineering and tweaks (prompt larger/smaller) that explain "why is this model everyone calls great not working for me." **Zone 3 — the danger zone**: overfitting / cheating to top a benchmark so you can tweet about it — don't. (15:43-16:53)
- This is a diagnostic loop distinct from an optimizer that rewrites prompts/datasets/scorers: the triage agent's job is to *classify failures and locate levers*, after which a human (or a separate optimizer) makes the change and re-runs. Combine it with parallel isolated environments so the suite is fast enough to iterate on. (13:03-13:51)
- The closing discipline: hill-climb a real benchmark *and* pass the vibe check; don't accept a good number alone, and don't trust vibes alone. (16:54-17:21)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Tune Coding-Agent Harnesses Per Model Family](tune-coding-agent-harnesses-per-model-family.md)
- [Use Eval Agents to Improve Prompts, Datasets, and Scorers](use-eval-agents-to-improve-prompts-datasets-and-scorers.md)
- [Trace Agent Tool Arguments to Debug Real Failures](trace-agent-tool-arguments-to-debug-real-failures.md)
- [Decompose Evals Into Rubrics to Target the Failing Behavior](decompose-evals-into-rubrics-to-target-the-failing-behavior.md)
- [Detect Reward Hacking in Code Optimization Evals](detect-reward-hacking-in-code-optimization-evals.md)

Sources:
- [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](../sources/20260606_QuuIywMG4s8.md), 13:03-17:21
