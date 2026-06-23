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
- Concrete production instance: Nebius runs the *same* collection/filtering pipeline (GitHub Archive + API → interactive-agent Docker build → LLM-message filtering → manual verification) for the SWE-rebench leaderboard, for collecting validation sets, and for training data, and open-sourced a ~30,000-environment set of real-world SE RL tasks (with Docker images) that frontier labs used to train better models, plus a SWE-rebench V2 spanning 20 programming languages with an adapter for Harbor (their terminal base). The recommended progression is to pick model/harness/parameters on a validation set, then auto-research or update prompts/tools, then rejection-sampling fine-tuning or distillation, then GRPO. ([SWE-rebench](../sources/20260604_wcUJWP6WpGM.md), 13:46-15:08)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Train coding-agent models with environments and expert developer reward](train-coding-agent-models-with-environments-and-expert-developer-reward.md)
- [Run Agentic Coding Evals as an Infrastructure-Reliability Problem](run-agentic-coding-evals-as-an-infrastructure-problem.md)

Sources:
- [RL Environments at Scale - Will Brown, Prime Intellect](../sources/20251209__IzZWeuTx7I.md), 05:42-14:12
- [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](../sources/20260604_wcUJWP6WpGM.md), 13:46-15:08
