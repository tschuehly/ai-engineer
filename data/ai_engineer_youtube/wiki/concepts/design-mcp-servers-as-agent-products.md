# Design MCP Servers as Agent Products

Summary: MCP servers should be designed as product interfaces for agents, not as transport wrappers over existing APIs. The useful unit is an agent workflow outcome, shaped around the agent's discovery, iteration, and context limits.

Use when:
- Designing a new MCP server for an existing product or API.
- Reviewing whether an MCP surface helps an agent complete a workflow or merely exposes endpoints.

Details:
- An MCP server is an interface for an agent, so it should be designed around agent strengths and weaknesses rather than assuming the model can use raw APIs as well as a human developer. 04:24-05:56
- Humans usually hide APIs behind products, SDKs, clients, mobile apps, or websites; agents deserve an interface optimized for their own use cases instead of a direct API dump. 05:24-05:56
- Discovery, iteration, and context have different economics for agents than for humans: every session may enumerate tools and descriptions, every extra call can resend conversation history, and the context window is the working memory budget. 06:12-07:37
- Outcome-oriented product thinking should decide what goes into the server; a tool should not be added unless it is expected to produce a useful agent workflow result. 14:47-15:18
- The talk frames future MCP work as "context products" rather than only MCP servers, emphasizing the product layer above the transport. 34:24-34:43

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Secure MCP Servers by Shrinking the Agent-Visible Surface](secure-mcp-servers-by-shrinking-the-agent-visible-surface.md)
- [Agent Experience Prioritizes APIs, CLIs, and MCP Over Dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)

Sources:
- [Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect](../sources/20260112_96G7FLab8xc.md), 04:24-07:37, 14:47-15:18, 34:24-34:43
