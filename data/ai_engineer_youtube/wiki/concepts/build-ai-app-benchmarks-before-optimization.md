# Build AI app benchmarks before optimization

Summary: Build the first eval benchmark near the start of an AI app project, then use it as the baseline for prompt, model, retrieval, logic, and guardrail experiments. The benchmark should expose individual failure reasons, not only aggregate scores.

Use when:
- Turning a promising AI proof of concept into a system that can be optimized without hidden regressions.
- Comparing model, prompt, RAG, agentic, or guardrail changes against the same task baseline.

Details:
- The talk recommends building evals at the beginning of the process: create a first proof of concept, define the first test set, run it, and inspect which cases fail or pass, 08:25-08:57.
- Average numbers are not enough because they do not explain what to change; case-level inspection can reveal whether the eval itself is malformed or whether the solution needs changes to its model, logic, prompt, or data, 08:57-09:37.
- Fixing one prompt case can break cases that previously worked, so frequent benchmark runs are needed to catch regressions before they reach users, 09:37-10:19.
- A trusted benchmark lets teams compare GPT-4o mini against GPT-4o, GraphRAG against simpler retrieval, and agentic approaches against simpler logic while considering latency and inference cost, 10:47-11:45.
- Eval mechanics should match the application type: support bots may use LLM-as-judge, text-to-SQL or text-to-graph systems can use mock databases with known answers, classifiers can use exact rubric matches, and guardrails should include cases that should not be answered or should be answered differently, 11:46-13:23.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Reverse-engineer AI app evals from user outcomes](reverse-engineer-ai-app-evals-from-user-outcomes.md)

Sources:
- [Practical tactics to build reliable AI apps — Dmitry Kuchin, Multinear](../sources/20250803_-T6uZYYzkWw.md), 08:25-13:23
