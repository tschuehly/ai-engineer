# Task-Tuned Tool Sets Beat Generic Integration Surfaces for Core Coding Loops

Summary: A coding agent's core tool set should be optimized for the feedback loops it must close, not simply assembled from generic integrations. Broad MCP surfaces can still be useful, but untuned tool descriptions and irrelevant tools create context load and tool-selection confusion.

Use when:
- Designing the default tools for a coding-agent harness.
- Deciding whether to expose a generic MCP server directly or wrap it with workflow-specific tools.
- Debugging a coding agent that gets distracted by irrelevant tools or fails to close local feedback loops.

Details:
- Amp frames agent construction as a loop with a model and tool calls; the controllable levers are the model, tool descriptions, and how the model iterates with tools. (03:58-04:30)
- The source argues that core coding-agent tools should be refined around feedback loops such as finding context and acting on it, because a generic MCP server author does not know the agent's local task or workflow. (04:40-05:40)
- Adding irrelevant tools to the context window increases the set of choices the agent must consider and can make the agent confused even before useful work begins. (05:42-05:58)
- This complements MCP context-budget guidance: the issue is not only the number of tools, but whether the visible tools and descriptions are tuned to the agent's current job.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Design MCP servers as agent products](design-mcp-servers-as-agent-products.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)

Sources:
- [Amp Code: Next Generation AI Coding - Beyang Liu, Amp Code](../sources/20251222_gvIAkmZUEZY.md), 03:58-05:58
