# Stage Regulated LLM Evals From Experts to Automated Judges

Summary: Regulated LLM products can start with manual domain-expert evaluation, convert expert judgments into golden data, and then use automated LLM-as-judge checks for smaller iterations. Major domain, prompt, or model changes should return to expert review.

Use when:
- Designing an eval lifecycle for tax, legal, healthcare, finance, or other expert-governed AI outputs.
- Balancing expensive domain review against frequent prompt and model iteration.

Details:
- Intuit uses tax analysts as domain experts for IRS changes, prompt engineering, initial manual evaluations, and correctness guidance, 05:52-07:08.
- Manual expert evaluations establish the baseline; those examples become golden data for automated evaluation and LLM-as-judge prompts, 07:04-07:14, 09:11-09:22.
- The reported evaluation pillars are accuracy, relevancy, and coherence, with monitoring over sampled real-user outputs, 08:32-08:57.
- Minor prompt iterations can use automated evals, while major changes such as moving from tax year 2023 to 2024 or substantially changing prompts should return to manual expert evaluation, 13:02-13:55.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Domain Evals Need Expert-Built Environments](domain-evals-need-expert-built-environments.md)
- [Calibrate LLM Judges Like Binary Classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Use Golden Data Sets and Mixed Scoring Functions for AI Application Confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)

Sources:
- [How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit](../sources/20250723__zl_zimMRak.md), 05:52-07:14, 08:32-09:22, 13:02-13:55
