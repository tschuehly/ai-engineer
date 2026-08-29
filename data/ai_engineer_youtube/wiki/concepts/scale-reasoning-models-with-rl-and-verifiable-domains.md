# Scale Reasoning Models With RL and Verifiable Domains

Summary: Reasoning-model post-training can scale capability by teaching a base model to spend variable test-time compute on hard prompts, especially when code and math tasks provide verifiable reward signals.

Use when:
- Deciding whether model improvement should come from more pretraining tokens or reasoning-oriented RL.
- Designing eval or training tasks where answers can be checked by compilation, factual checks, or mathematical correctness.

Details:
- The DeepSeek update is framed as better post-training on the same model family rather than a new base model, with larger gains in reasoning, math, coding, JSON output, and function calling. (09:50-12:04)
- The speaker contrasts Chinchilla-style training-budget scaling and overtraining for cheap inference with test-time compute, where harder prompts can receive more generated reasoning instead of every token receiving the same fixed compute. (18:20-20:18, 22:28-22:48)
- DeepSeek is described as training models with pure RL to reason through questions using verifiable code and math data, including whether code compiles, facts are correct, and math is logically correct. (22:45-23:07)
- The reported May 28 update roughly doubled average reasoning tokens on AIME from about 12k to 25k and improved AIME 2024 from about 70% to 87.5%, showing that reasoning-token budget is itself an optimization surface. (10:03-11:15)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Pair next-token prediction with reinforcement learning for long-horizon work](pair-next-token-prediction-with-reinforcement-learning-for-long-horizon-work.md)
- [Use Verifiable Rewards for Language-Model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Tune inference to the application Pareto point](tune-inference-to-the-application-pareto-point.md)
- [Curate Tasks by Live Human Demand and a Deterministic Verifier](curate-tasks-by-live-human-demand-and-a-deterministic-verifier.md)

Sources:
- [Latent Space Paper Club: AIEWF Special Edition (Test of Time, DeepSeek R1/V3) — VIbhu Sapra](../sources/20250725_9k3xPh-40mo.md), 09:50-23:07
