# Control Environment Noise for Group-Based RL

Summary: Group-based RL methods need comparable rollouts so reward differences reflect model behavior rather than environment randomness. Environment seeds, difficulty sampling, and batch size become part of the training design.

Use when:
- Training with GRPO, CISPO, or another grouped rollout method.
- Debugging unstable RL runs or model collapse in an interactive environment.

Details:
- Fiorucci explains GRPO-style training as comparing several rollouts from the same starting point, scoring them, computing a group baseline, and updating the model toward trajectories above that baseline. (28:19-29:12)
- Reward differences should come from how the model plays, not random environment variance; the tic-tac-toe environment assigns an example seed and derives turn seeds from board state so equivalent states produce equivalent opponent responses. (23:45-24:37)
- Opponent skill is sampled within controlled ranges: purely random opponents are too easy, purely optimal opponents can remove positive learning signal, and a mixed range gives the model both attack and defense opportunities. (21:35-22:47, 29:34-29:49)
- Batch size is a stability parameter because each update learns from a set of games and opponent types; too-small batches in diverse environments can reinforce suboptimal strategies and cause unstable training or model collapse. (30:12-30:48, 35:37-36:04)
- Raising temperature can help the model explore beyond learned strategies, but too much temperature risks gibberish and temporary reward drops before later improvement. (33:10-34:12)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use loss curves to debug local model training](use-loss-curves-to-debug-local-model-training.md)
- [Mitigate small-model doom loops during preference alignment and RL](mitigate-small-model-doom-loops-during-preference-alignment-and-rl.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)

Sources:
- [Let LLMs Wander: Engineering RL Environments - Stefano Fiorucci](../sources/20260408_71V3fTaUp2Q.md), 21:35-36:04
