# Route Between Model Tiers by Quality Dimension, Not Only Cost

Summary: Tiers within one model family do not sit on a single quality ladder. Sonar's per-dimension scoring of Claude Sonnet 4.6 against Claude Opus 4.6 puts Sonnet ahead on correctness and task-solving while Opus is the better pick when maintainability, security, or lower complexity is what the task needs — so the tier toggle teams already operate to control token burn is silently a quality decision, and the right routing key is the dimension the change demands.

Use when:
- A team toggles between a family's tiers purely on cost or rate limits and treats the tiers as "same model, less of it."
- Choosing a model for work whose failure mode is maintenance burden or a vulnerability rather than a failing test.
- Building a router and picking the feature it routes on.
- Reading a leaderboard that reports one aggregate score per model.

Details:
- **The measurement.** Sonar scores each major new model on "4,000 or so coding tasks… using all of the metrics that SonarQube uses to evaluate code" — "correctness, complexity, the rate at which they're solving the tasks we assign them, and then our classic things maintainability, reliability, and security" — and plots models across those axes. ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 04:51-05:29)
- **The split, stated against the cost decision teams already make.** "If you're a Claude customer, you might be toggling between these two models to control your token burn rates. And you'll see that Claude Sonnet is actually quite good from a correctness standpoint, from… solving tasks… But if you're requiring higher levels of maintainability or higher levels of security, if you're trying to get a lower complexity out of your code, you might benefit from switching to Opus for tasks like that." The consequence: downshifting for cost does not trade quality uniformly — it trades *some* dimensions and may improve others. (05:30-05:57)
- **Why this is a different claim from the wiki's leaderboard caution.** [Don't Trust a Single Leaderboard for Model Selection](do-not-trust-a-single-leaderboard-for-model-selection.md) is about disagreement *between* boards and aggregate scores hiding per-task variance. This is variance *within one vendor's own family on one board*, which is the case most likely to be assumed away, because the tiers are marketed as a capability ladder and priced as one. [Measure Generated Code Quality Beyond Pass Rate](measure-generated-code-quality-beyond-pass-rate.md) supplies the same vendor's earlier evidence that the axes genuinely diverge — the model with the highest pass rate also carried the highest security-issue rate per million lines.
- **Practical routing keys.** The dimension that matters is a property of the change, not of the repository: a throwaway script cares about correctness, a shared library cares about maintainability, an endpoint that takes untrusted input cares about security. That makes this compatible with [Route Each Request to the Cheapest Sufficient Model by Difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md) with one amendment — "sufficient" is per-dimension, so difficulty alone under-specifies the route. It is also the missing half of [Verification Guardrails Let You Downshift to Cheaper Models](verification-guardrails-let-you-downshift-to-cheaper-models.md): guardrails make a downshift safe on the dimensions the guardrails cover, and this page says to check which dimensions those are.
- **The talk's own use of the data is more modest than the routing advice**, and worth keeping: the leaderboard "serves to put some sunlight on the fact that you still need to be vigilant with these models… None of these models are ever going to be perfect. You're always going to have some kind of need for verification in the loop." Per-dimension routing narrows the gap; it does not close it. (06:12-06:27)
- Caveats: this is a vendor leaderboard whose axes are the vendor's own product metrics, including at least one proprietary measure (cognitive complexity). The comparison is spoken over a slide, so no numbers are stated for either model; "4,000 or so coding tasks" is the only sample figure given, and the earlier Sonar talk describes its dataset as Java assignments, so language generality is unestablished. Rankings on any such board are also perishable across model releases.

- **The dimensions worth routing on are the ones your own repository separates, which argues for measuring the split yourself.** Superconductor's private benchmark produces two plots rather than one ranking — quality against cost and quality against time — and the families separate differently on each: Anthropic's agents are "consistently getting better, but not really any faster" and "clearly just so much more expensive for us," while Codex and Cursor come out "pretty fast and quite good" and open models are improving but "kind of slow." Latency and price are cruder dimensions than maintainability or security, but the structural point is the same one this page makes: a single ordering hides the tradeoff you are actually making, and the ordering that matters is the one measured on your codebase ([replay your own merged PRs as the coding-agent benchmark](replay-your-own-merged-prs-as-the-agent-benchmark.md)). ([Arjun Singh](../sources/20260809_OL7kfezynJM.md), 13:46-14:51)

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Measure Generated Code Quality Beyond Pass Rate](measure-generated-code-quality-beyond-pass-rate.md)
- [Don't Trust a Single Leaderboard for Model Selection](do-not-trust-a-single-leaderboard-for-model-selection.md)
- [Route Each Request to the Cheapest Sufficient Model by Difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md)
- [Verification Guardrails Let You Downshift to Cheaper Models](verification-guardrails-let-you-downshift-to-cheaper-models.md)
- [Select State of the Art on a Quality-Efficiency Pareto Front](select-state-of-the-art-on-a-quality-efficiency-pareto-front.md)
- [Verification Debt Outlives the Productivity Spike](verification-debt-outlives-the-productivity-spike.md)
- [Replay Your Own Merged PRs as the Coding-Agent Benchmark](replay-your-own-merged-prs-as-the-agent-benchmark.md)

Sources:
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 04:51-06:27
- [Multiplayer agentic engineering — Arjun Singh, Superconductor](../sources/20260809_OL7kfezynJM.md), 13:46-14:51
