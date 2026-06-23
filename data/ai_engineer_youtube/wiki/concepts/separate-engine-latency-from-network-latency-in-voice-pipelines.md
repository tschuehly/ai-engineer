# Separate Engine Latency From Network Latency in Voice Pipelines

Summary: A voice agent's latency is the sum of engine latency (model compute) and network latency (data-center hops between the orchestrator and the models). These are separate budgets, and once engine latency is already optimized the dominant remaining win is often co-locating every model and the orchestrator so cross-region hops collapse.

Use when:
- A voice pipeline already hits good per-model engine latency but voice-to-voice time is still too high.
- Deciding where to host STT, the LLM, TTS, and the agent orchestrator relative to each other and to callers.
- Comparing a hosted third-party model API against a self-hosted open model for a latency-critical voice product.

Details:
- The latency you measure on a model ("how long the model takes to produce output") is only *engine* latency; when models sit in different data centers, *network* latency stacks on top and must be budgeted separately. (11:32-11:55)
- In an already-optimized pipeline (STT/LLM/TTS each at ~100-200 ms engine time-to-first-token/audio), models far from the agent orchestrator can add ~75 ms of network latency — and 75 ms is easy to incur (roughly US West↔Europe, and higher with worse networking). (13:06-13:33)
- Co-locating all models and ideally the orchestrator in the same data center, or literally the same building, drops that ~75 ms to ~5 ms — a ~30% latency reduction on top of an already-optimized setup, because every 10 ms matters in real-time voice. (13:33-14:24)
- Concrete failure case: a London voice agent that calls OpenAI's LLM hosted in the US pays a trans-Atlantic round trip per turn; running an open-source model in the same data center as the agent turns that into an intra-data-center hop. (17:50-19:18)
- This is also the latency rationale for self-hosting an open model on an AI-native cloud (Together AI here) rather than calling a distant managed API: distance alone "has that big of an impact." (18:29-19:18)
- Pairs with global deployment for residency: place media endpoints and agent code near callers (and within GDPR/data-residency regions) while keeping models close to the orchestrator. (12:07-12:40)

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Design voice agents around voice-to-voice latency budgets](design-voice-agents-around-voice-to-voice-latency-budgets.md)
- [Size the Voice-Agent LLM to the Time-to-First-Token Budget](size-the-voice-agent-llm-to-the-time-to-first-token-budget.md)
- [Voice Agent Infrastructure Needs Realtime Session Deployment](voice-agent-infrastructure-needs-realtime-session-deployment.md)

Sources:
- [Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI](../sources/20260531_N7b1PJc7SFc.md), 11:32-14:24, 17:50-19:18
