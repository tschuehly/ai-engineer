# An Empty Filter Stage Turns a Cleanup Into a Match-All Delete

Summary: When an agent composes a destructive command as a pipeline — list, filter, select, delete — an intermediate stage that produces nothing usually degrades to "no constraint" rather than to "no matches," and the selector then matches everything. The command is well-formed, the agent's reasoning is correct, and the blast radius is the entire namespace.

Use when:
- An agent builds shell pipelines, query filters, label selectors, or `WHERE` clauses that feed a delete, update, or shutdown.
- Reviewing a cleanup, garbage-collection, or cost-reduction automation before granting it write access.
- Designing tools for an agent where the argument is a predicate rather than an explicit list of targets.

Details:
- **The incident.** An agent was tidying up after itself, listing the workloads it no longer needed and deleting them — "that's completely reasonable except one stage in the pipeline basically evaluated to nothing and the filter dropped out and now the selector matched everything." It removed about 200 workloads, affecting roughly 20 engineers, in 90 seconds; some were long-running training jobs, "maybe some of these were not even checkpointed," so the loss was "hours of progress." ([Malhotra](../sources/20260822_rbjWzZK2LU0.md), 01:28-02:21)
- **Nothing about it was adversarial or even wrong.** "Nobody was being malicious in this case. The agent genuinely thought it was tidying up after itself," and "the agent technically hadn't done anything that I couldn't have done. It was using my token after all." There is no prompt to improve here and no model behavior to correct; the intent was right at every step. (02:05-02:11, 03:06-03:20)
- **The mechanism generalizes past this stack.** The pattern is any language where an absent or empty predicate means "unconstrained": an empty label selector in Kubernetes, a `WHERE` clause built from a variable that came back empty, a `grep` that matched nothing feeding `xargs` with no `-r`, a tag filter that silently returns all resources when the tag list is empty. In each case the failure is in the *composition*, not in any single stage, and each stage in isolation looks correct — which is why it survives both model reasoning and human review of the command.
- **A tool-design response the source does not give but the failure implies.** The generic mitigation for this class is to make emptiness non-degrading: have destructive tools reject a predicate that resolves to zero constraints, require the caller to pass the resolved target list rather than the predicate, or have the tool echo the match count and require it to be under a threshold. Any of these turns "matched everything" into an error the agent must handle. This is the same move the wiki records as [pre-binding tool arguments to give agents safe autonomy](pre-bind-tool-arguments-to-give-agents-safe-autonomy.md), applied to the predicate rather than to the value.
- **What the source's own controls do about it.** They do not prevent it, they truncate it: a [per-hour delete cap](rate-limit-every-write-with-a-ceiling-that-refills.md) "would have capped it at a few couple of tens of workloads," and the [undo test](size-agent-controls-with-the-undo-test.md) says the cap has to be a hard stop, "because you can't un-delete a running job in someone else's namespace." Worth stating precisely: the deployed fix for this incident reduces a 200-workload loss to a tens-of-workloads loss. It does not make the composition safe. (09:19-09:35, 14:44-15:03)
- **The unmentioned second contributor.** The talk does not raise it, but the training jobs that were "not even checkpointed" are the reason the loss was measured in hours rather than in a re-run. Blast radius here was a joint property of the agent's command and the workloads' own durability, and the second half is fixable without touching the agent at all.
- **Evidence limits.** One incident, narrated from memory, with counts but no artifact: the actual command, the stage that emptied, and why it emptied are all described rather than shown. There is no report of whether the same pipeline pattern is still in use, nor whether any tool-level fix was made beyond the admission webhook that caps the rate.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Replace the Token's Boolean With a Budget on Four Dimensions](replace-the-token-boolean-with-a-budget-on-four-dimensions.md)
- [Rate-Limit Every Write With a Ceiling That Refills](rate-limit-every-write-with-a-ceiling-that-refills.md)
- [Size Agent Controls With the Undo Test](size-agent-controls-with-the-undo-test.md)
- [Pre-Bind Tool Arguments to Give Agents Safe Autonomy](pre-bind-tool-arguments-to-give-agents-safe-autonomy.md)
- [Give the Agent the Verbs That Fail Loudly](give-the-agent-the-verbs-that-fail-loudly.md)
- [Enforce Deterministic Guardrails Around Sensitive Tool Calls](enforce-deterministic-guardrails-around-sensitive-tool-calls.md)

Sources:
- [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../sources/20260822_rbjWzZK2LU0.md), 01:28-03:26, 09:19-09:35, 14:44-15:03
