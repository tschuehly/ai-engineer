# Frequent intentional compaction keeps coding agents in the smart zone

Summary: Frequent intentional compaction keeps coding-agent sessions short enough and clean enough for reliable tool use by repeatedly compressing useful work state into reviewed artifacts. The point is not just fewer tokens; it is preserving correct, complete, task-specific context while discarding stale trajectory and noise.

Use when:
- A coding-agent task requires substantial codebase search before implementation.
- A long session starts carrying stale tool output, wrong assumptions, or repeated correction history.

Details:
- Intentional compaction asks the agent to compress the useful current context into a Markdown file, lets the human review or tag it, and then starts the next agent from that compact artifact instead of the whole conversation. 03:47-04:06
- Useful compaction should preserve exact files and line numbers relevant to the problem, not generic summaries that force the next agent to redo discovery. 04:08-04:35
- Context should be optimized for correctness, completeness, size, and trajectory; incorrect context is worse than missing context, and both are worse than ordinary noise. 04:38-05:43
- The "smart zone" framing warns that heavily filled context windows can degrade tool-call quality before the nominal model limit is reached; too many always-on MCP servers or JSON-heavy tools can push work into the degraded region. 05:48-06:25
- Subagents are a context-control mechanism: let a separate context window search and read broadly, then return a concise result so the parent agent only loads what matters. 06:35-07:27
- On-demand compressed context can beat broad static onboarding docs because it creates a task-specific snapshot from current code rather than relying on long documentation that may be stale or incomplete. 12:14-14:10

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Use subagents to isolate context-heavy subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Use research-plan-implement loops for coding agents](use-research-plan-implement-loops-for-coding-agents.md)

Sources:
- [No Vibes Allowed: Solving Hard Problems in Complex Codebases - Dex Horthy, HumanLayer](../sources/20251202_rmvDxxNubIg.md), 03:47-07:27, 12:14-14:10
