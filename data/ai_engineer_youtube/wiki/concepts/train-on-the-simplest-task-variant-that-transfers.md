# Train on the Simplest Task Variant That Transfers

Summary: When a shared core behavior is what fails across easy and hard task variants, training only on the simplest variant can give the largest uplift and still generalize to harder variants — more diverse, harder, or curriculum-ordered training data is not automatically better.

Use when:
- Designing the training-data mix for RL or fine-tuning when tasks come in easy and hard variants.
- Tempted to add multi-step or curriculum data to improve performance on a hard benchmark.

Details:
- Snorkel's FinQA data set contained both single-table and multi-table questions; the team compared three regimes: single-table only, the full single-plus-multi-table mix, and curriculum learning (start single-table, then progressively add multi-table). (16:35-16:58)
- Single-table-only training yielded the greatest uplift for these questions — beating both the mixed regime and the curriculum regime, which was a "pleasant surprise." (16:58-17:25)
- The single-table-only uplift transferred to the harder multi-table FinQA-reasoning benchmark, which saw a similar doubling: 13.9% → 26.6% pass rate after training. (17:25-17:50)
- The mechanism: the core failing behavior was tool discipline (tool discovery and error self-correction), which is shared between single- and multi-table tasks, so fixing it on the simplest variant generalized rather than requiring the harder variant in the training mix. (17:50-18:35)
- Practical implication: identify the specific shared behavior that is failing first, then train on the cheapest task variant that exercises it, rather than assuming harder or more varied training data is needed. (18:35-18:50)

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Fix Tool Discipline Before Reaching for a Bigger Model](fix-tool-discipline-before-reaching-for-a-bigger-model.md)
- [Decompose Evals Into Rubrics to Target the Failing Behavior](decompose-evals-into-rubrics-to-target-the-failing-behavior.md)
- [Post-train small models for narrow capabilities](post-train-small-models-for-narrow-capabilities.md)
- [Bootstrap RL with targeted SFT before reinforcement learning](bootstrap-rl-with-targeted-sft-before-reinforcement-learning.md)

Sources:
- [Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel](../sources/20260610_TNwJ1LMiENk.md), 16:35-18:50
