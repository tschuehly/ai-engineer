# Do Not Outsource the Memory System

Summary: After a year of reverse-engineering consumer memory implementations, the conclusion drawn is that there is no single way to do memory — the shipped designs differ at every level — so memory is something built alongside the product and evolving with it, not a component bought from a vendor and bolted on.

Use when:
- Evaluating a drop-in memory SaaS or library for a product whose personalization is part of the value proposition.
- Being told that "memory is solved" by a particular architecture and needing the counter-evidence.
- Planning a product roadmap where memory has been scheduled as a later phase.

Details:
- The industry default is not what the flagships do: the assumption "including me" was RAG — chunk conversations, embed, vector store, semantic search on the incoming query — and "neither ChatGPT nor Claude really do this" (10:32-11:00).
- Spread across shipped systems, at the same moment in time: ChatGPT and Claude each run a background-synthesized profile but disagree on size, prose style, refresh interval, and visibility; Gemini attaches per-memory creation and last-updated timing logs; Claude Code, OpenClaw, and Hermes use Markdown files, heartbeats, knowledge bases, and skills (11:00-11:31).
- The conclusion drawn from that spread: "memory cannot be outsourced. If you're a serious team, you do not outsource memory. It is something that you build alongside your product. Your memory system evolves with your product and it cannot be thought of as an afterthought" (11:31-11:50).
- Supporting survey rather than proof: across top consumer AI products in different categories, each has some form of memory, none outsource it, all build in-house (11:50-12:08). This is a revealed-preference argument about what serious teams do, not a controlled comparison against outsourced alternatives.
- The mechanism behind the claim is visible in the rest of the talk: the design levers that matter — what is stored, how densely, how often it is rewritten, what is served on every turn, what the user can see and edit — are all product decisions with product-specific answers, and a vendor default fixes them for you.
- Read together with the compute framing, the argument sharpens: an outsourced memory system also fixes your update-versus-serving operating point, and that point is set by the vendor's economics rather than your traffic and margin.

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Budget Memory Between Update Cost and Serving Cost](budget-memory-between-update-cost-and-serving-cost.md)
- [Pair a Running Profile With On-Demand Conversation Search](pair-a-running-profile-with-on-demand-conversation-search.md)
- [Rank Agent Memory by Outcome Utility, Not Just Similarity](rank-agent-memory-by-outcome-utility-not-just-similarity.md)
- [Give Enterprise Agents Tiered Database Memory With an Escape Hatch](give-enterprise-agents-tiered-database-memory-with-an-escape-hatch.md)
- [Knowledge Graphs Make Agent Memory Traversable and Explainable](knowledge-graphs-make-agent-memory-traversable-and-explainable.md)

Sources:
- [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../sources/20260812_5ZGyKWjQDr0.md), 10:32-12:08
