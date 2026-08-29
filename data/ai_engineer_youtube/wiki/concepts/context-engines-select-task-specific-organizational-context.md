# Context Engines Select Task-Specific Organizational Context

Summary: A context engine is the layer that selects organization-, user-, and task-specific context for an agent while avoiding irrelevant context. It is not equivalent to naive documentation RAG, a pile of MCP servers, or a larger context window.

Use when:
- Designing retrieval or context infrastructure for coding agents in a real organization.
- Evaluating whether a proposed RAG, MCP, or long-context setup actually supplies task-specific engineering context.

Details:
- Coding agents often begin at "ground zero" for a codebase and spend tokens exploring before doing useful work; the context engine's job is to front-load the relevant code, organizational expectations, and best practices. (01:27-02:19)
- Naive vector search can create unsatisfied search loops, token waste, compaction risk, conflicting retrieved facts, and task-irrelevant results from other teams or repositories. (10:51-12:12)
- A useful context engine should understand the asker, team, collaborators, organizational experts, and prior decisions behind the current codebase. (15:50-16:08)
- Context engines can feed coding agents, MCP or CLI tools, custom APIs, SCM code review, and messaging surfaces; those surfaces are access paths rather than the complete system. (17:42-18:19, 32:20-33:09)

- **The failure mode the earlier talk left unnamed, and the second reason a big window does not substitute.** Werry's conference version of this same argument supplies a name for what goes wrong when you hand an agent a searchable store instead of a selection layer: satisfaction of search, the radiology error of finding one indicator and stopping. "If you attach a wiki, it still doesn't tell the agent where the information is that it needs" — and the agent "finds something that they think is correct and then they stop." It also gives the everything-in-the-window alternative two independent refusals rather than one: the organizational corpus exceeds "even one that's a million tokens in size," *and* "it causes the agent to get distracted. When you're working on a task, you want task-specific flow." The second reason is the one that survives a larger window. See [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md). ([Werry, Aug 2026](../sources/20260827_qdAkxLoYNI8.md), 04:16-06:20)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](demand-driven-context-pulls-knowledge-from-failed-work.md)
- [Evaluate retrieval and MCP layers by task value, not only response availability](evaluate-retrieval-and-mcp-layers-by-task-value.md)
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md)
- [An Agent Is an Expert Who Onboards Again on Every Task](an-agent-is-an-expert-who-onboards-again-on-every-task.md)
- [Measure a Context Layer on Compounding, Not on the First Task](measure-a-context-layer-on-compounding-not-the-first-task.md)

Sources:
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md), 01:27-02:19, 10:51-12:12, 15:50-18:19, 32:20-33:09
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 04:16-06:20, 07:53-08:52, 11:52-12:27
