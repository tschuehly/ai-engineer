# Watch the Change Paths That Bypass Your Deployment Pipeline

Summary: Not every production change goes through CI/CD. Feature flag flips and infrastructure changes alter behavior without passing any gate, so they inherit no verification at all — and the only thing standing between a bad one and a customer is an alert firing and someone waking up to ask who changed what.

Use when:
- Auditing which change mechanisms in your environment actually have post-change verification attached.
- Investigating incidents whose first question is "did anything deploy?" and whose answer is "no."
- Deciding where an operations agent adds coverage rather than duplicating an existing gate.

Details:
- The gap is stated as a category, not an oversight: "often times you have change systems that you're not piping through a CICD system like a feature flag or maybe some infra changes that might happen which maybe don't get any monitoring at all" (14:35-14:47).
- The current detector for those paths is the incident response process itself: "you're sort of just trusting that an alert might fire and an on-caller will wake up and say, 'Who changed what?'" (14:47-14:52). That is detection after impact, by a person who was not involved in the change, reconstructing the change list from scratch.
- This sits beside a second, distinct gap in the pipeline path — that standard checks "are good baselines, but it's not exhaustive based on the type of changes that are going in" (14:20-14:31). The two failures are independent: one is thin coverage on changes that are gated, the other is no coverage on changes that are not. Fixing your pipeline's assertions does nothing for the second.
- The proposed coverage is the same mechanism used for releases, pointed at a different event source: an agent watching change events builds a check plan for what changed and rechecks on its own schedule, and the pattern is claimed to generalize — "this again works for feature flags, infra changes, sort of any sort of eventing system that you can think of" (19:45-19:53).
- The framing is deliberately non-competitive with existing tooling: "our goal is not to sit here and say, 'We're going to replace an entire CI/CD pipeline. You've spent time organizing that.' But this can sort of patch a lot of parts of your system that may not be as robust as they should be" (18:25-18:41). The argument for agents here is coverage of the ungated paths, not better gating of the gated one.
- The general premise is that the unit of risk is a change, not a deploy: "any change inside of your environment is an opportunity for something to go wrong" (13:47-13:55). Deployment monitoring is singled out as the highest-value starting workload — "deployment monitoring is actually a really big use case that we suggest people sort of go through" (14:53-15:00) — but the flag and infra paths are the part with no incumbent at all.
- A practical reading: enumerate every mechanism that can change production behavior, mark which ones emit an event you could trigger on, and mark which ones have any verification attached today. The rows with an event and no verification are the cheapest to cover.
- Caveats: this is a vendor talk with no measurement — no count of flag or infra changes caught, no false-positive rate, and no baseline. Feature flag systems' own guardrails (staged rollout, automatic rollback, per-flag metrics) are not discussed, so the claim that these paths get "no monitoring at all" is asserted generally rather than shown for a specific stack.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Derive the Post-Deploy Check Plan From What Actually Changed](derive-the-post-deploy-check-plan-from-what-changed.md)
- [Give Unowned Operational Work a Trigger](give-unowned-operational-work-a-trigger.md)
- [Run a Production AI Incident Playbook](run-a-production-ai-incident-playbook.md)
- [Incident Agents Turn Alerts Into RCA and Operational Memory](incident-agents-turn-alerts-into-rca-and-operational-memory.md)

Sources:
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 13:47-15:00, 18:25-18:41, 19:45-19:53
