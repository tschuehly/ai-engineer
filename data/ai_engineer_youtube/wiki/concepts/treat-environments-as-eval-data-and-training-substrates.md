# Treat Environments as Eval, Data, and Training Substrates

Summary: Agent environments are not only reinforcement-learning loops. A well-defined environment can serve as an eval, a synthetic-data generator, an SFT or distillation source, and an RL training substrate because it captures tasks, tools, harness behavior, and rewards in one reusable artifact.

Use when:
- Designing an agent benchmark that might later become a training loop.
- Deciding whether to collect labeled examples or build an interactive task harness.

Details:
- Brown defines an environment as a product or agent harness plus tasks and rewards, then argues the same abstraction covers offline data sets, user-task streams, evals, synthetic-data engines, SFT, distillation, and direct RL. 05:42-06:24
- The environment forces the builder to predefine tasks and rewards, which turns a loose harness into a proper eval and prevents relying only on a subjective vibe check before shipping. 07:20-07:55
- If a team can measure answers even when it does not have labeled solutions up front, the environment can create data on the fly and avoid the hardest part of ordinary SFT data collection. 08:55-09:22
- Treating evals as environments keeps later options open: the same artifact can support prompt tuning, model selection, model customization, parallel load testing, and RL. 13:42-14:12

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Train coding-agent models with environments and expert developer reward](train-coding-agent-models-with-environments-and-expert-developer-reward.md)

Sources:
- [RL Environments at Scale - Will Brown, Prime Intellect](../sources/20251209__IzZWeuTx7I.md), 05:42-14:12
