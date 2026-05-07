# How we hacked YC Spring 2025 batch's AI agents - Rene Brandel, Casco

Source: [How we hacked YC Spring 2025 batch's AI agents - Rene Brandel, Casco](https://www.youtube.com/watch?v=kv-QAuKWllQ)
Uploaded: 2025-07-30
Transcript: `raw/20250730_kv-QAuKWllQ/kv-QAuKWllQ.en-orig.vtt`

## Summary

Rene Brandel reports that Casco red-teamed 16 live YC Spring 2025 AI agents and found exploitable issues in seven within 30 minutes each. The durable lesson is that agent security must cover ordinary system and web-application boundaries, not only prompt injection: multi-tenant object authorization, user-scoped agent authority, sandbox isolation, service-token exposure, SSRF, and input/output sanitization all become more consequential when an LLM can select tools and operate backend infrastructure.

## Extracted Concepts

- [Treat Agents As Users For Authorization](../concepts/treat-agents-as-users-for-authorization.md) - supports user-scoped authorization, row/object access checks, and anti-IDOR design for agent tools.
- [Do Not Roll Your Own Agent Code Sandbox](../concepts/do-not-roll-your-own-agent-code-sandbox.md) - shows how limited code-tool permissions can escalate into arbitrary execution and lateral infrastructure movement.
- [Server-Side Request Forgery Exfiltrates Agent Credentials](../concepts/server-side-request-forgery-exfiltrates-agent-credentials.md) - demonstrates SSRF through a repository/schema-fetch workflow that leaked Git credentials.

## Topic Links

- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)

## Notes

- The red-team method started by extracting system prompts and tool definitions to understand whether agents could access data or run code, then probing those tools for exploitable paths. 03:20-04:12
- One agent exposed tools for user-by-ID and document-by-ID lookup; a user ID visible in a demo URL was enough to retrieve another user's personal information, and linked chat/document IDs widened traversal. 04:20-05:38
- The access-control fix is not just valid-token authentication; each object request needs authorization against the requester through an access-control matrix, row-level security, or equivalent control. 05:41-06:11
- Agents should be treated like users, not API servers: service-level permissions and LLM-decided authorization are red flags, and input/output sanitization still applies. 06:29-07:30
- Code execution tools can turn small read/write permissions into discovery of application files, removal of security checks, arbitrary code execution, service metadata probing, service-token discovery, BigQuery access, and customer-data exposure. 08:13-11:52
- The talk recommends not building custom code sandboxes; use hardened sandbox products with observability and agent-friendly integration such as MCP when code execution is needed. 11:54-12:24
- SSRF appeared when a database-agent workflow accepted a repository/schema string and sent a backend request with private Git credentials to an attacker-controlled endpoint, enabling private codebase download. 12:31-13:53
- The closing takeaways are: agent security is larger than LLM security, agents should be treated as users, and custom code sandboxes are dangerous. 14:49-15:18
