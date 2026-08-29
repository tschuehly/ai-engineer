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

- **Trajectory profiling used continuously in production rather than as an offline eval pass.** Uber calls it a runtime profile — "which is like the agent trajectory, which told us why the agent is doing what it did. We get to know what tools calls it made. We get to know what thinking process it had. And then with that insight, we were able to actually tune our runtime, tune our performance such that the agent could very quickly give us high-quality results at a low cost." The role it plays is diagnostic rather than evaluative: an outcome metric such as addressal rate says a comment was bad, and the trajectory says which tool call or reasoning step made it bad. That ordering matters — they added the outcome metric first, because trajectory storage is only useful once something tells you which runs to open. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 06:07-06:35)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Evaluate agent skills with task scenarios and comparative conditions](evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)

Sources:
- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md), 49:06-50:34
- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md), 52:24-54:03
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 06:07-06:35
