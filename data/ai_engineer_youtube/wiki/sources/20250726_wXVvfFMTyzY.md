# A2A & MCP Workshop: Automating Business Processes with LLMs - Damien Murphy, Bench

Source: [A2A & MCP Workshop: Automating Business Processes with LLMs - Damien Murphy, Bench](https://www.youtube.com/watch?v=wXVvfFMTyzY)
Uploaded: 2025-07-26
Transcript: `raw/20250726_wXVvfFMTyzY/wXVvfFMTyzY.en-orig.vtt`

## Summary

Damien Murphy's workshop frames A2A as a remote agent-to-agent interface and MCP as the tool, context, and resource surface behind agents, then demonstrates a webhook-driven business workflow where a host agent slices event context into smaller tasks for specialist agents backed by MCP integrations.

## Extracted Concepts

- [Choose A2A and MCP by Ownership Boundary](../concepts/choose-a2a-and-mcp-by-ownership-boundary.md) - This source distinguishes local function calls from protocolized remote agent and tool boundaries.
- [Turn Webhooks Into Host-Agent Task Delegation](../concepts/turn-webhooks-into-host-agent-task-delegation.md) - This source shows webhook processing as an orchestrated host-agent flow that delegates compact tasks to specialist agents.
- [Harden Third-Party MCP Tools Against Silent Failure and Endpoint Risk](../concepts/harden-third-party-mcp-tools-against-silent-failure-and-endpoint-risk.md) - This source identifies MCP integration failure modes and security controls needed around remote tools.

## Topic Links

- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- A2A is presented as a protocol for agents communicating over the web, while MCP gives agents access to context, tools, and resources; combining them lets A2A provide the remote interface and MCP provide tool use and context management. (01:47-02:19, 07:35-07:49)
- The workshop cautions that when tools or agents are fully owned inside the same codebase, direct local function calls are faster, easier to maintain, easier to debug, and avoid protocol overhead. (07:52-09:07)
- Third-party tools are the main reason to use MCP, because MCP can provide access to a broad external tool ecosystem that a product team may not want to implement as first-class integrations. (09:08-09:24)
- The demo uses a webhook trigger, a host agent, and specialist agents; the host processes the source event and sends compact tasks such as creating a GitHub issue rather than forwarding the whole transcript to every subagent. (02:22-02:35, 54:35-56:05)
- The Slack MCP example exposed a silent failure mode: a missing default Slack channel yielded an apparently successful result with empty content, so wrapper code had to detect the empty response and fail explicitly. (18:04-18:49)
- For regulated environments, remote MCP servers or A2A agents need controls beyond the protocols themselves, such as provider agreements, HTTPS, mutual TLS, IP allowlisting, endpoint controls, and private VPC deployment when applicable. (49:53-51:16)
