# Generate Disposable Visualizations to Find Gaps in Your Own Corpus

Summary: Asking an agent for a bespoke HTML view over your own data is now cheap enough that the view is disposable — you request a graph, restyle it on a whim, add a habit chart — and its value is diagnostic (what am I not writing about?) rather than navigational.

Use when:
- A corpus has grown past the point where reading or clicking through it gives you a sense of its shape.
- You are about to install or evaluate a visualization tool for data you already own in plain files.
- You want a bird's-eye read on a knowledge base, backlog, or note store rather than another way to search it.

Details:
- The ask is one prompt, and it names the goal rather than the implementation: "I want to take all these markdown files and I want you to just build with HTML and Tailwind some sort of graph view. So instead of me clicking around a wiki and following a bunch of links, I want to see a bird's eye view of everything that we're writing down here. Figure out common patterns and common areas of interest." ([LLM Knowledge Bases](../sources/20260812_I3bpdgFJCUY.md), 17:52-18:34)
- The cost claim that makes it disposable: "this is not a tool that you have to install. By the way, I told an agent, build this for me. So you can do that now." A one-off view that would previously have been a tool decision becomes a prompt. (18:34-18:41)
- Disposability demonstrated live rather than argued: "can you put it in space? I don't know. Let's put in space. How about that? Now it's in space… it looks a little bit more like a star constellation." Restyling costs a sentence, which is what distinguishes this from adopting a visualization product. (19:20-19:36)
- The payoff is diagnostic. The graph clustered his notes into books, startup founding, AI and engineering, and faith and scripture, with a center of "very stray thoughts," and the stated use is "just to get an idea of what you're actually interested in and where you have gaps in your thinking, but it's also useful if you want to drill down." A search interface answers questions you already have; an aggregate view shows you the shape of what you have and have not written. (18:41-19:20)
- Making nodes clickable through to the underlying note is what keeps it honest — the visualization stays anchored to the artifacts rather than becoming a separate summary you have to trust. (19:00-19:08)
- Generalizes beyond graphs: he also generated a GitHub-style contribution chart as a note-writing habit tracker — "if you're trying to build up a habit tracker of how often you're writing notes on certain things, you can invent one of those… Clearly, I don't have a super consistent habit, but it's building" — and closes with "whatever you want to put together, you can just ask an agent to do it." Meta-data about your own capture rate is a second, cheaper diagnostic than the content view. (19:37-19:56)
- This is the fully generative end of the agent-UI spectrum, and the tradeoffs there apply: maximum flexibility, no design-system consistency, and model-written code that is untrusted by default. What makes it safe *here* is the setting — a personal view over your own local files, rendered for you, not third-party UI shipped to users. See [Place Agent UI Generation on a Static–Declarative–Generative Spectrum](place-agent-ui-on-the-static-declarative-generative-spectrum.md).
- Caveat: nothing is validated. A generated clustering is an artifact of whatever the agent decided relatedness means, and no check is offered that the clusters or the "gaps" it implies are real. Use it to generate hypotheses about your corpus, not conclusions.

Related topics:
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Place Agent UI Generation on a Static–Declarative–Generative Spectrum](place-agent-ui-on-the-static-declarative-generative-spectrum.md)
- [Generate an Entity Wiki Over Your Own Notes](generate-an-entity-wiki-over-your-own-notes.md)
- [Materialize Backlinks at Ingest With Key-Term Search](materialize-backlinks-at-ingest-with-key-term-search.md)
- [Sandboxed code execution turns model reasoning into inspectable computation](sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md)

Sources:
- [LLM Knowledge Bases: a practical guide — Ben Holmes, Warp](../sources/20260812_I3bpdgFJCUY.md), 17:52-19:56
