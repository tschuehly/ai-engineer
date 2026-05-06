# Vault and Exchange Tokens for Scoped Upstream Agent Access

Summary: Agent applications can keep upstream API access safer by vaulting refresh tokens, exchanging user or app tokens for scoped upstream access tokens, and managing token lifetimes outside the model loop.

Use when:
- Building agents that need delegated access to Slack, calendars, social APIs, or other third-party resources.
- Avoiding broad long-lived credentials inside agent runtime state or prompts.

Details:
- Token Vault is described as a mechanism for persisting upstream resource refresh tokens so agent use cases can retrieve access without re-running full consent flows for every action. 10:52-11:28
- The flow supports exchanging an access or refresh token for requested scopes on an upstream service, such as Slack, Facebook, or another scoped API. 11:30-12:03
- The platform persists scopes and manages token lifetimes, keeping SDK integration simpler while the agent remains online and constrained by the approved scopes. 12:03-12:19
- In a LangGraph interrupt example, the agent detects a need for calendar access, requests additional scopes, performs token exchange through Token Vault, and receives a new access token for the upstream provider. 14:30-15:09

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Short-lived IdP-derived tokens reduce standing MCP access](short-lived-idp-derived-tokens-reduce-standing-mcp-access.md)
- [Filter MCP tools by scopes and step-up authorization](filter-mcp-tools-by-scopes-and-step-up-authorization.md)
- [Cross-app access does not replace authorization policy](cross-app-access-does-not-replace-authorization-policy.md)

Sources:
- [Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0](../sources/20260114_VSdV-AdSlis.md), 10:52-12:19, 14:30-15:09
