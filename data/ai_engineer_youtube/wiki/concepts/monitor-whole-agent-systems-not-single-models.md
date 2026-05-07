# Monitor Whole Agent Systems, Not Single Models

Summary: Agent evaluation and monitoring should cover the whole system that perceives, reasons, acts, and coordinates, rather than only the model inside one agent. Autonomy moves risk from isolated model output into action loops, tool use, virtual environments, cyber-physical systems, and multi-agent interactions.

Use when:
- Moving from a single-model AI feature to an autonomous or semi-autonomous agent deployment.
- Designing observability for multi-agent systems.

Details:
- Dickerson defines deployed agents as systems that perceive, learn, abstract, reason, and act in virtual or cyber-physical environments, which adds complexity and risk beyond traditional ML outputs. 11:38-12:03
- Agentic systems are starting to make decisions and take action through complex autonomous or semi-autonomous steps, making evaluation more urgent than when ML predictions were merely inputs to larger systems. 02:55-04:14
- Evaluation, observability, monitoring, and security vendors are shifting toward multi-agent systems monitoring because teams need to observe the whole system, not only one model used by one agent. 14:49-15:09

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Treat agents as embodied action systems](treat-agents-as-embodied-action-systems.md)
- [Apply Online Scoring to Production Traces With Cost-Aware Sampling](apply-online-scoring-to-production-traces-with-cost-aware-sampling.md)

Sources:
- [2025 is the Year of Evals! Just like 2024, and 2023, and ... - John Dickerson, CEO Mozilla AI](../sources/20250806_CQGuvf6gSrM.md), 02:55-04:14, 11:38-12:03, 14:49-15:09
