# Treat Embeddings as Cached Compute Decided by Query Volume

Summary: Building an embedding/semantic index is a way to cache retrieval compute, so whether to index or rediscover per session is a query-volume decision rather than a correctness one. Indexing pays off when the same corpus is searched repeatedly across sessions, developers, and days; one-off discovery does not amortize the index.

Use when:
- Deciding whether a coding or retrieval agent should grep-read-assess per session or build a persistent semantic index.
- Explaining why two production agents (Claude Code vs Cursor) make opposite retrieval choices without either being wrong.
- Estimating whether the upfront cost of parsing, chunking, and embedding a corpus will be repaid.

Details:
- Claude Code uses per-session discovery: grep → read → assess → repeat until the agent reaches a "happy state" with enough understanding to continue. There is no index, so the discovery cost is paid every run. Boris Cherney (cited as the founding father of Claude Code) said early iterations used RAG with a local vector DB but it "just didn't really work out," so Claude Code does not use vector search. (06:08-06:30)
- The same understanding question (e.g., "how does metadata filtering work?") gets rediscovered by 10 agents across 10 days and 10 developers, repeating the identical grep/read/assess steps each time; one such sub-step alone can cost ~6,000 tokens. (07:04-07:36)
- Cursor's trace pays a one-time upfront cost to parse, chunk, and embed the codebase, then exposes a lightweight semantic-search tool at runtime; the agent queries "how is metadata filtered?" and gets results cheaply, saving tokens, time, and money and making the agent faster. (07:47-08:14)
- The clarifying frame: embeddings and semantic search are *cached compute*. Whether to cache (index) depends on query volume — repeated retrieval of the same corpus amortizes the index, while a single discovery pass does not. Claude Code's grep-per-session is "not wrong, it is a deliberate tradeoff," and the indexed approach is the opposite tradeoff. (06:30, 08:14)
- Evidence the cache pays off: Turbopuffer team members who were heavy Claude Code users switched to Cursor for speed once composer-2 plus its semantic understanding became "really really good." (08:19-08:36)
- An earlier benchmark talk by the same speaker is where this cached-compute frame was first articulated, and it adds direct evidence that the cache improves retrieval quality, not just speed: adding a Turbopuffer semantic-search tool to Claude Code raised file precision from a 65% baseline to 87% — cutting wasted file reads from 1-in-3 to 1-in-8 — on a 50-task ContextBench run. The caveat is that the cache only pays off if the model knows when to query it (see "Native Tool Integration Beats a Bolted-On Tool the Model Can't Time"). (zKk7sDMGDEQ, 06:26-07:30, 09:55-10:36)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Redefine RAG as Iterative Multi-Tool Retrieval, Not Vector Search](redefine-rag-as-iterative-multi-tool-retrieval.md)
- [Share Codebase Indexes Across a Team With Merkle-Tree Diffing](share-codebase-indexes-across-a-team-with-merkle-tree-diffing.md)
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Codebase Intelligence Needs Structural and Historical Signals](codebase-intelligence-needs-structural-and-historical-signals.md)
- [Evaluate Agent Retrieval by Trajectory, Not Task Success](evaluate-agent-retrieval-by-trajectory-not-task-success.md)
- [Native Tool Integration Beats a Bolted-On Tool the Model Can't Time](native-tool-integration-beats-a-bolted-on-tool.md)

Sources:
- [RAG is dead, right?? - Kuba Rogut, Turbopuffer](../sources/20260609_UM6sFg_jdlE.md), 06:08-08:36
- [Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer](../sources/20260603_zKk7sDMGDEQ.md), 02:34-04:08, 06:26-07:30
