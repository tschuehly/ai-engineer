# Earn Release Confidence From Repeated Runs and Post-Launch Sampling

Summary: A nondeterministic system that passes its integration suite once has told you almost nothing. Convert the suite into a pass-rate gate by running every case many times against a threshold, then keep the loop running after launch with automated rubric scoring on every conversation plus a dedicated human group spot-checking output — raising sample coverage for new features, and treating the rubric itself as something the humans are calibrating.

Use when:
- Deciding whether an LLM feature is ready to release when its tests are stochastic.
- Designing CI for agent or conversational systems where a green build is not repeatable.
- Setting up post-launch quality monitoring that does not stop at dashboards.
- Deciding how much human review a launch needs relative to steady state.

Details:
- The suite is broad and growing: "we have like hundreds of integration tests, for which pretty much covered all the use cases we know, and we are keep adding to the integration test suite." Coverage is scoped to known use cases, which is an honest limit rather than a claim of completeness. (Maven Clinic, 15:17-15:33)
- The gate is a repeated-run pass rate, and the reason is stated plainly: passing once "is not good enough anymore, because the LLM can do different things. So, for each test case, we run it to many times. We consistently requires the high pass rate, like for example, 90% for all the time." The bar is on the *rate*, sustained, not on a single green run. (15:33-15:50)
- Post-launch, an automated evaluation system "carefully evaluate[s] each conversation" against "a lot of rubrics, what we think is good, what is bad," producing scores that get reviewed. This is full-population scoring, in contrast to the sampled human pass layered on top. (15:50-16:12)
- The human layer is a standing role, not a rotation: "a dedicated group, their job is mainly review those conversations. We will spot check our conversations." Its output is deliberately two-directional — it says "whether we need to come back to improve our systems, or our rubrics is too strict or too loose, and we need consistently improve it." The humans are auditing the judge as much as the product. (16:12-16:31)
- Sampling rate scales with novelty: for a new feature launch, "not only spot check probably not enough, we really want to review like say 20%, and we can do it." Coverage is a dial tied to how much is unknown, then relaxed as evidence accumulates. (16:31-16:41)
- The purpose is explicitly confidence under known imperfection rather than elimination of it: the whole process exists so "we are really confident whenever we release something, although we know hallucination is there." (16:41-16:50)
- Caveat on what repetition buys, from the computer-use side: repeating a *fixed* scenario narrows the interval around performance on that scenario, which is exactly the procedure D'Oro measures at ~17-20% real coverage against a nominal 95%. Repetition addresses variance in the model's actions; it does not address variance in the environment the task starts in, so a 90%-across-many-runs gate on a fixed set of cases can still be confidently wrong about deployment. The complement is to vary the configuration, not only the seed — see [computing intervals over both action and environment variance](compute-confidence-intervals-over-both-action-and-environment-variance.md). ([Computer Use at the Edge of the Statistical Precipice](../sources/20260814_CTLa_p6iOiY.md), 11:05-13:19)
- The same team pairs this with a pre-release decision about which failures matter at all — see the retryability sort — so the pass-rate bar and the sampling rate are applied hardest where a failure cannot be undone by a second click.
- **The same two-sided shape on a design-to-code MCP server: a high-frequency pre-release harness plus a deliberately weak post-launch signal.** Before release, "an eval that sort of runs like hundreds of times a week. Engineers can kick this off and sort of grade against prompt changes um, with LLM judges." After release, the only production signal available was self-reported: optional tool arguments through which the agent volunteers the user's language and framework, described as "imperfect uh agents lie but it was at least a signal" and used to segment which cohorts had a worse experience rather than to judge any single run. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 06:45-06:58, 12:45-13:09)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Sort Failures by Whether the User Can Retry](sort-failures-by-whether-the-user-can-retry.md)
- [Evaluate Context Changes with Lint, Task Scenarios, and Probabilistic Budgets](evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md)
- [Decompose Evals Into Rubrics to Target the Failing Behavior](decompose-evals-into-rubrics-to-target-the-failing-behavior.md)
- [AI System Evaluation Still Depends on Human Review](ai-system-evaluation-still-depends-on-human-review.md)
- [Size Eval Suites to the Error Rate the Consequence Demands](size-eval-suites-to-the-error-rate-the-consequence-demands.md)
- [Compute Confidence Intervals Over Both Action and Environment Variance](compute-confidence-intervals-over-both-action-and-environment-variance.md)
- [Simulated Conversations Test Customer-Facing Agents Before Launch](simulated-conversations-test-customer-facing-agents-before-launch.md)
- [Optional Self-Reported Tool Arguments Are Segmentation Signal, Not Ground Truth](optional-self-reported-tool-arguments-are-segmentation-signal.md)

Sources:
- [How to build an AI-Native Health Company — Dan Feng, Maven Clinic](../sources/20260819_WJRdLNhrsLQ.md), 15:17-16:50
- [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](../sources/20260814_CTLa_p6iOiY.md), 11:05-13:19
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 06:45-06:58, 12:45-13:09
