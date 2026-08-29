# Steer an Over-Budget Run Before You Kill It

Summary: Budget enforcement has two action flavors — halt, which kills the run, and steer, which changes the run's behaviour so it fits inside the budget — and the ordering matters more than the mechanism: exhaust the in-place steering policies first, and treat the cap as the last resort. A control that can only halt converts every budget overrun into a failed run.

Use when:
- Writing the enforcement half of a cost, context, or time budget for an agent.
- A spend control is already in place and the complaint is that runs die instead of finishing cheaper.
- Deciding what a policy engine is allowed to do to a running agent beyond stopping it.
- Reviewing a cost intervention whose only reported outcome is money saved.

Details:
- **The two flavors, as stated.** "On the actions part we have broadly two flavors. First is the halt type actions which basically just kill your agent if it exceeds a budget. The second part where we are adding value is the steer type actions. So here we do not kill the agent. Instead we try to steer the behavior of the agent or the components of the agent to try and fit that particular run within the alerted budget." ([Chawla & Koul](../sources/20260822_GJX19pNhmSw.md), 14:43-15:07)
- **The ordering rule is the durable part.** From the first-principles section: when a loop is running excessively or "your context is growing very out of range… you should have in place policies which can solve that particular thing there and there instead of halting," and "as the last resort only a halting… should happen from a budget cap." The architectural form is "enforcement actually happens in call path" with "in place compaction… or in place caching" firing before the cap. (05:01-05:46, 07:05-08:01)
- **What a steer action concretely is.** Three verbs are named — "allow, mutate, inject" — against halt's "simple kill." The demonstrated instance is an injection into the system instructions when overrun is predicted: "hey you're running out of budget so make sure that the LM outputs are more succinct or more summarized." The illustrative instance is a mutation of a tool result: a retrieval tool returning 20 chunks where the model "is not even using the chunks that are after five," so the control plane pushes down an action limiting the output to five. (12:52-13:22, 18:17-18:39, 19:49-19:58)
- **The policy catalog shows what "steer" spans in practice**, and it is broader than spend: spend management, context management (context compaction, tool-output reduction), and loop and progress detection, assembled from "what are the different failure modes that are there today out in the wild." Compaction appears here as an action a *budget* triggers rather than a token threshold — see [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md). (19:26-19:49)
- **Steering is a quality intervention wearing a cost intervention's clothes, and that is its real risk.** "Make outputs more succinct" changes what the agent produces, and the talk measures only whether runs completed. A halt is honest about its failure; a steer degrades silently, and a run that finishes under budget with a thinner answer scores as a success on every metric reported. Pair any steering policy with an output-quality measure before trusting the completion uplift — see [A Cost Control Must Report Completion Rate or It Is Just Throttling](a-cost-control-must-report-completion-rate-or-it-is-just-throttling.md) and [Measure Agent Interface Efficiency With Tokens Per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md).
- **Where this sits against the wiki's containment pages.** Circuit breakers, resource quotas, and output-cardinality caps are all halt-family: they bound the blast radius and accept the dead run. Steering is the missing complement, and it needs something none of those need — a channel back into the running agent, which is why it forces the instrumentation decision in [Make the Instrumentation Boundary Two-Way and Gate It With a Governor](make-the-instrumentation-boundary-two-way-and-gate-it-with-a-governor.md). Halt remains necessary: the demo's own scenario 2 is a plain kill on a cost cap, described as "the simple circuit breaker sort of a methodology." (17:32-17:49)
- **Caveat.** Vendor-reported, single system, no case shown where steering failed or made a run worse. The stated benchmark uplift (completion from 67% to roughly 96% against simple throttling) is the only evidence offered that ordering steer before halt pays, and it carries no quality term.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Agentic Workloads Turn Token Price Into Unit-Economics Pressure](agentic-workloads-turn-token-price-into-unit-economics-pressure.md)
- [Ship Enforcement Policies in Preview Mode Before Enabling Them](ship-enforcement-policies-in-preview-mode-before-enabling-them.md)
- [Put the Cost Control at the Agent Run, Not the Model Request](put-the-cost-control-at-the-agent-run-not-the-model-request.md)
- [A Cost Control Must Report Completion Rate or It Is Just Throttling](a-cost-control-must-report-completion-rate-or-it-is-just-throttling.md)
- [Predict Budget Overrun From Burn Velocity, Not Consumption Alone](predict-budget-overrun-from-burn-velocity-not-consumption-alone.md)
- [Make the Instrumentation Boundary Two-Way and Gate It With a Governor](make-the-instrumentation-boundary-two-way-and-gate-it-with-a-governor.md)
- [Contain Retry Amplification Before It Becomes a Compute Incident](contain-retry-amplification-in-agent-loops.md)
- [Wrap agent calls with circuit breakers and compensation](wrap-agent-calls-with-circuit-breakers-and-compensation.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)
- [Build an Agentic Control Plane So the Model Proposes and the Platform Decides](build-an-agentic-control-plane.md)
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)

Sources:
- [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 05:01-05:46, 07:05-08:01, 12:52-13:22, 14:43-15:07, 17:32-17:49, 18:17-18:39, 19:26-19:58
