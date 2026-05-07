# Choose Copilot Mode By Autonomy and Feedback Need

Summary: GitHub Copilot workflows should choose interaction mode by how much autonomy, repository mutation, and human feedback the task needs. Ask mode fits inquiry, edit mode fits directed file changes, local agent mode fits tool-using implementation with immediate supervision, and Copilot Coding Agent fits asynchronous issue-based work.

Use when:
- Deciding whether to keep a coding task in interactive chat or assign it to a background agent.
- Introducing Copilot agent features without treating every request as the same workflow.

Details:
- The workshop frames Copilot as a pair programmer with strengths, weaknesses, and workload fit rather than as a single universal automation mode. 03:56-04:45
- Harrison distinguishes ask mode, edit mode, local agent mode, and the newer Copilot Coding Agent, then treats them as different ways to collaborate with the same assistant. 04:47-05:00
- Local agent mode can lead more of the work: it explores the project, finds files, builds code, runs tests, and attempts self-healing when something goes wrong. 11:42-12:10
- Copilot Coding Agent is the higher-autonomy path: the user assigns an issue and lets the agent work asynchronously until it returns a pull request or session result. 30:19-30:56

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Configure Agent Modes, Rules, and Permissions as the Workflow Evolves](configure-agent-modes-rules-and-permissions-as-the-workflow-evolves.md)
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)

Sources:
- [Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft](../sources/20250726_DdaAABdAqZY.md), 03:56-05:00, 11:42-12:10, 30:19-30:56
