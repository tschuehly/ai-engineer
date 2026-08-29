# MCP Applications Ship UI and Tools Together

Summary: MCP applications extend MCP beyond tool calls by letting a server provide a reusable interface that clients can render while also exposing tools for the model to operate against that same application.

Use when:
- Designing an agent-facing product surface that should work across multiple clients without hardcoding UI into each client.
- Separating human interaction with an application from model interaction through tools while keeping both served by the same MCP server.

Details:
- The talk opens with an MCP application: a server-shipped interface that is not a plugin, SDK, client-side model-rendered UI, or hardcoded product screen. (00:22-00:47)
- Because the interface and tools come from the MCP server, the same server can be put into different clients such as Claude, ChatGPT, VS Code, or Cursor while preserving shared semantics. (00:38-01:13)
- MCP applications let a human interact with a rendered interface while the model interacts with the associated tools, a dual surface the speaker says the ecosystem has not explored much yet. (01:15-01:32)
- MCP applications depend on client support; the talk notes that web-based interfaces are natural targets because command-line clients cannot easily render HTML. (16:16-16:32)
- The UI half is delivered as "views": small HTML/JS/CSS snippets always rendered as the result of a tool call. Tools carry metadata indicating which view fits their output, views are advertised ahead of time on the `tools/list` call at conversation start, the host caches or fetches the resource on demand, and the host injects tool results into the rendered frame as dynamic content. ([Barthelet/Alpic] 02:02-03:31)
- The standard lineage: MCP UI was developed first (Leat and Ido), released by OpenAI as the Apps SDK in October 2025, then standardized across clients as the first official MCP extension, the "app extension." ([Barthelet/Alpic] 01:43-02:02)
- Hosts render those views inside an isolated nested iframe rather than directly, which is what keeps third-party app code away from the host's origin and storage. See [Render Third-Party Generative UI Through a Double Iframe](render-third-party-generative-ui-through-a-double-iframe.md). ([Barthelet/Alpic] 03:31-13:39)
- The concrete runtime data flow (GitHub/Microsoft framing for VS Code + Copilot): user prompts → the LLM decides which tool to call via the MCP server → the server returns the tool result *with a UI resource reference* (an MCP resource pointing to bundled HTML the server generated) → the host fetches that HTML → renders it in a sandboxed iframe → the app calls back and forth to the server so fresh data updates the UI live. ([GitHub] 05:15-06:33)
- The host renders, not the client: in VS Code the host (VS Code) fetches the HTML and renders the iframe, "not the client, it wouldn't be GitHub Copilot" — a useful role split because the same MCP app can ship to any host while the client only brokers tool calls. ([GitHub] 05:53-06:11)
- The sandbox is a security boundary, not styling: the iframe exists "the same reason you put a hamster in a cage" — to stop the app from touching the host's settings, external APIs, or anything outside the chat window. ([GitHub] 14:48-15:10)
- Adopters span commerce and design surfaces: Shopify renders in-chat checkout that preserves its on-site brand experience, Excalidraw renders interactive architecture diagrams (and Claude Code uses its MCP app), and Figma generates components on the fly. ([GitHub] 08:10-09:30)
- Independent confirmation of the lineage and mechanics (Manufact/`mcp-use`): MCP UI began ~May 2025 (Manufact co-founder Ido Solomon), OpenAI shipped the Apps SDK, and in January 2026 MCP UI converged into MCP Apps as "the official extension of the Model Context Protocol" for returning UI; the tool returns a `ui://` widget in a sandboxed iframe, declared at initialization and populated with the tool's arguments, with a bidirectional channel back to the host. ([Zullo] 03:00-07:32)
- Beyond the initial render, the App is a stateful two-way interaction layer with a distinct set of primitives — see [Use MCP App Primitives for Bidirectional Model–UI State](use-mcp-app-primitives-for-bidirectional-model-ui-state.md); and store submission plus dynamic discovery make it a distribution channel — see [Distribute MCP Apps Through Stores and Dynamic Discovery](distribute-mcp-apps-through-stores-and-dynamic-discovery.md). ([Zullo] 06:01-26:07)
- **What server authors did before interaction primitives were dependable.** Figma wanted elicitation to ask the user for permission to map their codebase, and "most of the clients didn't implement these features," so the interaction was faked through tool results: return a prompt asking the user, and on yes return another prompt directing the agent to do the work. The user experience the team wanted — a consent step with a typed answer — was reconstructed out of strings the agent might reword or answer on the user's behalf, which is the gap a real UI primitive closes. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 10:16-12:03)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Render Third-Party Generative UI Through a Double Iframe](render-third-party-generative-ui-through-a-double-iframe.md)
- [Declare Every External Domain Your MCP App Touches](declare-every-external-domain-your-mcp-app-touches.md)
- [Use MCP App Primitives for Bidirectional Model–UI State](use-mcp-app-primitives-for-bidirectional-model-ui-state.md)
- [Distribute MCP Apps Through Stores and Dynamic Discovery](distribute-mcp-apps-through-stores-and-dynamic-discovery.md)
- [Scaffold MCP Apps From a Repo Skill With a Coding Agent](scaffold-mcp-apps-from-a-repo-skill-with-a-coding-agent.md)
- [Agent Experience Prioritizes APIs, CLIs, and MCP Over Dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Collaborate with Complex Agents Through High-Bandwidth Artifacts](collaborate-with-complex-agents-through-high-bandwidth-artifacts.md)
- [Agent Tool Loops Turn Model-Required Actions Into Executable Results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Tools Are the Only Primitive Every Client Implements](tools-are-the-only-primitive-every-client-implements.md)

Sources:
- [The Future of MCP - David Soria Parra, Anthropic](../sources/20260419_v3Fr2JR47KA.md), 00:22-01:32, 16:16-16:32
- [Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic](../sources/20260615_c-2eEv2ou7Y.md), 01:43-13:39
- [Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub](../sources/20260606__xIwFcnHqp4.md), 05:15-15:10
- [MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc](../sources/20260705_sAOBXCDiDOs.md), 03:00-26:07
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 10:16-12:03
