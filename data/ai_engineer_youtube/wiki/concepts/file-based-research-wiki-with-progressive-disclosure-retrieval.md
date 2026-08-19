# Build a File-Based Research Wiki With Progressive-Disclosure Retrieval

Summary: A personal research memory can be built entirely from plain Markdown files plus a reference index — no vector or graph database — by layering three tiers (immutable raw sources, a catalog index, and an LLM-generated wiki of derivatives) and retrieving cheapest-first: read the index, then a source's executive summary, then wiki derivatives, and only fall through to a raw source when nothing else answers.

Use when:
- Turning thousands of notes, docs, videos, and repos into durable context an agent can reuse across sessions and projects.
- Deciding whether a personal/lightly-used knowledge base needs a vector DB, knowledge graph, or semantic search — or whether files and references suffice.
- Designing a token-efficient read path so an agent does not load whole raw sources when a summary would do.

Details:
- Three layers: `raw/` holds immutable copies of every source (you never touch them); an `index.yaml` catalogs all data with per-source summaries and metadata (origin, title, authors, date); `wiki/` holds LLM-generated derivatives — a *source page* (an expanded executive summary of each raw source, computed once at ingestion), plus concepts, entities, comparisons, notes, and open questions. One example index carried 10 sources and 38 derived wiki pages. (19:37-22:16)
- "Forget the infrastructure you think you need" — vector DBs, knowledge graphs, semantic/text search "add a lot of complexity, especially for a personal wiki you want to use very lightly." Build on files + references only; the index is a simple catalog of references, not a database. (19:37-20:17)
- Progressive-disclosure retrieval (cheapest-first): the agent reads the index summary/metadata → the source's executive summary (often enough, then it stops) → wiki derivatives (concepts/entities/notes/comparisons) → and only if still unanswered does it read the whole raw source. Pure referencing plus this hierarchy is what makes retrieval token-efficient. (22:49-24:04)
- The wiki is "alive": every question the user asks can spawn a new concept/note/comparison file and is tracked in a log, so the store evolves from *use*, not only from ingestion — "every question leaves a trace." It is never frozen; you can ingest a new custom link or run another deep-research round at any point. (24:04-25:01)
- The derived wiki does not sit over the *entire* second brain. The raw personal vault (Obsidian, organized with Tiago Forte's PARA method) is an immutable snapshot the LLM never edits; each project scopes its own wiki via a deep-research pass. "The project is the work, and your second brain is the research." (25:01-27:04)
- Ingestion can target the public web, personal sources (Obsidian/Readwise/NotebookLM), or code: pointing the loop at three harness repos produced per-repo architecture notes plus cross-repo comparisons and extracted "key architectural decisions" — a wiki good enough to design your own harness from. (31:58-34:24)
- Known gaps (by design a builder tool, not a product): source provenance/freshness is hard — "it's hard to know which sources are outdated or weak or strong" — and the next priorities are stronger *linting* and better *memory compaction*, which the authors call genuinely hard and fast-moving. (36:49-39:16)
- The same author later shipped and *measured* this structure inside a product, with a mixed verdict worth carrying back. Towards AI's AI tutor uses the identical three-tier layout — `raw` markdown, a `generated` title index, and an LLM-written `wiki` of topic pages built offline by Claude Code — with the agent reading a ~450-token index first and escalating index → chunk → raw file only when needed. But when they measured the browse tool against their tuned hybrid retriever on real student questions, recall was identical and latency was 50% worse. The cheapest-first *structure* remains sound; what did not hold in that setting was the assumption that an agent browsing the structure beats a well-tuned retriever over the same content. ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 13:01-14:52, 28:00-29:20, 31:15-32:18)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Personal Knowledge Bases Become Agent Context Substrates](personal-knowledge-bases-become-agent-context-substrates.md)
- [Externalize Agent State to Files and Reset Instead of Compact](externalize-agent-state-to-files-and-reset-instead-of-compact.md)
- [Use a Document Outline as the Retrieval Index for Chunkless Agentic RAG](use-a-document-outline-as-the-retrieval-index-for-chunkless-agentic-rag.md)
- [Do Not Treat Long Context as Durable Model Memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Choose the Research Tool by Reuse and Ownership, Not Just Speed](choose-the-research-tool-by-reuse-and-ownership.md)
- [Measure Agentic Knowledge-Base Browsing Before Adding It](measure-agentic-knowledge-base-browsing-before-adding-it.md)

Sources:
- [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](../sources/20260626_ZRM_TfEZcIo.md), 19:37-27:04, 31:58-34:24, 36:49-39:16
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 13:01-14:52, 28:00-29:20, 31:15-32:18
