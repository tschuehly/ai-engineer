# Coding-Agent Capability Tiers Change the Bottleneck

Summary: Coding-agent progress should be understood as changing task horizons, not only higher benchmark scores. As agents handle longer uninterrupted work, the limiting problem shifts from text prediction to instruction following, repository setup, codebase understanding, human collaboration, confidence, and verification.

Use when:
- Evaluating whether a coding-agent product needs a new interface or workflow as model capability improves.
- Explaining why a 2x capability gain can require different infrastructure rather than just a stronger model.

Details:
- Wu measures agent capacity by how much work an AI can do before a human must intervene or steer it; for code, he says the practical task length had been doubling roughly every 70 days, creating 16x-64x annual capacity growth over the observed period.
- The early interface was tab completion because the task was mostly a single-file text-prediction problem; later tiers needed playbooks, memory, repository snapshots, codebase intelligence, IDE collaboration, and backlog orchestration.
- Each capability tier changes the bottleneck: repetitive migrations emphasize instruction following, isolated bug fixes emphasize repo setup and local checks, broader issues emphasize cross-file context, and backlog-scale work emphasizes confidence, escalation, and asynchronous testing.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat long-horizon agents as asynchronous workers with evolving interfaces](treat-long-horizon-agents-as-asynchronous-workers-with-evolving-interfaces.md)
- [Measure AI intensity by human input to valuable output](measure-ai-intensity-by-human-input-to-valuable-output.md)
- [Reliability thresholds determine whether coding agents save time](reliability-thresholds-determine-whether-coding-agents-save-time.md)

Sources:
- [Devin 2.0 and the Future of SWE - Scott Wu, Cognition](../sources/20250725_MI83buT_23o.md), 00:47-03:06
