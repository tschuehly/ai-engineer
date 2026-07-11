# Optimize an Agent With a Branch-per-Hypothesis Coding-Agent Loop

Summary: Point a coding agent at a product agent's repo and its golden-dataset eval suite and let it self-improve as a hill-climb: each iteration is a fresh git branch that tests exactly one hypothesis (one failure class), keeps the branch when evals improve and rolls back when they regress, while a cross-run memory file and per-iteration reports accumulate a readable, steerable change log of every hypothesis tried.

Use when:
- You want to raise an agent's eval accuracy without hand-tuning prompts/tools one at a time.
- You have a golden dataset + scorers and a coding agent (e.g. Claude Code) that can edit the target agent's code.
- You need the optimization to be auditable and reversible, not an opaque one-shot rewrite.

Details:
- The setup is two agents with different jobs: a **coding agent** (Claude Code, but it works with multiple coding tools) is the *builder* that writes and changes the target agent's code; the **target/product agent** is what you ship, and it feeds evals and full/thinking traces back so the builder can see regressions and self-improve. 09:45-12:40
- Precedent: Andrej Karpathy's "auto research" loop showed a coding agent that mutates ML code/hyperparameters can drive down loss / improve a deep-learning model over many experiments; this concept ("AutoAgent") applies the same closed loop to *agents* rather than models. 08:28-09:47
- Step 1 — define an **optimization job** as a markdown file: objective, target repository, metrics, and as much context as you want (what the agent may/may not touch). 13:40-14:20
- Step 2 — run the loop. First run the evals once to generate **baseline data / a baseline report** (the cases, a summary, what's working vs not) so the coding agent has a clear picture of the current system before changing anything. 14:20-16:40
- Iteration mechanics: every iteration starts a **new git branch**, forms one **hypothesis** (tackle one class of problems at a time), changes the agent to implement it, reruns the eval suite, writes a `reports.md`, and updates a **global memory file across all runs**. If metrics improved, continue from that branch; if metrics regressed or something bad happened, **roll back to the previous branch**. New hypotheses are grounded in the memory file + reports file. 15:36-18:00
- Observed run shape: iteration 1 regressed → roll back; then +5%; then a 0% hypothesis; then +12%; number of iterations is a knob you set. The output is a full **change log** of every improvement/regression, and because each hypothesis builds a report, a human can reopen a *promising-but-failed* hypothesis, understand what the agent tried, and steer it next time. 14:14-20:00
- Anti-gaming guardrail (the key human-in-the-loop rule): explicitly forbid the coding agent from editing the golden datasets or scorers just to make evals pass — that's cheating, not improvement. Humans also structure the initial agent and supply domain context. 12:40-13:40
- Reported lift, without cheating: a naive tool-less "hello world" math agent (Mastra) went **18% → 83%** in ~10 iterations; a real production agent went **67% → 86%** in ~10 iterations (the loop found edge cases, improved the system prompt, improved tool descriptions, and fixed tool logic) and is now in production; on an *already human-optimized* production agent it still found **+10%** on internal benchmarks — improvements humans hadn't found. 05:22-06:42, 10:33-11:21, 18:17-18:30
- Common eval-failure modes it fixes are the obvious levers: missing tools, a wrong/incomplete system prompt, and poor context retrieval (usually implemented as tools). 06:40-08:00

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Automate the Agent-Building Loop With an Agentic AI Engineer](automate-the-agent-building-loop-with-an-agentic-ai-engineer.md)
- [Route Agent Repairs to the Right Layer With the Smallest Durable Change](route-agent-repairs-to-the-right-layer-smallest-durable-change.md)
- [Make Regression-Aware Optimization Part of the Continual-Learning Loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md)
- [Promote Validated Live-Trace Failure Clusters Into the Golden Dataset](promote-validated-live-trace-failure-clusters-into-the-golden-dataset.md)
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)

Sources:
- [Agents Building Agents - Alfonso Graziano, Nearform](../sources/20260628_aHhB3sjGjkI.md), 05:22-20:00
