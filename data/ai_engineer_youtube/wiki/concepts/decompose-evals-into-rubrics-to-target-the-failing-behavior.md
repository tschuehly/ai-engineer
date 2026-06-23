# Decompose Evals Into Rubrics to Target the Failing Behavior

Summary: Break a single pass/fail correctness judgment into a rubric of sub-question checks, then use the per-check feedback to diagnose which specific behavior is failing and decide which training data to generate — before writing any of it — even though the RL reward itself collapses back to a single value.

Use when:
- A model passes or fails an eval and you need to know *which* behavior to fix before generating training data.
- Choosing which datasets to build for fine-tuning or RL on a multi-step tool task.

Details:
- Snorkel's research team builds rubrics as part of evals: instead of one final yes/no, the rightness or wrongness of a response is broken into a list of individual questions that can each be answered. (18:37-18:55)
- Looking at each sub-question lets you find where the actual problem is "among all the multiple possible arenas" — e.g. distinguishing tool discovery, schema inspection, query construction, and error self-correction as separate failure points. (18:55-19:20)
- The richer per-check feedback drives data decisions: you choose which behaviors to generate datasets for, and which data to work with, based on what the rubric surfaces — diagnosis before any training data is written. (19:18-19:30)
- The rubric is a diagnostic and data-design layer, not the reward signal: GRPO and similar grouped methods still consume a single scalar value for the actual RL cycle, so the final pass/fail still drives reinforcement. (19:30-19:40)
- This is the upstream complement to verifiable single-value rewards: rubrics tell you what to fix, verifiable rewards tell the optimizer whether it was fixed.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Failure-Mode Ontologies Prioritize Domain AI Work](failure-mode-ontologies-prioritize-domain-ai-work.md)
- [Fix Tool Discipline Before Reaching for a Bigger Model](fix-tool-discipline-before-reaching-for-a-bigger-model.md)
- [Train on the Simplest Task Variant That Transfers](train-on-the-simplest-task-variant-that-transfers.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Layer agent evals as deterministic, semantic, and behavioral checks](layer-agent-evals-as-deterministic-semantic-and-behavioral-checks.md)

Sources:
- [Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel](../sources/20260610_TNwJ1LMiENk.md), 18:37-19:40
