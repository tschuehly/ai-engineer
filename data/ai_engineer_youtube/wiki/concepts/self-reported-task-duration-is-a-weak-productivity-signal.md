# Self-Reported Task Duration Is a Weak Productivity Signal

Summary: Developer surveys can capture perceived productivity, but self-reported task duration is a poor basis for speedup estimates. Productivity studies should prefer observed timing, assignment logs, task traces, or controlled comparisons over recalled elapsed time.

Use when:
- Designing surveys or telemetry for AI coding-tool productivity studies.
- Interpreting claims that developers say AI made specific tasks faster or slower.

Details:
- The source says software-engineering studies repeatedly find that asking people how long a task took is unreliable; people can report felt productivity, but elapsed-time recall is often wrong. (08:53-09:15)
- Because speedup is a ratio over time, weak timing measurements can dominate the conclusion even when participants accurately describe whether the tool felt useful. (08:53-10:13)
- For AI productivity evaluation, self-report should be paired with observed task traces or experimental assignment data so J-curves, task selection, and repository familiarity do not become post-hoc explanations for noisy timing estimates. (10:41-16:12)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Measure AI developer productivity with field experiments, not benchmark extrapolation alone](measure-ai-developer-productivity-with-field-experiments-not-benchmark-extrapolation-alone.md)
- [Do not use token volume as a developer productivity metric](do-not-use-token-volume-as-a-developer-productivity-metric.md)

Sources:
- [How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR](../sources/20260119_k1t2xyWMUdY.md), 08:53-16:12
