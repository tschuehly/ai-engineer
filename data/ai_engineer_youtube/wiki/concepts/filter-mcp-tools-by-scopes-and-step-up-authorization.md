# Filter MCP Tools By Scopes And Step-Up Authorization

Summary: MCP servers should expose tools according to the caller's actual authorization and make secure authorization the easiest path. Scope filtering and step-up OAuth reduce wasted context and avoid brittle failures.

Use when:
- Building a remote MCP server that supports personal access tokens or OAuth.
- Avoiding over-privileged default tool access while keeping agent workflows usable.

Details:
- Plaintext MCP access tokens are often long-lived, over-privileged, and stored where the agent can reach them, so local configuration can become both easy and unsafe. (08:13-08:55)
- GitHub's remote MCP server supports OAuth 2.1 and PKCE so secure remote HTTP login can be the path of least resistance rather than requiring a local runtime and plaintext token. (09:00-09:33)
- PAT-based access can immediately filter the exposed MCP tools down to the scopes on the token. (12:27-12:50)
- OAuth step-up can return a scope challenge, ask the user to approve the extra scope, and continue the tool call instead of failing the workflow outright. (12:50-13:29)
- Removing user-specific tools for server tokens such as CI/action contexts can eliminate predictable failures and context waste when no user identity exists. (13:29-13:45)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Short-lived IdP-derived tokens reduce standing MCP access](short-lived-idp-derived-tokens-reduce-standing-mcp-access.md)
- [Cross-app access does not replace authorization policy](cross-app-access-does-not-replace-authorization-policy.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Expose the Background Agents' Tool Surface to Employees Over MCP](expose-the-background-agents-tool-surface-to-employees-over-mcp.md)

Sources:
- [Scaling GitHub for your Agents — Sam Morrow, GitHub](../sources/20260427_0n3MKk7r60w.md), 08:13-13:45
