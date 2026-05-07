# Group Agent Tools by Human-Facing Actions

Summary: Agent tool catalogs should be curated around clear human-facing actions, not mirrored one-to-one from every backend API endpoint.

Use when:
- Designing a function-calling or MCP tool surface for a large API portfolio.
- Debugging tool-selection errors caused by overlapping names, descriptions, or capabilities.

Details:
- The talk warns not to register hundreds of organizational APIs as hundreds of agent tools; too many tools in one prompt empirically reduce accuracy because semantically overlapping tools confuse the model, 05:52-06:24.
- Tool surfaces should expose fewer tools at a time, group related capabilities logically, keep scopes specific, and use clear names and descriptions, 06:23-06:33.
- A useful tool should feel like one human-facing action rather than a raw low-level endpoint, 06:30-06:36.

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Translate API Endpoints Into Agent Stories](translate-api-endpoints-into-agent-stories.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)

Sources:
- [Building Applications with AI Agents — Michael Albada, Microsoft](../sources/20250724_R30col3UPUg.md), 05:52-06:36
