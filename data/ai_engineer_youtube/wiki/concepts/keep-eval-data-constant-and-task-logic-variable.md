# Keep Eval Data Constant and Task Logic Variable

Summary: Eval suites should keep representative input data stable while varying the task logic being tested. This makes prompt, RAG, preprocessing, middleware, and model changes comparable without rebuilding the dataset for every experiment.

Use when:
- Structuring an eval harness so teams can compare system prompts, retrieval logic, preprocessing, and models.
- Preventing eval data from becoming entangled with the implementation variant under test.

Details:
- The talk recommends putting constants in data and variables in the task: user prompts such as "how many Rs in strawberry" remain fixed data, while the task section changes system prompt, preprocessing, RAG, or model behavior, 09:15-09:59.
- Keeping data constant improves clarity, reuse, and generalization because changing a system prompt should not require rewriting the eval cases, 09:20-09:59.
- Vercel AI SDK middleware is presented as a way to share preprocessing, RAG, system-prompt logic, and completion behavior between the production API route and evals, 10:02-10:20.
- Evals should run code as close as possible to production, because useful practice should resemble the real game, 10:20-10:38.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Build AI app benchmarks before optimization](build-ai-app-benchmarks-before-optimization.md)
- [Use evals as durable AI system specifications](use-evals-as-durable-ai-system-specifications.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)

Sources:
- [Evals Are Not Unit Tests - Ido Pesok, Vercel v0](../sources/20250806_L8OoYeDI_ls.md), 09:15-10:38
