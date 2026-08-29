# Emit Attribution Dimensions So Budgets Can Target Any Cohort

Summary: Tag every agent run with arbitrary caller-defined dimensions at the point the run starts, and the budget layer stops being limited to per-agent and per-run caps — segments built from those tags let you budget a customer cohort, an environment, a feature flag, or a conference audience, at whatever grain the spend question actually has.

Use when:
- A spend question is asked in a shape your metering cannot answer ("what did the trial users cost us last week").
- Designing the instrumentation for a multi-tenant or multi-surface agent before the cost controls exist.
- Budgets are currently per-agent and the overruns are concentrated in a cohort that cuts across agents.
- Deciding what metadata a trace or ledger entry must carry.

Details:
- **The chain: dimensions → segments → budgets → policies.** "Every agent run that you do, it's attributed to some user dimensions." Then "any dimensions that you float from the attribution layer" become a segment — the worked example is a preview agent tagging `cohort = AIE 2026` for a room of conference attendees — "and you can apply your budgets at this cohort level, so you don't necessarily have to restrict everything at an agent level or a run level. You can do rollups, you can do fine grain or coarse grain control." ([Chawla & Koul](../sources/20260822_GJX19pNhmSw.md), 11:40-12:00, 13:51-14:31)
- **Budgets are defined over segments and time windows, not just runs.** "Budgets are basically just the static thresholds that work across a time window against a particular segment or an agent run," and policies bind budgets to actions "against certain segments or agent runs." The dimension you failed to emit is a budget you cannot express later. (14:31-15:19)
- **Attribution is a precondition for control, not a reporting feature.** "If we don't have proper attribution — if we don't know what agent, what run made that particular call — we can't control it. We just know the broad picture of what went wrong but we can't trace it back or narrow it down." The billing surprise and the enforcement gap have the same root cause: the spend arrives aggregated. (04:27-05:01)
- **Where the dimensions have to be attached.** At the run boundary, in your own code, because that is the only place that knows the tenant, cohort, feature, or experiment the run belongs to — the model call itself carries none of it. This is the same in-process boundary that carries the ledger entry and the action downlink; see [Make the Instrumentation Boundary Two-Way and Gate It With a Governor](make-the-instrumentation-boundary-two-way-and-gate-it-with-a-governor.md). (12:01-12:32)
- **How this compares to the wiki's other spend-boundary proposals.** A gateway budgets by verified caller identity; an agent wallet makes the agent identity the spending boundary; per-seat caps make the employee the boundary. Free-form dimensions subsume all three as special cases and add the ones nobody anticipated — but they buy that generality with a discipline problem, since a segment is only as good as the tag consistently emitted by every code path that starts a run. Untagged runs land nowhere and are governed by nothing. See [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md).
- **The accounting side.** The ledger is "just one agent run, all the traces in one place," accumulated by an accounting module above an instrumentation layer carrying OpenTelemetry telemetry, per-call cost, an enrichment layer, and the attribution itself. Cost lands in the trace rather than being reconstructed from an invoice — which is what makes the run, rather than the billing period, the unit you can act on. (08:57-09:56, 14:31-14:43)
- **Caveat.** No cardinality guidance is given, and free-form dimensions on a high-volume workload are the classic path to an unusable metrics store. Nothing in the talk addresses tag governance, overlapping segments, or which budget wins when a run belongs to several.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Treat Token Spend as a Strategic Axis](treat-token-spend-as-a-strategic-axis.md)
- [Put the Cost Control at the Agent Run, Not the Model Request](put-the-cost-control-at-the-agent-run-not-the-model-request.md)
- [Make the Instrumentation Boundary Two-Way and Gate It With a Governor](make-the-instrumentation-boundary-two-way-and-gate-it-with-a-governor.md)
- [Predict Budget Overrun From Burn Velocity, Not Consumption Alone](predict-budget-overrun-from-burn-velocity-not-consumption-alone.md)
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Make the LLM Gateway the Agent Observability Chokepoint](make-the-llm-gateway-the-agent-observability-chokepoint.md)
- [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md)
- [Thread Every Outcome Back to the Decision That Caused It](thread-every-outcome-back-to-the-decision-that-caused-it.md)

Sources:
- [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 04:27-05:01, 08:57-09:56, 11:40-12:32, 13:51-15:19
