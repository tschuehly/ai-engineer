# Distillation Is a Separate Step From Retrieval, and the Task Agent Will Not Do It

Summary: Retrieval returns pieces; understanding is the relation between pieces. An agent working a task can find every relevant document and still not know how the dependencies interact or how the architecture constrains what it is about to write, because assembling that picture is work someone has to have done — and a task-time search loop has neither the budget nor the incentive to do it.

Use when:
- An agent retrieves the right files and still proposes a change that violates a constraint spread across several of them.
- Deciding whether a context system needs a synthesis layer or only a better index.
- Choosing what artifact to produce from a corpus: chunks, summaries, or explicit cross-source structure.
- Arguing about whether "we have RAG" means the context problem is solved.

Details:
- The claim in the speaker's words: agents "don't distill understanding. They can look around, they can find information, but they don't understand how all the pieces fit together… without doing that leg work ahead of time." ([Werry](../sources/20260827_qdAkxLoYNI8.md), 05:12-05:34)
- What specifically goes missing is forward-looking, not just factual: "they don't understand how your dependencies interact with each other and how your architecture and sort of future planning is going to scope the work that it does next." The synthesis constrains the *next* action, which is why discovering it late is expensive. (05:34-05:52)
- The demo's positive form is a synthesis artifact rather than a retrieved one. A question about an internal component returned an architecture explanation with a diagram that "doesn't exist. It just figures it out based on the way the code operates today," together with proposals for future architecture. The deliverable is a relation over the corpus, and no document in the corpus contains it. (07:53-08:33)
- Why the task agent is the wrong place to do it. Distillation is corpus-wide and task-independent; task work is narrow and deadline-bound. Asking a coding agent to build the picture inside the task means paying for it on every task, in the condition least able to afford it, and stopping as soon as the task looks answerable — which is exactly the stopping failure in [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md).
- The unresolved design question this source leaves open, and it is load-bearing: the talk does not say whether the distillation happens at ingest or at question time. If at ingest, it is a precomputed derivative that can go stale like any cache. If at question time, it is recomputed per question and costs more but tracks the sources. The wiki's rule for the second case is already written — cache what you can re-derive and date-stamp it, recompute what you concluded — and a synthesis is a conclusion. See [Do Not Cache Context-Engine Answers as Durable Truth](do-not-cache-context-engine-answers-as-durable-truth.md).
- Convergent evidence for the *shape* of the answer, from a different scale: personal-knowledge pipelines that materialize backlinks and entity indexes at ingest are making the same bet — spend once, in an unhurried pass, on relations that a query-time search would have to rediscover. See [Materialize Backlinks at Ingest With Key-Term Search](materialize-backlinks-at-ingest-with-key-term-search.md) and [Search Engines Shift Retrieval Work to Ingestion](search-engines-shift-retrieval-work-to-ingestion.md).
- Consequence for humans, which the talk states plainly and which survives full automation: "the human layer hasn't gone away… ultimately the accountability stops with us. When you hit merge on a PR, you need to understand what it's doing and you need to understand how the architecture works." The synthesis is a deliverable for the reviewer, not only for the agent. (07:14-07:53)
- Limit: this is a vendor demo, and the generated diagram is not verified against the system it describes. What the source supports is that the *artifact type* is different from a retrieval result, not that generated syntheses are accurate.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md)
- [Do Not Cache Context-Engine Answers as Durable Truth](do-not-cache-context-engine-answers-as-durable-truth.md)
- [Materialize Backlinks at Ingest With Key-Term Search](materialize-backlinks-at-ingest-with-key-term-search.md)
- [Search engines shift retrieval work to ingestion](search-engines-shift-retrieval-work-to-ingestion.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Distill Behaving as if the Corpus Were in Context, Not the Documents](distill-behaving-as-if-the-corpus-were-in-context.md)

Sources:
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 05:12-05:52, 07:14-08:33
