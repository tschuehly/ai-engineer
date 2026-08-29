# Coding-Agent Capability Tiers Change the Bottleneck

Summary: Coding-agent progress should be understood as changing task horizons, not only higher benchmark scores. As agents handle longer uninterrupted work, the limiting problem shifts from text prediction to instruction following, repository setup, codebase understanding, human collaboration, confidence, and verification.

Use when:
- Evaluating whether a coding-agent product needs a new interface or workflow as model capability improves.
- Explaining why a 2x capability gain can require different infrastructure rather than just a stronger model.

Details:
- Wu measures agent capacity by how much work an AI can do before a human must intervene or steer it; for code, he says the practical task length had been doubling roughly every 70 days, creating 16x-64x annual capacity growth over the observed period.
- The early interface was tab completion because the task was mostly a single-file text-prediction problem; later tiers needed playbooks, memory, repository snapshots, codebase intelligence, IDE collaboration, and backlog orchestration.
- Each capability tier changes the bottleneck: repetitive migrations emphasize instruction following, isolated bug fixes emphasize repo setup and local checks, broader issues emphasize cross-file context, and backlog-scale work emphasizes confidence, escalation, and asynchronous testing.
- Theo Browne gives an independent field framing of the same tier progression as three model "eras": Sonnet 3.5 = the tool-call era (first model to do tool calls consistently enough for day-to-day codebase work), Opus 4.5 = the long-running-task era (tests its own work and completes hour-scale tasks without losing track), and Mythos = the orchestration era where the model "understands itself," spawns and verifies subagents, and does so from a prompt with "no fancy software factory" needed — reinforcing that new tiers deliver value only on work sized to match them ("My previous work would not benefit from a model like Mythos"). [Theo Browne, 00:54-03:34]

- **The tier where the bottleneck leaves engineering entirely.** Amazon's report is that after the coding constraint lifts, the next one is not a harness problem at all: "previously, writing code manually was the bottleneck… the speed of decision-making becomes a new bottleneck… because the code only takes 1 to two months to write. All of the review processes associated with the launch of a product become the bottleneck." The earlier tiers on this page move the constraint within the loop — instruction following, repo setup, context, verification — and each has an engineering fix. This one moves it to product approval and launch review, owned by people who were not part of the rollout, which is why an engineering-side adoption program can succeed on every internal metric and change nothing a customer sees. See [When Code Stops Being the Long Pole, Approvals Become It](when-code-stops-being-the-long-pole-approvals-become-it.md). ([Liguori](../sources/20260828_pqlWNihgdjI.md), 18:45-19:56)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat long-horizon agents as asynchronous workers with evolving interfaces](treat-long-horizon-agents-as-asynchronous-workers-with-evolving-interfaces.md)
- [Measure AI intensity by human input to valuable output](measure-ai-intensity-by-human-input-to-valuable-output.md)
- [Reliability thresholds determine whether coding agents save time](reliability-thresholds-determine-whether-coding-agents-save-time.md)
- [Rescope Ambition Down a Tier as Models Improve](rescope-ambition-down-a-tier-as-models-improve.md)
- [When Code Stops Being the Long Pole, Approvals Become It](when-code-stops-being-the-long-pole-approvals-become-it.md)

Sources:
- [Devin 2.0 and the Future of SWE - Scott Wu, Cognition](../sources/20250725_MI83buT_23o.md), 00:47-03:06
- [Everything we knew about software has changed — Theo Browne, @t3dotgg](../sources/20260708_xUnRQ9vLXxo.md), 00:54-03:34
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 18:45-19:56
