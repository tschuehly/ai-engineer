# Model MCP Servers as OAuth Clients in Downstream API Chains

Summary: In delegated API chains, an MCP server may need its own OAuth client identity because it mediates between an agent client and upstream resource APIs.

Use when:
- Securing MCP servers that call third-party APIs on behalf of an agent or user.
- Designing identity flows where both the agent application and MCP server participate in authorization.

Details:
- The workshop models the agent as a client and the APIs as traditional OAuth resource servers, then extends that model to MCP servers that access remote data. 13:45-14:07
- For MCP flows, the MCP server is also modeled as a client: an agent client talks to the MCP server, and the MCP server talks to upstream APIs. 15:14-15:43
- The described MCP semantics include dynamic client registration, which lets the identity layer reason about the MCP server as a registered client rather than a hidden implementation detail. 15:47-15:56
- A Next.js workshop example places MCP tools alongside the agent, then has the agent client communicate with the MCP server and let that server talk to third parties. 16:33-16:55

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Move production MCP from API keys to scoped OAuth token flows](move-production-mcp-from-api-keys-to-scoped-oauth-token-flows.md)
- [MCP gateways create an enterprise root of trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)

Sources:
- [Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0](../sources/20260114_VSdV-AdSlis.md), 13:45-14:07, 15:14-16:55
