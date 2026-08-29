# A Model Swap Moves Your Agent Product's Output Metrics, and the Explanation Lives in Chat

Summary: Upgrading the model under an agent product changes its output distribution, and the downstream metric moves without anyone touching the pipeline. The record of *why* usually exists — in the PR that did the swap and the Slack thread that noticed it — and nowhere in the telemetry, which is what makes an org-context layer useful for root-cause analysis rather than only for code generation.

Use when:
- A production metric on an agent product steps rather than drifts, and no code changed.
- Deciding what to log around a model version bump.
- Debugging a review bot, triage bot, or classifier whose volume changed after an upgrade.
- Arguing for indexing chat and PR history as operational data, not just as coding-agent context.

Details:
- The incident: a senior engineer "discovered that the number of code review issues that were being surfaced dropped precipitously," debugged it conversationally against the org context, "got all the way to the bottom and realized roughly what the problem was, and then asked Unblocked to fix it." ([Werry](../sources/20260827_qdAkxLoYNI8.md), 13:40-14:10)
- The cause, as written into the generated fix: "After this PR, we switched to Claude 4.8 and it dropped a ton in issues because the behavior is quite a bit different." A model upgrade, not a regression in the review pipeline. (14:31-14:50)
- The provenance detail that carries the lesson: the citation behind that explanation resolved to a Slack conversation. The correlation between the deploy and the metric was made by a person in chat, and that message was the artifact that made the root cause recoverable later. (14:50-15:08)
- Why the direction of the change is ambiguous and must be established separately: fewer flagged issues is what you would expect both from a model that got worse at finding problems and from a model that got better at suppressing false positives. Volume alone cannot distinguish them, which is why the outcome metric has to be whether comments changed code. See [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md).
- The pipeline-design consequence: comment volume is emergent across generators, filters, and now model versions, so a model bump is one more input to a number no single component owns. Treat a version change as a pipeline change and re-baseline it. See [Comment Volume Is a Property of the Review Pipeline, Not the Model](comment-volume-is-a-property-of-the-review-pipeline.md).
- Operational practices this implies: stamp the model version on every generated artifact; hold a fixed replay set to run across a version bump before it ships; alert on distribution shifts in output volume, not only on errors; and index PRs and chat so the "what changed" search has somewhere to land.
- The agent-facing half: a cloud agent "has all your organizational context at its fingertips" and produced a PR that "not only generates the fix, it also is able to relate it to all the conversations that were happening." A fix that carries its own causal history is reviewable in a way a diff is not — the reviewer can check the reasoning, not just the change. This is the incident-to-PR pattern with a chat corpus substituted for observability data. See [Observability-to-PR Agents Turn Incidents Into Reviewable Fixes](observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md). (14:10-14:50)
- Limits: one incident narrated after the fact in a vendor demo, on an internal experimental agent. The magnitude of the drop, the prior model, the fix, and whether the drop was in fact undesirable are all unstated.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Comment Volume Is a Property of the Review Pipeline, Not the Model](comment-volume-is-a-property-of-the-review-pipeline.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)
- [Observability-to-PR agents turn incidents into reviewable fixes](observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Weight Mined Review Guidance by the Author's Expertise](weight-mined-review-guidance-by-the-authors-expertise.md)

Sources:
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 13:40-15:08
