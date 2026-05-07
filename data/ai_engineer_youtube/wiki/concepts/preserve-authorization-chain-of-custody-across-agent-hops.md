# Preserve Authorization Chain of Custody Across Agent Hops

Summary: Agent authorization should remain visible as requests move from an MCP client to an MCP server, onward to internal or third-party APIs, and eventually across agent-to-agent graphs. Token exchange, identity chaining, and end-to-end traces keep downstream calls from losing the original authority context.

Use when:
- Building an MCP server that calls internal APIs or third-party APIs.
- Designing multi-agent systems where one agent invokes another on a user's or organization's behalf.

Details:
- MCP authorization primarily covers the first leg between agents and MCP servers; the security profile of the MCP server's downstream API calls can otherwise remain unspecified. 16:02-16:24
- OAuth token exchange is recommended for MCP-server-to-API calls inside the same domain so downstream services do not depend on blindly forwarding the original token. 16:24-16:30
- Cross-domain MCP-to-third-party-API calls need identity chaining and an identity assertion grant style so backend services can preserve authority across domain boundaries. 16:38-16:48
- Agent-to-agent graphs need end-to-end visibility as authorization flows across many agents and servers. 16:58-17:13

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Model MCP Servers as OAuth Clients in Downstream API Chains](model-mcp-servers-as-oauth-clients-in-downstream-api-chains.md)
- [Govern MCP Tool Calls With Tool-Level Policy and End-to-End Traces](govern-mcp-tool-calls-with-tool-level-policy-and-end-to-end-traces.md)
- [Authenticate Agents With URL-Based PKI Identities](authenticate-agents-with-url-based-pki-identities.md)

Sources:
- [How to Secure Agents using OAuth - Jared Hanson (Keycard, Passport.js)](../sources/20250730_blmAkayzE8M.md), 16:02-17:13
