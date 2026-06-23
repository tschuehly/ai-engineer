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

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Render Third-Party Generative UI Through a Double Iframe](render-third-party-generative-ui-through-a-double-iframe.md)
- [Declare Every External Domain Your MCP App Touches](declare-every-external-domain-your-mcp-app-touches.md)
- [Agent Experience Prioritizes APIs, CLIs, and MCP Over Dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Collaborate with Complex Agents Through High-Bandwidth Artifacts](collaborate-with-complex-agents-through-high-bandwidth-artifacts.md)
- [Agent Tool Loops Turn Model-Required Actions Into Executable Results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)

Sources:
- [The Future of MCP - David Soria Parra, Anthropic](../sources/20260419_v3Fr2JR47KA.md), 00:22-01:32, 16:16-16:32
- [Why MCP and ChatGPT Apps Use Double Iframes — Frédéric Barthelet, Alpic](../sources/20260615_c-2eEv2ou7Y.md), 01:43-13:39
