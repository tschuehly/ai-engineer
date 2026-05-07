# Write custom scorers as product specifications

Summary: Scoring functions should express the product's intended behavior, not only reuse generic quality checks. Treating scorers as executable specifications justifies engineering investment in custom, frequently revised scoring logic.

Use when:
- Choosing between off-the-shelf scorers and product-specific evaluation functions.
- Translating AI product requirements, PRDs, or acceptance criteria into eval metrics.

Details:
- Goyal says advanced teams write and constantly modify their own scoring functions rather than asking which built-in scorer removes the need to think about scoring, 03:11-03:39.
- Scorers can be understood as a spec or PRD for an AI application; a generic scorer is therefore a spec for someone else's project, 03:39-04:00.
- In the recap, he recommends not using only off-the-shelf scores and instead crafting the product spec into scoring functions, 12:51-13:08.
- Braintrust's Auto Evals is described as open source and flexible because teams need to adapt scoring to their own use cases rather than accept one fixed metric surface, 03:23-03:37.

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Reverse-engineer AI app evals from user outcomes](reverse-engineer-ai-app-evals-from-user-outcomes.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)

Sources:
- [Five hard earned lessons about Evals - Ankur Goyal, Braintrust](../sources/20250823_a4BV0gGmXgA.md), 03:11-04:00, 12:51-13:08
