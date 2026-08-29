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
- **The cheapest outcome verifier is one you do not write, because the operation produces it.** Shenoy's version for services work needs no reward function at all: "there is a ground truth here. In the case of the roofing example, the question is, did the roof get repaired? Did the books get closed?" That is the outcome test this page argues for, with the scorer supplied by the business process rather than by a test author who might encode incidental path details — which also means it cannot be overfitted to a reference solution. The costs are the mirror image: the label is one bit, it arrives days later, and it attributes nothing to a step. See [Operational Outcomes Are Eval Labels You Only See If You Own the Operation](operational-outcomes-are-eval-labels-you-only-see-if-you-own-the-operation.md). ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 10:52-11:49)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Build coding benchmarks around construct validity](build-coding-benchmarks-around-construct-validity.md)
- [Detect reward hacking in code optimization evals](detect-reward-hacking-in-code-optimization-evals.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Operational Outcomes Are Eval Labels You Only See If You Own the Operation](operational-outcomes-are-eval-labels-you-only-see-if-you-own-the-operation.md)
- [Curate Tasks by Live Human Demand and a Deterministic Verifier](curate-tasks-by-live-human-demand-and-a-deterministic-verifier.md)
- [Design the Environment, Not the Workflow](design-the-environment-not-the-workflow.md)
- [Open Agent Arenas Reach Solutions No Single Agent Reaches](open-agent-arenas-reach-solutions-no-single-agent-reaches.md)

Sources:
- [Hard Won Lessons from Building Effective AI Coding Agents - Nik Pash, Cline](../sources/20251212_I8fs4omN1no.md), 05:33-09:41
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 10:52-11:49
