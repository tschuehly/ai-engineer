# Self-Reported Task Duration Is a Weak Productivity Signal

Summary: Developer surveys can capture perceived productivity, but self-reported task duration is a poor basis for speedup estimates. Productivity studies should prefer observed timing, assignment logs, task traces, or controlled comparisons over recalled elapsed time.

Use when:
- Designing surveys or telemetry for AI coding-tool productivity studies.
- Interpreting claims that developers say AI made specific tasks faster or slower.

Details:
- The source says software-engineering studies repeatedly find that asking people how long a task took is unreliable; people can report felt productivity, but elapsed-time recall is often wrong. (08:53-09:15)
- Because speedup is a ratio over time, weak timing measurements can dominate the conclusion even when participants accurately describe whether the tool felt useful. (08:53-10:13)
- For AI productivity evaluation, self-report should be paired with observed task traces or experimental assignment data so J-curves, task selection, and repository familiarity do not become post-hoc explanations for noisy timing estimates. (10:41-16:12)

- **A talk that keeps the two instruments apart, and a self-report that lands far from the measurement.** Liguori's own estimate is explicitly flagged as anecdotal — "completely anecdotally, based on my own experience, I've really only felt maybe 10 to 20% more productive with all of these phases that have come before" — while the pilot number is a deployment-velocity measurement across 50 teams. She uses self-report only for the *causal explanation*: the five habits come from interviewing participating teams about what they changed, not from measuring which change produced which gain. That division is the usable pattern — measure the outcome, interview for the mechanism, and do not let the interview supply the magnitude — and it also bounds the habits' evidential status, since no habit is attributed to any share of the improvement. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 01:11-01:34, 07:49-08:24)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Measure AI developer productivity with field experiments, not benchmark extrapolation alone](measure-ai-developer-productivity-with-field-experiments-not-benchmark-extrapolation-alone.md)
- [Do not use token volume as a developer productivity metric](do-not-use-token-volume-as-a-developer-productivity-metric.md)
- [Stage Productivity Pilots to Strip One Confound at a Time](stage-productivity-pilots-to-strip-one-confound-at-a-time.md)

Sources:
- [How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR](../sources/20260119_k1t2xyWMUdY.md), 08:53-16:12
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 01:11-01:34, 07:49-08:24
