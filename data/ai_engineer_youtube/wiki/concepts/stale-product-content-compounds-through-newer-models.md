# Stale Product Content Compounds Through Newer Models

Summary: Model upgrades are not a fix for assistants recommending your deprecated product. Sourcegraph's older-model GEO run kept pitching a retired product; re-running it on a newer model pitched it *more*, because superseded models have been publishing content onto the internet that newer models then read. Stale material about you accumulates rather than decays.

Use when:
- Assuming a documentation or naming problem will resolve itself at the next model release.
- An assistant recommends a sunset product, an old API version, or an obsolete integration path.
- Planning content work whose payoff you need to observe this quarter.

Details:
- **The falsified expectation.** The GEO pilot ran on Claude Sonnet 4, where the assistant "kept pitching Cody, which was one of our older products." Re-run the afternoon of the talk on 4.6 thinking, on the explicit expectation that "surely it's going to be better. It's going to know improved information about our product," the result went the wrong way: "it pitched Cody even more." ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 10:30-11:15)
- **The proposed mechanism is a feedback loop, not a lag.** "Now you have all of these like old models like outputting content that then is like compounding in the internet. So, you have to figure out like how to bury all of that noise with your true signal." Under this account, each generation of models trains on and retrieves a web that previous generations have been writing, so an error about your product gets re-published faster than you can correct the original sources. (11:15-11:27)
- **How this differs from ordinary model rot.** [Fresh Markdown Context Mitigates Model Rot in Codegen](fresh-markdown-context-mitigates-model-rot-in-codegen.md) treats the gap as a snapshot problem, fixed by putting current docs in context at runtime. This page names the harder case: the stale claim is not merely absent from the newer model, it is *better attested* in the newer model's corpus. Supplying current docs still helps, but only if the agent retrieves them; nothing about a newer release does the work for you.
- **The response, with its precondition.** `llms.txt`-style pages are offered as "more authoritative sources of truth that you're hoping to direct the agent to" — but "they still need to be using the tools and using real-time information and provenance to be able to give accurate answers about your product." A published authoritative file is inert against a model answering from weights. See [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md). (11:27-11:45)
- **Refresh unconditionally, not on change.** "Even if your stuff hasn't changed in 2 years, which would be shocking. Even if it hasn't, keep everything up-to-date and fresh because that is how they have their relevance algorithm." Recency here is a retrieval-ranking input, decoupled from whether the content is still correct — a maintenance obligation that a correctness-driven docs process will not generate. (11:53-12:07)
- **Give the assistant something quotable and structured.** "You want to give the agent something to quote… they want to bring something that they can really sell to the user," and assistants "really really like charts and FAQs and things like that." Prose that states a claim without a citable, extractable unit is harder for an assistant to relay. (11:45-12:12)
- **Operational consequence.** Deprecating a product name is now a content campaign with a measurement loop attached, not a changelog entry. Track mentions of the retired name per model version as a standing metric; expect it to rise on some releases, and target the retrieval path — see [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md).
- **Limit.** One product, one pair of model versions, one re-run performed the same afternoon, with no repetition count and no control for prompt or sampling variance. The compounding mechanism is the speaker's explanation, not a measured causal finding. ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), Provenance and Limits)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Models](../topics/models.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md)
- [Fresh Markdown Context Mitigates Model Rot in Codegen](fresh-markdown-context-mitigates-model-rot-in-codegen.md)
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Agent skills should point to current docs instead of embedding every API detail](agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md)
- [Human and Agent Credibility Reward Opposite Writing Styles](human-and-agent-credibility-reward-opposite-writing-styles.md)
- [Retire Completed Planning Docs Before They Become Agent Doc Rot](retire-completed-planning-docs-before-they-become-agent-doc-rot.md)

Sources:
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 10:30-12:12
