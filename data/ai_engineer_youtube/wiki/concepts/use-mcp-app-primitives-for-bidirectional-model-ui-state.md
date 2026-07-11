# Use MCP App Primitives for Bidirectional Model–UI State

Summary: An MCP App is a full interaction layer, not "an MCP server with a UI bolted on": beyond the initial widget render, a set of primitives keeps the model and the rendered UI in sync bidirectionally — the widget can push its state into the model's context, message the conversation, call other tools, receive streamed tool arguments live, and return a separate redacted output to the model.

Use when:
- Designing an MCP App where the user acts on a rendered widget and the model needs to stay aware of, or respond to, those actions.
- Deciding how much of a tool's data reaches the model vs the human, especially with privacy-sensitive information.
- Choosing an interaction pattern (streaming render, in-widget follow-ups, in-widget tool calls) rather than a static tool-result card.

Details:
- Baseline architecture: the host owns the model and tools; the server's tool returns a widget in a sandboxed iframe rather than JSON. The `ui://` UI resource is declared at initialization; when the model populates the tool arguments the tool populates the UI resource's arguments, which the client renders, and a postMessage-style channel carries messages both ways. (06:01-07:32)
- Primitive — **set state / update-model-context**: the model can't introspect live UI state, so the protocol has a set-state primitive; from the widget you call `setState` (shown here in `mcp-use` syntax) to update what the model knows about what's displayed (e.g. which article is selected) *without* a user message. (08:34-10:00)
- Primitive — **UI message / follow-up**: the widget can send a message back into the conversation unprompted, e.g. a "learn more" button wired to `sendFollowUpMessage`. Client behavior differs: Claude prefills the chat input and lets the user choose to send; OpenAI sends it to the model directly and streams the answer immediately. (10:01-11:15)
- Primitive — **stream partial tool args into the UI**: as the model streams input tokens into the tool arguments, take the partial input live and update the UI incrementally. The showcase demos use this — Excalidraw MCP streams mermaid syntax into a canvas that draws as tokens arrive, and Manufact's Remotion MCP app renders a React video inside the widget in real time. (11:17-12:24, 16:56-18:05)
- Primitive — **widget calls other tools**: from the widget you can trigger additional tool calls (e.g. a button that fetches more data from the server) beyond the tool that originally rendered it. (12:24-13:03)
- Primitive — **dual output for privacy**: an MCP tool returns a list of outputs; send a structured output into the widget and a *separate* output (or nothing) to the model. Common pattern: show full private info in a rich UI card but tell the model only "the user is seeing their private information in the widget above," enabling agent UX in fields where sharing raw data with the model provider is disallowed. (13:03-15:23)
- Minor display primitives round out the layer: inline vs full-screen display mode (chat input overlaid on the widget, good for video editing where the model streams into the widget you're watching), picture-in-picture, opening external links from the widget, and listening to the host/OS theme so the app matches. (15:23-16:36)
- Client capability differs and is discoverable: because the client is known from exchanged metadata, a server can return a widget only for hosts that can render it and a different model-facing output otherwise; non-supporting clients simply don't show the widget, but you often must supply an alternative output when it isn't shown. (18:35-20:30)

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [MCP Applications Ship UI and Tools Together](mcp-applications-ship-ui-and-tools-together.md)
- [Distribute MCP Apps Through Stores and Dynamic Discovery](distribute-mcp-apps-through-stores-and-dynamic-discovery.md)
- [Render Third-Party Generative UI Through a Double Iframe](render-third-party-generative-ui-through-a-double-iframe.md)
- [Scaffold MCP Apps From a Repo Skill With a Coding Agent](scaffold-mcp-apps-from-a-repo-skill-with-a-coding-agent.md)

Sources:
- [MCP Apps: Primitives, discovery, and the Future of Software - Pietro Zullo, Manufact, Inc](../sources/20260705_sAOBXCDiDOs.md), 06:01-20:30
