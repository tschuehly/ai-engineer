# Derive the Post-Deploy Check Plan From What Actually Changed

Summary: Standard pipeline checks run the same assertions on every release. A per-release check plan is built instead by reading what the change touched, choosing the telemetry that would expose trouble for that specific change, walking the causal chain outward to the systems downstream of it, and letting the agent decide when to look again rather than hard-coding a wait.

Use when:
- Post-deploy verification passes on every release and incidents still get found by customers or by an alert hours later.
- A change class (a service swap, a schema change, a dependency upgrade) has failure modes your standard KPI panel does not cover.
- Deciding whether a verification window of minutes is long enough for the failure you actually fear.

Details:
- The premise is generic to change, not to code: "any change inside of your environment is an opportunity for something to go wrong… having an agent that's able to watch as all these change events come in just to do a sanity check of is everything stable is incredibly important" (13:47-14:07).
- The gap named in existing pipelines is coverage, not correctness: "a lot of people have decent CICD system. I mean, this is like tried and true stuff that we've had as an industry for quite a while… typically the checks that it does are good. They're good baselines, but it's not exhaustive based on the type of changes that are going in. There's certain signals you'd want to watch or not want to watch. And so, every rollout is a bit unique" (14:07-14:35).
- The plan is derived from the diff: the agent will "actually look at the changes that are going in, understand what telemetry might help us evaluate whether those changes are good or not good or like are putting the system in an abnormal state, and build a sort of customized plan that it's going to check just for this specific release" (17:57-18:25).
- Selection follows the causal chain rather than stopping at the changed service. In the demo, "the checkout replaces currency service, we're monitoring the checkout latency and the error rates. Well, let's take a look at the Kafka pipeline cuz that's sort of involved. This is the sort of causal chain I want to sort of say, I want to make sure is is healthy" (18:56-19:10) — the changed component, the metrics that would show it degrading, then the asynchronous system it feeds.
- Recheck timing is a decision, not a constant: "it can check it not just once, but sort of on an ongoing basis. And none of this is hard-coded in. It's not like, oh, let's just wait for 15 minutes and then try this again, and then we'll be done" (19:10-19:22). The agent "could decide, I want to wait for another hour cuz this type of issue might only hit every so often… Maybe I'll come back in 3 days and say, is this deploy still kind of healthy? Are we seeing the change in the effect that I expected to see out of this?" (19:22-19:45). Autonomy over the schedule is adjustable — "you get to guide it a bit on how much autonomy you want it to have."
- The three-day recheck also carries an expectation, not only a health question: whether the change produced the effect it was shipped to produce. That is a different assertion from "no alarms fired," and it is not one a pipeline gate can make at merge time.
- The trigger in the demo is a classification rather than a webhook: "anytime somebody posts a sort of GitHub tag, our agent's going to sort of see that and say, 'Oh, That's a release. Is that a release? Yes, that is a release. Let me go watch that'" (17:43-17:54). The same shape is claimed for "feature flags, infra changes, sort of any sort of eventing system that you can think of" (19:45-19:53).
- The posture toward the existing pipeline is additive by design: "our goal is not to sit here and say, 'We're going to replace an entire CI/CD pipeline. You've spent time organizing that.' But this can sort of patch a lot of parts of your system that may not be as robust as they should be" (18:25-18:41). The alternative being priced is a person: "it would be great if you had a single engineer just focused on like watching all the things on every release, but that's really expensive. There's a lot of cognitive load" (18:41-18:50).
- Caveats: the demo runs in an explicitly "sort of fake environment," and nothing about the pattern is measured — no catch rate, no false-positive rate, no comparison against the baseline pipeline checks it complements, and no cost accounting for an agent that may keep re-checking for three days. The escalation path when a derived check does fail is not shown.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Watch the Change Paths That Bypass Your Deployment Pipeline](watch-the-change-paths-that-bypass-your-deployment-pipeline.md)
- [Separate Execution From the Production Context That Judges It](separate-execution-from-the-production-context-that-judges-it.md)
- [Analyze Operational Health Over Time Slices Before Invoking Repair Agents](analyze-operational-health-over-time-slices-before-invoking-repair-agents.md)
- [Observability-to-PR Agents Turn Incidents Into Reviewable Fixes](observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md)
- [Give Unowned Operational Work a Trigger](give-unowned-operational-work-a-trigger.md)

Sources:
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 13:47-14:35, 17:43-19:53
