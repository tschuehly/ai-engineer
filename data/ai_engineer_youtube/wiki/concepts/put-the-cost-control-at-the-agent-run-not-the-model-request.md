# Put the Cost Control at the Agent Run, Not the Model Request

Summary: An LLM gateway governs one request at a time, but nothing that actually burns an agent's budget is visible in one request — the tool loop, sub-agent fan-out, and monotonically growing context are all properties of the run. Budget, attribute, and enforce at the run boundary, and treat the per-request cap as the outer backstop rather than the control.

Use when:
- Someone proposes solving agent cost overruns by adding hard caps or model downgrading to an existing gateway.
- Deciding where a cost or context policy should live: inside the agent code, at the gateway, or in a separate control plane.
- A spend post-mortem can identify the expensive *model* but not the expensive *run*.
- Designing budgets for a system where one user prompt fans out into many heterogeneous model calls.

Details:
- **The gap, stated as a granularity claim.** Existing token-management frameworks "basically monitor the model… request. They are like model gateways which will do model routing or hard budget capping. But what we need right now is something which monitors you at the run instead." ([Chawla & Koul](../sources/20260822_GJX19pNhmSw.md), 05:56-06:35)
- **Three specific behaviours a request-level view cannot see**, and they are the ones that spend the money: "the loop between the agent call, the tool and the agent"; "the spawning of multiple sub agents happening from a one main agent"; and "the growing of context." Each is cheap per request and expensive per run, which is exactly the shape a per-request cap is blind to. (06:35-07:05)
- **The named landscape.** "LiteLLM, Portkey, Cloudflare — all of those they happen at again the request level… halting is there, routing is there for some of those but all of this again is at a request and you can't control the cost at the request layer." The claim is about the layer, not the products: a proxy that sees one `POST /messages` at a time can allow it, deny it, or send it somewhere cheaper, and that is the whole action space. (08:01-08:34)
- **The era framing that motivates it.** SaaS priced a UI and grew usage caps, seat limits, and tier policies; cloud priced pay-as-you-go and grew autoprovisioning and autoscaling policies; the agentic era prices model calls and has no control surface at "the part where the code calls the model." Every prior era's control surface ended up at the layer where consumption was *generated*, not where it was billed. (01:30-02:57)
- **The design consequence: enforcement in the call path, halting last.** The proposal is a cumulative budget across attributed runs where "enforcement actually happens in call path rather than a separate thing" — runaway context triggers "in place compaction… or in place caching," and only "after basically exhausting the list of all in place policies" does the budget cap fire. A gateway cannot do this because it has no way to change the run; it can only refuse the next request. See [Steer an Over-Budget Run Before You Kill It](steer-an-over-budget-run-before-you-kill-it.md). (07:05-08:01)
- **Where this genuinely disagrees with the wiki's gateway pages, and where it does not.** Aperture's gateway *does* aggregate spend across an identity and a session and enforces cross-provider budgets and per-day quotas from that position, so the claim that gateways only cap per request is too strong as stated — accumulation at the gateway is possible whenever the caller's identity is on the wire. The distinction that survives is the *action space*, not the accounting: a gateway sees every call and can allow or deny, but it has no channel back into the agent's loop, so its only lever on an over-budget run is to stop serving it. That is the same reason this page's argument and the gateway-chokepoint argument are complementary rather than competing. See [Make the LLM Gateway the Agent Observability Chokepoint](make-the-llm-gateway-the-agent-observability-chokepoint.md).
- **Attribution is the precondition, not a reporting nicety.** "If we don't know what agent, what run made that particular call we can't control it — we just know the broad picture of what went wrong but we can't trace it back or narrow it down." A run-level budget is only enforceable if every model call already carries the run identity that the budget is defined over. See [Emit Attribution Dimensions So Budgets Can Target Any Cohort](emit-attribution-dimensions-so-budgets-can-target-any-cohort.md). (04:27-05:01)
- **Caveat on evidence.** The layer argument is asserted from first principles by a vendor building the run-level product; the talk demonstrates it on its own two-agent test bench and reports benchmark deltas without ever showing a case where a request-level cap failed. Treat the granularity distinction as sound and the implied inadequacy of gateways as unmeasured.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Agentic Workloads Turn Token Price Into Unit-Economics Pressure](agentic-workloads-turn-token-price-into-unit-economics-pressure.md)
- [Treat Token Spend as a Strategic Axis](treat-token-spend-as-a-strategic-axis.md)
- [A Cost Control Must Report Completion Rate or It Is Just Throttling](a-cost-control-must-report-completion-rate-or-it-is-just-throttling.md)
- [Predict Budget Overrun From Burn Velocity, Not Consumption Alone](predict-budget-overrun-from-burn-velocity-not-consumption-alone.md)
- [Ship Enforcement Policies in Preview Mode Before Enabling Them](ship-enforcement-policies-in-preview-mode-before-enabling-them.md)
- [Steer an Over-Budget Run Before You Kill It](steer-an-over-budget-run-before-you-kill-it.md)
- [Emit Attribution Dimensions So Budgets Can Target Any Cohort](emit-attribution-dimensions-so-budgets-can-target-any-cohort.md)
- [Make the Instrumentation Boundary Two-Way and Gate It With a Governor](make-the-instrumentation-boundary-two-way-and-gate-it-with-a-governor.md)
- [Make the LLM Gateway the Agent Observability Chokepoint](make-the-llm-gateway-the-agent-observability-chokepoint.md)
- [An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once](an-llm-gateway-cannot-maximize-availability-latency-guardrails-and-cost.md)
- [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md)
- [Contain Retry Amplification Before It Becomes a Compute Incident](contain-retry-amplification-in-agent-loops.md)
- [Build an Agentic Control Plane So the Model Proposes and the Platform Decides](build-an-agentic-control-plane.md)
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Routing Savings Compound Across an Agent Session](routing-savings-compound-across-an-agent-session.md)

Sources:
- [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 01:30-02:57, 04:27-05:01, 05:56-08:34
