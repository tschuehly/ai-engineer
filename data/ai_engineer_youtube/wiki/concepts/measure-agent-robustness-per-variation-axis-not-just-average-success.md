# Measure Agent Robustness per Variation Axis, Not Just Average Success

Summary: Once an environment varies tasks along named axes — data instance, data profile, visual theme, starting screen — you can score a model per axis and read its worst case instead of its average. Doing so shows frontier computer-use models are "pretty bad" at holding performance under changes that should not matter, which is a different and more deployment-relevant number than task success rate.

Use when:
- Deciding whether a computer-use or GUI agent that scored well in evaluation will hold up in production.
- Choosing which variation axes to build into an environment, and what to report from it.
- Explaining why an agent that demoed reliably fails on a customer's differently-configured instance.
- Setting expectations with a stakeholder who has seen one headline success rate.

Details:
- The axes come from the environment's configuration factors, so they are named rather than emergent: the task *instance* ("what is the exact amount of money that you're sending"), the *data profile* ("which kind of contacts or emails you have in the data"), the *theme* of the app, and the *starting screen* ("do you start from the login page or do you start from another valid page?"). (06:22-06:51)
- The expectation being tested is an invariance claim, stated explicitly: "if you have a model that seems to be good at a given task, you would expect that if you just vary which screen the task is starting from, or what is the theme of the app, the model should pretty much have the same performance." Theme and entry point are cosmetic with respect to the task's goal. (10:27-10:42)
- The finding: "in the worst case, frontier models are pretty bad actually at being robust to these variations… this is actually not the case for most frontier models." Reported as a per-axis worst case rather than a delta on the mean — the useful statistic is where the model falls apart, not how much the average moved. (10:16-10:46)
- What it is for: "if you have infrastructure like this, you can actually measure that and tailor your expectation about this kind of robustness." The output is a calibrated expectation for deployment, not a leaderboard entry. (10:46-10:55)
- This measurement only exists as a byproduct of building the environment correctly — it requires configurations that vary one factor at a time while holding the task fixed, which is what [the config compiler](generate-task-configurations-by-compiling-and-rejecting-invalid-combinations.md) produces and what [the multifactorial PRISM property](design-eval-environments-to-the-prism-principles.md) requires. A benchmark that only reports average success across a fixed task set cannot compute it at all.
- It also connects the two halves of the talk: per-axis variation is what produces environment variance, and environment variance is the term [naive confidence intervals omit](compute-confidence-intervals-over-both-action-and-environment-variance.md). A model with a bad worst-case axis is exactly the model whose single-base-case interval will be most misleadingly tight.
- Consistent with, and mechanistically explained by, the browser-automation account elsewhere in this wiki: an agent whose competence lives in a recorded or memorized action path has nothing to fall back on when the entry screen changes, whereas one that [senses, acts, and verifies through a different channel](verify-an-action-through-a-different-channel-than-the-one-that-acted.md) can detect that it is not where it expected to be. Fragility to starting state is the observable symptom of the former.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Design Eval Environments to the PRISM Principles](design-eval-environments-to-the-prism-principles.md)
- [Generate Task Configurations by Compiling and Rejecting the Invalid Ones](generate-task-configurations-by-compiling-and-rejecting-invalid-combinations.md)
- [Compute Confidence Intervals Over Both Action and Environment Variance](compute-confidence-intervals-over-both-action-and-environment-variance.md)
- [A Blind Replay Script Exposes a Deterministic Benchmark](a-blind-replay-script-exposes-a-deterministic-benchmark.md)
- [Compose Computer-Use Agents From Reliable Atomic Actions](compose-computer-use-agents-from-reliable-atomic-actions.md)
- [Verify an Action Through a Different Channel Than the One That Acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md)
- [Push Agent Benchmarks on Environment Complexity, Autonomy Horizon, and Output Complexity](push-agent-benchmarks-on-environment-autonomy-and-output-complexity.md)

Sources:
- [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../sources/20260814_CTLa_p6iOiY.md), 06:22-06:51, 09:59-10:55
