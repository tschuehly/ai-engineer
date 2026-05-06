# Decouple Agent Harnesses From Enterprise Data Layers

Summary: Gateways help separate the agent harness from the enterprise data and MCP layer so new agent surfaces can connect through a stable trust and routing boundary. This keeps decisions about in-house or external agents independent from how internal tools and data stores are structured.

Use when:
- Planning MCP architecture for many agent clients, hosted agents, internal SDK agents, or future agent surfaces.
- Avoiding tight coupling between each agent runtime and each internal MCP server or data source.

Details:
- Once a gateway exists, MCP servers can plug into new surfaces such as hosted agents, internal SDK agents, and other clients because all surfaces listen to the same gateway. (11:40-12:08)
- Without this layer, each MCP server may be configured for only one service or client, making new agent surfaces expensive and inconsistent to add. (11:54-12:08)
- The larger architecture goal is to separate the agent harness from where data lives so exploding agent surfaces are not tightly coupled to internal data and MCP structure. (15:11-15:44)
- The gateway remains stable while enterprises decide which agents stay in-house and which run outside, giving flexibility for future agent needs. (16:19-16:41)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Unified coding-agent harnesses combine models, tools, environments, and safety](unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md)
- [Stateless remote MCP servers rebuild allowed tools per request](stateless-remote-mcp-servers-rebuild-allowed-tools-per-request.md)
- [MCP gateways create an enterprise root of trust](mcp-gateways-create-an-enterprise-root-of-trust.md)

Sources:
- [Gateways are All You Need - Karan Sampath, Anthropic](../sources/20260427_CD6R4Wf3jnY.md), 11:40-16:41
