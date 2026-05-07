# Use Browser UI Control When APIs Are Absent

Summary: Browser-based computer use is a practical agent tool surface when useful websites expose visual interfaces but no suitable APIs. It trades clean machine contracts for broad reach, so reliability work shifts into UI perception, action grounding, and workflow-level guardrails.

Use when:
- A target workflow spans websites or tools that do not expose enough API coverage.
- Comparing API, MCP, CLI, and browser-control surfaces for an agent product.

Details:
- Perszyk says the future atomic unit of digital interaction may be an agent call, but the obstacle is that most infrastructure still assumes APIs while many websites are built for visual UIs. (07:48-08:09)
- Nova Act is presented as a specialized Amazon Nova computer-use model plus SDK where an `act` call translates natural language into screen actions. (08:09-08:31)
- The talk notes that current models still cannot reliably click, type, and scroll, making UI-control reliability a prerequisite before broad computer-use agents can be trusted. (03:17-03:27)
- Browser control complements, rather than replaces, machine-readable APIs and CLIs: it reaches existing human-facing workflows but inherits visual ambiguity, latency, and safety constraints. (08:00-08:31)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Choose agent observation and action spaces explicitly](choose-agent-observation-and-action-spaces-explicitly.md)

Sources:
- [Useful General Intelligence - Danielle Perszyk, Amazon AGI](../sources/20250802_Dj0b_cEBHBI.md), 03:17-03:27, 07:48-08:31
