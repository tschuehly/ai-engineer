# Train Computer-Use Agents in a Flight Simulator, Not on Exams

Summary: A clean training environment produces an agent that has never met a pop-up, an expired session, or an ad styled like the submit button. Model the messiness of real software inside the training environment so the agent falls into those traps during training, and make adversarial tasks part of mainstream training rather than a separate safety eval.

Use when:
- Building an RL or agentic post-training environment for browser, desktop, or app automation.
- Deciding whether an edge case belongs in an eval suite or in the training distribution.
- Explaining why an agent with strong benchmark scores behaves badly on real user tasks.

Details:
- The analogy is the argument: "for computer use agents… we need flight school, not just exams." All the messiness of the real world "has to be modeled into a simulation during training, so that the model can fall into all those traps, learn from them, and then become better." ([From RL to IRL](../sources/20260814_Cc0_nyxROBA.md), 08:22-08:47)
- The scope claim is that this is not a reward-model change: "it's not just producing a generation that is rewarded by a reward model, but it's actually the environment, and all of the training setup has to reflect the messiness and all the edge cases of the real world." (08:47-08:57)
- The named messiness to build in — "high-fidelity digital sandboxes" — is a concrete list: layout shift, slow loads, missing labels, pop-ups, focus stealing, random account states, and stale tabs. (09:03-09:20)
- **Adversarial tasks are mainstream training, not a byproduct.** The two demo traps (an ad button styled like submit, and a session that expires mid-task) are environment features, and the rule stated is: "This has to be part of the mainstream training. It cannot be something that's just [a] byproduct. You have to actually test the model during training to make mistakes and then learn from them so that it does well in production." (10:34-11:00)
- Where the messiness comes from is a product question, not a research one: "simulating reality in your training setup… can only happen when you actually deploy the product and let it fail." The lab's route is design partners and internal customers using the model, with the harness catching the failure modes so they can be trained on ([keep the harness thick early](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md)). (16:23-17:05)
- **Convergent evidence from the evaluation side.** D'Oro's argument for [multifactorial variation in PRISM](design-eval-environments-to-the-prism-principles.md) arrives at the same environment property from the opposite direction: a static, deterministic environment can be beaten by [a blind replay script](a-blind-replay-script-exposes-a-deterministic-benchmark.md), and frontier models turn out to be [fragile per variation axis](measure-agent-robustness-per-variation-axis-not-just-average-success.md) when only the theme or the starting screen changes. Varying the environment is what makes an eval honest *and* what makes a training run teach recovery; the two teams state the requirement in the same talk slot at the same event. ([Computer Use at the Edge of the Statistical Precipice](../sources/20260814_CTLa_p6iOiY.md), 03:47-05:31, 09:59-10:55)
- Practical distinction worth keeping: PRISM's variation axes (data, theme, starting screen) vary *what the task is*, while this list varies *how the software misbehaves*. An environment can be fully multifactorial and still never drop a network request or steal focus.

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Map RL Assumptions to Deployment Realities for Computer-Use Agents](map-rl-assumptions-to-deployment-realities-for-computer-use-agents.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Design Eval Environments to the PRISM Principles](design-eval-environments-to-the-prism-principles.md)
- [Make Recovery a Native Model Action, Not an Infra Reset](make-recovery-a-native-model-action-not-an-infra-reset.md)
- [Penalize Dangerous Steps With a Process Reward Model](penalize-dangerous-steps-with-a-process-reward-model.md)
- [Production-Matched RL Environments Train Coding Agents on Real Tool Surfaces](production-matched-rl-environments-train-coding-agents-on-real-tool-surfaces.md)

Sources:
- [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../sources/20260814_Cc0_nyxROBA.md), 08:22-11:00, 16:23-17:05
- [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../sources/20260814_CTLa_p6iOiY.md), 03:47-05:31, 09:59-10:55
