# Bootstrap RL With Targeted SFT Before Reinforcement Learning

Summary: A small model may need a targeted supervised fine-tuning warm-up before RL can improve deeper behavior. Use SFT to teach protocol, format, and basic valid actions, then use reinforcement learning for outcome optimization.

Use when:
- A model cannot reliably produce the action or output format required by an RL environment.
- Designing a post-training path for a small open model on a narrow interactive task.

Details:
- The baseline LFM-2 model struggled to follow tic-tac-toe output format and make valid moves, so the workflow used SFT first to teach XML move syntax and valid-action behavior. (25:42-27:05)
- Once the environment existed, synthetic data generation was a single-command workflow: GPT-5 mini generated 200 games, and losing games were filtered out to avoid teaching suboptimal strategies. (27:05-27:36)
- After SFT, the model learned the format almost perfectly and reduced invalid moves, but game performance still needed RL to improve. (27:36-28:15)
- The source suggests choosing a base model by first evaluating it in the environment and inspecting completions for promising behavior, not only by aggregate score. (37:23-37:45)

Related topics:
- [Models](../topics/models.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Post-train small models for narrow capabilities](post-train-small-models-for-narrow-capabilities.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Control environment noise for group-based RL](control-environment-noise-for-group-based-rl.md)

Sources:
- [Let LLMs Wander: Engineering RL Environments - Stefano Fiorucci](../sources/20260408_71V3fTaUp2Q.md), 25:42-28:15, 37:23-37:45
