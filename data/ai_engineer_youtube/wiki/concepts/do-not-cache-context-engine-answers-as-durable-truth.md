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

- **The distinction gets harder when the artifact is a synthesis rather than an answer.** Werry's demo returns an architecture diagram that "doesn't exist. It just figures it out based on the way the code operates today" — a relation over the corpus, not a retrieved document, and not obviously either a fact or a conclusion. The talk does not say whether that synthesis is built at ingest or per question, which is exactly the fork this page cares about: precomputed, it decays like any cache and needs a date stamp and a refresh trigger; recomputed, it tracks the sources and costs more every time. The rule stated here still resolves it — cache what you can re-derive and date-stamp, recompute what you concluded — but a synthesis sits close enough to the line that a system should decide explicitly rather than by default. See [Distillation Is a Separate Step From Retrieval, and the Task Agent Will Not Do It](distillation-is-a-separate-step-from-retrieval.md). ([Werry, Aug 2026](../sources/20260827_qdAkxLoYNI8.md), 05:12-05:52, 07:53-08:33)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Find the Crossover Point Between Renting and Owning Context](find-the-crossover-point-between-renting-and-owning-context.md)
- [Frequency, Not Volume, Drives Web-Context Cost](frequency-not-volume-drives-web-context-cost.md)
- [Distillation Is a Separate Step From Retrieval, and the Task Agent Will Not Do It](distillation-is-a-separate-step-from-retrieval.md)

Sources:
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md), 19:10-19:41, 24:42-25:28, 38:26-39:19
- [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](../sources/20260814_Ot4OPrPH4xY.md), 02:47-03:28, 19:46-21:40
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 05:12-05:52, 07:53-08:33
