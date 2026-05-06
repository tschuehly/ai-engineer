# Parallel Coding-Agent Queues Need Focus-Preserving Review Interfaces

Summary: As coding-agent runs grow from seconds to many minutes, humans need queue and review interfaces that preserve focus across multiple concurrent streams. The goal is not constant monitoring, but batching attention around completed work, diffs, previews, comments, and deployment handoffs.

Use when:
- Designing interfaces for multiple concurrent coding-agent runs.
- Deciding when to parallelize agent work instead of waiting on one run.
- Reviewing workflow risks created by long-running autonomous coding tasks.

Details:
- Coding agents are moving from instant completions toward longer executions that run type checks, tests, browser automation, and QA before returning to the human. (07:26-09:14)
- When average run time exceeds roughly five minutes, watching logs stops being a viable human workflow and the developer role shifts toward managing multiple work streams. (09:52-10:26)
- Parallelism can reduce idle waiting when several agent tasks run at once and completed work is reviewed as it becomes available. Vibe Kanban is presented as one implementation with multiple workspaces, diffs, comments, previews, setup scripts, Git worktrees, and pluggable coding agents. (10:26-11:28, 15:00-15:28)
- Interfaces should avoid pulling humans between tasks every thirty seconds; they should let agents run long enough to produce reviewable output and then yield back with the right context for QA, code review, and deployment shepherding. (11:47-14:01)
- A parent-agent comparison flow can make parallel work more reviewable by running model-specific subagents in isolated worktrees, summarizing differences, and helping the user combine preferred pieces instead of choosing one run blindly. 06:18-12:13

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ralph loops process one ticket at a time with fresh context](ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Use parent agents to compare and merge parallel subagent outputs](use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md)

Sources:
- [Software Engineering Is Becoming Plan and Review - Louis Knight-Webb, Vibe Kanban](../sources/20260502_W76woOYHlvY.md), 07:26-15:28
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md), 06:18-12:13
