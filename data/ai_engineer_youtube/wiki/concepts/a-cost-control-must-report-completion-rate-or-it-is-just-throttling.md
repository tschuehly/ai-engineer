# A Cost Control Must Report Completion Rate or It Is Just Throttling

Summary: Spend reduction is the one agent metric with a trivial degenerate solution — kill the run — so any cost intervention benchmarked on money alone is unfalsifiable. Report the completion rate of the governed runs in the same table, against a throttling arm rather than an ungoverned one, or the number says nothing about whether the control is better than a hard cap.

Use when:
- Evaluating a cost-optimization feature: a budget cap, a router, a compaction policy, a cheaper model tier.
- Reading a vendor claim of an N% spend reduction with no second axis.
- Designing the arms of an experiment where one arm is allowed to abandon work.
- Someone proposes "just cap it" as the baseline that a more complex control has to beat.

Details:
- **The degenerate-solution argument, stated plainly.** "When we compare it with throttling — just simple throttling — your simple throttling is going to kill your agent runs no matter what." A throttle is guaranteed to win any spend-only comparison, because the cheapest possible run is the one that stops. ([Chawla & Koul](../sources/20260822_GJX19pNhmSw.md), 19:00-19:26)
- **The reported pair.** Average spend down "almost 78% with token ops enabled with the full policy suit," and "with the reduced average spend what you get is you get an uplift in that completion percentage from 67% to roughly 96%." The second number is the load-bearing one: the first only establishes that the control is cheap, the second that it is cheap *without* abandoning the work.
- **Read the baselines separately — they are not the same arm.** The 78% is against ungoverned runs; the 67%→96% is against simple throttling. That is two experiments reported as one line, and neither number tells you the throttle's spend or the ungoverned arm's completion rate. A complete table for this claim needs spend *and* completion for all three arms (ungoverned, throttled, governed); this one publishes one cell from each.
- **The missing third axis is quality**, and it is missing here specifically because the intervention touches output. The governed arm's steering action injects "make sure that the LM outputs are more succinct or more summarized," so a completed run is not necessarily an equivalent run. Completion is a binary that a degraded answer still satisfies. This is the same distinction that makes [Measure Agent Interface Efficiency With Tokens Per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md) insist on *successful*, and the same reason a loop eval carries correctness beside cost — see [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md). (18:17-18:39)
- **Generalize the arm, not the number.** Any metric a system is allowed to improve by doing less work needs its own do-nothing-shaped adversary: a throttle for spend, an empty answer for latency, a refusal for safety-violation rate. The wiki's control discipline for context presets is the same move from the other direction — see [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md), where the do-nothing arm exists to catch a technique that is worse than nothing, while the throttle arm here exists to catch a control that is better than nothing only because it quits.
- **Related failure to keep in view.** A budget that terminates runs also distorts whatever you measure downstream of it, because the surviving runs are a filtered sample — the same artifact described in [A Budget Stopping Rule Can Masquerade as a Capability Ceiling](a-budget-stopping-rule-can-masquerade-as-a-capability-ceiling.md). Governed-arm results should say how many runs hit the cap.
- **Provenance.** Vendor self-report on their own pre-release system, benchmarked on two open-source repositories ("browser use as well as metagp[t]") across unspecified "multiple iterations," "stress tests," and "simple scenarios hard scenarios." The methodology is the transferable content; the two percentages are not evidence about anyone else's workload. (18:44-19:26)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Treat Token Spend as a Strategic Axis](treat-token-spend-as-a-strategic-axis.md)
- [Ship Enforcement Policies in Preview Mode Before Enabling Them](ship-enforcement-policies-in-preview-mode-before-enabling-them.md)
- [Steer an Over-Budget Run Before You Kill It](steer-an-over-budget-run-before-you-kill-it.md)
- [Put the Cost Control at the Agent Run, Not the Model Request](put-the-cost-control-at-the-agent-run-not-the-model-request.md)
- [Measure Agent Interface Efficiency With Tokens Per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [A Budget Stopping Rule Can Masquerade as a Capability Ceiling](a-budget-stopping-rule-can-masquerade-as-a-capability-ceiling.md)
- [Evaluate a Router Against the Always-Frontier Arm](evaluate-a-router-against-the-always-frontier-arm.md)

Sources:
- [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 18:17-18:39, 18:44-19:26
