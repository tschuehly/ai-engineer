# Agent Software Factories Need Runnable, Contextual, and Verifiable Primitives

Summary: A coding-agent factory is not just more agents. It needs repository structure, reproducible project commands, accessible external context, and validation paths that let agents work without repeated human setup.

Use when:
- Preparing a repository for parallel or autonomous coding-agent work.
- Diagnosing why agents require constant human setup, navigation, or verification.

Details:
- Codebase structure matters because colocated and modular files let an agent discover relevant implementation areas with a local listing instead of broad repository search (05:02-05:50).
- Usage patterns such as authentication helpers, startup scripts, and test conventions should exist as reproducible references the agent can follow instead of rediscovering each workflow (05:50-06:17).
- The factory readiness checklist includes whether the project is runnable, whether required context is accessible, whether agents can interface with systems such as Linear, Notion, Datadog, or Slack, and whether the work is verifiable (09:24-10:10).
- Verifiability should cover unit tests, integration tests, and UI tests; front-end work may require actual DOM interaction and user-flow checks rather than only backend contracts (07:51-10:42).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Unified coding-agent harnesses combine models, tools, environments, and safety](unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)

Sources:
- [Building your own software factory — Eric Zakariasson, Cursor](../sources/20260428_rnDm57Py54A.md), 05:02-10:42
