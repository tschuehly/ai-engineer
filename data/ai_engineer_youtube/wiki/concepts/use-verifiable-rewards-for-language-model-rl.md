# Use Verifiable Rewards for Language-Model RL

Summary: Language-model RL works best when the environment can automatically verify outcomes and convert them into deterministic reward signals. These rewards can measure task success, output format, tool-call success, penalties, or other observable behaviors.

Use when:
- Designing an RL or eval environment for a task with checkable outcomes.
- Replacing imitation-only post-training with outcome-backed feedback.

Details:
- The talk connects recent reasoning-model progress to reinforcement learning with verifiable rewards, where a correct answer, successful tool call, or checked outcome becomes a training signal. (06:22-07:41)
- RL environments add a dynamic layer beyond SFT: instead of only learning from demonstrations, the model explores actions and is reinforced toward outputs that maximize rewards. (07:33-08:53)
- The reverse-text example uses a longest-common-subsequence ratio against the known reversed answer; the tic-tac-toe example uses a winner reward, an XML-format reward, and invalid-move penalties. (12:50-13:05, 20:52-23:40)
- The source cautions that task difficulty matters: if an opponent is too perfect too early, the model may never see wins and fail to receive useful positive learning signal. (21:35-22:09)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Mitigate small-model doom loops during preference alignment and RL](mitigate-small-model-doom-loops-during-preference-alignment-and-rl.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)

Sources:
- [Let LLMs Wander: Engineering RL Environments - Stefano Fiorucci](../sources/20260408_71V3fTaUp2Q.md), 06:22-23:40
