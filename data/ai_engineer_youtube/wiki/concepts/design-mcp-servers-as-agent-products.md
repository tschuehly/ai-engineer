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
- **A vendor describing its MCP surface in exactly those terms.** Resolve AI sells a production-context and learning layer, and its integration story is that the layer is available to someone else's agent: "if you have an agent harness, if you're… building your own, everything that I showed is accessible through kind of MCP servers, etc. So you can really graft resolve into kind of any system that you have as just kind of an extension of learning to kind of do deeper work or to sort of pull production context a bit more efficiently." The complement follows the same logic in reverse — "bring your own skills along for the ride. Um, don't go duplicate a bunch of stuff" — which is a product boundary claim: the server supplies what the host harness cannot derive, and declines to re-supply what it already has. ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 13:02-13:12, 23:28-23:58)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Secure MCP Servers by Shrinking the Agent-Visible Surface](secure-mcp-servers-by-shrinking-the-agent-visible-surface.md)
- [Agent Experience Prioritizes APIs, CLIs, and MCP Over Dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Separate Execution From the Production Context That Judges It](separate-execution-from-the-production-context-that-judges-it.md)

Sources:
- [Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect](../sources/20260112_96G7FLab8xc.md), 04:24-07:37, 14:47-15:18, 34:24-34:43
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 13:02-13:12, 23:28-23:58
