# Preserve long-context ability with single-stage RL

Summary: Long-context models can lose context-handling ability when reinforcement learning ramps through shorter context windows. If the model was already prepared for long contexts, training directly at the target long context can preserve that capability better than a short-to-long curriculum.

Use when:
- Planning RL schedules for models expected to handle long documents, repositories, chats, or agent traces.
- Investigating regressions where post-training improves reasoning but hurts long-context use.

Details:
- GLM 4.6 used long-context and agent data after repo-level code mid-training, with context pushed to 128k and described as 200k for GLM 4.6 handling documents, codebases, and long chats. (07:11-07:38)
- The talk contrasts multistage RL context schedules such as 16k, 32k, 48k, then 64k against single-stage RL at 64k tokens. (11:51-12:08)
- For a model already trained with 64k-token SFT, shorter RL stages made the model forget long-context ability, and the final 64k stage could not fully recover the loss. (12:11-12:32)
- The reported GLM 4.6 approach starts directly with 64k-token RL in one stage and outperforms the multistage curve. (12:32-12:48)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Pair next-token prediction with reinforcement learning for long-horizon work](pair-next-token-prediction-with-reinforcement-learning-for-long-horizon-work.md)
- [Use Agent RFT after baseline and task optimization](use-agent-rft-after-baseline-and-task-optimization.md)

Sources:
- [Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads - Yuxuan Zhang, Z.ai](../sources/20251122_m6MF1OR_9kM.md), 07:11-07:38, 11:51-12:48
