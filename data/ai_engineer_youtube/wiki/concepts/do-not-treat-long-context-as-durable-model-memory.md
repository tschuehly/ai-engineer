# Do not treat long context as durable model memory

Summary: Long context windows can increase what a model can see, but they are not the same as reliable model memory. Larger prompts add latency, cost, and reasoning degradation, so teams should distinguish temporary activations from knowledge the model can retrieve or use efficiently across tasks.

Use when:
- Deciding whether to paste a whole corpus into a prompt, build retrieval, or adapt a model.
- Evaluating claims that million-token context windows make memory, RAG, or knowledge adaptation unnecessary.

Details:
- The source distinguishes full context, RAG, and weight updates as separate ways to inject knowledge into a model. Full context is the easiest path for bounded data, but it keeps knowledge in transient activations rather than durable model behavior. (02:35-03:16, 03:30-04:07)
- Full context has a serving cost: the talk cites a drop from roughly 10,000 output tokens per second with 1,000 context tokens to roughly 130 tokens per second with 128k context tokens. (04:11-05:08)
- Self-attention creates a quadratic pressure because tokens need to attend to one another; this becomes a memory and latency bottleneck as the prompt grows. (05:16-05:54)
- A long window can avoid hard failure while still failing to reason well. The speaker separates "not breaking" at many tokens from actually reasoning across large chunks, and cites context-rot behavior where performance worsens as extra context grows. (06:18-07:51)
- A measured qualification, not a refutation: Towards AI probed *single-fact* recall across a growing session transcript and found distinctive facts recovered consistently out to 800k tokens with no visible rot, while ambiguous facts (no distinguishing surface form) degraded to about half that. Within one session, on this model class, keeping the full history recalled specific details 95% of the time against 32% after summarizing — so for retrieval of distinctive details, the window outperformed the alternative rather than rotting. The claim this page makes still holds where it was made: across sessions the model is stateless, the serving cost of long prompts is real, and reasoning *across* a large span is a different task from pulling one fact out of it. ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 50:53-51:56, 53:16-54:33)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [RAG stacks need modular baselines instead of one fixed recipe](rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md)
- [Train long-tail knowledge into weights with curated synthetic data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)
- [Full History Recalls Details That Summaries Delete](full-history-recalls-details-that-summaries-delete.md)

Sources:
- [Jack Morris: Stuffing Context is not Memory, Updating Weights is](../sources/20251229_Jty4s9-Jb78.md), 02:35-07:51
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 50:53-51:56, 53:16-54:33
