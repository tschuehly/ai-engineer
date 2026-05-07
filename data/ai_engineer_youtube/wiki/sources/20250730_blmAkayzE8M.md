# How to Secure Agents using OAuth - Jared Hanson (Keycard, Passport.js)

Source: [How to Secure Agents using OAuth - Jared Hanson (Keycard, Passport.js)](https://www.youtube.com/watch?v=blmAkayzE8M)
Uploaded: 2025-07-30
Transcript: `raw/20250730_blmAkayzE8M/blmAkayzE8M.en-orig.vtt`

## Summary

Jared Hanson frames OAuth as the identity and authorization substrate needed to move agents and MCP servers away from long-lived, broadly scoped API keys. The talk explains why MCP servers should act as OAuth resource servers rather than authorization servers, then outlines future agent-security needs: client credentials for agent-to-agent access, URL/PKI-backed agent identity, attestation-aware authorization, transaction-level authorization, chain-of-custody across MCP and upstream API hops, and asynchronous user reauthorization for background agents.

## Extracted Concepts

- [Move Production MCP From API Keys to Scoped OAuth Token Flows](../concepts/move-production-mcp-from-api-keys-to-scoped-oauth-token-flows.md) - reinforces the migration from static agent secrets to short-lived OAuth-mediated access.
- [Model MCP Servers as OAuth Resource Servers](../concepts/model-mcp-servers-as-oauth-resource-servers.md) - explains why MCP servers should verify tokens while a separate authorization server handles login, consent, and token issuance.
- [Authenticate Agents With URL-Based PKI Identities](../concepts/authenticate-agents-with-url-based-pki-identities.md) - proposes URL identifiers plus public-key verification for agent client identity.
- [Authorize High-Impact Agent Actions Transactionally](../concepts/authorize-high-impact-agent-actions-transactionally.md) - applies richer authorization requests to amount-, budget-, or action-specific agent decisions.
- [Preserve Authorization Chain of Custody Across Agent Hops](../concepts/preserve-authorization-chain-of-custody-across-agent-hops.md) - extends MCP authorization through downstream APIs and agent-to-agent graphs.
- [Plan Asynchronous Authorization for Background Agents](../concepts/plan-asynchronous-authorization-for-background-agents.md) - covers agents that need more access after the user leaves the browser flow.

## Topic Links

- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)

## Notes

- The current local-MCP pattern often puts long-lived, broadly scoped API keys into config files or environment variables, which becomes a serious risk when scaled to hundreds or thousands of agents. 01:21-01:46
- OAuth separates clients, resource servers, and authorization servers; the authorization server mediates login, consent, token issuance, refresh-token rotation, and policy while APIs verify tokens. 02:10-06:16
- Earlier MCP authorization drafts collapsed the OAuth authorization-server role into the MCP server; the talk argues MCP servers should instead be OAuth resource servers that verify incoming HTTP tokens and delegate login/token issuance elsewhere. 06:57-10:35
- Authorization-code flows fit end-user delegation, while client-credentials flows matter when agents talk to other agents or MCP servers on their own behalf. 10:54-11:21
- Dynamic client registration reduces pre-registration friction but leaves registration requests uncredentialed, making agents effectively anonymous and hard to trust. 11:24-12:45
- URL identifiers plus PKI, signed JWT assertions, or HTTP message signatures can authenticate agent clients with public keys. 12:49-14:02
- Agent attestation should let authorization decisions account for the device, software, and LLM that will receive sensitive data, especially for desktop and mobile agents outside a controlled server environment. 14:07-14:57
- Scopes are better than passwords but can be too coarse and long-lived for agent-initiated financial or commercial transactions; richer, transaction-specific authorization is needed for amounts and budgets. 14:59-16:02
- MCP covers the client-to-server leg, but downstream MCP-to-API calls and agent-to-agent graphs need token exchange, identity chaining, and end-to-end authorization visibility. 16:02-17:13
- Background agents may need to request more access after the user leaves the browser, so OAuth UX needs asynchronous channels such as SMS or push notifications rather than only synchronous browser consent. 17:13-17:39
