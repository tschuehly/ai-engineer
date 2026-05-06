# Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0

Source: [Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0](https://www.youtube.com/watch?v=VSdV-AdSlis)
Uploaded: 2026-01-14
Transcript: `raw/20260114_VSdV-AdSlis/VSdV-AdSlis.en-orig.vtt`

## Summary

This workshop frames agent identity as a security prerequisite: agents need to know the human or enterprise subject they act for, call APIs on that subject's behalf, pause for approval on risky operations, and receive fine-grained access rather than broad resource authority. It describes Auth0/Okta patterns including async approval built on client-initiated back-channel authentication, token vault storage and exchange for upstream API scopes, and MCP server flows where both the agent and MCP server are modeled as OAuth clients.

## Extracted Concepts

- [Identify the Human Subject Behind Agent Actions](../concepts/identify-the-human-subject-behind-agent-actions.md) - this source explains why agents cannot apply policy or restrictions while acting as anonymous actors.
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](../concepts/route-high-impact-agent-actions-through-explicit-human-approval-gates.md) - this source adds an OAuth-style async approval pattern for long-running agents.
- [Vault and Exchange Tokens for Scoped Upstream Agent Access](../concepts/vault-and-exchange-tokens-for-scoped-upstream-agent-access.md) - this source shows how agents can request scoped upstream API tokens without holding broad standing credentials.
- [Model MCP Servers as OAuth Clients in Downstream API Chains](../concepts/model-mcp-servers-as-oauth-clients-in-downstream-api-chains.md) - this source describes an agent client calling an MCP server that itself acts as a client to upstream APIs.

## Topic Links

- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

## Notes

- The presenters identify four identity pillars for agents: know who the user is, call APIs on the user's behalf, request user confirmation for riskier operations, and constrain access at a fine-grained resource level. 05:18-06:54
- Enterprise use cases add a company-control layer because an employee's agent may act both for the person and for the organization. 07:05-07:33
- Async approval is described as a mechanism where a long-running agent initiates an authorization request, the user receives structured transaction details, and approval returns to the agent as an access token containing the approved details. 09:02-10:40
- Token Vault persists upstream refresh tokens, supports token exchange for requested scopes such as Slack, Facebook, or other scoped APIs, and manages scopes and token lifetimes to keep agent SDK flows simpler. 10:52-12:19
- For MCP, the workshop models the MCP server as a client too: the agent client talks to the MCP server, and the MCP server talks to upstream APIs, with dynamic client registration as part of the MCP semantics. 15:14-16:55
