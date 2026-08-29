# Fast Inference Moves the Agent Bottleneck to the Network

Summary: An agent turn is a request/response round trip plus a resend of the whole conversation. Once token generation gets fast enough, those two costs dominate and further inference optimization buys nothing. The fix is transport-level: hold a persistent connection and keep conversation state on the server so a turn ships only what changed.

Use when:
- Serving an agent on a very fast model or accelerator and finding that wall-clock time per tool call has not improved proportionally.
- Deciding whether the next optimization should target the model, the harness, or the wire.
- Designing an agent protocol where a turn currently re-sends every prior item.

Details:
- The observation came from a specific launch: GPT 5.3 Codex Spark "running on Cerebras at 1,000 tokens per second. So, with that, we realized that with all of these tool calls and the interactions, inference… no longer was the bottleneck. It was actually the network." ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 15:32-16:02)
- The precondition is agent shape, not model speed alone: "because agents can do a lot of tool calls, and while we are doing a lot of work on speeding up inference, it's only part of the equation." A one-shot completion pays the round trip once; a fifty-tool-call trajectory pays it fifty times. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 15:32-15:44)
- The response is **WebSocket mode**: "the responses API doesn't run through [server-sent] events and HTTP, but instead uses… a persistent WebSocket connection." ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 16:02-16:14)
- The connection buys two separate things and it is worth keeping them apart. Connection reuse removes per-turn setup overhead. **Stateful context** removes the resend: "we only have to send the data that actually changed. So, for example, if there's a tool call, we only send back the result of the tool call rather than sending all of the items back." In the demo that was one item per turn instead of nine. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 16:14-17:20)
- The resend cost is superlinear in trajectory length under a stateless protocol: turn *n* uploads *n* items, so a long agent run pays quadratic upload volume for a linearly growing conversation. That is why the effect shows up on agents before it shows up on chat.
- **This generalizes the split the wiki already draws for voice.** [Separate Engine Latency From Network Latency in Voice Pipelines](separate-engine-latency-from-network-latency-in-voice-pipelines.md) makes the same argument in a domain where the budget was always tight enough to force the distinction; coding agents reach it later because they were slow enough for the network to hide behind generation. The instrument transfers: measure the two independently before optimizing either.
- Note the direction this points relative to a nearby wiki page. [Use WebRTC Instead Of WebSockets For Realtime Media Streams](use-webrtc-instead-of-websockets-for-realtime-media-streams.md) argues against WebSockets for realtime *media*, where jitter and loss recovery matter; the workload here is reliable, ordered, text-shaped tool traffic, where a persistent WebSocket is the cheap win. The two are not in conflict — the transport follows the payload.
- **No measurement is offered.** The reported effect is "speeds up things quite significantly" and "a pretty drastic impact on the performance," with no latency figures, workload, or baseline; the nine-versus-one comparison is a payload item count. The live demo of this feature crashed on stage and was replaced with a pre-recorded backup. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 16:31-17:25, Provenance and Caveats)
- **Retail is a domain where paying for a high token rate has a direct revenue justification.** Prio runs his commerce demo on a Cerebras-hosted model at "3,000 tokens per second," and argues separately that "every second in retail on the shopping journey where you're actually not selling, there are chances that the other website's going to be faster, and people are just going to move away." The figure is a demo configuration rather than a measurement and no end-to-end checkout latency is reported, but it names a use case where the ceiling this page describes — the point past which further generation speed buys nothing — would be worth locating precisely. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 11:09-11:14, 18:12-18:29)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Separate Engine Latency From Network Latency in Voice Pipelines](separate-engine-latency-from-network-latency-in-voice-pipelines.md)
- [Use WebRTC Instead Of WebSockets For Realtime Media Streams](use-webrtc-instead-of-websockets-for-realtime-media-streams.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Match Agent Tooling to the Model's Training Distribution](match-agent-tooling-to-the-models-training-distribution.md)
- [Latency Shapes Coding-Agent Interaction Mode](latency-shapes-coding-agent-interaction-mode.md)
- [Eval an Agent Surface for Protocol Compliance, Not Just Behavior](eval-agent-surfaces-for-protocol-compliance-not-just-behavior.md)

Sources:
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 15:32-17:25
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 11:09-11:14, 18:12-18:29
