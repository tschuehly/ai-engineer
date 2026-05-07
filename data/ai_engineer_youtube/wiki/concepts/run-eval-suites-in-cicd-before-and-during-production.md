# Run eval suites in CI/CD before and during production

Summary: LLM evals should become CI/CD automation, not only notebook experiments. The intended workflow is to rerun evaluation suites when prompts, data sets, models, or production use cases change, similar to ordinary software tests.

Use when:
- Moving evals from manual experiments into release gates.
- Connecting offline prompt/model tests to production customer behavior.

Details:
- Smith says teams need a CI process for continuously improving evaluation and benchmark setups because no eval suite catches everything at first. (11:13-11:31)
- When asked how evals connect to running customer use cases, she describes the desired shape as CI/CD automation of an evaluation framework, analogous to software-engineering tests. (31:03-31:49)
- The CI/CD eval suite should include evaluation tests like unit testing setups, but scoped to the LLM application's prompts, data sets, model swaps, and real production use cases. (31:49-31:58)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)

Sources:
- [Strategies for LLM Evals (GuideLLM, lm-eval-harness, OpenAI Evals Workshop) - Taylor Jordan Smith](../sources/20250727_89NuzmKokIk.md), 11:13-11:31, 31:03-31:58
