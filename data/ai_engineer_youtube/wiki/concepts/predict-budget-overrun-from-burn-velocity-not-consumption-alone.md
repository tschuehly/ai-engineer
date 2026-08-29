# Predict Budget Overrun From Burn Velocity, Not Consumption Alone

Summary: A budget check that only reads "how much have I spent" can act only after the money is gone. Reading the *rate* alongside the fraction consumed turns the check into a forecast — you can predict that a run will exhaust its budget before it finishes and intervene while intervention is still cheap.

Use when:
- Implementing a cost, token, time, or step budget for a long-running agent.
- A budget guard is firing too late to do anything except kill the run.
- Deciding what signal a mid-run policy should evaluate against.
- Building alerting for spend on workloads whose per-run cost varies by an order of magnitude.

Details:
- **The two-signal rule.** "This cost guard, it takes into account two things. First how much of your allotted budget have you consumed? Second what is the velocity at which you're consuming tokens. Now based on these two things, if it predicts that you're going to run out of your tokens or your allotted budget by the end of the run," it acts. ([Chawla & Koul](../sources/20260822_GJX19pNhmSw.md), 18:09-18:28)
- **Why one signal is not enough.** Fraction-consumed is a threshold on a lagging quantity: at 90% of budget the remaining 10% bounds every action you can still take. Velocity is what makes the check anticipatory — a run at 40% burning fast is a problem, a run at 80% that has gone quiet is not. The pair is the minimum to distinguish them, and it is the same reason capacity alerting reads rate of change rather than level.
- **The prediction is what licenses the cheap intervention.** Because the guard fires on a forecast rather than on exhaustion, there is still budget left to spend differently — the demonstrated response is an injection into the system instructions telling the model to keep outputs succinct, which only helps if there are calls left to make. A guard that waits for the cap has one action available, and it is a kill. See [Steer an Over-Budget Run Before You Kill It](steer-an-over-budget-run-before-you-kill-it.md). (18:28-18:39)
- **The demo's own setup shows the regime this matters in.** Scenario 3 used "a budget slightly higher but… still not high enough for the agent to complete in time" — that is, the interesting case is not the run that blows the budget in one step, but the run that is on track to overrun and would have died at the cap. (17:57-18:09)
- **What the talk does not specify, and you will have to decide.** No window length, smoothing, or units are given for the velocity term, and no threshold is given for what counts as a predicted overrun. Burn rate over a short window on an agent whose steps vary in cost is noisy, so a naive linear extrapolation will trip on a single expensive tool call; the run's remaining *work* is also unknown, which is what the forecast is implicitly assuming away. Treat the two-signal shape as the transferable part and the estimator as unspecified.
- **The complementary signal this does not catch.** Velocity is spend per unit time; it says nothing about whether the spend is producing progress. The talk's policy catalog lists loop detection and progress detection as separate policies for exactly that reason, and the wiki's retry-amplification page describes the loop that spends steadily while going nowhere. A run circling a failing tool at a modest, constant burn rate is invisible to a cost guard and obvious to a progress check. See [Contain Retry Amplification Before It Becomes a Compute Incident](contain-retry-amplification-in-agent-loops.md). (19:26-19:49)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Wrap agent calls with circuit breakers and compensation](wrap-agent-calls-with-circuit-breakers-and-compensation.md)
- [Steer an Over-Budget Run Before You Kill It](steer-an-over-budget-run-before-you-kill-it.md)
- [Put the Cost Control at the Agent Run, Not the Model Request](put-the-cost-control-at-the-agent-run-not-the-model-request.md)
- [Contain Retry Amplification Before It Becomes a Compute Incident](contain-retry-amplification-in-agent-loops.md)
- [Emit Attribution Dimensions So Budgets Can Target Any Cohort](emit-attribution-dimensions-so-budgets-can-target-any-cohort.md)
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)

Sources:
- [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 17:57-18:39, 19:26-19:49
