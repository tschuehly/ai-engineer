# MCP Tool Surfaces Need Default Context Budgets

Summary: MCP servers with broad platform coverage should treat default tool exposure and output size as a context budget. More tools can make agents worse when all descriptions and schemas are loaded upfront.

Use when:
- Designing MCP defaults for a large product surface such as repos, issues, pull requests, actions, and projects.
- Debugging agents that select the wrong tool, forget available tools, or burn context before useful work begins.

Details:
- GitHub's MCP server exceeded 100 tools after public contribution growth, and agents became worse at using GitHub while context windows filled faster. (02:06-02:24)
- Configurable tool sets and dynamic discovery were not enough because most users stayed on default settings rather than editing JSON configuration. (03:21-04:15)
- GitHub reduced initial context load by focusing defaults for common use cases and grouping CRUD tools; the default configuration still allowed expansion or contraction for users who needed it. (05:10-05:48)
- Output payloads count against the same budget as tool descriptions: tailoring a pull-request listing output cut more than 75% of its output tokens. (05:53-06:13)
- Cloudflare hit the same context-budget wall at API scale: a 2.3 million-token OpenAPI spec became roughly 1.1 million tokens when naively converted into endpoint tools, making progressive discovery necessary. (02:37-03:30)
- Agent discovery is not a one-time human documentation read: every session may enumerate tool names and descriptions during handshake, so tool count and description size become recurring context costs. 06:12-06:56
- A visible tool count above roughly 50 tools per agent is a performance smell unless the team invests in routing, splitting, namespacing, and evaluation; the budget is per agent, not per individual server. 35:32-37:14
- Amp adds a coding-agent-specific version of this failure mode: irrelevant tools increase context confusion, and generic MCP server descriptions may not be tuned to the feedback loops a particular coding agent needs to close. 04:40-05:58

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Discover large API tool surfaces progressively](discover-large-api-tool-surfaces-progressively.md)
- [Design MCP Servers as Agent Products](design-mcp-servers-as-agent-products.md)
- [Task-tuned tool sets beat generic integration surfaces for core coding loops](task-tuned-tool-sets-beat-generic-integration-surfaces-for-core-coding-loops.md)

Sources:
- [Scaling GitHub for your Agents — Sam Morrow, GitHub](../sources/20260427_0n3MKk7r60w.md), 02:06-06:13
- [MCP = Mega Context Problem - Matt Carey](../sources/20260425_YBYUvGOuotE.md), 02:37-03:30
- [Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect](../sources/20260112_96G7FLab8xc.md), 06:12-06:56, 28:25-29:24, 35:32-37:14
- [Amp Code: Next Generation AI Coding - Beyang Liu, Amp Code](../sources/20251222_gvIAkmZUEZY.md), 04:40-05:58
