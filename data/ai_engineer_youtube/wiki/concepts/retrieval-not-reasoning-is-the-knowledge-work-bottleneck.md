# Retrieval, Not Reasoning, Is the Knowledge-Work Bottleneck

Summary: Model reasoning has improved far faster than retrieval, so for knowledge tasks (legal, finance, deep research) the limiter is access to the right documents, not the model's ability to reason over them. The "Oracle gap" quantifies this: measure the score a model gets when handed the correct documents, then measure it over the real noisy corpus, and the difference is retrieval loss you can recover by upgrading the search tool rather than the model.

Use when:
- Deciding whether to invest in a bigger/reasoning-heavier model or in better retrieval for a RAG or deep-research product.
- Diagnosing why a strong model underperforms on a knowledge task despite good reasoning benchmarks.
- Building an eval that separates retrieval quality from reasoning quality.

Details:
- The framing: LLM reasoning has grown roughly exponentially (GPT-3.5 → GPT-5) while search has improved "very very slowly" over ~20 years, and retrieval tools are "the main access pattern for this reasoning" to reach real knowledge — so the divergence (Mixedbread's "knowledge gap") makes retrieval the binding constraint for work beyond code (00:22-01:16).
- Oracle performance = "the maximum theoretical performance of the models if you would put in the right documents with the question." Measured: 93% on BrowseComp (Plus) and 64% on FinanceQA Pro — the reasoning ceiling is high (01:57-02:34).
- Over the real corpus, Codex with its default tools collapses to single digits (~9 points on BrowseComp, ~8 on FinanceQA Pro): "the bottleneck here is not the reasoning, it's the access to the right knowledge it needs to answer this question" (02:34-03:17).
- The gap is recoverable at the tool layer, not the model layer: dropping in Mixedbread's late-interaction search as a single search tool brought GPT-5 within ~3 points of Oracle on BrowseComp and "almost completely closed the gap" on FinanceQA Pro (03:21-03:47).
- Benchmarks used: BrowseComp (OpenAI, open-web) → BrowseComp Plus is the fixed 100k-document corpus version; FinanceQA Pro ("Office QA Pro" in the ASR, by Databricks) spans ~100 years of US treasuries with complex questions (01:26-02:11).
- Practical corollary: an Oracle-vs-real-corpus delta is a cheap diagnostic — a large delta says spend on retrieval (better search tool, query quality, indexing), a small delta says spend on reasoning or the answer model.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Co-Design Agents to Write Natural-Language Queries for Strong Retrieval](co-design-agents-to-write-natural-language-queries-for-strong-retrieval.md)
- [Evaluate Agent Retrieval by Trajectory, Not Task Success](evaluate-agent-retrieval-by-trajectory-not-task-success.md)
- [Redefine RAG as Iterative Multi-Tool Retrieval, Not Vector Search](redefine-rag-as-iterative-multi-tool-retrieval.md)
- [Agents Punish Bad Data and Need Question and Tracking Data Foundations](agents-punish-bad-data-and-need-question-and-tracking-data-foundations.md)

Sources:
- [How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI](../sources/20260707_1IdzkRVmWAA.md), 00:22-03:47
