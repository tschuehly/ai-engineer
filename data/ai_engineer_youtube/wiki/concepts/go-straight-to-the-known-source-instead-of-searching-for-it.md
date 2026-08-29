# Go Straight to the Known Source Instead of Searching for It

Summary: Search exists to find where an answer lives. When you already know where it lives — and for many recurring enrichment tasks everyone does, including the vendors you would pay — routing through a general search layer adds a discovery step you do not need, plus the tokens to re-structure what comes back. Hitting the two or three known sources directly can drop the AI cost of the task to zero.

Use when:
- Building a recurring enrichment, monitoring, or research task over a stable set of entities.
- A pipeline calls a search API for a fact that always comes from the same site.
- Deciding whether to pay a data vendor that is itself reading the sources you could read.
- Evaluating whether a task needs an agent loop at all, or a scraper plus merge heuristics.

Details:
- The rule as stated: "You use search when you don't know the source, but when we're talking about company enrichment, we all know these sources. We all know where that data comes from. The CaaS also bring it from them, ZoomInfo bring it from that. It's the same thing over and over again. Why not just go straight to the source? Why are we doing that middleman thing?" (16:37-16:53)
- The worked instance: LinkedIn companies, LinkedIn jobs, and Crunchbase, reached with two dedicated scrapers built in an AI scraper builder with a self-healing function, then "merge it all into one entities. Basic heuristics of those conflict, choose that over that." Output was a 100-company dataset. (16:53-17:28)
- The cost claim that follows: "Zero AI cost involved. There's no tokens." This is the mirror image of the same test's finding that search-based paths converged to similar total cost only because they "needed a lot of token burn… to actually structure that data so you can actually act on it and use it as something retrievable. So it's the same output." Direct extraction from a known-schema source skips both the discovery and the structuring. (12:42-12:57, 17:28-17:33)
- A second, less obvious saving: the ontology may already exist. "We think about knowledge graphs, we think about entities, but if you think about, for example, LinkedIn, the data is already structured in form of entities. There's an entity for a company, there's an entity for a job, and they're connected between them. Sometimes the ontology is already there." Where the source models your domain, entity extraction and graph construction reduce to a mapping. (18:08-18:25)
- Where it does not apply, from the same talk's own framing: this is for tasks that are "persistent and consistent," where the source set is stable. Ad-hoc, changing, or exploratory questions are exactly what search is good at — "if it's a one-time question, use AI search, it will be amazing" — and a fixed-source path inherits the [ceiling of a prebuilt index](a-prebuilt-context-vendor-cannot-answer-outside-its-index.md): a question outside the chosen sources has no answer. (19:25-19:46, 21:41-21:44)
- Two costs the source is candid about. The known-source path is where the maintenance burden moves — hence the self-healing scraper, and the wiki's separate page on [letting an agent build and maintain scrapers](let-agents-build-and-maintain-self-healing-scrapers.md). And the demonstration is deliberately small: "very specific task, very limited context, very limited situation… tread lightly," with the speaker also granting "this is not the most complicated of scenarios" about the already-structured ontology. (17:00-17:16, 17:45-17:58, 18:25-18:29)
- Access is the unstated prerequisite: the named sources are among the most aggressively bot-defended sites on the web, so "straight to the source" presumes the access layer in [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md). Removing the search middleman does not remove the access middleman.

- **The failure that makes this more than a cost optimization.** Routing through search is not only a wasted discovery step; it is a step with a bad stopping rule. An agent searching a store "finds something that they think is correct and then they stop" — so the search path can return a true answer built on one of the three documents that mattered, while a direct fetch of a known location returns the whole thing. Where the location is known, skipping search removes an error mode, not just a latency. The corollary is that answers should hand back their sources so the *next* hop is also a known location. See [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md) and [Attach Sources as Both a Correction Surface and a Continuation Pointer](attach-sources-as-a-correction-surface-and-a-continuation-pointer.md). ([Werry](../sources/20260827_qdAkxLoYNI8.md), 04:37-05:12, 10:35-11:13)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Let an Agent Build and Maintain Self-Healing Scrapers](let-agents-build-and-maintain-self-healing-scrapers.md)
- [A Prebuilt Context Vendor Cannot Answer Outside Its Index](a-prebuilt-context-vendor-cannot-answer-outside-its-index.md)
- [Find the Crossover Point Between Renting and Owning Context](find-the-crossover-point-between-renting-and-owning-context.md)
- [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md)
- [Context as a Service Is Vertical Search for Agents](context-as-a-service-is-vertical-search-for-agents.md)
- [Move Mandatory Brittle Tool Steps Outside the Agent Loop](move-mandatory-brittle-tool-steps-outside-the-agent-loop.md)
- [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md)
- [Attach Sources as Both a Correction Surface and a Continuation Pointer](attach-sources-as-a-correction-surface-and-a-continuation-pointer.md)

Sources:
- [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](../sources/20260814_Ot4OPrPH4xY.md), 12:42-12:57, 16:37-18:29, 19:25-19:46
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 04:37-05:12, 10:35-11:13
