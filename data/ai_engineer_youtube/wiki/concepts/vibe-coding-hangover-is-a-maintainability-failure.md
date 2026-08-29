# Vibe Coding Hangover Is a Maintainability Failure

Summary: Low-spec, zero-planning coding-agent work can produce a working app while leaving the human unable to understand, maintain, or evolve it. The failure is not that AI wrote the code; it is that the workflow skipped the thinking and artifacts needed for ownership.

Use when:
- Diagnosing why a generated prototype became brittle after the first demo.
- Arguing for planning, decomposition, and validation before giving coding agents broad implementation authority.

Details:
- Gallon defines vibe coding as low-spec, zero-planning AI-accelerated development that feels productive but results in brittle, unmaintainable demo software (01:03-01:24).
- The "hangover" appears when the user wants to add or change a feature and realizes they do not understand the generated system well enough to maintain it (00:47-01:03).
- Treating AI coding agents only as productivity tools can turn augmentation into dependency when engineers stop learning from debugging, modification, and architecture decisions (05:20-05:57).
- The recommended posture is that the human remains the boss of the coding agent: the agent can assist, but the human owns understanding, architectural thinking, and final decisions (06:34-07:00, 17:31-17:58).
- **The team-scale version, and why it is an argument against deferring cleanup.** Denys Linkov reports the same failure at organizational scale rather than on a single prototype: "when you build a lot of code and you do this kind of development in an AI-native world, it starts looking like some of the legacy code we've seen in the past. There's a lot of code written. It's written with low performance or quality, and the broader problem is people don't actually understand what's happening there. So, if you have some issues within the code base or you want to adjust based on customer requirements, it's actually much harder to do so." The consequence he draws is a scheduling one: the pile of un-understood code grows while a team waits for models good enough to clean it up, so "you do have to make sure that there are appropriate guardrails, whether or not you do a full refactor or only a partial one." ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 13:03-13:32)
- **In a money domain the hangover arrives as a wrong invoice, not as unmaintainable code.** Garvin has watched "all sorts of crazy things happen" in billing for years and says it is "getting crazier now that people are expecting to operate Metronome, a very complicated and deep product, with a coding agent." The failure mode is not that the generated configuration is hard to maintain later; it is that it charged a customer incorrectly on day one, which no amount of subsequent refactoring undoes. That inverts the mitigation: not better structure, but a hard environment boundary before the first real charge. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 02:01-02:14, 07:19-07:47)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Vibe engineering is supervised agentic coding with judgment](vibe-engineering-is-supervised-agentic-coding-with-judgment.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Long AI coding conversations compound accidental complexity](long-ai-coding-conversations-compound-accidental-complexity.md)
- [Audit a Refactor Against Having Waited for Better Models](audit-a-refactor-against-having-waited-for-better-models.md)
- [Let the Agent Reach a Test Environment, Not Production, When the Domain Carries Money](let-the-agent-reach-a-test-environment-not-production.md)

Sources:
- [The Cure for the Vibe Coding Hangover - Corey J. Gallon, Rexmore](../sources/20251124_JsKTQbT58BY.md), 00:47-01:24, 05:20-07:00
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 13:03-13:32
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 02:01-02:14, 07:19-07:47
