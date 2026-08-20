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

- Mishra states the same three requirements from the training side — the task must have a verifiable outcome, be targeted at the skill being taught, and sit in a difficulty window, "if the task is very easy or very difficult, then we're not going to get much training signal" — and gives the verifier ladder as string equality, compiler, linter, unit tests, database lookups, and rubric-graded agent judges. His criteria for preferring RL over SFT: tasks are easy to generate but demonstrations are hard to collect; many valid paths exist and SFT would "narrow down the model to following a few patterns only"; or the domain is reasoning-heavy and subjective enough that only the outcome should be judged. ([From RL to IRL](../sources/20260814_Cc0_nyxROBA.md), 01:26-03:16)
- **Limit of outcome-only verification.** Once actions touch the real world, a verified outcome stops being a sufficient reward: an agent that files the expense report *and* sends a resignation letter to the CEO passes the outcome check, and an agent that locks an account while retrying passes it too. Verifiable rewards then need a path-scoring companion — see [Penalize Dangerous Steps With a Process Reward Model](penalize-dangerous-steps-with-a-process-reward-model.md). (07:48-08:02, 09:49-10:07)

- **The share of work this technique does not reach is the argument for the next phase.** Sara Hooker names non-verifiable tasks as a day-one scope decision for her company's training system, on the grounds that they are "really the bulk of… everyday tasks that people do" and "where the meat of… what is interesting for progress is going to be over the next year," alongside covering 242 languages from the start ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 08:53-09:21). This is a claim about workload composition, not a method — no non-verifiable training approach is described or measured — but it is worth carrying next to the verifier ladder above, because that ladder's rungs (string equality, compiler, linter, unit tests, database lookups) all assume the task ends in something checkable, and the wiki's [modern Moravec's paradox](a-modern-moravecs-paradox-explains-the-coding-agent-gap.md) page gives the structural reason coding is where verifiable-reward RL has landed first.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [A Modern Moravec's Paradox Explains the Coding-Agent Gap](a-modern-moravecs-paradox-explains-the-coding-agent-gap.md)
- [Mitigate small-model doom loops during preference alignment and RL](mitigate-small-model-doom-loops-during-preference-alignment-and-rl.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Penalize Dangerous Steps With a Process Reward Model](penalize-dangerous-steps-with-a-process-reward-model.md)

Sources:
- [Let LLMs Wander: Engineering RL Environments - Stefano Fiorucci](../sources/20260408_71V3fTaUp2Q.md), 06:22-23:40
- [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../sources/20260814_Cc0_nyxROBA.md), 01:26-03:16, 07:48-10:07
- [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](../sources/20260812_XEd_SRVHBgU.md), 08:53-09:21
