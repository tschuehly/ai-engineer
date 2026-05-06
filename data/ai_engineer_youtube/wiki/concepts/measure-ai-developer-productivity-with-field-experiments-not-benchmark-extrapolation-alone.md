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

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Benchmark narrow slices separately from real expert work](benchmark-narrow-slices-separately-from-real-expert-work.md)
- [Do not use token volume as a developer productivity metric](do-not-use-token-volume-as-a-developer-productivity-metric.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)

Sources:
- [How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR](../sources/20260119_k1t2xyWMUdY.md), 00:20-23:09
