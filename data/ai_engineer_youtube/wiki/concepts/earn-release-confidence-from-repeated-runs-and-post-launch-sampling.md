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
- The same team pairs this with a pre-release decision about which failures matter at all — see the retryability sort — so the pass-rate bar and the sampling rate are applied hardest where a failure cannot be undone by a second click.

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
- [Simulated Conversations Test Customer-Facing Agents Before Launch](simulated-conversations-test-customer-facing-agents-before-launch.md)

Sources:
- [How to build an AI-Native Health Company — Dan Feng, Maven Clinic](../sources/20260819_WJRdLNhrsLQ.md), 15:17-16:50
