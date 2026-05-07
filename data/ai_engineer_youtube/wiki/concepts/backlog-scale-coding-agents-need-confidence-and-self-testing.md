# Backlog-Scale Coding Agents Need Confidence and Self-Testing

Summary: Backlog-scale coding agents need to know when to execute, when to ask for help, and how to test their own work. Parallel task execution depends on confidence estimation, task scoping, human escalation, local execution, and asynchronous validation before PR delivery.

Use when:
- Moving from single coding-agent tasks to many queued issues or backlog cleanup.
- Designing review, escalation, and validation loops for asynchronous PR-producing agents.

Details:
- Wu says backlog-scale work requires integrating with issue systems such as Linear or Jira, understanding the right repository or codebase area, and scoping what the task means.
- The agent needs a confidence boundary: proceed when it understands the task, but ask the human for approval or clarification when it does not.
- For larger tasks, asynchronous testing becomes critical because an agent delivering entire PRs must run the code locally, know what to test, inspect outputs, debug its own changes, and run the right shell commands for feedback.
- The Devin 2.0 IDE workflow supports partial close monitoring: humans can watch the early part of a task, then let the agent complete most of the work independently.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Treat long-horizon agents as asynchronous workers with evolving interfaces](treat-long-horizon-agents-as-asynchronous-workers-with-evolving-interfaces.md)
- [Keep humans aligned with proactive agent work](keep-humans-aligned-with-proactive-agent-work.md)
- [Run eval suites in CI/CD before and during production](run-eval-suites-in-cicd-before-and-during-production.md)

Sources:
- [Devin 2.0 and the Future of SWE - Scott Wu, Cognition](../sources/20250725_MI83buT_23o.md), 12:28-15:48
