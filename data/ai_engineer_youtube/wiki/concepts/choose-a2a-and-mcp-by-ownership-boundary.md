# Choose A2A and MCP by Ownership Boundary

Summary: Use A2A when agent communication crosses remote ownership or deployment boundaries, and use MCP when agents need tool, context, or resource access across a standard integration surface. If the tools and agents are fully local to one codebase, direct function calls can be simpler, faster, and easier to debug.

Use when:
- Deciding whether a multi-agent workflow needs a protocol boundary or a local function boundary.
- Designing an agent system that mixes remote specialist agents with MCP-backed tools.

Details:
- A2A is useful as the remote interface between agents, while MCP supplies the tool-use and context-management layer behind those agents. (07:35-07:49)
- The workshop cautions against adding protocols when the function or agent is already local to the codebase: local calls have less overhead and are easier to maintain and debug. (07:52-09:07)
- Third-party tool ecosystems are a stronger reason to use MCP because they avoid building every integration as a first-class product feature. (09:08-09:24)
- A2A was described as early compared with MCP adoption, so teams should be careful about assuming production maturity where a local or MCP-only design is enough. (71:15-71:27)
- **A worked commerce example where both apply at once, at different layers.** One user turn in Prio's demo produces an A2A message from the customer agent to the merchant agent — a cross-organization boundary where neither side controls the other's process — and, beneath it, an MCP `product_search` tool call the merchant agent makes to reach its own capabilities. He also names the intra-merchant A2A case, domain agents for payments and loyalty that "need to talk to each other." The ownership-boundary rule therefore selects a *layer* rather than a winner: A2A is the envelope between parties, MCP is how each party's capabilities were named in the first place. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 07:11-08:03, 11:20-12:20)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [A2A Agent Registries Make Deployed Agents Discoverable Through Agent Cards](a2a-agent-registries-make-deployed-agents-discoverable-through-agent-cards.md)
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Design MCP servers as agent products](design-mcp-servers-as-agent-products.md)
- [Map the Agentic Commerce Protocol Stack by Layer](map-the-agentic-commerce-protocol-stack-by-layer.md)

Sources:
- [A2A & MCP Workshop: Automating Business Processes with LLMs - Damien Murphy, Bench](../sources/20250726_wXVvfFMTyzY.md), 07:35-09:24, 71:15-71:27
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 07:11-08:03, 11:20-12:20

