# Share Codebase Indexes Across a Team With Merkle-Tree Diffing

Summary: A team of engineers mostly opens the same few codebases, so re-embedding each working copy from scratch is wasteful. Cursor uses Merkle (hash) trees to detect when a newly opened codebase is similar to one already indexed, copies the existing index, and re-chunks and re-embeds only the files that changed.

Use when:
- Indexing many near-duplicate working copies of the same repository (per developer, per branch).
- Reducing the upfront embedding cost that makes a persistent codebase index expensive to justify.
- Designing a multi-tenant code-index store that must keep one team's copied index secure.

Details:
- When a developer opens a new codebase or branch in Cursor, Cursor parses, chunks, and embeds the code to make it available for semantic search. (03:15-03:48)
- Observation: on a 100-engineer team, people open the same one or two codebases roughly 99% of the time, so re-chunking, re-embedding, and re-uploading from scratch on every open is expensive. (03:53-04:11)
- Mechanism: use Merkle trees (a crypto hash tree) to compute similarity between the codebases a team opens; if a new codebase is similar enough to an indexed one, copy over the existing index data and re-chunk and re-embed only the changed files. Turbopuffer is used to keep this copy-and-update secure across tenants. (04:11-04:39)
- Why the upfront index is worth it — measured semantic-search gains on Cursor's internal context benchmark (not public): ~12.5–13.5% average answer-accuracy increase across models, and almost 24% on the composer model (pre-composer-2). An online A/B test showed ~2.6% increase in code retention in large codebases and ~2.2% decrease in dissatisfied requests. (04:43-05:43)
- Reading those numbers: semantic search does not fire on every query, so aggregate A/B deltas look small even though the effect on the queries that do benefit is larger. (05:44-06:06)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Treat Embeddings as Cached Compute Decided by Query Volume](treat-embeddings-as-cached-compute-decided-by-query-volume.md)
- [Codebase Intelligence Needs Structural and Historical Signals](codebase-intelligence-needs-structural-and-historical-signals.md)

Sources:
- [RAG is dead, right?? - Kuba Rogut, Turbopuffer](../sources/20260609_UM6sFg_jdlE.md), 03:15-06:06
