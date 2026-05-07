# Keep agent context small, fresh, and task-specific

Summary: Agent context should be deliberately curated, externalized, trimmed, and isolated by task. More context can increase cost, degrade quality, and preserve stale or wrong assumptions that pull later work back toward failed paths.

Use when:
- A long coding-agent session starts producing confused or repetitive changes.
- Deciding whether to add files, MCP servers, history, or project notes to an agent run.

Details:
- Each additional context token adds recurring input cost because chat history is resent, and heavily filled context windows can degrade output quality rather than improve it. (04:33-05:32)
- Always-enabled MCP servers and broad file references can add background tool and code context that is unrelated to the current step. (05:32-05:52)
- Bad context can poison output when a session mixes unrelated tasks, includes outdated comments, or retains earlier wrong decisions after the human tries to steer back. (05:58-06:49)
- Durable information should live outside the active context window in scratchpads, memory files, and AGENTS.md-like project instructions, then be selectively pulled in for the current task. (07:16-08:05)
- When the session has drifted, start a new session, have the agent summarize the useful state for the next agent, manually verify the summary, and continue with only the corrected context. (10:37-11:15)
- Splitting work across agents or sessions can be useful primarily because it isolates task context and prevents irrelevant or wrong history from accumulating. (08:30-08:48)
- Vibe engineering needs explicit context surfaces such as rules, docs, commands, and memories because the model cannot hold an entire app context or infer project intent like a mind reader. (10:59-11:13)
- Frequent intentional compaction treats correctness, completeness, size, and trajectory as context-quality dimensions; repeated correction history and wrong research can poison the next tool choice even when the prompt still fits in the model window. 04:38-05:43
- For coding agents, broad static onboarding can become too large or stale, while on-demand compressed context can summarize only the current vertical slice from source-backed code. 12:14-14:10

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Context development lifecycle treats context as an engineered artifact](context-development-lifecycle-treats-context-as-an-engineered-artifact.md)
- [Own agent context instead of accepting hidden harness mutation](own-agent-context-instead-of-accepting-hidden-harness-mutation.md)
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)

Sources:
- [Agentic Engineering: Working With AI, Not Just Using It - Brendan O'Leary](../sources/20260407_BEKc4P87XKo.md), 04:33-11:15
- [From Vibe Coding To Vibe Engineering - Kitze, Sizzy](../sources/20251214_JV-wY5pxXLo.md), 10:59-11:13
- [No Vibes Allowed: Solving Hard Problems in Complex Codebases - Dex Horthy, HumanLayer](../sources/20251202_rmvDxxNubIg.md), 04:38-05:43, 12:14-14:10
