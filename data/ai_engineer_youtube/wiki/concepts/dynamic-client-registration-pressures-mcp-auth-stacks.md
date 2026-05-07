# Dynamic Client Registration Pressures MCP Auth Stacks

Summary: MCP dynamic client registration can stress ordinary developer and application-management surfaces because each registering MCP client may appear like another application that must be governed.

Use when:
- Designing admin dashboards or auth operations for many MCP clients.
- Evaluating whether existing application-management tooling is ready for MCP scale.

Details:
- MCP servers can dynamically register clients, and that can suddenly flood developer or application dashboards with MCP-related applications. 07:21-07:42
- Existing auth, application-management, and admin tooling may need MCP-specific adaptation rather than assuming ordinary SaaS app registration volumes and semantics. 07:42-07:56
- Dynamic registration becomes more difficult for remote asynchronous workloads that need headless auth into MCP servers while still preserving correct authorization controls. 10:31-10:46

Related topics:
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Move Production MCP From API Keys to Scoped OAuth Token Flows](move-production-mcp-from-api-keys-to-scoped-oauth-token-flows.md)
- [Cross-App Access Centralizes MCP Authentication Through the Identity Provider](cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md)
- [Gateway Platform Primitives Let Teams Focus on MCP Business Logic](gateway-platform-primitives-let-teams-focus-on-mcp-business-logic.md)

Sources:
- [(possible dupe but better sound) What does Enterprise Ready MCP mean? - Tobin South, WorkOS](../sources/20250627_0MqYA52iWQU.md), 07:21-07:56, 10:31-10:46
