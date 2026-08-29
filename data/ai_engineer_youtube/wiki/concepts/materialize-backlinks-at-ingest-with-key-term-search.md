# Materialize Backlinks at Ingest With Key-Term Search

Summary: Instead of computing relatedness at query time, have the enrichment pass find related documents by plain key-term search and write the links into the document itself — the corpus becomes navigable by following links, and the retrieval index is the file tree rather than a vector store.

Use when:
- Building a personal or team knowledge base where the primary consumer is a human browsing, or an agent reading files, rather than a similarity query.
- Deciding whether a note store needs embeddings at all.
- Turning a flat folder of captured material into something that supports "what else have I written about this?"

Details:
- The whole mechanism, stated without ceremony: "to find back links, use some file calls, find related notes using key term search, and put them into the bottom. So then we have that interconnected web." No embedding model, no index build, no vector database. ([LLM Knowledge Bases](../sources/20260812_I3bpdgFJCUY.md), 07:38-07:47)
- Links accumulate rather than being recomputed: "This is related to that other podcast you were listening to. Let's go ahead and link them together. And that web gets tighter and tighter the more things that you get down." Each ingest pass adds edges, so density grows with corpus size instead of degrading. (06:16-06:26)
- The payoff is browsing, not recall@k. Notes on the same book taken weeks apart end up linked, "so I'm not hunting around where did I save in my Apple Notes the last time I wrote about this like two weeks ago. It's able to find it by related topics… it kind of invents a Wikipedia rabbit hole of your own thoughts." (09:20-09:53)
- Materializing at write time is a deliberate cost shift: link-finding runs once per document, in a background pass with no latency budget, instead of on every read. The talk pairs it with a slow scheduled runner precisely because the expensive work is allowed to be slow — see [Run Recurring Knowledge Jobs in a Cloud Sandbox With Sync-Down/Sync-Back](run-recurring-knowledge-jobs-in-a-cloud-sandbox-with-sync-down-sync-back.md).
- Key-term search is weaker than embeddings at exactly the thing embeddings are for — connecting documents that share meaning but no vocabulary. This source presents no comparison, so treat the choice as a complexity tradeoff, not a demonstrated equivalence. The related wiki argument that a personal store should "forget the infrastructure you think you need" (no vector DB, no knowledge graph, files plus references only) is the stronger version of the same claim, and it too is an argument from complexity rather than from measurement. See [Build a File-Based Research Wiki With Progressive-Disclosure Retrieval](file-based-research-wiki-with-progressive-disclosure-retrieval.md).
- The counterweight in the wiki is real: when Towards AI measured agentic browsing over a generated wiki against a *tuned* hybrid retriever, recall was identical and latency 50% worse. That result is about an agent navigating structure to answer questions; it is not about a human clicking backlinks, which is the use this page describes. See [Measure Agentic Knowledge-Base Browsing Before Adding It](measure-agentic-knowledge-base-browsing-before-adding-it.md).
- The links are written to the bottom of the note, alongside tags, a recovered source URL, and an enrichment timestamp, by a single `enrich note` skill — so backlinking is one field of a broader enrichment record rather than a standalone system. (05:53-06:26)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Build a File-Based Research Wiki With Progressive-Disclosure Retrieval](file-based-research-wiki-with-progressive-disclosure-retrieval.md)
- [Generate an Entity Wiki Over Your Own Notes](generate-an-entity-wiki-over-your-own-notes.md)
- [Measure Agentic Knowledge-Base Browsing Before Adding It](measure-agentic-knowledge-base-browsing-before-adding-it.md)
- [Personal Knowledge Bases Become Agent Context Substrates](personal-knowledge-bases-become-agent-context-substrates.md)
- [Constrain Agent-Generated Tags to a Reference Vocabulary](constrain-agent-generated-tags-to-a-reference-vocabulary.md)
- [Hydrate a Trigger Event to Its Entity Once and Persist the Mapping](hydrate-a-trigger-event-to-its-entity-once-and-persist-the-mapping.md)

Sources:
- [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../sources/20260812_I3bpdgFJCUY.md), 05:53-06:26, 07:38-07:47, 09:20-09:53
