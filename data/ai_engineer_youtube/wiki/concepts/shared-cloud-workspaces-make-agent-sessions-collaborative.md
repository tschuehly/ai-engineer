# Shared Cloud Workspaces Make Agent Sessions Collaborative

Summary: A multiplayer agent workspace can make coding-agent work reviewable while it is happening by putting humans, agents, code, terminal output, previews, diffs, commits, and prompting history into the same cloud-backed session.

Use when:
- Building collaborative coding-agent infrastructure.
- Comparing local terminal agents with cloud session environments.

Details:
- ACE sessions are described as multiplayer chats that include teammates and coding agents, with each session backed by a sandboxed cloud micro-VM on its own Git branch. 07:18-07:44
- The micro-VM model isolates session changes while allowing parallel tasks, instant switching, shared terminals, shared dev servers, shared browser previews, diffs, and PR creation. 07:41-08:45, 09:21-09:40, 11:02-11:28
- Teammates can join a session without stashing local work or checking out another branch, and they see the prompting history that led to current outputs. 07:47-08:05
- Because the session lives in the cloud, work can continue when one collaborator closes their laptop, and future clients can attach without depending on a developer's local machine. 11:44-12:18

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Cloud agents turn coding work into asynchronous VM-backed queues](cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md)
- [Isolate parallel coding work with project worktrees](isolate-parallel-coding-work-with-project-worktrees.md)
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)

Sources:
- [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment - Maggie Appleton, GitHub](../sources/20260426_ClWD8OEYgp8.md), 07:18-12:18
