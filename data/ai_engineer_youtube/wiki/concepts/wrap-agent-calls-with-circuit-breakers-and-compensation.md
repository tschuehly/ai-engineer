# Wrap agent calls with circuit breakers and compensation

Summary: Multi-agent workflows should assume agent calls will fail and isolate those failures with circuit breakers, graceful degradation, and saga-style compensation for already completed steps.

Use when:
- Agents call other agents, models, APIs, or tools that may time out, rate limit, or crash.
- A partially completed workflow needs a controlled rollback path.

Details:
- Circuit breakers track call failures and move between closed, open, and half-open states. After repeated failures, the circuit opens so calls fail fast instead of repeatedly timing out or overwhelming the failing agent.
- A half-open test request can close the circuit after recovery or reopen it when the dependency is still failing.
- Circuit breakers prevent one agent failure from cascading into the entire workflow; fallback behavior can include reduced functionality, cached results, human alerts, or retrying later.
- Saga-style compensation gives each agent an `execute` path and a `compensate` path. If a later agent fails, the orchestrator walks backward through successful agents and calls their compensation methods in reverse order.
- Compensation should be planned as part of the workflow contract, especially in workflows where partial recommendations, cached data, or side effects must be undone.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Choose choreography or orchestration by complexity and autonomy](choose-choreography-or-orchestration-by-complexity-and-autonomy.md)
- [Use immutable versioned state for agent handoffs](use-immutable-versioned-state-for-agent-handoffs.md)

Sources:
- [From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work - Sandipan Bhaumik](../sources/20260408_2czYyrTzILg.md), 16:36-20:56
