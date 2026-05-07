# Evaluating AI Search: A Practical Framework for Augmented AI Systems - Quotient AI + Tavily

Source: [Evaluating AI Search: A Practical Framework for Augmented AI Systems - Quotient AI + Tavily](https://www.youtube.com/watch?v=wRJD0inpmjU)
Uploaded: 2025-07-29
Transcript: `raw/20250729_wRJD0inpmjU/wRJD0inpmjU.en-orig.vtt`

## Summary

Quotient AI and Tavily frame AI-search evaluation as a dynamic, multi-metric problem: web content changes, users ask malformed or underspecified questions, static QA benchmarks can mis-rank providers, and production systems need reference-free checks over answer completeness, document relevance, and hallucination against retrieved evidence.

## Extracted Concepts

- [Dynamic AI Search Evals Need Fresh Grounding Sets](../concepts/dynamic-ai-search-evals-need-fresh-grounding-sets.md) - this source explains why static QA sets are insufficient for real-time web-backed RAG and how dynamic eval sets can be generated.
- [Reference-Free AI Search Metrics Decompose Answer Quality](../concepts/reference-free-ai-search-metrics-decompose-answer-quality.md) - this source defines answer completeness, document relevance, and hallucination checks as complementary production metrics.
- [AI Search Providers Should Return Grounding Documents](../concepts/ai-search-providers-should-return-grounding-documents.md) - this source highlights that citations alone limit debugging and reference-free evaluation at scale.

## Topic Links

- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

## Notes

- Tavily's production setting combines two moving targets: web content changes continuously, and users ask odd, malformed, or implicit-context questions outside fixed test cases (01:37-02:25).
- SimpleQA and HotpotQA are useful starts for short factual and multi-hop questions, but static datasets do not cover real-time systems, subjective questions, or cases without one stable truth answer (04:05-05:49).
- Tavily's dynamic eval-set agent uses LangGraph to generate broad domain search queries, aggregate grounding documents from multiple real-time AI search providers, and create evidence-backed question-answer pairs with source context (06:34-08:29).
- In an experiment over six AI search providers, static SimpleQA scores and a dynamic benchmark produced substantially different scores and provider rankings; one provider that scored worst on SimpleQA scored best on the dynamic benchmark (10:21-12:40).
- The reference-free metrics discussed were answer completeness, document relevance, and hallucination detection against retrieved documents; answer completeness correlated strongly with dynamic benchmark performance but was not equivalent to correctness (14:03-15:44).
- Only three of the evaluated providers returned the retrieved documents used to generate answers; providers that returned only citations limited transparency and debugging at scale (15:56-16:14).
- Completeness and hallucination can trade off: a provider with high completeness and relevant documents may hallucinate more because detailed responses add unsupported reasoning or interpretation (17:04-18:25).
