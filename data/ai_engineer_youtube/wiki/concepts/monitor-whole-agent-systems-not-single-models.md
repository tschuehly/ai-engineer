# Monitor Whole Agent Systems, Not Single Models

Summary: Agent evaluation and monitoring should cover the whole system that perceives, reasons, acts, and coordinates, rather than only the model inside one agent. Autonomy moves risk from isolated model output into action loops, tool use, virtual environments, cyber-physical systems, and multi-agent interactions.

Use when:
- Moving from a single-model AI feature to an autonomous or semi-autonomous agent deployment.
- Designing observability for multi-agent systems.

Details:
- Dickerson defines deployed agents as systems that perceive, learn, abstract, reason, and act in virtual or cyber-physical environments, which adds complexity and risk beyond traditional ML outputs. 11:38-12:03
- Agentic systems are starting to make decisions and take action through complex autonomous or semi-autonomous steps, making evaluation more urgent than when ML predictions were merely inputs to larger systems. 02:55-04:14
- Evaluation, observability, monitoring, and security vendors are shifting toward multi-agent systems monitoring because teams need to observe the whole system, not only one model used by one agent. 14:49-15:09
- **Whole-system monitoring still has a granularity trap, and aggregates are where it hides.** Manuja's version is about latency: a system serving embeddings, classification, chat, and reasoning has no meaningful service-wide number — "it doesn't make sense. It's a lie. You should be tracking your P99 per model per route" — because "a reasoning model's normal is actually a chat model's outage." The general lesson for agent-system observability is that widening the scope of what you monitor and coarsening the unit you aggregate over are opposite moves, and the second silently undoes the first. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 06:54-08:16)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Treat agents as embodied action systems](treat-agents-as-embodied-action-systems.md)
- [Apply Online Scoring to Production Traces With Cost-Aware Sampling](apply-online-scoring-to-production-traces-with-cost-aware-sampling.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)

Sources:
- [2025 is the Year of Evals! Just like 2024, and 2023, and ... - John Dickerson, CEO Mozilla AI](../sources/20250806_CQGuvf6gSrM.md), 02:55-04:14, 11:38-12:03, 14:49-15:09
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 06:54-08:16
