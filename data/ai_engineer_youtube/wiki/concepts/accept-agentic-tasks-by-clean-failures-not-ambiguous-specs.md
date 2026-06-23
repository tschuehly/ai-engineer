# Accept Agentic Training Tasks by Clean Failures, Not Ambiguous Specs

Summary: When curating agentic RL or eval tasks, accept the ones that are genuinely hard and reject the ones that only *look* hard because of bad specification. The reliable signal is whether failures are "clean" (the model fails for a real reason) versus degenerate (the task is unsolvable, the spec and tests disagree, or required context was never provided). Ambiguous specs do not produce harder tasks; they produce noise.

Use when:
- Building or filtering agentic tasks for RL training or benchmarking and deciding which to keep.
- Diagnosing why a benchmark's failures are not giving useful training or evaluation signal.
- Telling a genuinely difficult, multi-step task apart from an under-specified one.

Details:
- Snorkel gates each task on four automated criteria: achievable, non-trivial, functionally correct (the logic plays as expected), and environment-reliable/reproducible. Pass all → "accepted" (high quality, usable for training); otherwise → "rejected." Tasks run in containerized environments (reproducibility, isolation, parallel rollouts) built with the Harbor framework / OpenEnv. (03:30-04:54, 02:27-03:57)
- Behavioral proxies confirm the gate: accepted tasks averaged 2x as many tool calls (more steps, more external-tool engagement), a lower pass rate (higher intrinsic difficulty), and more output tokens (more reasoning) when run with Sonnet 4.5 and Codex. (05:17-06:06)
- Clean-failure diagnostic: categorize the failures. Accepted tasks produce *cleaner* failures — the model fails because the steps are genuinely harder (logic error, incomplete task = not reaching the needed logical conclusion), which is useful to hill-climb on. Rejected tasks fail for degenerate reasons: an environmental problem no model could solve, or a tactical context that is "just not working" — failures with no meaningful learning signal. (06:08-08:40)
- Under-specification is the canonical rejected-task failure: the desired testable outcome is not clearly specified up front, but the back-end tests expect things "never actually requested," so the task only *appears* harder (a spec-test mismatch). A related case is implicit dependencies — the tests require a dependency the task never specifies and never feeds into the model's context, so the model lacks what it needs to satisfy them. (14:19-15:17)
- Noise-masking corollary: tasks that "can never be completed" become a source of noise that masks whether the model actually improved, conflating task-quality issues with genuine benchmark saturation. (12:54-13:52)
- Caveat — do not confuse under-specified (noise) with genuinely multi-step/iterative (good): not every task is one-shot, so the fix is to make the outcome verifiable on the back end. Done right, the learned skills still transfer to unverifiable or iterative settings; verifiable domains (coding, math) are easy, "fuzzy" domains are harder. (15:20-16:15)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Task Quality Drives a 5x RL Training Uplift](task-quality-drives-rl-training-uplift.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Benchmark saturation pushes capability evals toward human time horizons](benchmark-saturation-pushes-capability-evals-toward-human-time-horizons.md)
- [Inspect rollouts before trusting RL environment scores](inspect-rollouts-before-trusting-rl-environment-scores.md)
- [Prefer outcome verifiers over ground-truth path checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md)

Sources:
- [Task Fidelity Scaling Laws — Kobie Crawford, Snorkel](../sources/20260602_YYH0DMQr30A.md), 03:30-08:40, 12:54-16:15
</content>
