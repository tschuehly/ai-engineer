# Native Tool Integration Beats a Bolted-On Tool the Model Can't Time

Summary: Giving an agent a capable tool is not the same as the agent using it well. The same retrieval tool produced a large gain inside a model trained to call it (Cursor's Composer) but a much smaller gain bolted onto a model that only sees it as "another tool in the list" (Claude Code), because the value lives in the model knowing *when and why* to invoke the tool, not in the tool's availability.

Use when:
- Adding a new tool (semantic search, a custom retrieval API, an MCP server) to an off-the-shelf agent and expecting it to match a vendor's published gains.
- Explaining why an A/B test of "tool present vs absent" underperforms the benchmark a tool's maker reports.
- Deciding whether to integrate a capability at the harness/prompt level or to train/select a model that natively understands the tool.

Details:
- Turbopuffer benchmarked adding a semantic-search tool to Claude Code and got real but modest precision gains — "not as great as Cursor's." The explanation is not the tool quality but the integration: Claude Code "is built for just grepping" (Anthropic's focus), and semantic search was added as "just another tool in the list" — effectively "here's this cool tool, you probably should use it sometimes." (09:55-10:24)
- "It's very hard for it to have a true understanding of when to use it, why to use it." Cursor's Composer, by contrast, treats semantic search as a built-in tool "it knows when and how to use," which is why Cursor measured ~23.5% gains while the bolted-on version did not. (10:10-10:36)
- The general lesson: tool availability ≠ tool effectiveness. A model that has not been trained or tuned to gate a tool will under-call it, over-call it, or call it on the wrong task, so the measured uplift collapses relative to a native integration even though the underlying capability is identical. (09:55-10:36)
- This is the gating counterpart to tool-use discipline: "Fix Tool Discipline Before Reaching for a Bigger Model" shows behavior *within* a tool sequence (discover → inspect → self-correct) is trainable; this concept is the upstream decision of *whether and when* to reach for the tool at all, and it is likewise a learned competence, not a property of the tool. (09:55-10:36)
- The forward-looking framing: long-term winners "provide lightweight tools to find the right context in various different ways" — but the value is realized only when the model is competent at wielding them to shrink a huge context window "into the right million." Shipping the tool is necessary, not sufficient. (10:36-11:01)

Related topics:
- [Tools](../topics/tools.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Fix Tool Discipline Before Reaching for a Bigger Model](fix-tool-discipline-before-reaching-for-a-bigger-model.md)
- [Use Tool Names and Descriptions as Operational Prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Treat Embeddings as Cached Compute Decided by Query Volume](treat-embeddings-as-cached-compute-decided-by-query-volume.md)
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Evaluate Agent Retrieval by Trajectory, Not Task Success](evaluate-agent-retrieval-by-trajectory-not-task-success.md)

Sources:
- [Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer](../sources/20260603_zKk7sDMGDEQ.md), 09:55-11:01
