# Use Golden Data Sets and Mixed Scoring Functions for AI Application Confidence

Summary: AI application releases need curated test cases and scoring functions that combine deterministic assertions with LLM-as-judge checks for nuanced behavior.

Use when:
- Replacing anecdotal manual testing with a repeatable pre-production confidence gate.
- Choosing between deterministic checks and judge-model scoring for an AI workflow.

Details:
- The workshop recommends creating a golden data set of edge cases for a support application so teams can show business stakeholders concrete release evidence instead of relying on vibe-based demos, 58:17-58:48.
- Deterministic scoring functions are analogous to unit tests: cheap, easy to run, and useful where the expected condition can be encoded without another model, 58:51-59:13.
- LLM-as-judge scoring is reserved for nuanced criteria that deterministic checks cannot capture, such as brand style or customer satisfaction, 59:15-59:46.
- Golden data sets should include failure modes and edge cases that are likely to matter in production, and later production failures can be added as regression cases, 01:35:30-01:35:43.

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)

Sources:
- [Shipping complex AI applications - Braintrust & Trainline](../sources/20260501_ZdheJTfLu-s.md), 58:17-59:46, 01:35:30-01:35:43
