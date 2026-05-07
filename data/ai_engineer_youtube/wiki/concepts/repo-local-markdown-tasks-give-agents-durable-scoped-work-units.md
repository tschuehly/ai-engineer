# Repo-local Markdown tasks give agents durable scoped work units

Summary: Versioned Markdown task files can hold task state, requirements, acceptance criteria, implementation notes, and status outside the active context window. This makes agent work easier to scope, resume, review, and share through the same repository workflow as code.

Use when:
- Breaking a large coding-agent feature into smaller independently reviewable tasks.
- Choosing where to store task intent and progress so agents do not rely on one long chat history.
- Designing agent workflows that should stay local to a Git repository.

Details:
- Backlog.md stores tasks as Markdown files in the repository, with front matter metadata such as task ID, title, labels, and other fields plus description and acceptance criteria. (03:14-04:22)
- Keeping tasks in the repo gives agents a durable source for what to implement, while humans can inspect task details directly in a terminal Kanban board. (00:47-01:17, 03:14-03:57)
- Atomic Markdown tasks are presented as context engineering: the human can define how much the agent should implement in one task, reduce context-window exhaustion, and prevent unwanted extra features. (11:08-12:05)
- Small tasks make recovery cheaper: if a task goes wrong, the team can roll back, revise the description or acceptance criteria, and restart from the implementation plan instead of salvaging a sprawling chat. (11:35-11:54)
- Because task files live in Git, teams can share them without extra databases, accounts, or project-management APIs, and Backlog.md can detect status changes made from another branch. (12:51-13:37)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Keep spec artifacts feature-scoped, mutable, and context-backed](keep-spec-artifacts-feature-scoped-mutable-and-context-backed.md)
- [Offload long-horizon agent state outside the context window](offload-long-horizon-agent-state-outside-the-context-window.md)
- [Ralph loops process one ticket at a time with fresh context](ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md)

Sources:
- [Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents - Alex Gavrilescu, Funstage](../sources/20251124_zMXKhhwiCIc.md), 00:47-01:17, 03:14-04:22, 11:08-13:37
