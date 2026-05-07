# Role-Specialized Agent Systems Beat One Giant Coding Agent

Summary: Large coding tasks should be decomposed across role-specialized agents instead of handed to one oversized agent with a larger context window. Specialization can reduce context pressure, model-cost waste, and review ambiguity.

Use when:
- Designing multi-agent coding workbenches.
- Deciding whether to scale a coding tool by adding context and model power or by decomposing roles.
- Reviewing an agent architecture that sends every request to the same expensive model.

Details:
- Yegge criticizes current coding-agent products for routing both complex codebase analysis and trivial file checks to the same expensive model, which makes the agent an overpowered single worker rather than a coordinated system. (05:02-05:24)
- He frames the context window as an oxygen tank: increasing context helps only temporarily if one agent must swim through the whole codebase alone. (05:38-06:01)
- The proposed decomposition is to send different role agents for product management, coding, review, testing, Git merge, and related responsibilities. (06:03-06:13)
- This extends existing multi-agent guidance: use decomposition when roles have different context, model, tool, or verification needs, not merely to create more parallel chat threads.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use subagents to isolate context-heavy subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Customize subagents by task, model, tools, and permissions](customize-subagents-by-task-model-tools-and-permissions.md)
- [Let the core agent loop orchestrate parallel subtasks](let-the-core-agent-loop-orchestrate-parallel-subtasks.md)

Sources:
- [2026: The Year The IDE Died - Steve Yegge & Gene Kim, Authors, Vibe Coding](../sources/20251206_7Dtu2bilcFs.md), 05:02-06:31
