# Building Agents (the hard parts!) - Rita Kozlov, Cloudflare

Source: [Building Agents (the hard parts!) - Rita Kozlov, Cloudflare](https://www.youtube.com/watch?v=j_TKDweOsYE)
Uploaded: 2025-07-23
Transcript: `raw/20250723_j_TKDweOsYE/j_TKDweOsYE.en-orig.vtt`

## Summary

Rita Kozlov frames production agents as a four-part system of client, reasoning model, workflow coordination, and tools, then uses Cloudflare's Agents SDK, remote MCP servers, Durable Objects, WebSockets, React hooks, and human approval workflows to show where state, transport, memory, and side-effect control belong.

## Extracted Concepts

- [Compose Agents From Client, Reasoning, Workflow, and Tools](../concepts/compose-agents-from-client-reasoning-workflow-and-tools.md) - this source gives a compact architecture breakdown for agent systems.
- [Stateful Remote MCP Servers Persist Agent Memory Across Clients](../concepts/stateful-remote-mcp-servers-persist-agent-memory-across-clients.md) - this source explains how remote MCP plus Durable Objects can keep state outside any single client.
- [Defer Sensitive Tool Execution Until Approval Resumes](../concepts/defer-sensitive-tool-execution-until-approval-resumes.md) - this source demonstrates a human approval gate around a card-issuing tool call.
- [Agent Clients Can Be Custom or Existing MCP Surfaces](../concepts/agent-clients-can-be-custom-or-existing-mcp-surfaces.md) - this source clarifies the client deployment choice between existing MCP clients and custom voice or app clients.

## Topic Links

- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

## Notes

- Agent architecture is broken into client, AI reasoning, workflow execution/state, and tools; the workflow layer tracks executed and pending actions while tools may include browsers, APIs, internal services, or vector databases. 05:22-07:26
- A voice-enabled CRM agent needs modality and infrastructure pieces around the model: WebRTC, speech-to-text, chat or voice hosting, caching/eval gateway, reasoning model, workflow agent, tools, and sometimes human verification. 06:19-07:31
- MCP is presented as a client-server standard with resources, prompts, tools, and sampling; the talk notes that sampling was not something Kozlov had seen used in production MCP servers while preparing the talk. 07:44-09:49
- Cloudflare's Agents SDK can host remote MCP servers with OAuth, transport, HTTP streaming, state management, WebSocket communication, React hooks, and chat capabilities. 10:17-11:50
- Durable Objects provide attached state for serverless-style agent services, letting an MCP server persist preferences or workflow memory without a separate database setup. 11:09-13:56
- The Knock approval example wraps a card-issuing action in required human input, defers execution until approval, routes approval webhooks back to the correct durable object, resumes the paused tool call, and stores status to avoid duplicate provisioning. 14:32-18:44
- Remote MCP lets an agent service meet users through existing clients such as Cursor, Claude, and ChatGPT, while custom MCP clients can support product-specific control and voice interaction through WebRTC-to-WebSocket paths. 19:20-20:43
