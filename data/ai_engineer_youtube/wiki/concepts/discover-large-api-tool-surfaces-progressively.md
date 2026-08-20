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
- Progressive discovery is also a client-harness responsibility: MCP can move information across the wire, but clients decide whether to load every tool into context or give the model a search/load mechanism for tools it needs later. (07:47-09:18)
- AWS gives a concrete large-catalog variant: store descriptions for thousands of tools in a knowledge base, retrieve relevant tools for the task, and only then expose the narrowed set to the model. (10:57-11:30)
- **A shipping harness makes the client-side half of this a per-tool flag.** Codex marks tools as deferred so their definitions never enter the window, and pairs them with a tool-search tool the model calls when it needs one — "you can mark any tool as deferred loading and by that not showing up in the tool registry" ([Defer Tool Definitions Out of Context and Let the Model Search for Them](defer-tool-definitions-out-of-context-and-let-the-model-search-for-them.md)). Note where this lands on this page's own list: it is not the top-k pre-selection variant this page criticizes for leaving irrelevant tools resident, because the model — not a retriever running ahead of it — decides when to spend context on a definition, and it spends it only on what it asked for. What the source does not say is how the model learns a deferred tool exists in the first place, which is the corresponding cost. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 05:59-06:59)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Agent Experience Prioritizes APIs, CLIs, and MCP Over Dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Retrieve Tool Descriptions Before Loading Large Tool Catalogs](retrieve-tool-descriptions-before-loading-large-tool-catalogs.md)
- [Defer Tool Definitions Out of Context and Let the Model Search for Them](defer-tool-definitions-out-of-context-and-let-the-model-search-for-them.md)

Sources:
- [MCP = Mega Context Problem - Matt Carey](../sources/20260425_YBYUvGOuotE.md), 02:37-07:20
- [The Future of MCP - David Soria Parra, Anthropic](../sources/20260419_v3Fr2JR47KA.md), 07:47-09:18
- [Building Agents at Cloud Scale - Antje Barth, AWS](../sources/20250802_WJjInLeaJjo.md), 10:57-11:30
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 05:59-06:59
