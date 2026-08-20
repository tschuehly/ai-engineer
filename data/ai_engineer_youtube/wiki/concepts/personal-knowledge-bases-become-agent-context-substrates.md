# Personal Knowledge Bases Become Agent Context Substrates

Summary: A personal Markdown knowledge base can become an agent context substrate when search, memory, tagging, and link analysis connect new inputs to existing notes. The value is not only storage, but surfacing forgotten context at the moment new material arrives.

Use when:
- Connecting an agent to Obsidian, Markdown notes, bookmarks, research folders, or personal project records.
- Designing ingestion flows that enrich saved links instead of leaving them as passive bookmarks.

Details:
- The source describes an Obsidian vault with about 3,000 Markdown notes spanning work, personal material, tasks, projects, research, articles, and an inbox of links (04:53-05:47).
- OpenClaw uses search and memory over the vault, including normal search, Obsidian-oriented search, and workspace memory, so the agent can connect current work with prior notes (05:50-06:17).
- Link-inbox automation can analyze a tweet, thread, article, or YouTube video, add tags and context, inspect related vault content, and add connections to other notes (07:30-08:07).
- A useful agent memory workflow surfaces related prior notes when a new bookmark arrives, turning forgotten saved material into active context (08:07-08:45).

- A second shipped instance gives the substrate a full pipeline shape, and its ordering is the lesson: capture → enrich → generate → visualize, with the human doing only the first step. Ben Holmes dictates raw notes, an `enrich note` skill adds tags, a researched source URL, an enrichment timestamp, and key-term backlinks, a second pass generates an entity wiki of people, concepts, organizations, and sources over a stated focus area, and an agent-written HTML graph view sits on top. The whole thing runs nightly in a cloud sandbox that syncs the Markdown down and back. His justification for generating every layer above capture: "all I have time to do is generate the raw ingredients not connecting it all together myself." ([LLM Knowledge Bases](../sources/20260812_I3bpdgFJCUY.md), 01:29-02:39, 11:27-11:37)
- The reason a user-owned substrate is worth the effort is that vendor memory does not accumulate across the stack. Shlok Khemani's personal stack of chatbots, assistants, vertical applications, agents, and hardware devices each builds a private memory of him, shares none of it, and forces him to "rebuild context within every single product from scratch" and update all of them by hand whenever his life changes — while email, calendar, and photos stay unread by all of them. A personal knowledge base is the one copy of that context the user controls. ([Lessons from Studying Every Memory System](../sources/20260812_5ZGyKWjQDr0.md), 17:34-18:21)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Memory Quality Is Capped by the Context It Can Reach](memory-quality-is-capped-by-the-context-it-can-reach.md)
- [Optimize Capture Bandwidth Before Note Organization](optimize-capture-bandwidth-before-note-organization.md)
- [Materialize Backlinks at Ingest With Key-Term Search](materialize-backlinks-at-ingest-with-key-term-search.md)
- [Generate an Entity Wiki Over Your Own Notes](generate-an-entity-wiki-over-your-own-notes.md)

Sources:
- [I Gave an AI Agent the Keys to My Life (Here's What Happened) - Radek Sienkiewicz (@velvetshark-com)](../sources/20260502_sJ2jc7leKBk.md), 04:53-08:45
- [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../sources/20260812_5ZGyKWjQDr0.md), 17:34-18:21
- [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../sources/20260812_I3bpdgFJCUY.md), 01:29-02:39, 11:27-11:37
