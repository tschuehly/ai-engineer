# Stateless Remote MCP Servers Rebuild Allowed Tools Per Request

Summary: Remote MCP servers can scale horizontally by keeping request handling stateless and deriving the allowed tool surface from configuration, scopes, and policy on each request.

Use when:
- Scaling a remote MCP server beyond a single stateful process.
- Designing session handling where client identity and observability matter but request routing should not require affinity.

Details:
- GitHub runs a stateless remote MCP server with Redis session storage and standard observability rather than a single stateful server process. (13:48-14:11)
- The implementation creates a fresh SDK server instance on every request and adds tools at startup according to requested configuration and allowed policy. (14:23-14:42)
- This shape scales without session affinity; GitHub reported roughly 7 million tool calls per week at the time of the talk and used sessions mainly to identify the self-reported MCP client identity. (14:46-15:08)
- A future MCP stateless transport was described as a way to make MCP servers easier to deploy like ordinary stateless REST services on infrastructure such as Cloud Run or Kubernetes, especially for large hyperscalers. (13:49-14:29)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Cross-app access centralizes MCP authentication through the identity provider](cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md)
- [Agent traces require specialized eval infrastructure](agent-traces-require-specialized-eval-infrastructure.md)

Sources:
- [Scaling GitHub for your Agents — Sam Morrow, GitHub](../sources/20260427_0n3MKk7r60w.md), 13:48-15:08
- [The Future of MCP - David Soria Parra, Anthropic](../sources/20260419_v3Fr2JR47KA.md), 13:49-14:29
