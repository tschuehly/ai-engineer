# Context Window Editing Clears Stale Tool Results

Summary: Long-running tool agents need active context editing, not just larger context windows. Old tool outputs can consume space without helping later decisions, so the runtime should remove stale results while preserving or reloading durable state elsewhere.

Use when:
- Designing coding agents that call many file, search, edit, or test tools in one session.
- Deciding whether to expand context length, add memory, or prune low-value context.

Details:
- Anthropic frames context management as keeping technical designs, codebase snippets, instructions, and tool calls in the window only when they are the right context for the current step. 03:50-04:28
- The first context-editing example clears old tool results because prior file reads and other large outputs may take substantial window space while no longer being relevant. 05:58-06:43
- Anthropic reports that combining memory with context editing improved an internal benchmark by 39%, which supports treating context pruning as an eval-backed runtime feature rather than prompt hygiene alone. 06:46-07:05
- Larger context windows still benefit from editing; the talk argues that million-token windows and tools for editing active context work together, rather than size replacing relevance management. 07:07-07:17

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Offload Long-Horizon Agent State Outside the Context Window](offload-long-horizon-agent-state-outside-the-context-window.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)

Sources:
- [Katelyn Lesse - Evolving Claude APIs for Agents, Anthropic](../sources/20251204_aqW68Is_Kj4.md), 03:50-07:17
