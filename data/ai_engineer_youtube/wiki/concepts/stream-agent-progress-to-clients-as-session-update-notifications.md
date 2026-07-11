# Stream Agent Progress to Clients as Session-Update Notifications

Summary: Surface an agent's internal loop to its UI through fire-and-forget *notifications* keyed to a session, not request/response — stream text as message chunks, announce each tool call and then update it on completion, and send edits as a diff the client renders. This makes the agent's work visible in real time without the client polling.

Use when:
- Wiring a coding agent's token stream, tool calls, and file edits into an editor/client UI (e.g., over ACP).
- Designing any agent-to-client channel where progress arrives at unpredictable times and the client must react without a matching request.
- Deciding how much rendering to push to the client versus the agent.

Details:
- Without progress events the loop is invisible: Zed's debug view showed a `session/new` request, a returned session ID, and a prompt that returned only a stop reason with no tokens — the model ran but nothing surfaced. Session updates fix this. (07:37-08:11)
- A session update is a notification associated with a session ID, "not like a usual request response… it can happen at any time and the client reacts to it." (09:11-09:34)
- Stream text with `agent_message_chunk`: react to the model SDK's text event and forward each chunk as a session update, so tokens appear in the client as they arrive from the provider. (08:17-09:38)
- Make tool calls visible in two phases: emit an initial `tool_call` update (title, kind/data used for icons, status `in_progress`, associated file locations), then on completion emit a `tool_call_update` for that call carrying the final status and returned content. The client must learn about the tool call before it can receive updates for it. (10:51-12:16)
- Push rendering work to the client via typed content: edits are sent as a diff content type — the agent sends old_text + new_text and the editor does the diffing/rendering — keeping the agent thin. (17:27-17:38)
- Route side effects through client-advertised capabilities so the UI reflects true state: reading files over the proxied file system (`read_text_file`) lets the agent see unsaved editor-buffer changes, and a client-managed terminal surfaces a live terminal + output in the UI. (12:23-13:04, 15:08-16:30)

Related topics:
- [Tools](../topics/tools.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Standardize the Editor–Agent Boundary With a Client-Agent Protocol](standardize-the-editor-agent-boundary-with-a-client-agent-protocol.md)
- [Design Coding-Agent Editors as Review Surfaces](design-coding-agent-editors-as-review-surfaces.md)
- [Group Agent Tools by Human-Facing Actions](group-agent-tools-by-human-facing-actions.md)

Sources:
- [Building an ACP-Compatible Agent Live — Bennet Fenner, Zed](../sources/20260708_HsxQICTLF84.md), 07:37-13:04, 15:08-17:38
