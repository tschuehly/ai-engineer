# Your Insecure MCP Server Won't Survive Production - Tun Shwe, Lenses

Source: [Your Insecure MCP Server Won't Survive Production - Tun Shwe, Lenses](https://www.youtube.com/watch?v=BurJvbqFr4c)
Uploaded: 2026-04-08
Transcript: `raw/20260408_BurJvbqFr4c/BurJvbqFr4c.en-orig.vtt`

## Summary

This talk treats production MCP security as both an interface-design problem and an infrastructure problem: small, outcome-oriented tool surfaces reduce prompt-injection and oversharing risk, while remote deployment needs streamable HTTP, OAuth 2.1, scoped short-lived tokens, client identity metadata, tool/resource-level RBAC, data masking, and end-to-end observability.

## Extracted Concepts

- [Secure MCP servers by shrinking the agent-visible surface](../concepts/secure-mcp-servers-by-shrinking-the-agent-visible-surface.md) - The source connects tool count, schema looseness, documentation ambiguity, and oversized responses to concrete MCP attack paths.
- [Move production MCP from API keys to scoped OAuth token flows](../concepts/move-production-mcp-from-api-keys-to-scoped-oauth-token-flows.md) - The source contrasts long-lived API-key setups with OAuth 2.1, PKCE, token exchange, and CIMD-based client identity.
- [Govern MCP tool calls with tool-level policy and end-to-end traces](../concepts/govern-mcp-tool-calls-with-tool-level-policy-and-end-to-end-traces.md) - The source identifies RBAC, masking, interaction logs, and full-request tracing as enterprise requirements beyond basic OAuth.

## Topic Links

- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

## Notes

- Agent-facing interfaces have a different threat profile from human APIs: agents enumerate all tools and descriptions on connection, so each exposed tool description becomes both context cost and a tool-poisoning surface. 02:24-03:03
- Retried agent calls can resend full conversation history, including prior tool results, making poorly scoped MCP responses a repeated data-leakage risk. 03:03-03:29
- Secure MCP design should expose coarse-grained outcome tools, constrained schemas, clear tool documentation, minimal response payloads, and tool/resource-scoped permissions rather than broad low-level API operations. 04:27-07:54
- Local stdio MCP is convenient for single-user development but does not scale to production; remote streamable HTTP introduces OAuth, token management, CORS, TLS, rate limits, and governance concerns all at once. 08:11-10:03
- Long-lived API keys in MCP client config or HTTP headers are often unscoped, rarely rotated, sometimes shared, and may be passed through in ways that create confused-deputy vulnerabilities. 10:51-13:20
- Dynamic Client Registration solves self-registration for unbounded MCP clients, but creates non-portable registrations and can trust self-asserted client metadata from attackers. 13:51-19:54
- CIMD improves client identity by making the client ID a metadata URL controlled by the client owner, binding redirect URIs in that metadata, and letting authorization servers allow or deny clients. 20:00-22:35
- Enterprise-grade MCP still needs tool/resource-level RBAC, data masking before agent exposure, logs of agent/tool/parameter/return-data interactions, and end-to-end tracing from validation through response generation. 22:42-24:07
