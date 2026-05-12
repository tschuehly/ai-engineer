# Stateful Remote MCP Servers Persist Agent Memory Across Clients

Summary: Remote MCP servers can hold user or workflow state outside any single chat client, letting multiple clients call the same agent-facing service while sharing durable memory.

Use when:
- Building an MCP server that should work from Cursor, Claude, ChatGPT, a custom app, or a voice client.
- Deciding where personalization, preferences, or workflow state should live in an agent integration.

Details:
- The talk describes MCP as a client-server architecture where multiple clients can connect to one server, with resources, prompts, tools, and sampling as server-side concepts. 07:44-09:49
- Cloudflare's Agents SDK is presented as a remote MCP hosting path with OAuth, transport, HTTP streaming, state management, WebSocket communication, React hooks, and chat capabilities. 10:17-11:50
- Durable Objects are described as serverless functions with attached state, allowing an MCP server to persist preferences such as liked book genres without separately managing a database connection. 11:09-13:56
- Because the MCP server is standalone, memory persists regardless of which client calls it; the same service can be reached from developer tools, general chat clients, custom apps, or voice paths. 13:16-13:29, 19:20-20:43

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [MCP Gateways Create an Enterprise Root of Trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Deploy Remote MCP Servers on Serverless Cloud Infrastructure](deploy-remote-mcp-servers-on-serverless-cloud-infrastructure.md)
- [Server-side interaction state simplifies branching conversational agents](server-side-interaction-state-simplifies-branching-conversational-agents.md)

Sources:
- [Building Agents (the hard parts!) - Rita Kozlov, Cloudflare](../sources/20250723_j_TKDweOsYE.md), 07:44-13:56, 19:20-20:43
