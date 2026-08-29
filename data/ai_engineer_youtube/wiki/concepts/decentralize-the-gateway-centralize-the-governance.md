# Decentralize the Gateway, Centralize the Governance

Summary: A company-wide LLM gateway is a single point of failure in every team's request path, and most teams asking for one have misdiagnosed their requirement: they want consistent cost tracking, rate limits, and policy — governance — which can be distributed as plugins or shared code without funnelling all traffic through one deployment.

Use when:
- Someone proposes one central LLM gateway for an entire organization.
- Deciding whether a platform team should own a service or own a library and a policy.
- The gateway itself has become the thing that takes production down.
- Designing multi-tenant isolation, load shedding, or traffic prioritization for shared AI infrastructure.

Details:
- **The gateway is a dependency you added, and it deserves the same scrutiny as the ones it protects you from.** After a talk spent on provider and guardrail failures: "we haven't discussed that we are actually adding another dependency in the request path itself which is… the LLM gateway itself." ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 12:58-13:16)
- **The misdiagnosis, and the separation it licenses.** "If you're thinking of having a central gateway for your entire company for LLMs, I would recommend rethink that… It is a single point of failure. What I've noticed is that in most scenarios, it's not the central gateway that they want. They want centralized governance. And there is a path forward where you can actually decentralize the gateway and still centralize governance. So do not try to centralize your traffic, but you can have plugins, you can have custom code that can centralize your governance." Governance here means "cost tracking, rate limit management" and comparable policy. (14:34-15:28)
- **Single ownership is fine; single deployment is not.** "It can be managed by a single team, but I wouldn't recommend deploying it as a single deployment for the entire company even though it's distributed." The organizational centralization and the topological centralization are separable, and only the second one creates the blast radius. (15:28-15:42)
- **Multi-tenancy is the failure mode that pushes hardest toward this.** "Make sure that your API keys are segregated per route, per use case, to the most granular thing that you can imagine. Having a noisy tenant can be one of the biggest problems here" — because on shared credentials, one team's traffic spends another team's rate limit. (13:24-13:48)
- **Load shedding, because a retry storm cannot be scaled out of.** "Make sure that the gateway that you're using supports load shedding, because when you have a retry storm, it becomes really hard to just scale out. You cannot simply scale out services that is under a retry storm." Concretely: web servers "have an internal queue and they're configurable. Make sure that they're bounded and they cannot accept requests that are unbounded," plus "traffic prioritization… to make sure under load your most important use cases get served." This belongs in "your runbooks, game days" rather than being discovered live. (13:49-14:31)
- **What this costs, which the talk does not price.** A decentralized fleet means many deployments to upgrade, config and policy-version drift, and enforcement that is only as consistent as the least-recently-updated instance. Centralizing traffic is also what makes a gateway a complete observability chokepoint — see [Make the LLM Gateway the Agent Observability Chokepoint](make-the-llm-gateway-the-agent-observability-chokepoint.md), which argues the opposite direction from a visibility and policy standpoint. The reconciliation is that the *governance plane* can be central while the *data plane* is not, but a plugin distributed across many deployments still has to report to somewhere for cost tracking to be complete.
- **Caveat.** This is the least supported claim in the talk. "In most scenarios, it's not the central gateway that they want" is an observation about teams the speaker has spoken to, with no count; and the plugin/custom-code path to distributed enforcement is asserted rather than demonstrated. No named product, reference architecture, or incident is offered.

- **A third topology for the same separation: governance centralized, enforcement in the call path, and the plane in your own tenant.** Chawla and Koul reach this page's conclusion from the cost side without going through a proxy at all. Their control plane is "an out of band plane… it doesn't interfere with your code," holding segments, budgets, and policies centrally, while what actually acts sits inside the application as an annotation and a governor, so "enforcement actually happens in call path rather than… a separate thing." Because that boundary floats method inputs and outputs upward, they place the plane "in your own tenant. So you do not need to worry about any data leaks." This is the decentralized-enforcement, centralized-governance split applied one layer deeper than plugins in a gateway — the policy is shared, the acting code is in every agent, and no traffic is funnelled anywhere. See [Put the Cost Control at the Agent Run, Not the Model Request](put-the-cost-control-at-the-agent-run-not-the-model-request.md) and [Make the Instrumentation Boundary Two-Way and Gate It With a Governor](make-the-instrumentation-boundary-two-way-and-gate-it-with-a-governor.md). ([FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 07:05-08:01, 08:57-09:07, 15:19-15:38)
Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Put the Cost Control at the Agent Run, Not the Model Request](put-the-cost-control-at-the-agent-run-not-the-model-request.md)
- [Make the Instrumentation Boundary Two-Way and Gate It With a Governor](make-the-instrumentation-boundary-two-way-and-gate-it-with-a-governor.md)
- [Emit Attribution Dimensions So Budgets Can Target Any Cohort](emit-attribution-dimensions-so-budgets-can-target-any-cohort.md)
- [Make the LLM Gateway the Agent Observability Chokepoint](make-the-llm-gateway-the-agent-observability-chokepoint.md)
- [An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once](an-llm-gateway-cannot-maximize-availability-latency-guardrails-and-cost.md)
- [Contain Retry Amplification Before It Becomes a Compute Incident](contain-retry-amplification-in-agent-loops.md)
- [MCP Gateways Create an Enterprise Root of Trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Your Fallback Provider Is Under-Tested and Under-Provisioned](your-fallback-provider-is-under-tested-and-under-provisioned.md)
- [Run a Production AI Incident Playbook](run-a-production-ai-incident-playbook.md)

Sources:
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 12:58-15:42
- [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 07:05-08:01, 08:57-09:07, 15:19-15:38
