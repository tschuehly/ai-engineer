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

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [RAG stacks need modular baselines instead of one fixed recipe](rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md)
- [Train long-tail knowledge into weights with curated synthetic data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)

Sources:
- [Jack Morris: Stuffing Context is not Memory, Updating Weights is](../sources/20251229_Jty4s9-Jb78.md), 02:35-07:51
