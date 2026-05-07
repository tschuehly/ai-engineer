# Train coding-agent models with environments and expert developer reward

Summary: Coding-agent model training should combine runnable task environments with expert developer feedback, so the model learns from verifiable coding goals and from judgments about what developers trust in real workflows.

Use when:
- Designing training or post-training loops for coding, bug-fixing, refactoring, or workplace-agent models.
- Evaluating whether a model's benchmark strength is likely to transfer into developer workflows.

Details:
- MiniMax frames M2 as a coding and workplace-agent model, then cautions that benchmark numbers alone do not prove a model will work well when plugged into a real development environment.
- Scaled training environments let reinforcement learning expose the model to environment feedback and verifiable coding goals rather than only static prompt/answer examples.
- In-house expert developers supplied problem definitions, bug-fixing and repository-refactoring tasks, reliability judgments, trust judgments, and reward/evaluation feedback on final deliverables.
- The reusable pattern is to scale both environments and domain-expert reward sources; more tool tasks without expert judgment can miss whether the behavior is actually useful to developers.
- Pash argues that coding-agent reliability improves when models practice in RL environments that force tool use, failure handling, retries, and real engineering problem solving. 04:18-05:04
- Cline's RL environment factory turns real coding sessions into training substrates by qualifying tasks, reconstructing start and end states, containerizing the environment, and defining verifiers whose scores can train the policy model. 05:33-10:16

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Train code models on execution traces, not only syntax](train-code-models-on-execution-traces-not-only-syntax.md)
- [Turn real coding sessions into RL environments](turn-real-coding-sessions-into-rl-environments.md)

Sources:
- [Minimax M2: Building the #1 Open Model - Olive Song, MiniMax](../sources/20251213_lY1iFbDPRlw.md), 02:12-05:29
- [Hard Won Lessons from Building Effective AI Coding Agents - Nik Pash, Cline](../sources/20251212_I8fs4omN1no.md), 04:18-10:16
