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
- **The breaker's core assumption fails for model calls, because the dependency is replaceable.** Manuja keeps the pattern but demotes it: "tripping over a circuit breaker when you have another perfectly fine model provider to route to doesn't make sense. You should use the second model provider." A breaker exists to stop hammering a dependency you cannot substitute; with two providers behind a gateway, the right response to a failed call is a per-request fallback to provider B, and the breaker's remaining job is the slower one of parking a persistently failing primary — "take it out of the load balancer or your request path and put it in a cool down and then after a few minutes have passed, try putting that back again." He adds one design choice this page does not raise: whether the failure counts live in memory per instance or in shared fleet-wide state, where "if you want quick failovers, then fleetwide helps," but local counters mean the threshold silently changes meaning "whenever you change your deployment size." ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 02:24-04:35)

- **The same primitive applied to a budget rather than a dependency, and the reason it is not enough on its own.** Chawla and Koul's halt action is a plain breaker on spend: a run exceeded its allotted cost cap and "was killed immediately… the simple circuit breaker sort of a methodology." What they add is a second action class ahead of it — steer, which changes the run's behaviour so it fits the budget instead of tripping — with the ordering rule that in-place policies fire first and "as the last resort only a halting… should happen from a budget cap." A breaker on a failing dependency is protecting the dependency; a breaker on a budget is destroying your own work, which is why the budget case wants a graduated response and the dependency case does not. See [Steer an Over-Budget Run Before You Kill It](steer-an-over-budget-run-before-you-kill-it.md). ([FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 05:01-05:46, 14:43-15:07, 17:32-17:49)
Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Steer an Over-Budget Run Before You Kill It](steer-an-over-budget-run-before-you-kill-it.md)
- [Predict Budget Overrun From Burn Velocity, Not Consumption Alone](predict-budget-overrun-from-burn-velocity-not-consumption-alone.md)
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Choose choreography or orchestration by complexity and autonomy](choose-choreography-or-orchestration-by-complexity-and-autonomy.md)
- [Use immutable versioned state for agent handoffs](use-immutable-versioned-state-for-agent-handoffs.md)
- [Prefer Per-Request Fallback to Retries and Circuit Breakers for LLM Calls](prefer-per-request-fallback-to-retries-and-circuit-breakers-for-llm-calls.md)

Sources:
- [From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work - Sandipan Bhaumik](../sources/20260408_2czYyrTzILg.md), 16:36-20:56
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 02:24-04:35
- [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 05:01-05:46, 14:43-15:07, 17:32-17:49
