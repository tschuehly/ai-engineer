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

- **The complementary property: never in context at all.** Anthropic's managed-agent design holds credentials in vaults "decrypted only when needed at tool execution runtime… the model never sees your security tokens." That is a different guarantee from the one on this page and the two compose cleanly — scope exchange bounds *what the credential can do*, never-in-context bounds *who can read it*. Neither substitutes for the other: a narrowly scoped token that appears in the prompt can still be exfiltrated and replayed within its scope, and an invisible token with broad scope can still be misused through the tool that holds it. The architectural precondition for the second guarantee is that tool execution runs outside the model's process; see [decrypt agent credentials only at tool execution time](decrypt-agent-credentials-only-at-tool-execution-time.md). ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 22:25-22:47)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Short-lived IdP-derived tokens reduce standing MCP access](short-lived-idp-derived-tokens-reduce-standing-mcp-access.md)
- [Filter MCP tools by scopes and step-up authorization](filter-mcp-tools-by-scopes-and-step-up-authorization.md)
- [Cross-app access does not replace authorization policy](cross-app-access-does-not-replace-authorization-policy.md)
- [Decrypt Agent Credentials Only at Tool Execution Time](decrypt-agent-credentials-only-at-tool-execution-time.md)

Sources:
- [Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0](../sources/20260114_VSdV-AdSlis.md), 10:52-12:19, 14:30-15:09
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 22:25-22:47
