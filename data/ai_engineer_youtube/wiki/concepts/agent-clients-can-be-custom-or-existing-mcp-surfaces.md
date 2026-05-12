# Agent Clients Can Be Custom or Existing MCP Surfaces

Summary: Agent products do not always need a bespoke UI first; a remote MCP server can meet users through existing MCP-capable clients, while custom clients are useful when the product needs tighter control over modality, workflow, or UX.

Use when:
- Deciding whether to ship an agent through existing tools such as Cursor, Claude, ChatGPT, or a custom application.
- Planning client surfaces for voice, chat, or product-specific agent workflows.

Details:
- Kozlov argues that after building an MCP server once, teams can meet users where they already work; Cursor, Claude, and ChatGPT are named as clients that can connect to remote MCP servers. 19:20-20:03
- A custom app and MCP client become useful when the builder wants more control over both client and server behavior, including voice interaction through WebRTC-to-WebSocket translation. 20:03-20:43
- This client/server split makes the agent interface a deployment choice rather than a single mandatory chat UI. 19:20-20:43

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md)

Sources:
- [Building Agents (the hard parts!) - Rita Kozlov, Cloudflare](../sources/20250723_j_TKDweOsYE.md), 19:20-20:43
