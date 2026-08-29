# Stage Proactive Coding Agents From Maintenance to System Awareness

Summary: Proactive coding agents can be staged from local maintenance, to personalized project awareness, to cross-system consequence awareness. This progression keeps early proactivity grounded in concrete code signals before expanding to product, design, telemetry, and outcome signals.

Use when:
- Planning a roadmap for coding agents that should do useful background work.
- Deciding which proactive actions are safe enough before the agent understands broader product consequences.

Details:
- Level one proactivity is local and maintenance-oriented: Jules detects missing tests, unused dependencies, and unsafe patterns, then fixes them while doing other requested tasks (06:39-07:19).
- Level two adds project and user context: the agent observes how the user works, the code they write, their role, frameworks, and deployment style so it can anticipate next needs (07:21-07:49).
- Level three connects code, design, and data agents around consequences: Jules sees software breakage, Stitch understands user interaction, and Insights connects analytics, telemetry, and conversion signals (07:49-08:39).
- Cross-boundary proposals can include performance fixes to improve UX and design changes to prevent regressions, organized around live data rather than isolated code edits (08:39-08:55).
- A concrete Jules implementation path includes repository indexing, to-do discovery, best-practice suggestions, environment setup, and just-in-time context that agents can consult before asking the user (10:08-10:58).
- **An operations vendor inverts the staging order, which is worth taking seriously as a counter-case.** This page starts proactivity at local code maintenance and reaches production consequences last, on the grounds that early actions should be grounded in concrete code signals. Resolve AI starts at the far end — the first recommended workload is deployment monitoring, "a really big use case that we suggest people sort of go through" — and the argument for it is that the action is read-only observation rather than change: watching a release, choosing telemetry, reporting. Level-three signals (metrics, deploys, downstream systems) can be safe to *read* long before an agent is trusted to act on them, so consequence awareness and autonomy are separable axes rather than one ramp. ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 13:47-15:00)

- **The staging boundary, named from the other side: what actually broke when the agent moved past maintenance.** Uber's cloud agent handled toil fine and needed a new stopping point for features — "this was great for doing like toil sort of workloads but to build more advanced end-to-end features we really need to be able to validate the feature first" ([Huda](../sources/20260821_17-YSUHo6Lk.md), 13:42-14:07). That is a more precise statement of why the staging exists than task risk alone: a toil diff's correctness is legible *in the diff*, and a feature's is not, so the later stage needs an oracle outside the code — here a simulator screenshot compared against the Figma spec, plus a staged backend to check integration (14:31-14:56). Uber's maintenance stage is also further developed than the local-cleanup form this page describes: services enroll into shared maintenance skills run from one managed loop surface, and incident reviews are mined monthly for new ones (15:54-17:10).

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Stage complex AI applications into inspectable deterministic and agentic steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)
- [Expose observability as agent-readable feedback](expose-observability-as-agent-readable-feedback.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Derive the Post-Deploy Check Plan From What Actually Changed](derive-the-post-deploy-check-plan-from-what-changed.md)
- [Run Maintenance Skills From One Managed Loop Surface](run-maintenance-skills-from-one-managed-loop-surface.md)

Sources:
- [Proactive Agents - Kath Korevec, Google Labs](../sources/20251213_v3u8xc0zLec.md), 06:39-10:58
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 13:47-15:00
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 13:42-14:56, 15:54-17:10
