# Discover Large API Tool Surfaces Progressively

Summary: Large API providers should expose agent tools through progressive discovery rather than eagerly loading every endpoint as MCP tools. MCP remains useful as a protocol, but the default tool surface must respect the agent's context budget.

Use when:
- Designing MCP access for a platform with hundreds or thousands of API endpoints.
- Choosing between one broad MCP server, many product-specific servers, CLI access, tool search, and code-mode access.

Details:
- Cloudflare's REST OpenAPI spec was described as 2.3 million tokens; a naive tool conversion was roughly 1.1 million tokens, which would overwhelm agent context before useful work begins. (02:37-03:30)
- Splitting the API into product-specific MCP servers reduces initial context, but users must pick the right server and partial coverage can leave many endpoints unreachable. (03:45-04:47)
- MCP is not the core failure; the failure is dumping too many tools, prompts, resources, or skills into context at once instead of letting capabilities be discovered only when needed. (04:47-05:25)
- CLIs provide progressive discovery through command lists and `--help`, but they require shell access and may not suit hosted agent clients. (05:27-06:36)
- Tool search can select a small top-k set of relevant tools for a request, but irrelevant selected tools still occupy context after the model chooses the one it needs. (06:37-07:20)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Agent Experience Prioritizes APIs, CLIs, and MCP Over Dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)

Sources:
- [MCP = Mega Context Problem - Matt Carey](../sources/20260425_YBYUvGOuotE.md), 02:37-07:20
