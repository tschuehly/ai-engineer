# pass@k on a Deterministic Environment Measures Replay, Not Capability

Summary: On a deterministic environment, pass@k is provably identical to the success rate of a blind replay agent built from those same k attempts — so reporting pass@k on computer-use tasks is reporting how replayable the benchmark is, not how capable the agent is. The metric is a formalization of the exploit rather than a measurement that survives it.

Use when:
- Choosing which headline metric to report for an agent benchmark.
- Reading a computer-use, GUI, or browser-agent result quoted as pass@k or best-of-k.
- Arguing about whether "the model can do it sometimes" is the capability you actually want to buy.
- Deciding whether repeated sampling is a legitimate way to raise a reported score.

Details:
- Definition, as restated in the talk: pass@k is "the probability of at least one of k attempts succeeding." (02:22-02:36)
- The claim and its status: "if you look into the details of how this metric works on a deterministic environment, you will see that it is literally — and we prove it formally in the paper — evaluating the success rate of the replay agent." This is presented as a proved equivalence in the accompanying paper (arXiv 2605.08261), not as an analogy. (02:36-02:53)
- The mechanism, restated from the two definitions the talk gives: [the replay agent](a-blind-replay-script-exposes-a-deterministic-benchmark.md) is *constructed from* a successful sampled trajectory, and on a deterministic environment replaying that trajectory reproduces the success. So the replay agent succeeds on exactly the tasks where at least one of the k sampled attempts succeeded — which is pass@k.
- The conclusion the speaker draws is about instinct, and is the usable form: "if that replay agent felt weird to you, also pass@k on computer-use tasks should somehow feel weird to you… pass@k is sort of a metrification of that exploit of the replay agent." A metric that inherits an exploit's value is not neutral. (02:53-03:12)
- Scope matters and is stated: the equivalence is derived *on a deterministic environment*. Once the environment varies its data, theme, and starting screen across runs, replaying a recorded trajectory stops reproducing the success, and pass@k stops collapsing onto it. The fix for the metric is therefore the same fix as for the environment — see [the PRISM principles](design-eval-environments-to-the-prism-principles.md).
- Practical reading rule: a pass@k number on a static benchmark answers "does a working action sequence exist for this task, and did sampling find it?" That is a useful question for building training data or for a system that can verify and retry, and a misleading one when quoted as agent success rate for a single-shot deployment.
- The talk generalizes it as one of two classes of failure to design against: environments should not "have exploitable structure," and metrics should not "be based on fragile statistics" — pass@k is the first failure showing up in the second place. (03:12-03:43)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [A Blind Replay Script Exposes a Deterministic Benchmark](a-blind-replay-script-exposes-a-deterministic-benchmark.md)
- [Design Eval Environments to the PRISM Principles](design-eval-environments-to-the-prism-principles.md)
- [Compute Confidence Intervals Over Both Action and Environment Variance](compute-confidence-intervals-over-both-action-and-environment-variance.md)
- [Prefer simple, debuggable eval scores](prefer-simple-debuggable-eval-scores.md)
- [Measure generated code quality beyond pass rate](measure-generated-code-quality-beyond-pass-rate.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)

Sources:
- [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../sources/20260814_CTLa_p6iOiY.md), 02:22-03:43
