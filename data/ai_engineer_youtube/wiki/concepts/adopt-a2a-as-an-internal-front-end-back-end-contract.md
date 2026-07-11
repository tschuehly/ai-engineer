# Adopt A2A's Spec as an Internal Front-End/Back-End Contract

Summary: You can adopt Google's A2A (agent-to-agent) protocol spec — agent cards and agent routes — as the internal API contract between your own front-end and back-end, even when there is no cross-organization boundary, because a rigorous shared spec drives development alignment: both sides just align to the one contract they each consume and produce.

Use when:
- Building an agent product where your own front-end and back-end must agree on agent routing, capabilities, and message shape.
- Deciding whether to invent an internal API shape or reuse an existing open agent protocol as the contract.
- You want a spec rigorous enough to drive alignment across teams without designing one from scratch.

Details:
- OpenGov modeled its back-end agent routes, model, and schema to follow the A2A protocol, using the agent card (name, description, etc.) as the contract that the front-end and back-end both consume and produce. ([Gabe De Mesa](../sources/20260626_4uFVSLgD2Q4.md), 07:46-08:49)
- The cited payoff is alignment, not interop: "having this kind of rigorous protocol, this rigorous spec really helped drive our development and drive alignment because all we had to do was align with this spec and follow this spec." ([Gabe De Mesa](../sources/20260626_4uFVSLgD2Q4.md), 08:24-08:49)
- A2A supports extensions (add metadata) and A2UI, so the protocol can grow with product needs while staying a single shared contract. ([Gabe De Mesa](../sources/20260626_4uFVSLgD2Q4.md), 08:52-09:13)
- This qualifies the usual ownership-boundary heuristic: A2A is normally recommended for communication that crosses remote ownership boundaries, but here it is adopted internally purely for spec discipline between two components the same team owns.
- Context: OG Assist's loop is otherwise self-owned (an Effect-native loop after migrating off LangGraph), so A2A here is the interface contract, not the runtime. ([Gabe De Mesa](../sources/20260626_4uFVSLgD2Q4.md), 05:50-06:22)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Choose A2A and MCP by Ownership Boundary](choose-a2a-and-mcp-by-ownership-boundary.md)
- [A2A Agent Registries Make Deployed Agents Discoverable Through Agent Cards](a2a-agent-registries-make-deployed-agents-discoverable-through-agent-cards.md)
- [Own the Agent Loop on a Typed Effects Runtime](own-the-agent-loop-on-a-typed-effects-runtime.md)

Sources:
- [Agents in Production: How OpenGov Built and Scaled OG Assist - Gabe De Mesa, OpenGov](../sources/20260626_4uFVSLgD2Q4.md), 07:46-09:13
