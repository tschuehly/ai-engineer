# Customize open benchmark harnesses with proprietary task data

Summary: Open benchmark harnesses are useful starting points, but production teams should adapt them to proprietary data, fine-tuned model domains, and application-specific safety or bias cases. The reusable pattern is the eval format and runner, not the assumption that public benchmark data matches the product.

Use when:
- Evaluating a fine-tuned or domain-specific model against private task data.
- Choosing between public benchmark suites and custom product evals.

Details:
- The workshop uses lm-eval-harness with MMLU-Pro for factual accuracy work and notes that the harness contains many benchmark options beyond the chosen exercise. (29:28-29:56)
- In response to a proprietary-data question, Smith says open-source evals can be customized by creating a similar multiple-choice format to MMLU with the team's own data set. (26:07-26:29)
- A fine-tuned model can be evaluated against proprietary data through an MMLU-like branch or adapted data source rather than only public general-knowledge tasks. (26:29-26:59)
- The safety activity uses promptfoo because it supports custom tests, with the workshop choosing a safety-focused example while pointing to other examples in the repository. (29:56-30:28)

- **For coding agents there is a version that skips the open harness entirely, because the task data already exists as merged pull requests.** Superconductor's objection to adapting a public coding benchmark is subject matter rather than task format — "SWE-bench is all in Python, we're Ruby on Rails" — and their answer is to select merged PRs that "represent great engineering work. It could be agent created, could be human created, could be a hybrid, doesn't matter," replay them through candidate agents, and plot quality against cost and time. The tradeoff against this page's approach is explicit: you give up the harness's scoring machinery and have to supply the scorer yourself, which is exactly the part their talk leaves undescribed. See [replay your own merged PRs as the coding-agent benchmark](replay-your-own-merged-prs-as-the-agent-benchmark.md). ([Arjun Singh](../sources/20260809_OL7kfezynJM.md), 13:25-14:51)

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Write custom scorers as product specifications](write-custom-scorers-as-product-specifications.md)
- [Keep eval data constant and task logic variable](keep-eval-data-constant-and-task-logic-variable.md)
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md)
- [Replay Your Own Merged PRs as the Coding-Agent Benchmark](replay-your-own-merged-prs-as-the-agent-benchmark.md)

Sources:
- [Strategies for LLM Evals (GuideLLM, lm-eval-harness, OpenAI Evals Workshop) - Taylor Jordan Smith](../sources/20250727_89NuzmKokIk.md), 25:33-26:59, 29:28-30:28
- [Multiplayer agentic engineering — Arjun Singh, Superconductor](../sources/20260809_OL7kfezynJM.md), 13:25-14:51
