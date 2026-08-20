# Observability-to-PR Agents Turn Incidents Into Reviewable Fixes

Summary: Observability and incident agents can convert operational evidence into a reviewed code change by chaining monitoring, signal grouping, context gathering, planning, coding-agent execution, and pull-request creation. The useful handoff is usually not an autonomous production mutation; it is a PR with evidence, root-cause notes, and a human merge decision (or a low-risk change shipped behind a feature flag).

Use when:
- Designing an agent that responds to production health signals (infra metrics, errors, replays, support messages).
- Deciding how far an observability-driven repair workflow should automate before human review.

Details:
- Railway Autofix monitors application infrastructure, detects issues from metrics and thresholds, and aims to move from issue detection on Railway to an open GitHub pull request, 02:33-03:00, 03:11-03:24.
- The workflow first gathers project architecture, service resource metrics, HTTP metrics, threshold breaches, and affected services before asking an agent to write a fix, 03:11-04:17.
- After service context is gathered, the system writes a detailed plan that includes architecture, affected services, failure signals, and debugging recommendations, then passes that plan to a coding agent that clones the repo, creates todos, implements fixes, and opens a PR, 06:06-06:55.
- The demo's successful output is a pull request with a summary, analysis, root causes, and fixed changes so a human can review and merge, 17:24-17:47.
- PostHog generalizes the input side beyond infra metrics: a six-stage pipeline ingests heterogeneous product signals (errors, logs, session replays, Slack messages, experiments), normalizes each into one schema with an importance weight, and groups them into "reports" that promote to a research agent once accumulated weight passes a threshold — so cross-source signals describing the same problem are linked before any fix is attempted (PostHog 03:00-05:53).
- PostHog's research agent runs the Claude Agent SDK in a Modal sandbox with three tool sources — its own MCP server to pull extra data (e.g., logs) for the signal group, codebase context, and external MCPs (Linear, Notion) to ground the research — and outputs a problem summary, a priority, and a Git-blame-derived reviewer for the PR (PostHog 07:32-08:45).
- PostHog's execute step clones the repo into a sandbox, writes a fix with the Claude Agent SDK, pushes a PR, then snapshots the sandbox and rehydrates the snapshot on CI failures or review comments to keep iterating until the PR is green — so engineers wake up to green PRs instead of CI failures and comments to address manually (PostHog 10:00-11:03).
- Both systems keep a human in the loop by default, but PostHog notes low-risk changes can ship immediately behind a feature flag (rolled back and deleted if they fail), and aims to learn from every outcome — rejected PRs, deployment issues, errors resolved in production — to improve the next generated PR (PostHog 02:09-02:46, 13:38-14:56).
- Lovable's vent loop shows the same pattern with an agent-authored signal source: the platform's coding agent reports tooling/platform friction to a Slack channel, and a second monitoring agent deduplicates the vents, investigates, and opens PRs automatically; devs review (review requests arrive on the phone) and in many cases merge to prod — vent-volume spikes also serve as the incident-detection input that kicks the loop off (Lovable 16:44-18:43).

- **The same pipeline shape runs on human speech, where the hard step moves from grouping to noticing.** Superconductor puts a bot in customer calls, onboarding calls and internal meetings alongside Sentry and bug-tracker feeds, and its output is a prototype rather than a fix — "am I going to ship this one exactly how it is? Like, no, probably not. But it's a new idea, it's concrete, I can play with it." Machine signals arrive with structure, a timestamp, and an implicit claim that something is wrong; a spoken remark has none of those, so the deduplication rule ("if it finds existing work, it'll link to it") does the job that grouping and weighting do here, and the output contract is loosened from mergeable to reactable. Useful as the complementary input to the same signal-to-diff machinery — see [turn unfiled conversation into concrete prototypes](turn-unfiled-conversation-into-concrete-prototypes.md). ([Arjun Singh](../sources/20260809_OL7kfezynJM.md), 05:51-08:14)

- **A fourth variant stops before the diff on purpose, and its input is the change rather than the failure.** Resolve AI triggers on a release, a feature flag flip, or an infra change instead of on a symptom, derives which telemetry would expose trouble for that specific change, follows the causal chain outward ("the checkout replaces currency service… let's take a look at the Kafka pipeline cuz that's sort of involved"), and re-checks on a schedule it chooses — an hour, three days. The output is a judgment about whether the change is healthy, not a pull request. That inverts this page's ordering: here a signal fires and the pipeline reconstructs what caused it, there the cause is known first and the question is which signals to watch. It also covers the paths this page's inputs never see, since a feature flag emits no error until it does harm ([Watch the Change Paths That Bypass Your Deployment Pipeline](watch-the-change-paths-that-bypass-your-deployment-pipeline.md)). ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 14:35-14:52, 17:57-19:53)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Expose observability as agent-readable feedback](expose-observability-as-agent-readable-feedback.md)
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)
- [Gate Autonomous Fixes on Problem Specificity](gate-autonomous-fixes-on-problem-specificity.md)
- [Embed LLM-Generated Queries, Not Raw Heterogeneous Signals](embed-llm-generated-queries-not-raw-heterogeneous-signals.md)
- [Start Expensive With Agents, Then Collapse Proven Steps](start-expensive-with-agents-then-collapse-proven-steps.md)
- [Give agents a vent tool to report platform friction](give-agents-a-vent-tool-to-report-platform-friction.md)
- [Turn Unfiled Conversation Into Concrete Prototypes](turn-unfiled-conversation-into-concrete-prototypes.md)
- [Derive the Post-Deploy Check Plan From What Actually Changed](derive-the-post-deploy-check-plan-from-what-changed.md)
- [Watch the Change Paths That Bypass Your Deployment Pipeline](watch-the-change-paths-that-bypass-your-deployment-pipeline.md)

Sources:
- [Infra that fixes itself, thanks to coding agents - Mahmoud Abdelwahab, Railway](../sources/20251124_Q5IVm_CxN2w.md), 02:33-06:55, 17:24-17:47
- [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](../sources/20260610_zMiSRliEzv4.md), 02:09-05:53, 07:32-08:45, 10:00-11:03, 13:38-14:56
- [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](../sources/20260602_KA5kPbdkK2E.md), 16:44-18:43
- [Multiplayer agentic engineering — Arjun Singh, Superconductor](../sources/20260809_OL7kfezynJM.md), 05:51-08:14
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 14:35-14:52, 17:57-19:53
