# Align Synthetic Retrieval Queries With Real User Specificity

Summary: Synthetic query generation can bootstrap retrieval evals when a product lacks real user traffic, but generated questions must be calibrated against realistic user specificity and messiness. Overly clean or document-specific generated queries can make a retrieval system look stronger than it is.

Use when:
- Building a retrieval benchmark before real query logs exist.
- Generating query/document pairs with an LLM.
- Validating whether a benchmark reflects the production query distribution.

Details:
- LLMs can generate retrieval questions when teams have documents and chunks but no user queries, but naive prompts such as asking for "a question for this document" are not enough (03:06-03:31).
- Benchmark examples can be unrealistically clean: the talk contrasts clean public benchmark phrasing with real-world data and warns that synthetic queries can be overly specific to the document they were generated from (03:39-04:18).
- Synthetic query sets should be checked for semantic alignment with real user queries, including specificity, so the generated eval predicts the same model-ranking behavior as a ground-truth query set (04:18-06:04).
- Once real users exist, teams should replace or augment synthetic data with actual application queries and outputs (16:55-17:09).

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Fuzz AI applications for local input brittleness](fuzz-ai-applications-for-local-input-brittleness.md)
- [Keep eval data constant and task logic variable](keep-eval-data-constant-and-task-logic-variable.md)

Sources:
- [How to look at your data - Jeff Huber (Chroma) + Jason Liu (567)](../sources/20250806_jryZvCuA0Uc.md), 03:06-06:04
