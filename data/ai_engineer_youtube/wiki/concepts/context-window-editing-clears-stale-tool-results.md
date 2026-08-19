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
- Chin gives the same warning from a context-engineering angle: old tool outputs can dump enough information into the window that they crowd out relevant current evidence. 04:17-04:43
- The "stale" judgement has to be right, and a measured counter-case shows what happens when it is not. In Towards AI's tutor bake-off, a preset that cleared tool outputs after 5,000 tokens (keeping the last 5) scored *worse than touching nothing* on recall, cost, and latency simultaneously, because "if you remove the tool outputs consistently then the agent needs to retrieve afterwards for information it already had" — deleting a result the agent still needs converts saved tokens into extra tool calls. The safer version of the same instinct is in the source's non-LLM toolkit: truncate an outlier tool output to head and tail and leave an explicit "truncated" marker so the model can *re-call* the tool if it later needs the middle, rather than erasing the fact that the output existed. ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 09:13-10:16, 32:19-33:30, 45:57-46:41)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Offload Long-Horizon Agent State Outside the Context Window](offload-long-horizon-agent-state-outside-the-context-window.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Prompt Caching Sets the Break-Even Bar for Compaction](prompt-caching-sets-the-break-even-bar-for-compaction.md)
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)

Sources:
- [Katelyn Lesse - Evolving Claude APIs for Agents, Anthropic](../sources/20251204_aqW68Is_Kj4.md), 03:50-07:17
- [Context Engineering: Connecting the Dots with Graphs - Stephen Chin, Neo4j](../sources/20251124_LLuKshphGOE.md), 04:17-04:43
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 09:13-10:16, 32:19-33:30, 45:57-46:41
