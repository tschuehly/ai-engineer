# Treat CI and Experiment Capacity as the Scarce Resource Agent Throughput Consumes

Summary: When agents write most of the code, the next constraint is not reviewer headcount but the shared infrastructure every change has to pass through: build and test capacity, and the number of experiments an organization can feasibly run. Uber names both as bottlenecks it is now capacity-planning for, and the constraint already shapes two unrelated design decisions in the same talk — where a coding agent stops, and when recurring maintenance jobs are scheduled.

Use when:
- Planning the infrastructure investment that follows a successful coding-agent rollout.
- CI queue time has grown and the cause is attempt volume rather than test duration.
- Deciding whether agent-generated changes should each get an experiment, and finding that they cannot.
- Arguing that a throughput gain in one place needs a matching investment somewhere else.

Details:
- **Named as a bottleneck, and as a forecasting problem.** "We're now putting more strain on our infrastructure. So we're trying to anticipate where our CI capacity needs to be and make the right foundational investments there." The verb is *anticipate* — CI capacity becomes something to model ahead of demand rather than to scale after complaints. ([Huda](../sources/20260821_17-YSUHo6Lk.md), 17:10-17:36)
- **The experiment ceiling is the less obvious one.** "There's only so many experiments that we can feasibly run as well. So that's another bottleneck." This is not a compute limit. Concurrent experiments contend for traffic and for statistical power, so a product organization has a hard cap on how many variants it can evaluate regardless of how quickly they can be built. Cheap implementation does not buy cheap validation. (17:36-17:46)
- **The constraint is already visible earlier in the same talk, twice.** Minion stops at a draft PR partly because "we want to prevent a lot of extra load coming on to CI" (13:42-14:07), and maintenance loops "run on Sunday when we know we have better CI capacity available" (16:22-16:46). Two independent design decisions — a stopping point and a schedule — are both determined by a shared queue. That is what a real bottleneck looks like from inside a system.
- **This is a sideways move, not only a downstream one.** The wiki records the argument that a faster engineering org relocates its bottleneck *downstream* onto go-to-market, support, and requirements intake — see [A Faster Team Relocates the Bottleneck Downstream](a-faster-team-relocates-the-bottleneck-downstream.md). Uber's report adds a stop before that one: the constraint first lands on shared infrastructure the engineering org itself owns, and CI is the clearest case because every agent attempt consumes it while only merged work reaches anyone downstream. The two are complementary, and the ordering matters for planning — the infrastructure bill arrives first and is the one you can actually buy your way out of.
- **The last bottleneck named is not a resource at all.** "It's not about can we build — we know we can probably build it now — it's more of a question of should we build it." Once implementation and validation capacity are both addressed, what is left is prioritization judgment, which no amount of capacity relieves.
- **Caveat.** No figures for CI load, queue time, cost, or experiment throughput appear, and no before-and-after is given for the two mitigations already deployed. This is a stated experience with a clear mechanism, not a measured result — its value is in the prediction that CI is where the strain appears first, which a team can check cheaply against its own queue metrics.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [A Faster Team Relocates the Bottleneck Downstream](a-faster-team-relocates-the-bottleneck-downstream.md)
- [Stop the Autonomous Agent at a Draft PR and Validate Before CI](stop-the-autonomous-agent-at-a-draft-pr-and-validate-before-ci.md)
- [Run Maintenance Skills From One Managed Loop Surface](run-maintenance-skills-from-one-managed-loop-surface.md)
- [AI Output Speed Can Overwhelm Review Capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Coding-Agent Capability Tiers Change the Bottleneck](coding-agent-capability-tiers-change-the-bottleneck.md)
- [Make Code Review the Bottleneck Skill for AI-Generated Code](make-code-review-the-bottleneck-skill-for-ai-generated-code.md)

Sources:
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 13:42-14:07, 16:22-16:46, 17:10-17:52
