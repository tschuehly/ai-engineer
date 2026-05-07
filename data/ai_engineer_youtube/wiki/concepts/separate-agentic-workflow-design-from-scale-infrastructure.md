# Separate Agentic Workflow Design From Scale Infrastructure

Summary: Agentic platforms benefit from separating the intelligent workflow graph from the distributed system that runs it at enterprise scale.

Use when:
- Building AI features that must handle both one hard item and very large content volumes.
- Deciding whether to evolve a brittle pipeline by adding more deterministic patches or by introducing agentic orchestration.

Details:
- Box frames the agentic abstraction as a directed graph of instructions, objectives, model background, tools, secure access, memory, and orchestrated steps.
- The same feature still needs ordinary scale engineering for large content volumes, but that should be kept distinct from the team and design surface that owns the agentic framework.
- This separation made the workflow easier to evolve: adding a prompt, a final summarization step, or another verification node could address a new failure without redesigning the whole product pipeline.
- The pattern is not "make everything agentic"; it is to introduce an agentic architecture early when a task plausibly needs a set of AI models to reason, check, and iterate over a difficult workflow.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Choose choreography or orchestration by complexity and autonomy](choose-choreography-or-orchestration-by-complexity-and-autonomy.md)
- [Stage complex AI applications into inspectable deterministic and agentic steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)

Sources:
- [Building an Agentic Platform - Ben Kus, CTO Box](../sources/20250824_12v5S1n1eOY.md), 09:27-10:18, 14:14-16:24
