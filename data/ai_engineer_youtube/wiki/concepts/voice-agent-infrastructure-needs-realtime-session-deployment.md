# Voice Agent Infrastructure Needs Realtime Session Deployment

Summary: Production voice agents need deployment infrastructure designed for long-running realtime media sessions, not only ordinary request/response HTTP workloads. Cold starts, autoscaling, global routing, data residency, and media transport all affect whether the agent can answer and respond inside a conversational latency budget.

Use when:
- Deploying a voice agent beyond a local prototype.
- Deciding whether ordinary container or HTTP autoscaling is enough for a realtime audio workload.

Details:
- The talk decomposes voice-agent delivery into code, deployment, and user connectivity over network or telephony, making deployment and transport first-class parts of the agent architecture. 01:32-01:50
- Voice sessions are long-running and require low-latency protocols; autoscaling is not available out of the box in the same way as common HTTP workloads. 08:23-08:49
- Cold starts matter because callers expect the agent to pick up and speak quickly; the deployment layer has to reduce start time as part of the user experience. 10:18-10:57
- Realtime voice P95 latency is much less forgiving than ordinary HTTP latency: the full voice-to-voice path should stay near the 800-1000 ms range, so every inference call and network hop has a tighter budget. 11:20-12:05
- Global deployment can be required for latency, GDPR, data residency, or other privacy constraints, and the system should place media endpoints and agent code with awareness of inference-server location. 12:07-12:32, 15:15-16:26

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Design voice agents around voice-to-voice latency budgets](design-voice-agents-around-voice-to-voice-latency-budgets.md)
- [Use WebRTC instead of WebSockets for realtime media streams](use-webrtc-instead-of-websockets-for-realtime-media-streams.md)

Sources:
- [Pipecat Cloud: Enterprise Voice Agents Built On Open Source - Kwindla Hultman Kramer, Daily](../sources/20250731_IA4lZjh9sTs.md), 01:32-01:50, 08:23-12:32, 15:15-16:26
