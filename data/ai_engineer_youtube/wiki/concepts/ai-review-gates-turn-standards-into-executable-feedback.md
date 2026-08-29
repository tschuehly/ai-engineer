# AI Review Gates Turn Standards Into Executable Feedback

Summary: AI code review can make standards enforceable when it runs at PR time, checks explicit rules, uses local examples, reports trends, and learns from whether suggestions are accepted. This is stronger than hoping generation-time rules are followed perfectly.

Use when:
- Turning team style, safety, reliability, or testing standards into repeatable PR checks.
- Deciding whether an AI code-review tool should block, warn, or collect feedback on recurring issues.

Details:
- The talk notes that editor rules for code generation are often followed only partially, so the review layer should not assume generation-time prompts enforce every standard. (02:26-03:19)
- AI review tools can gate PRs on process expectations such as required test coverage, thereby using review to enforce a testing-quality workflow. (12:57-13:24)
- A review rule can be built from team context, good examples, and bad examples, then applied to PRs that violate the intended pattern. (19:04-19:55)
- Rule systems should provide statistics, CLI checks, and acceptance signals so teams can see whether a standard is being followed and adjust the rule over time. (19:19-20:20)

- **What has to be written down before a gate can execute anything**, enumerated by Sonar as the Guide phase: "your desired architecture for the software" and its constraints, "your coding standards and your coding patterns that are acceptable," "the list of dependencies that you are and are not allowed to use," syntax standards, and "your logging practices or your observability and tracing practices." Then the thresholds themselves — "what are the levels of security, of quality, of maintainability that you're willing to accept in your code that you're pushing into production. You need to basically write that down and encode it." The pairing with this page's point is that the same encoded standard serves both ends of the loop: it is context handed to the agent before it writes *and* the criterion the gate applies after. Sonar ships defaults that teams adjust, which is a different starting point from deriving every rule from observed violations. ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 16:03-16:59)
- **A blocking instantiation that splits the two layers by what each is good for**: at PR time "a superhuman review that is LLM driven" produces findings while "a computational review… actually assigns grades" for quality, security, and maintainability and "won't allow the PR to go past into production unless it gets a passing grade across that criteria." The reasoning layer advises; the reproducible layer blocks. That is the answer to this page's block-or-warn question when the gate has to be defensible: only the deterministic layer can be shown to have run the same way every time. See [Choose Verification Layers by Defect-Class Coverage](choose-verification-layers-by-defect-class-coverage.md). Vendor talk with no measurement of either layer. (18:25-18:58)

- **Why a mandatory check cannot live in the coding agent's own configuration.** Uber's reliability argument for putting security and compliance review in the platform rather than in each team's skill set: "we need to make sure that we have security and compliance reviews run across everything. We can't rely on teams hoping to run the code review skill that happens. We need reliability there." A rule in the harness is advisory, because whether it ran depends on how somebody invoked the agent; the same rule in the review service runs on every change by construction. The corollary they draw is loop parity — route the agent loop into the same review platform as the pull request so "our agents are getting the same code review, the same rules, everything applied as our humans do," which also prevents agents from optimizing against a rule set the merge gate does not hold. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 01:46-02:04, 02:43-02:57)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use reviewer agents and lints to turn review lessons into guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)
- [Agent rules should emerge from observed off-rail behavior](agent-rules-should-emerge-from-observed-off-rail-behavior.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Choose Verification Layers by Defect-Class Coverage](choose-verification-layers-by-defect-class-coverage.md)
- [Fix Defects Inside the Agent Loop Before They Become Foundation](fix-defects-inside-the-agent-loop-before-they-become-foundation.md)
- [Distributed Rule Authoring Is a Platform Problem, Not an Authoring Problem](distributed-rule-authoring-is-a-platform-problem.md)

Sources:
- [The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo](../sources/20251211_rgjF5o2Qjsc.md), 02:26-03:19, 12:57-13:24, 19:04-20:20
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 16:03-16:59, 18:25-18:58
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 01:46-02:04, 02:43-02:57
