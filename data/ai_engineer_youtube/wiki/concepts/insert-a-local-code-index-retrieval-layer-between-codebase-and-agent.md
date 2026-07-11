# Insert a Local Code-Index Retrieval Layer Between the Codebase and the Coding Agent

Summary: Instead of letting a coding agent send whole files, put a local retrieval/index layer between the codebase and the agent that returns only the small relevant code pieces — via AST-aware chunking, parallel hybrid search, compression, a call-graph relationship layer, and a cheap relevance gate — and share one index (plus memory) across all your coding tools.

Use when:
- A coding agent ships too much context per query and you want to cut input tokens (see the input-dominates-cost argument) without changing the model.
- Building or evaluating a codebase-retrieval layer and deciding what pipeline stages actually earn their keep.
- Choosing between an LLM self-judge and a deterministic heuristic for gating whether retrieved code is relevant.
- Multiple coding tools each re-discover the same codebase from scratch and you want a shared, tool-agnostic index.

Details:
- Placement: a local search layer "sits between your code base and the AI"; instead of sending whole files, the agent searches the index and gets back only the small piece of code it actually needs. Everything runs on the machine — nothing goes to the cloud (a privacy plus).
- Five-step pipeline: (1) **AST-aware chunking** into meaningful units — functions, classes, methods — "not random chunks"; (2) **parallel hybrid search** — run a semantic-by-meaning search and a keyword-by-exact-name search at the same time and combine ("this is where the big saving comes from"); (3) **compression** — keep only the function name + description, cutting a 50-line function to five lines; (4) **call-graph relationship layer** — track which function calls which so finding one piece surfaces everything connected to it across files; (5) **relevance gate** — score every result and drop low-scoring ones ("no bad context").
- Why hybrid, not one search: meaning-based search finds related ideas but misses exact names (searching "authenticate user function" may return a different auth function); word-based search nails exact names but misses related ideas ("login flow" misses "sign in"). Alone each misses ~1 in 4 results; together ~1 in 10 — "they fix each other's weakness spots." (Corroborates the general lexical-vs-vector split, now on code.)
- The hard part is the relevance gate — knowing when retrieval is wrong, because bad results yield a "confident wrong answer… worse than no answer." An LLM judging its own results was too slow (+2-3 s/query); a fixed score threshold was too crude (short queries score low even on a perfect match). What worked: a simple weighted formula — **50% meaning + 30% keyword + 20% recency** — with a limit that adapts to the current results, running in ~0.4 ms with no extra AI calls. Lesson: "simple formula beats the complex model most of the time" (echoing "choose speed over perfection," a small fast embedding model, and re-indexing under a second).
- One shared index + memory: each tool (Claude Code for hard problems, Cursor for quick edits, Copilot for completions) normally "starts fresh every time" and shares nothing; a single shared index all tools connect to, plus a memory layer, lets a lesson persist across tools/sessions — "explain the code base once."
- Results and honest limits: on FastAPI (53 files, 20 questions) tokens fell 83K→4.9K/question (94%, or 523/question with compression) at ~90% right-code accuracy; across 247 real queries, 12.4M tokens (~$186) saved, 84% from the search layer and the rest from compression. But 94% is the **worst case** measured against a full-file baseline — real tools "are already smarter than that," so real savings are lower — and the approach breaks on **big mixed codebases**: on a 396-file project recall "dropped almost zero." It works when files each do one thing and struggles when files do many. Open-sourced as Code Context Engine (`CCE`).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Cut coding-agent cost by fixing the input, not the model or output](cut-coding-agent-cost-by-fixing-the-input-not-the-model-or-output.md)
- [Hybrid Retrieval Combines Lexical, Sparse, Dense, and Reranking Signals](hybrid-retrieval-combines-lexical-sparse-dense-and-reranking-signals.md)
- [Treat Embeddings as Cached Compute Decided by Query Volume](treat-embeddings-as-cached-compute-decided-by-query-volume.md)
- [Share Codebase Indexes Across a Team With Merkle-Tree Diffing](share-codebase-indexes-across-a-team-with-merkle-tree-diffing.md)
- [Codebase Intelligence Needs Structural and Historical Signals](codebase-intelligence-needs-structural-and-historical-signals.md)

Sources:
- [We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco](../sources/20260628_dRmWYHuIJxM.md), 03:20-10:05
