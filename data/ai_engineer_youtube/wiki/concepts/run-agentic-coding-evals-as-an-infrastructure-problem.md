# Run Agentic Coding Evals as an Infrastructure-Reliability Problem

Summary: Evaluating coding agents on real repositories at scale is dominated by infrastructure reliability, not agent cleverness: each task is a multi-gigabyte Docker image, runs fail for non-model reasons, and model defaults drift between updates. A trustworthy leaderboard comes from a minimalistic agent on strong infrastructure, a retry policy that separates model errors from infrastructural errors, noise control, and validating the harness against an external benchmark before trusting any number.

Use when:
- Standing up a SWE-style benchmark or internal coding-agent eval that runs many models repeatedly.
- A run's numbers look off and you need to decide whether the cause is the model, the harness, or the infrastructure.
- Deciding where to spend effort: a fancier agent scaffold vs. more stable execution infrastructure.

Details:
- Prefer "a minimalistic agent with strong infrastructure" over "an over-engineered agent with weak infrastructure." SWE-rebench's scaffold is a small set of tools + bash commands, run in a "YOLO" setup (no clarification questions), and it minimizes context because modern models are already good at tool calling rather than needing ReAct-style tool demonstrations. (08:12-09:09)
- Each task is not just a prompt but a 1-10 GB Docker image with dependencies installed so the project's tests run, so good infrastructure is a prerequisite, not an afterthought. (05:11-05:21)
- Define a retry policy that separates *model* errors (too-long context, too many tool calls) from *infrastructural/provider* errors, and decide which exit statuses get rerun — ~1-2 model runs become invalid every month without it. (09:09-09:40)
- Minimize infrastructural noise that silently invalidates tasks: tests that reach external resources, or a default container clock set to 1970 that breaks time-sensitive tests, look like model failures but are environment bugs. (06:23-07:00)
- Watch for default-parameter drift across model updates *even within a family* (e.g. GPT 5.2 → 5.4): reasoning level, caching level, and other defaults can change between versions, so re-verify that your settings still apply. (10:10-10:38)
- Validate your harness against an external benchmark (SWE-bench, Terminal Bench) and confirm your numbers match the reported numbers *before* running your own experiments. (10:38-10:53)
- Caching materially improves cost efficiency (~4x for the simple agent), but token-hungry harnesses like Claude Code stay expensive even with caching and Haiku sub-agents — so cost is part of the infrastructure budget, not a footnote. (09:40-10:10)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Seal Eval Environments Against Agents That Read the Leaked Answer](seal-eval-environments-against-answer-leaking-agents.md)
- [Tune Coding-Agent Harnesses Per Model Family](tune-coding-agent-harnesses-per-model-family.md)
- [Validate eval harnesses before trusting skill scores](validate-eval-harnesses-before-trusting-skill-scores.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Portfolio-Allocate Eval Failures With a Triage Agent](portfolio-allocate-eval-failures-with-a-triage-agent.md)

Sources:
- [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](../sources/20260604_wcUJWP6WpGM.md), 05:11-10:53
