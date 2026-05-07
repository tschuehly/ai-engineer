# Dynamic AI Search Evals Need Fresh Grounding Sets

Summary: Real-time AI search and web-backed RAG need evaluation sets that refresh with the underlying information environment. Static QA benchmarks are useful baselines, but they can misrepresent systems whose answers depend on current web content, source timing, and user context.

Use when:
- Evaluating web-backed RAG, SAG, or AI search providers against changing information.
- A static benchmark score conflicts with observed production search quality.

Details:
- Static datasets such as SimpleQA and HotpotQA cover short factual and multi-hop retrieval cases, but they do not address questions with no single truth answer, subjective user needs, or fast-changing source material (04:05-05:49).
- Tavily's dynamic eval-set agent generates broad domain search queries, gathers grounding documents from multiple real-time AI search providers, and turns the gathered evidence into question-answer pairs with source context (06:34-08:29).
- Using multiple search providers to gather grounding documents can reduce single-provider bias and improve coverage when the target system is itself an AI search provider (07:34-07:59).
- In the reported experiment, static SimpleQA scores and a dynamic benchmark produced materially different provider rankings, including a provider that ranked worst on SimpleQA but best on the dynamic benchmark (10:21-12:40).

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Keep eval data constant and task logic variable](keep-eval-data-constant-and-task-logic-variable.md)
- [Align synthetic retrieval queries with real user specificity](align-synthetic-retrieval-queries-with-real-user-specificity.md)
- [Use fast query-document evals for retrieval changes](use-fast-query-document-evals-for-retrieval-changes.md)

Sources:
- [Evaluating AI Search: A Practical Framework for Augmented AI Systems - Quotient AI + Tavily](../sources/20250729_wRJD0inpmjU.md), 04:05-12:40
