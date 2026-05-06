# Benchmark Narrow Slices Separately From Real Expert Work

Summary: Narrow benchmark improvements can be real while still missing failures in fuzzy, high-context expert work. Evaluation should separate well-specified task scores from broader user-judgment signals over real prompts.

Use when:
- Reconciling rising public benchmark scores with persistent user complaints.
- Building eval suites for expert workflows where the task distribution changes as users trust models with harder work.

Details:
- The talk argues that public benchmark charts can rise while failing to capture the whole story of what models still struggle with in practice. (00:29-02:03)
- Arena's long-running open-ended battles are useful because users can enter arbitrary prompts, but the prompt distribution shifts as users ask harder questions, so trends reflect both model quality and expectation drift. (09:31-10:59, 14:51-15:13)
- Expert-prompt breakdowns showed uneven progress: quantitative work improved substantially, while creative writing improved less dramatically and finance, law, and some software subcategories had flatter dissatisfaction trends. (13:12-15:47)
- In software prompts, the speaker highlights game-building as a category where models may generate code but still fail at actual mechanics, challenge, and game-design quality; he also notes a lack of strong benchmarks for that behavior. (15:47-18:35)
- The source's synthesis is that super-narrow, well-specified benchmark tasks can be valid and still miss fuzzy human judgment about real white-collar work, so eval programs should inspect the bottom of the distribution rather than only frontier gains. (18:49-19:36)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Track user dissatisfaction alongside pairwise model preference](track-user-dissatisfaction-alongside-pairwise-model-preference.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)

Sources:
- [What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench](../sources/20260424_R7A8rX-09Zw.md), 00:29-19:36
