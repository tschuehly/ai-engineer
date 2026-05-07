# Keep Voice Agents Conversational During Long Tool Latency

Summary: Voice agents that call slow enterprise systems should make waiting audible and bounded instead of leaving dead air. Tool timeouts, spoken status updates, and queue-based handoffs preserve trust when retrieval, databases, or downstream systems cannot return inside normal conversational timing.

Use when:
- A voice agent calls RAG, databases, claims systems, or other slow tools.
- Designing UX for unavoidable latency during a live voice call.

Details:
- The workshop warns that simple demos hide enterprise latency: RAG, databases, and chained systems can make an end user hear silence while the agent waits. 39:07-40:19
- Tool configuration can choose whether to wait for a tool response, with an allowed timeout; while waiting, the agent can say that it is looking something up or still waiting for a response. 40:19-41:32
- The speaker suggests keeping timeout thresholds fairly low for live calls, because long synchronous waits harm the spoken experience even if the backend eventually succeeds. 41:38-42:12
- For work that cannot finish inside the conversation, a queue plus later context injection through websocket events is proposed as a possible orchestration shape, but the speaker marks this as a use-case-specific pattern to verify rather than a confirmed default. 42:15-43:39

Related topics:
- [Voice Agents](../topics/voice-agents.md)

Related concepts:
- [Design Voice Agents Around Voice-To-Voice Latency Budgets](design-voice-agents-around-voice-to-voice-latency-budgets.md)
- [Delegate Complex Voice-Agent Tasks Through Specialist Tools and Handoffs](delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md)

Sources:
- [[Full Workshop] Building Conversational AI Agents - Thor Schaeff, ElevenLabs](../sources/20250731_MPtCBaZn84A.md), 39:07-43:39
