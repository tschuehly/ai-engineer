# Sequence RAG Techniques by Loss Analysis and Complexity-Adjusted Impact

Summary: RAG work should start with product outcomes, query sets, a baseline, and loss analysis before choosing techniques. Add complexity only when observed failures show that the expected quality gain justifies the implementation and operating cost.

Use when:
- Deciding whether to add BM25, embeddings, rerankers, custom models, fan-out, distillation, or product fallback to a RAG system.
- A team is debating retrieval techniques before it has inspected failing queries.

Details:
- The quality-engineering loop starts from a launch bar and staged query sets, then baselines the simplest approach, analyzes what broke, and chooses the next intervention from the toolbox (01:56-02:59).
- Technique-first debates are a warning sign: before asking whether the system needs BM25 or vector retrieval, the team should know what it is trying to do, which query sets matter, and where those queries fail (03:05-03:21).
- Complexity-adjusted impact favors the easiest useful intervention first; BM25 is cheap enough to try early, while custom embeddings or distillation require evidence that simpler techniques cannot hit the quality bar (03:24-04:08, 16:13-17:10).
- The empirical loop should continue after each layer: baseline, analyze losses, inspect which easy or medium changes remain, and avoid hard work too far ahead of the quality curve (19:18-19:49).

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use Fast Query-Document Evals for Retrieval Changes](use-fast-query-document-evals-for-retrieval-changes.md)
- [RAG Stacks Need Modular Baselines Instead Of One Fixed Recipe](rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md)

Sources:
- [Layering every technique in RAG, one query at a time - David Karam, Pi Labs (fmr. Google Search)](../sources/20250729_w9u11ioHGA0.md), 01:17-04:08, 19:18-19:49
