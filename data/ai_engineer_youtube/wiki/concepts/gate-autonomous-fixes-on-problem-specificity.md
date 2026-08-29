# Gate Autonomous Fixes on Problem Specificity

Summary: A coding agent handed a problem will try to fix something whether or not the problem is well defined, so an autonomous signal-to-PR pipeline must gate dispatch on how specific the problem is. Route under-specified or undecidable problems away from the agent instead of letting it produce random fixes.

Use when:
- Building a pipeline that automatically turns issues, alerts, or signals into agent-written code changes.
- Deciding which incoming problems are safe to hand to an autonomous coding agent versus which need more evidence or a human decision.

Details:
- The core failure mode: if you throw a generic report like "onboarding is broken" at the agent SDK or Claude Code, "it will just try and fix something," yielding a lot of noisy PRs that aren't doing meaningful things — so the gate must ask whether the described problem is specific enough and ignore it if not (12:04-12:35).
- Specificity tracks the signal source. Error-tracking data (e.g., Sentry-style stack traces) is specific and "very actionable" — a coding agent works on it well. Slack messages and session replays produce generic problems with many possible solutions, which are much harder to make immediately actionable (09:31-09:57).
- PostHog implements this as a three-way actionability gate before code execution: not-actionable (often just insufficient data) is returned to the pool to gather more evidence; needs-human-input (a product decision the agent can't make a good call on) goes to a morning inbox for review; immediately-actionable is the only branch where the agent writes a fix (08:46-09:31).
- The gate is upstream of the coding agent on purpose: specificity is assessed from the grouped report and research summary, not discovered by letting the agent flail on the codebase.
- Implication for signal design: enrich or wait for vague signals (replay/chat) until they correlate with a specific, reproducible artifact (an error) before dispatching an autonomous fix, rather than dispatching on the vague signal alone.
- **A gate on the target rather than on the problem statement.** Garvin's instruction is maximally under-specified — one sentence asking to replicate a named competitor's pricing model, "nothing more difficult than that" — and it is allowed to run anyway, because the write target is a sandbox. Specificity gates and environment gates substitute for each other: a vague ask into a disposable environment is cheap, and a precise ask into production still is not. When neither gate is present, the combination is the dangerous one. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 07:33-07:47, 15:41-15:51)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Observability-to-PR Agents Turn Incidents Into Reviewable Fixes](observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md)
- [Choose autonomy level by task uncertainty and control needs](choose-autonomy-level-by-task-uncertainty-and-control-needs.md)
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)
- [Start Coding Agents With Small Verifiable Chores](start-coding-agents-with-small-verifiable-chores.md)
- [Let the Agent Reach a Test Environment, Not Production, When the Domain Carries Money](let-the-agent-reach-a-test-environment-not-production.md)

Sources:
- [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](../sources/20260610_zMiSRliEzv4.md), 08:46-09:57, 12:04-12:35
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 07:33-07:47, 15:41-15:51
