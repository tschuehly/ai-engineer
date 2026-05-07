# Agent Managers Orchestrate Editor, Browser, and Background Agents

Summary: Agent-first coding environments can move the primary control surface above the editor. An agent manager lets the human supervise many background agents while the editor and browser become tools that agents can use and humans can jump into when direct control is needed.

Use when:
- Designing an IDE or developer platform for long-running or parallel coding agents.
- Deciding where approvals, notifications, browser evidence, and editor escape hatches should live.

Details:
- Antigravity is presented as a three-surface developer platform: editor, browser, and agent manager. The agent manager is the central hub, while the editor and browser are agent tools. 01:45-04:32
- The editor remains available for manual work, autocomplete, and synchronous chat, and the product emphasizes fast switching between the agent manager and exact editor context when the human needs to finish the last part of a task. 02:32-03:11, 19:57-20:19
- The agent-controlled browser expands the agent's work surface beyond code into authenticated docs, GitHub dashboards, bug dashboards, experiments, UI interaction, JavaScript execution, DOM retrieval, and browser recordings. 03:14-04:24, 08:48-10:27
- The agent manager includes an inbox and OS-level notifications for work requiring attention, such as terminal-command approvals, so many background runs can proceed without constant monitoring. 04:39-05:13
- The product bet is that stronger models stretch task time and tool breadth, making the human's primary job more like supervising artifacts, approvals, and parallel work than watching one terminal transcript. 07:19-08:16, 19:20-20:29

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Autonomous browser verification finds painted-door failures](autonomous-browser-verification-finds-painted-door-failures.md)
- [Dynamic artifacts make agent work reviewable and reusable](dynamic-artifacts-make-agent-work-reviewable-and-reusable.md)

Sources:
- [Defying Gravity - Kevin Hou, Google DeepMind](../sources/20251202_HN-F-OQe6j0.md), 01:45-05:13, 07:19-10:27, 19:20-20:29
