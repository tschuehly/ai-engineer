# Prefer outcome verifiers over ground-truth path checks

Summary: Coding-agent verifiers should test whether the task outcome was achieved, not whether the agent copied incidental details from the human solution path. Overprescribed verifiers can reward brittle mimicry and reject valid alternate implementations.

Use when:
- Designing tests or reward functions for repository-scale coding tasks.
- Reviewing whether a benchmark verifier overfits to the reference patch.

Details:
- The talk frames a good verifier as outcome-driven: like a kettle whistle, it checks whether the desired state happened without caring which valid path produced it. 08:33-09:04
- Bad tests can emerge when benchmark builders inspect the ground-truth solution and encode incidental details, such as a particular setting, location, or elapsed time, instead of the user-visible task result. 09:07-09:34
- The recommended verifier target is the "spirit" and outcome of the task, not a narrow replay of the reference path. 09:34-09:41
- For RL environments, this verifier design matters because the score can update model behavior, so a path-biased verifier can train the model toward the wrong shortcut. 05:33-06:03

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Build coding benchmarks around construct validity](build-coding-benchmarks-around-construct-validity.md)
- [Detect reward hacking in code optimization evals](detect-reward-hacking-in-code-optimization-evals.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)

Sources:
- [Hard Won Lessons from Building Effective AI Coding Agents - Nik Pash, Cline](../sources/20251212_I8fs4omN1no.md), 05:33-09:41
