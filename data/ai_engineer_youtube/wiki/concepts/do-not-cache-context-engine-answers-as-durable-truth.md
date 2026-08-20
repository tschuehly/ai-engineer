# Do Not Cache Context-Engine Answers as Durable Truth

Summary: Cache source-derived structures or retrieval aids carefully, but do not treat a context-engine answer as durable truth for future tasks. Code, docs, and rationale change, and reusing prior answers can pollute later context.

Use when:
- Designing persistence, memory, or caching for context engines and agent retrieval systems.
- Debugging stale or self-reinforcing answers in coding-agent workflows.

Details:
- The speaker calls answer caching a bad idea: similar future questions should not automatically receive the same prior context-engine answer. (24:42-24:57)
- Complete answers go stale because code changes, docs change, and the reasons behind decisions change. (24:58-25:08)
- Feeding prior answers into later answers can regress behavior toward previous mistakes; if a model was misbehaving, repeatedly adding its old output pollutes context. (25:10-25:28)
- A safer pattern is to recompute from current sources and use durable source-backed memories, graphs, and retrieval tools as inputs rather than treating generated conclusions as canonical. (19:10-19:41, 38:26-39:19)
- The boundary this page needs, from a source arguing the *opposite* direction of travel: Bright Data's Omer Primor makes the case for owning a collected corpus so "whatever retrieval happens later on from the agents… is free," and calls the result compounding — "owned context compounds while rented decays." That does not contradict this page, because what he owns is source-derived structured facts on a refresh schedule, not answers. His own decay measurements (social stale inside a day; news, finance, and retail mostly irrelevant after 30) are the reason the distinction holds: a stored *fact* has a knowable expiry tied to its source, while a stored *answer* has none. The rule that reconciles them is cache what you can re-derive and date-stamp; recompute what you concluded. (Ot4OPrPH4xY, 02:47-03:28, 19:46-20:05, 21:32-21:40)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Find the Crossover Point Between Renting and Owning Context](find-the-crossover-point-between-renting-and-owning-context.md)
- [Frequency, Not Volume, Drives Web-Context Cost](frequency-not-volume-drives-web-context-cost.md)

Sources:
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md), 19:10-19:41, 24:42-25:28, 38:26-39:19
- [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](../sources/20260814_Ot4OPrPH4xY.md), 02:47-03:28, 19:46-21:40
