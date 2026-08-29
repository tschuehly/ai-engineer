# Measure AI Developer Productivity With Field Experiments, Not Benchmark Extrapolation Alone

Summary: Rising benchmark scores and model time horizons should be checked against field studies on real developer work. Experienced developers, brownfield repositories, task assignment, learning curves, and review constraints can erase or hide the speedups suggested by lab measurements.

Use when:
- Reconciling SWE-bench or long-task capability gains with measured engineering productivity.
- Designing evals for AI coding tools used by experienced developers on existing codebases.

Details:
- The source frames the core puzzle as a mismatch between improving model benchmarks or time horizons and a METR field study where experienced developers did not clearly speed up on real open-source work. (00:20-01:48, 10:41-11:58)
- Tool-learning or "J-curve" explanations are plausible in general, but the source argues they did not explain much of this study because participants with stronger prior Cursor or AI experience did not show a large point-estimate shift, and many subgroup plots were too noisy to trust. (07:26-16:12)
- Field productivity measurements should preserve the messiness that benchmarks remove: developer experience, repository familiarity, task selection, brownfield constraints, and whether AI shifts effort into review or orchestration. (10:41-16:38, 54:15-54:30)
- A greenfield AI-allowed versus AI-disallowed hackathon is presented as suggestive but too noisy to publish or rely on; the discussion warns against drawing conclusions from overlapping distributions and small point estimates. (21:41-23:09)
- A later METR talk describes the RCT more concretely: 16 experienced maintainers completed real GitHub issues from large mature repositories such as GHC, scikit-learn, and Hugging Face Transformers, with tasks randomly assigned to AI-disallowed or AI-allowed conditions. (10:40-12:29)
- The same talk reports a 19% measured slowdown when AI was allowed, despite experts forecasting about 40% time savings and participants forecasting or retrospectively perceiving positive speedups. (12:29-13:24)
- The speaker cautions against overgeneralizing the result because the study population was unusually high-context, the tasks came from complex long-lived repositories, the experiment was concentrated in March 2025, and the study remained small enough to require follow-up. (15:56-18:10)

- **An internal observational study at the opposite corner of the design space, and why it does not contradict the RCT.** Amazon Stores watched 50 teams with a "normal distribution of early career folks, mid-career, senior engineers" on brownfield codebases "for the better part of last year," measured on "deployment velocity to production," and reports half the teams under 3x and half at a median of 4.5x. The two designs vary different things: METR randomizes *whether AI is allowed* and holds practice fixed, while this pilot holds the tool roughly fixed ("90% of these teams used Kiro") and lets practice vary, so its finding is about dispersion rather than a treatment effect — "it wasn't about the tools, it was about the way that they worked." Neither result licenses the other's headline. This one has no control arm, no per-group n, no distribution, and an output-proxy metric with no quality adjustment; what it has that a lab study cannot is a year of ordinary teams in existing repositories. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 05:48-07:34)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Benchmark narrow slices separately from real expert work](benchmark-narrow-slices-separately-from-real-expert-work.md)
- [Benchmark saturation pushes capability evals toward human time horizons](benchmark-saturation-pushes-capability-evals-toward-human-time-horizons.md)
- [Reliability thresholds determine whether coding agents save time](reliability-thresholds-determine-whether-coding-agents-save-time.md)
- [Do not use token volume as a developer productivity metric](do-not-use-token-volume-as-a-developer-productivity-metric.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)
- [Stage Productivity Pilots to Strip One Confound at a Time](stage-productivity-pilots-to-strip-one-confound-at-a-time.md)

Sources:
- [How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR](../sources/20260119_k1t2xyWMUdY.md), 00:20-23:09
- [Why Agent Hype can fall short of reality - Joel Becker, METR](../sources/20251224_RhfqQKe22ZA.md), 10:40-18:10
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 05:48-07:34
