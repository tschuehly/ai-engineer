# Retrieve Tool Descriptions Before Loading Large Tool Catalogs

Summary: When an agent has access to thousands of tools, store tool descriptions in a searchable knowledge base and retrieve a small relevant set before loading executable tool schemas into model context.

Use when:
- A product or platform has too many tools to expose in one model context window.
- The agent needs broad capability discovery without paying the context and selection cost of every tool on every run.

Details:
- AWS describes an internal agent with over 6,000 tools, which is too many descriptions and schemas to place in one model context for selection. (10:57-11:13)
- The described mitigation stores tool descriptions in a knowledge base and uses a `retrieve` tool for semantic search over that catalog. (10:47-11:18)
- The agent pulls only the relevant tools back into model context, then lets the model choose among that narrowed set. (11:18-11:30)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Discover Large API Tool Surfaces Progressively](discover-large-api-tool-surfaces-progressively.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)

Sources:
- [Building Agents at Cloud Scale - Antje Barth, AWS](../sources/20250802_WJjInLeaJjo.md), 10:47-11:30
