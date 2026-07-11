# Standardize the Editor–Agent Boundary With a Client-Agent Protocol

Summary: Decouple editors (clients) from agents with a JSON-RPC protocol — an LSP/MCP analog for the *client↔agent* boundary — so any editor can drive any agent through one unified interface, and users can bring their agent of choice into their tool. A minimal agent implements only four methods and negotiates capabilities with the client.

Use when:
- Letting many editors/IDEs/clients work with many independently built coding agents without an N×M integration matrix.
- Deciding where the standard boundary sits when MCP already covers agent↔tools and A2A covers agent↔agent — ACP covers editor↔agent.
- Building a bring-your-own-agent surface, or making an existing CLI agent embeddable in third-party editors.

Details:
- Motivation: 2025 produced a terminal coding agent from every major provider (Claude Code, Codex, Gemini CLI); Zed defined the Agent Client Protocol (ACP) so users could bring any agent and still get one unified interface, "similar to MCP or LSP… a JSON-RPC based protocol" where agents and clients talk through a unified interface. (00:14-01:06)
- Open source (agentclientprotocol.com); ~40 clients implement it (JetBrains, Obsidian, open claw — itself both a client and an agent). Agents join via an adapter that translates the agent's native language to ACP, or a native ACP mode built into the CLI agent (opencode, cursor). (01:07-01:54)
- A minimal agent implements four interface methods: `initialize` (respond with supported protocol version + capabilities), `authenticate` (optional; skipped when the key comes from an env var), `newSession`, and `prompt`; `cancel` is a nice-to-have. (04:16-04:33, 06:33-06:46)
- Capability negotiation is the extensibility hinge: both client and agent advertise capabilities in `initialize`, and a minimal agent advertises nothing extra; richer clients advertise file-system and terminal capabilities the agent can then use. (04:37-04:57, 12:23-13:04, 15:08-16:30)
- Session lifecycle: `newSession` generates a random session ID, instantiates an agent bound to the client-provided working directory, stores it in a map, and returns the ID; `prompt` carries that session ID plus content blocks and looks the agent up — the ID is how one client thread maps to one agent instance. (05:04-06:30)
- Integration is config, not code: Zed runs an ACP agent by being told it exists and is launchable as `node <path>/agent.js`. (06:46-07:00)
- Transport is stdio today; remote transport (JetBrains) is in progress, so the same protocol can later cross process/machine boundaries. (17:51-18:03)

Related topics:
- [Tools](../topics/tools.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Stream Agent Progress to Clients as Session-Update Notifications](stream-agent-progress-to-clients-as-session-update-notifications.md)
- [Choose A2A and MCP by Ownership Boundary](choose-a2a-and-mcp-by-ownership-boundary.md)
- [Agent Clients Can Be Custom or Existing MCP Surfaces](agent-clients-can-be-custom-or-existing-mcp-surfaces.md)
- [Design Coding-Agent Editors as Review Surfaces](design-coding-agent-editors-as-review-surfaces.md)

Sources:
- [Building an ACP-Compatible Agent Live — Bennet Fenner, Zed](../sources/20260708_HsxQICTLF84.md), 00:14-07:00, 17:51-18:03
