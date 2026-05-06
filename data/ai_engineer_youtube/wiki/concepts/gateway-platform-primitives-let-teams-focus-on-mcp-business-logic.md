# Gateway Platform Primitives Let Teams Focus on MCP Business Logic

Summary: Shared gateway primitives let domain teams create MCP servers without reimplementing auth, routing, deployment, observability, credentials, and scaling. The domain server can focus on workflow policy and business logic while the platform enforces common enterprise controls.

Use when:
- Legal, finance, observability, or other domain teams need to build MCP workflows without owning platform security.
- Standardizing MCP server creation with a CLI, subregistry, proxy, tunnel, and role-based access controls.

Details:
- A gateway can give new MCP servers auth, role-based access control, proxy routing, secure tunnels, an internal subregistry, and a developer CLI. (08:28-09:33)
- Once these primitives exist, a legal-team MCP server can focus on contract review, redlining, and escalation behavior rather than who can access it, how often it is used, whether it scales, or whether new agents can connect. (07:37-08:26)
- A gateway CLI can make MCP server creation understandable to the coding agent a team is using, so teams integrate with shared primitives and focus on the server-specific workflow. (09:14-09:48)
- Standard primitives can encode enterprise operating procedures by defining expected tools, forbidden tools, and required behavior for agents and MCP servers. (13:30-14:03)

Related topics:
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [MCP gateways create an enterprise root of trust](mcp-gateways-create-an-enterprise-root-of-trust.md)

Sources:
- [Gateways are All You Need - Karan Sampath, Anthropic](../sources/20260427_CD6R4Wf3jnY.md), 07:37-14:03
