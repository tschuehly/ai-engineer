# Ship Enforcement Policies in Preview Mode Before Enabling Them

Summary: Deploy a new budget, guardrail, or policy engine into production with evaluation on and enforcement off, so the policies fire against real traffic and record what they *would* have done. The thresholds you need cannot be guessed from a test bench, and the alternative — shipping enforcement and discovering the threshold from the runs it killed — makes calibration cost production incidents.

Use when:
- Introducing cost caps, rate limits, safety guardrails, or any policy engine to an agent that is already serving users.
- A team is stuck picking a numeric threshold and has no distribution of real runs to pick it from.
- A policy layer is being evaluated for adoption and the buyer needs to see it act before granting it authority.
- Rolling out a control that can terminate work.

Details:
- **The mode, as described.** "In preview mode… all the policies run as is, but the enforcement doesn't happen." The demo run "completed but we did not see any sort of failures there. The policies executed but the actions that were associated with those policies were not allowed to be executed," and the dashboard still showed the cost budget and cost guard policies having evaluated. ([Chawla & Koul](../sources/20260822_GJX19pNhmSw.md), 16:23-17:08)
- **The stated purpose is threshold calibration, not confidence-building.** "If you want to include this product into your production agents, you want to have a safe environment or a safe way to firstly put it in your production environment, test the guardrails, tweak the guardrail, see what's the policies are doing and then finalize the thresholds." The output of a preview period is a number, and it is a number you could not have obtained anywhere else, because the distribution of real run costs is the thing being measured. (17:08-17:32)
- **Why this matters more for cost policies than for most rollouts.** A budget threshold has no principled value: it is a quantile of your own run-cost distribution, and that distribution is workload-specific, drifts with model prices and prompt changes, and has a long tail. Shipping a guess with enforcement on means the first thing the policy tells you is which legitimate runs it killed.
- **The preview period is also the honest place to compare arms.** Policies evaluating with actions suppressed produce exactly the counterfactual a cost benchmark needs — how often each policy would have fired, on which segments, and at what point in the run — which is the data that turns a spend-reduction claim into a table with a completion column. See [A Cost Control Must Report Completion Rate or It Is Just Throttling](a-cost-control-must-report-completion-rate-or-it-is-just-throttling.md).
- **It is the general shadow-deploy discipline applied to an agent control plane**, and the demo makes it scenario 1 of 3 rather than a footnote — preview, then halt, then steer — which is the right order to introduce a component that can terminate runs. The same staging is what the wiki's routing evaluation asks for from the other side: measure against the incumbent arm before switching traffic. See [Evaluate a Router Against the Always-Frontier Arm](evaluate-a-router-against-the-always-frontier-arm.md).
- **What is left unspecified.** No guidance on how long a preview period should run, how to size it against the tail, whether preview should be per-policy or per-environment, or how to promote a single policy out of preview while the rest stay in it. Treat those as design decisions the pattern requires and the source does not supply.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Build an Agentic Control Plane So the Model Proposes and the Platform Decides](build-an-agentic-control-plane.md)
- [A Cost Control Must Report Completion Rate or It Is Just Throttling](a-cost-control-must-report-completion-rate-or-it-is-just-throttling.md)
- [Steer an Over-Budget Run Before You Kill It](steer-an-over-budget-run-before-you-kill-it.md)
- [Make the Instrumentation Boundary Two-Way and Gate It With a Governor](make-the-instrumentation-boundary-two-way-and-gate-it-with-a-governor.md)
- [Put the Cost Control at the Agent Run, Not the Model Request](put-the-cost-control-at-the-agent-run-not-the-model-request.md)
- [Evaluate a Router Against the Always-Frontier Arm](evaluate-a-router-against-the-always-frontier-arm.md)
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)

Sources:
- [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 16:23-17:32
