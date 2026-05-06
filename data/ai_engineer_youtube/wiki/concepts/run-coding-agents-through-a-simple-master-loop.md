# Run coding agents through a simple master loop

Summary: Strong coding agents can be built around a small loop that lets the model choose tools, observe results, and continue until it stops needing tools. This reduces workflow machinery compared with fixed DAGs and lets better models improve the same harness over time.

Use when:
- Designing a coding-agent harness or deciding whether to start with a DAG.
- Explaining why simple tool loops can outperform complex orchestration for exploratory coding work.

Details:
- The source describes Claude Code, Codex, Cursor, and Amp as variants of one master while loop: run model-selected tools, return tool results, and keep looping until there are no more tool calls. 11:29-12:09
- The speaker argues that models are increasingly good at knowing when to call tools, recover from mistakes, and continue exploration, making the surrounding architecture simpler. 12:15-12:41
- DAGs can provide stronger guardrails for narrow classifications or high-risk decisions, but they can also grow into brittle webs of prompts and routing nodes. 22:15-23:24
- The practical middle ground is to keep the flexible master loop for exploration and reserve deterministic structure for the parts that truly need guarantees. 25:10-25:57

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Minimal coding-agent harnesses can outperform feature-heavy surfaces](minimal-coding-agent-harnesses-can-outperform-feature-heavy-surfaces.md)
- [Choose choreography or orchestration by complexity and autonomy](choose-choreography-or-orchestration-by-complexity-and-autonomy.md)

Sources:
- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md), 11:29-12:41
- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md), 22:15-25:57
