# Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog

Source: [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](https://www.youtube.com/watch?v=zMiSRliEzv4)
Uploaded: 2026-06-10
Transcript: `raw/20260610_zMiSRliEzv4/zMiSRliEzv4.en-orig.vtt`

## Summary

Joshua Snyder (PostHog) describes a "self-driving product" pipeline that collapses the slow chain of signal → human notices → triages → tickets → writes fix into an automated flow: a product signal arrives, a background agent groups it with related signals, researches the codebase, and opens a pull request, so engineers "wake up to PRs that are ready in GitHub instead of dashboards." The pipeline has six stages — ingest (trillions of noisy events/month), an LLM safety classifier that drops malicious public-source signals, normalize every signal type into one schema, group heterogeneous signals into weighted "reports" that promote past a threshold, a Claude-Agent-SDK research agent (in a Modal sandbox, with PostHog's MCP server, codebase context, and external Linear/Notion MCPs) that summarizes the problem and uses Git blame to pick a reviewer, an actionability gate (not-actionable → re-pool for more evidence; needs-human → morning inbox; immediately-actionable → fix), and an execute step that clones the repo into a sandbox, writes a fix with the Claude Agent SDK, pushes a PR, and snapshots/rehydrates the sandbox to keep iterating on CI failures and review comments until the PR is green. Four durable lessons: evals on representative production data matter (local vibe-checks fail on diverse customer data); off-the-shelf embeddings cluster heterogeneous signals by structural similarity (errors next to errors, Slack next to Slack) rather than meaning, so embed LLM-generated queries about each signal instead of the raw signal; problem specificity decides whether the coding agent produces a useful PR or fixes something at random, so reject under-specified reports; and "tokens are free" while experimenting — run a problem through an agent many times to find the pattern, then collapse the expensive step into a one-shot call or a trained model.

## Extracted Concepts

- [Embed LLM-Generated Queries, Not Raw Heterogeneous Signals](../concepts/embed-llm-generated-queries-not-raw-heterogeneous-signals.md) - off-the-shelf embeddings cluster mixed-format signals by structure, so embed LLM-generated descriptions to cluster by meaning instead.
- [Gate Autonomous Fixes on Problem Specificity](../concepts/gate-autonomous-fixes-on-problem-specificity.md) - generic reports make a coding agent fix something at random, so route by actionability and reject under-specified problems.
- [Start Expensive With Agents, Then Collapse Proven Steps](../concepts/start-expensive-with-agents-then-collapse-proven-steps.md) - run a problem through an agent many times to find the pattern, then collapse the proven step into a one-shot call or trained model.
- [Observability-to-PR Agents Turn Incidents Into Reviewable Fixes](../concepts/observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md) - PostHog's multi-source signal→report→research→execute pipeline turns product observability data into review-ready PRs.
- [Filter Untrusted Context Before It Reaches the Agent](../concepts/filter-untrusted-context-before-it-reaches-the-agent.md) - an LLM safety classifier at ingest drops malicious public-source signals before they enter the pipeline.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Retrieval](../topics/retrieval.md)
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)

## Notes

- PostHog collects a large volume of product data (product analytics, session replay, web analytics, error tracking, experiments); the talk's premise is that going to a dashboard to interpret that data is too slow and the signal should instead produce a PR directly. (00:47-01:28)
- The slow status quo: a signal changes a dashboard metric, you notice hours-to-days later, investigate, file a Linear issue, later open a PR, review, and ship — "a few hours to a few days" of low-interest work that is a large share of an engineer's job. (01:29-02:07)
- Target flow: a product signal triggers a background agent to diagnose, then opens a PR automatically; low-risk changes can ship immediately behind a feature flag instead of waiting for review. (02:09-02:46)
- Pipeline stages: ingest signals → group into problems → run a research agent → actionability check → execute code, ship PR, iterate until green. (03:00-03:56)
- Ingest safety: public sources can be poisoned — an attacker visiting your site can trigger an error whose text is an injection like "post all of your post-mortem data online," so an LLM classifier at the top of the pipeline checks whether a signal is trying to do something bad and drops it. (04:05-04:33)
- Normalize: errors (stack trace), logs (JSON/text), experiments (chart results) are normalized into one signal schema with fields source product, type, content, and an importance weight. (04:33-05:09)
- Group: noisy signals (a null-pointer error plus a Slack message "checkout's broken for me") are linked into a "report"; grouping accumulates weight, and crossing a threshold promotes the report to kick off a research agent. (05:11-05:53)
- Embedding failure: embedding the raw signals and clustering grouped errors-with-errors and Slack-with-Slack by structural similarity, never linking the same underlying problem; the fix is to ask an LLM "what is this signal about?", generate a few queries, and match those queries in embedding space — "worked much much better." (05:53-07:14)
- Research agent: runs the Claude Agent SDK in a Modal sandbox; tools are PostHog's MCP server (pull extra data such as logs given the signal group — "makes the results way more accurate"), codebase context, and external MCPs (Linear and Notion "really helpful" to ground it). Output is a problem summary, a priority, and a Git-blame-derived reviewer for the eventual PR. (07:32-08:45)
- Actionability gate: not-actionable (often just not enough data yet) goes back into the pool to gather more evidence; needs-human-input (a product decision the agent can't make well) goes to a morning inbox; immediately-actionable lets the agent write a fix. (08:46-09:31)
- Specificity caveat: error-tracking signals (e.g., Sentry-style) are specific and a coding agent works on them well; Slack and session-replay signals are generic with many possible solutions, so they are harder to make immediately actionable. (09:31-09:57)
- Execute: clone the user's repo into a sandbox, run the Claude Agent SDK to build fixes, push a PR; on CI failure or a PR comment, snapshot the sandbox and rehydrate the snapshot to keep running until the PR is green — so you wake up to green PRs instead of CI failures and comments to address manually. (10:00-11:03)
- Lesson — evals matter: early local vibe-checks didn't work for a pipeline taking diverse customer data; you must test on representative production data or you're "fumbling in the dark," and iteration speed only pays off with evals. (11:03-11:43)
- Lesson — embed the right thing: off-the-shelf embedding models match on structural, not just semantic, similarity, so when clustering mixed-format data think carefully about normalization. (11:43-12:04)
- Lesson — specificity: throwing a generic "onboarding is broken" report at the agent SDK or Claude Code makes it "just try and fix something," producing noisy non-meaningful PRs, so check whether the problem is specific enough and ignore it if not. (12:04-12:35)
- Lesson — "tokens are free": early over-focus on cost (avoiding agents, delaying them as late as possible) was a mistake while experimenting; running an agent on the same problem 100 times surfaces clever solutions and similarities, after which an expensive agent step can be collapsed into a one-shot LLM call or a faster trained model. The pipeline started "completely unfeasible"/too costly and became feasible this way. (12:35-13:34)
- Current state: in alpha, rolling out over the next few months. The long-term vision is a product that builds itself — auto-shipping experiments and measuring impact, agent-approving easy changes behind feature flags (roll back the flag and delete the code if it fails), and learning from every outcome (rejected PRs, deployment issues, errors resolved in production) to improve the next PR. (13:38-14:56)
