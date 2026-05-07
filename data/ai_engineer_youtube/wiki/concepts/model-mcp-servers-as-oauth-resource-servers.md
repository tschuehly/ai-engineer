# Model MCP Servers as OAuth Resource Servers

Summary: MCP servers should verify OAuth tokens as resource servers rather than issuing credentials as authorization servers. Keeping authorization servers separate preserves OAuth's three-role model and lets MCP builders delegate login, consent, token issuance, refresh, and central policy to identity infrastructure.

Use when:
- Designing OAuth support for a remote MCP server.
- Deciding whether an MCP server should own authentication and token issuance.

Details:
- OAuth separates clients, resource servers, and authorization servers; clients request resources, authorization servers mediate access by issuing tokens, and resource servers verify those tokens. 05:10-05:41
- The talk criticizes an MCP authorization design that collapsed the authorization server into the MCP server, forcing MCP servers to implement authentication, token issuance, and other OAuth behavior. 07:58-08:40
- Modeling the MCP server as an OAuth resource server makes the server's job narrower: verify incoming HTTP tokens and hand off login, consent, token issuance, and policy to a separate authorization server. 09:56-10:35

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Move Production MCP From API Keys to Scoped OAuth Token Flows](move-production-mcp-from-api-keys-to-scoped-oauth-token-flows.md)
- [Model MCP Servers as OAuth Clients in Downstream API Chains](model-mcp-servers-as-oauth-clients-in-downstream-api-chains.md)
- [Cross-App Access Centralizes MCP Authentication Through the Identity Provider](cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md)

Sources:
- [How to Secure Agents using OAuth - Jared Hanson (Keycard, Passport.js)](../sources/20250730_blmAkayzE8M.md), 05:10-10:35
