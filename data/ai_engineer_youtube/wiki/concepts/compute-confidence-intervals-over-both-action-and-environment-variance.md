# Compute Confidence Intervals Over Both Action and Environment Variance

Summary: An agent eval has two independent sources of randomness — the model's actions, and the environment configuration the task starts in — and repeating rollouts on a single base case only measures the first. Confidence intervals computed that way have real coverage around 17-20% while claiming 95%, and the intervals look *tighter* than honest ones, so they cause confident wrong deployment decisions rather than visibly uncertain ones.

Use when:
- Reporting an agent's benchmark score with error bars, or reading someone else's.
- Choosing between two models whose scores differ by a few points.
- Deciding how many eval runs are enough.
- Building an eval harness whose task set has multiple configurations per task.
- Justifying eval spend to someone who thinks the current numbers already settle the question.

Details:
- The two sources, framed as "not exactly the same but equally important": **action variance** — "you run your model multiple times; in many cases you can have even quite different trajectories out of it because the action at each step would be different" — and **environment variance**, which exists only once the benchmark has multiple configurations per task. (11:05-12:09)
- Why the second is not optional: environment variation "is what we are going to find in the real world," so an interval that omits it is answering a question about a fixed screen rather than about deployment. (11:55-12:04)
- The methodology has to respect the benchmark's *hierarchy*: tasks contain configurations contain rollouts, and the paper's contribution is a method that "can accurately capture these two types of variation taking into account the structure of the benchmark." Pooling all runs as if they were independent samples ignores that two rollouts on the same config are more alike than two rollouts on different configs. (12:09-12:26)
- **Coverage is the diagnostic.** A 95% interval should contain the true performance 95% of the time. Measured: "if you only use rollouts, so you only use the base case — and what people would use normally, actually, in realistic cases — you have something like 17% or 20% coverage." The video description states it as "around 20% rather than 95%." Computing the interval with the hierarchy respected restores "90-95% accurate." (12:26-13:19)
- The direction of the error is what makes it dangerous: the bad intervals are *narrow*. "You can have cases in which the confidence intervals seem really really small, and so you make a decision based on those small confidence intervals, but they are actually overconfident" — the true values fall outside. An honest analysis would have produced wide bars that stopped the decision; the naive one produces tight bars that authorize it. (13:22-13:49)
- Priced, which is the argument to use with a budget owner: one million tasks, a real 4% gap between the two models, and a cost per mistake of "$20 — uh, like $12 on average" (a self-correction, kept as spoken) "can cost you like hundreds of thousands of dollars in a single month… just for a confidence interval being overconfident." (13:52-14:22)
- **The useful output of an honest interval is a refusal.** "The method would tell you 'I'm not confident enough to make an informed decision,' and so you can choose to spend more money, to spend more time on evaluating models, and avoid the costly mistake." Treat "insufficient evidence, buy more evaluation" as a first-class verdict alongside A-wins and B-wins. (14:24-14:47)
- Relation to the wiki's existing repeated-run practice: [converting a suite into a repeated-run pass-rate gate](earn-release-confidence-from-repeated-runs-and-post-launch-sampling.md) attacks action variance and is necessary but not sufficient — running the same fixed scenario 100 times narrows the interval around performance *on that scenario*, which is precisely the naive procedure measured here at ~20% coverage. The complement is varying the configuration, not only the seed.
- Relation to [sizing a suite to the error rate the consequence demands](size-eval-suites-to-the-error-rate-the-consequence-demands.md): that page sizes the suite from detection statistics for a known target failure rate; this one says the sample must be spread across environment configurations, not only across repetitions, or the resulting interval overstates what the sample supports.
- The disposition the talk closes on, aimed at the "there is no error bar but I don't see people using them" shrug: "a non-rigorous benchmark is misleading" — for the field, and "especially for your own decisions." (15:57-16:46)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [pass@k on a Deterministic Environment Measures Replay, Not Capability](passk-on-a-deterministic-environment-measures-replay.md)
- [Design Eval Environments to the PRISM Principles](design-eval-environments-to-the-prism-principles.md)
- [Measure Agent Robustness per Variation Axis, Not Just Average Success](measure-agent-robustness-per-variation-axis-not-just-average-success.md)
- [Earn Release Confidence From Repeated Runs and Post-Launch Sampling](earn-release-confidence-from-repeated-runs-and-post-launch-sampling.md)
- [Size Eval Suites to the Error Rate the Consequence Demands](size-eval-suites-to-the-error-rate-the-consequence-demands.md)
- [Realistic Traffic, Not Volume, Is the Hard Part of Load Testing](realistic-traffic-not-volume-is-the-hard-part-of-load-testing.md)
- [Prefer simple, debuggable eval scores](prefer-simple-debuggable-eval-scores.md)

Sources:
- [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../sources/20260814_CTLa_p6iOiY.md), 11:05-14:47, 15:57-16:46
