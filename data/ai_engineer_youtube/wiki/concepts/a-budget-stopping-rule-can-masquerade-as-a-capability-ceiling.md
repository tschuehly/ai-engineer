# A Budget Stopping Rule Can Masquerade as a Capability Ceiling

Summary: When an automated search is told to stop once a metric clears a threshold, every result it reports lands just above that threshold — and the resulting table reads like a capability ceiling when it is only an exit condition. If a set of scores clusters suspiciously tightly just above one round number, look for the stopping rule before you interpret the number.

Use when:
- Reading results from an automated search, sweep, evolutionary loop, or agentic optimizer where a budget or termination criterion was configured.
- Reporting your own search results, and deciding what a reader will infer from the numbers you print.
- Comparing two systems where one ran to a threshold and the other ran to exhaustion.
- Auditing a vendor's benchmark table where the wins are all narrow and all similar.

Details:
- The canonical instance is volunteered by the speaker as a "cheeky fact" about her own slide: "You'll notice all these percentages for win rates are like 60 plus… that's because we put the budget stopping it above 60. So, like once it was above 60, the our our [genetic] flow could exit. But we since… removed that barrier and… you can see it just go up over time." ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 06:54-07:16)
- The two readings the same table supports are very different. Read as a result, "win rates just above 60%" says the method is marginally better than the baseline and roughly at its limit. Read with the stopping rule attached, it says nothing at all about the limit — only that the search was cheap enough to be told to stop early, and that the ceiling was never probed.
- The diagnostic is distributional, not statistical: a genuine capability ceiling produces scores scattered around some value, high and low. A stopping rule produces scores that are *all* above one value and *none* far above it, because every run that crossed the line exited. Tight one-sided clustering just above a round number is the signature.
- This is not fraud and usually is not even a mistake — stopping early is the correct engineering choice when the search is a means to an end and compute is the constraint. The failure is in reporting: the exit condition is a configuration detail that lives in the harness, while the number travels alone into slides, blog posts, and other people's comparisons.
- What to publish alongside any searched result: the termination criterion, whether it bound (how many runs exited on the threshold rather than on exhaustion), and at least one run with the criterion removed. The last one is what converts "we hit 60%" into a claim about the method rather than about the budget.
- The general form covers more than win rates. Any early-exit condition — a "good enough" eval gate, a max-iterations cap, a cost ceiling, a first-passing-candidate accept — creates the same artifact in whatever metric it is defined over, and the wiki's [do-nothing baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md) and [ladder-with-an-oracle](ablate-the-recall-policy-with-a-ladder-and-an-oracle.md) designs both assume the rungs were run to the same stopping condition. Compare rungs that stopped differently and the ladder measures budgets rather than policies.
- Provenance: this is a single anecdote from a founder describing her own unpublished product, with no benchmark, baseline protocol, or task set named for the win rates in question, and the post-removal improvement shown only as a rising curve on a slide. The disclosure is the durable content; the numbers are not evidence of anything. ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 05:45-07:16)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Automated Training Search Beats Staff by Not Carrying Architecture Priors](automated-training-search-beats-staff-by-not-carrying-architecture-priors.md)
- [Co-Optimize Data With the Model or the Search Does Not Pay](co-optimize-data-with-the-model-or-the-search-does-not-pay.md)
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [Ablate the Recall Policy With a Ladder and an Oracle](ablate-the-recall-policy-with-a-ladder-and-an-oracle.md)
- [A Perfect Training Loss on Your Corpus Is Not Knowledge](a-perfect-training-loss-on-your-corpus-is-not-knowledge.md)
- [Do Not Trust a Single Leaderboard for Model Selection](do-not-trust-a-single-leaderboard-for-model-selection.md)
- [Judge Benchmark Quality by Task Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)

Sources:
- [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](../sources/20260812_XEd_SRVHBgU.md), 06:54-07:16
