# Build an Agentic Control Plane So the Model Proposes and the Platform Decides

Summary: A probabilistic model should never directly control production systems. Insert a deterministic control plane between the model and production — the model generates proposals, infrastructure validates them, a policy engine approves them, and an execution gateway enforces them — so reliability holds even when the underlying model stays stochastic.

Use when:
- Moving an agent from a demo that showcases capability to a production system that must act reliably, safely, and cost-bounded at scale.
- Deciding what layer owns scheduling, memory coordination, policy enforcement, evaluation, monitoring, and workload routing for autonomous agents.
- An agent has (or is about to get) direct authority to mutate production state, and you need a place to put validation, approval, and enforcement.

Details:
- The failure this prevents is "the great mismatch": autonomous agents are stateful, long-running, decide dynamically, and may run different workflows for the same input, so running them on infrastructure designed for short-lived deterministic microservices lets a single model mistake become an outage.
- The separation: "the model just suggests, the platform decides." The model emits proposals; infrastructure validates them; a policy engine approves them; an execution gateway enforces them. Because enforcement is deterministic, the system can be reliable even though the model is not — "never let the model directly control production systems."
- The control plane is the emerging analog to Kubernetes (for containers) and service meshes (for microservices) — an "operating system for autonomous AI" that owns scheduling, memory coordination, policy enforcement, evaluation, monitoring, and workload routing. Organizations that build this layer gain a durable competitive advantage.
- The stance reflects a phase shift: prompts were the differentiator, then models, and both are commoditizing; "the next frontier is infrastructure," and "the organization that wins is not necessarily the one with the best prompts — they'll have the most reliable systems."
- This is the architecture home for the topic's other reliability primitives: layered defense-in-depth safety (prompt controls, tool permissions, policy validation, human approval, audit), humans as permanent exception handlers who get attention allocated where it adds the most value, and multi-dimensional observability that traces planning decisions, tool calls, memory lookups, and state transitions to explain *why*, not just *what*, happened.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Contain Retry Amplification Before It Becomes a Compute Incident](contain-retry-amplification-in-agent-loops.md)
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Keep Human Review on High-Risk Agent Operations](keep-human-review-on-high-risk-agent-operations.md)
- [LLM guardrails need checkpoints at every untrusted boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Make the LLM Gateway the Agent Observability Chokepoint](make-the-llm-gateway-the-agent-observability-chokepoint.md)

Sources:
- [Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs](../sources/20260629_APh1Vx0oLmQ.md), 03:08-03:55
