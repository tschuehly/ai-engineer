# Ask Agents After Each Run What Blocked Their Success

Summary: A cheap post-run interrogation step can turn the agent's own experience into debugging signal for missing tools, permissions, contradictory instructions, and wrong context.

Use when:
- Agent runs fail silently or work around missing capabilities instead of reporting them clearly.
- A team needs operational feedback about whether prompts, tools, permissions, or context are blocking success.

Details:
- PostHog asks the agent at the stop hook what the system could have done better to set it up for success in the run. 11:12-11:35
- This surfaced missing MCP tools, missing permissions, contradictory directives, and language-mismatched instructions such as JavaScript guidance in a Python project. 10:22-12:05
- The pattern is framed as low-cost inference-time user research where the "user" is the agent itself; without asking, repeated failures could continue across hundreds of runs. 10:39-11:48

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)

Sources:
- [LLM codegen fails and how to stop 'em - Danilo Campos, PostHog](../sources/20260430_juoNbJiZUi0.md), 10:22-12:05
