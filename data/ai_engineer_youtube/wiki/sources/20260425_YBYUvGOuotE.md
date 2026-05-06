# MCP = Mega Context Problem - Matt Carey

Source: [MCP = Mega Context Problem - Matt Carey](https://www.youtube.com/watch?v=YBYUvGOuotE)
Uploaded: 2026-04-25
Transcript: `raw/20260425_YBYUvGOuotE/YBYUvGOuotE.en-orig.vtt`

## Summary

Matt Carey argues that large API providers should not expose every endpoint as eagerly loaded MCP tools because the tool descriptions themselves can overwhelm agent context. Cloudflare's response is to treat MCP as a protocol surface for progressive discovery: use CLIs or tool search when appropriate, but for very large APIs prefer typed code-mode access where an agent writes code against generated SDK types and executes it inside a constrained sandbox with programmable network and secret-access guardrails.

## Extracted Concepts

- [Discover large API tool surfaces progressively](../concepts/discover-large-api-tool-surfaces-progressively.md) - this source frames MCP scale as a context-loading problem rather than a reason to abandon the protocol.
- [MCP Tool Surfaces Need Default Context Budgets](../concepts/mcp-tool-surfaces-need-default-context-budgets.md) - this source extends the existing MCP tool-budget concept from broad catalogs to whole-API endpoint surfaces.
- [Expose large APIs through typed code mode](../concepts/expose-large-apis-through-typed-code-mode.md) - this source shows how generated types can compress a broad API into code the agent can reason over.
- [Run agent-written API code inside programmable sandboxes](../concepts/run-agent-written-api-code-inside-programmable-sandboxes.md) - this source details why generated code execution needs isolation, network controls, and secret boundaries.

## Topic Links

- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

## Notes

- Naively converting Cloudflare's full API into MCP tools produced roughly 1.1 million tokens from a 2.3 million-token OpenAPI spec, making whole-API eager loading impractical even for large context windows. (02:37-03:30)
- Splitting a large API into many product-specific MCP servers reduces context but pushes selection onto users and often leaves incomplete endpoint coverage. (03:45-04:47)
- MCP is presented as a protocol that can carry progressive discovery; the failure mode is dumping every tool, prompt, resource, or skill into context at once. (04:47-05:25)
- CLI self-discovery works because agents can call commands and `--help`, but it requires shell access and may not fit hosted or structured agent environments. (05:27-06:36)
- Tool search can select a small set of relevant tools for a user request, but unused selected tools still remain in context. (06:37-07:20)
- Code mode uses generated TypeScript types or SDK types from the API spec so the model can write code against a compact typed surface instead of reading every endpoint as an MCP tool schema. (07:20-09:06)
- Running generated code is a security boundary, not just an agent feature: filesystem reads, secret exfiltration, network calls, infinite loops, and resource abuse are explicit failure modes. (09:40-10:24)
- Cloudflare's dynamic worker example executes generated code in an isolated backend worker, with node compatibility, environment access, and outbound network access controlled by server-side policy. (11:15-13:00)
- Agent-written code can put pressure on APIs because loops and many sandboxes can hammer endpoints, so service providers need rate limits and abuse protection for agent callers. (17:02-17:31)
- Saved mini-scripts can turn generated one-off tool actions into reusable jobs such as scheduled scraping workflows, but the agent then needs to repair and resave brittle scripts when they fail. (19:04-19:44)
