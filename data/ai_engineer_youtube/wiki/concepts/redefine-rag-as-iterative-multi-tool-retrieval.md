# Redefine RAG as Iterative Multi-Tool Retrieval, Not Vector Search

Summary: "RAG is dead" only holds against a strawman where RAG means a single vector-search call stuffed into context. Retrieval in retrieval-augmented generation spans vector search, full-text/BM25, grep, glob, regex, and filters used iteratively by an agent — which is exactly what "agentic search" describes, so agentic search is a superset of RAG, not its replacement.

Use when:
- Someone claims RAG is dead because agents can just grep, or because context windows are now huge.
- Deciding which retrieval primitives to expose to an agent and how to frame the retrieval layer.
- Distinguishing "simple RAG" (one-shot vector lookup) from agentic retrieval in a design discussion.

Details:
- The "RAG is dead, agentic file search is all we need" discourse spiked on X in late 2025 / early 2026, but Google search volume for "RAG" capped in 2024, settled for about a year, then hit a new inflection point mid-2025 and went "through the roof" — usage and discourse moved in opposite directions. (00:54-01:36)
- The strawman: people equate RAG with simple vector search (embed a corpus, embed the query, return top-k, pass to the LLM) and equate "agentic search" with filesystem grep (Claude Code / Codex). Both definitions are too narrow. (01:44-02:43)
- Turbopuffer's reframe: break RAG into retrieval-augmented generation. Retrieval is not just vector search — it is vector search, full-text search (BM25), grepping, globbing, regex, and basic filters; "augmented generation" is just passing results into the LLM. Agentic search is "giving the agent a set of tools to progressively and iteratively find and reason over context," so the two terms collapse into the same thing. (02:00-02:56)
- Simple RAG (one vector call → context window) worked in 2023 / early 2024; sophisticated customers now do agentic retrieval: many calls, reasoning across several steps, searching semantically or full-text as needed, and fetching only what each step requires. Retrieval becomes "super iterative" — agents search to understand and understand to search. (08:38-09:42)
- Long context does not kill retrieval; it raises the need for staged retrieval. Jeff Dean's framing: even at a trillion-token context window you need a lightweight mechanism to narrow trillions of tokens down to the right millions — "you don't need a trillion at once, you need the right million." Turbopuffer customers embed trillions of tokens, and the job is getting down to the right 100K / 10K / million for the context window. (09:42-10:42)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Treat Embeddings as Cached Compute Decided by Query Volume](treat-embeddings-as-cached-compute-decided-by-query-volume.md)
- [RAG stacks need modular baselines instead of one fixed recipe](rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md)
- [Hybrid Retrieval Combines Lexical, Sparse, Dense, and Reranking Signals](hybrid-retrieval-combines-lexical-sparse-dense-and-reranking-signals.md)
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)

Sources:
- [RAG is dead, right?? - Kuba Rogut, Turbopuffer](../sources/20260609_UM6sFg_jdlE.md), 00:54-10:42
