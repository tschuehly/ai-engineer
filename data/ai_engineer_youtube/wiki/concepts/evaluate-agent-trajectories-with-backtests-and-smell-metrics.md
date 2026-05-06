# Evaluate agent trajectories with backtests and smell metrics

Summary: Flexible tool-loop agents need evaluation beyond final-answer checks. Historical backtests, point-in-time snapshots, end-to-end task checks, and trajectory metrics can reveal whether the agent is taking brittle or wasteful paths.

Use when:
- Evaluating coding agents, browser agents, or other tool-using agents with flexible trajectories.
- Looking for lightweight signals before building a full task-success benchmark.

Details:
- The source notes that simple master-loop agents become harder to evaluate because they rely on model flexibility rather than fixed workflow branches. 49:06-49:25
- Suggested eval shapes include end-to-end checks that ask whether the agent solved the task, point-in-time snapshots that test whether a partial conversation triggers the right tool call, and backtests over historical data. 49:25-50:34
- The speaker proposes "agent smell" metrics such as number of tool calls, retries, and total runtime as surface-level sanity checks for agent trajectories. 49:52-50:08
- For highly specific output workflows, a more constrained tool or workflow can be easier to test with sample inputs, simple LLM judges, code execution, and repeated eval runs. 52:24-54:03

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Evaluate agent skills with task scenarios and comparative conditions](evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md)

Sources:
- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md), 49:06-50:34
- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md), 52:24-54:03
