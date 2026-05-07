# MCP Gateways Create an Enterprise Root of Trust

Summary: An MCP gateway is a shared middle layer between MCP clients and many MCP servers that centralizes authentication, authorization, observability, secure connectivity, and deployment. Use it when decentralized MCP development is blocked by security review, opaque usage, or inconsistent access control.

Use when:
- Scaling MCP beyond a few approved servers across many enterprise teams.
- Giving security teams one trusted control point while letting domain teams build business-specific MCP servers.

Details:
- Enterprises struggle with MCP table stakes such as knowing who uses each tool, which tools are failing, which users should have access, and whether servers prevent data exfiltration or harmful tool use. (01:42-03:20)
- Registries help discovery but do not provide the enterprise layer for authentication, access control, observability, and credential management. (03:20-04:07)
- A gateway acts as a middle layer between many MCP servers and any MCP client, supplying authorization, authentication, observability, secure connectivity, and deployment support. (06:52-07:49)
- Security teams can bless one platform as the root of trust while MCP servers treat the gateway as the only trusted endpoint. (06:01-06:31, 08:51-09:08)
- Anthropic's remote-MCP gateway example adds an internal adoption pattern: make `connect to MCP` the easy path, route by URL to internal or external servers, centralize credential management, rate limiting, and observability, and return a normal MCP SDK client session so protocol features roll out through ordinary package updates. 07:50-09:43
- A gateway also becomes a central inspection point for model-bound context: standardized MCP messages let teams hook policy, malicious-server blocking, content classification, audit, tool-execution processors, tool-definition processors, and resource management into one stream. 12:39-14:05

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Cross-app access centralizes MCP authentication through the identity provider](cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md)
- [Filter MCP tools by scopes and step-up authorization](filter-mcp-tools-by-scopes-and-step-up-authorization.md)
- [Stateless remote MCP servers rebuild allowed tools per request](stateless-remote-mcp-servers-rebuild-allowed-tools-per-request.md)
- [Carry MCP JSON-RPC Over Internal Transports](carry-mcp-json-rpc-over-internal-transports.md)

Sources:
- [Gateways are All You Need - Karan Sampath, Anthropic](../sources/20260427_CD6R4Wf3jnY.md), 01:42-09:08
- [Remote MCPs: What we learned from shipping - John Welsh, Anthropic](../sources/20250619_0NHCyq8bBcM.md), 07:50-09:43, 12:39-14:05
