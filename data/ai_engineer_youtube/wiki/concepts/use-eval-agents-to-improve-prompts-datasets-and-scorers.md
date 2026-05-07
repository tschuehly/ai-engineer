# Use eval agents to improve prompts, datasets, and scorers

Summary: Eval platforms can become active optimization workbenches when an agent proposes changes to the system under test and to the eval artifacts themselves. The useful loop optimizes prompts, datasets, and scorers together while preserving human visibility into the proposed edits.

Use when:
- Designing eval tooling that should recommend fixes instead of only showing pass/fail dashboards.
- Deciding whether prompt optimization is enough, or whether dataset and scorer quality also need agent-assisted iteration.

Details:
- Goyal argues that passive eval dashboards still leave teams asking what code or prompt changes to make after looking at results, 01:40-01:57.
- Braintrust's Loop is described as an agent that runs inside Braintrust and can optimize prompts through complex agents, while also helping improve datasets and scorers, 02:39-02:56.
- The talk frames prompt, dataset, and scorer improvements as coupled: strong evals come from the combination of all three rather than from prompt editing alone, 02:49-02:56.
- Human inspection remains part of the workflow: Loop shows suggested data edits, scorer ideas, and prompt edits side by side in the UI, with an optional autonomous optimization toggle for users who want less manual review, 03:31-04:05.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Mature eval platforms from spreadsheets into experiment systems](mature-eval-platforms-from-spreadsheets-into-experiment-systems.md)
- [Continuously reconcile eval datasets with user reality](continuously-reconcile-eval-datasets-with-user-reality.md)
- [Write custom scorers as product specifications](write-custom-scorers-as-product-specifications.md)
- [Evaluator quality is a dependency of prompt optimization](evaluator-quality-is-a-dependency-of-prompt-optimization.md)

Sources:
- [The Future of Evals - Ankur Goyal, Braintrust](../sources/20250809_MC55hdWLq4o.md), 01:40-04:05
