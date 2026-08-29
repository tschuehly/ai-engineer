# Shift Review and Testing Left for Confident Vibe Coding

Summary: Enterprise AI coding needs review, testing, and best-practice context inside the generation workflow, not only as after-the-fact PR feedback. "Confidence" comes from turning quality work into agentic SDLC workflows rather than treating vibe-coded output as done when it runs once.

Use when:
- Designing AI coding workflows for mature repositories where maintainability and standards matter.
- Deciding where review and testing agents should sit relative to code generation.

Details:
- The talk distinguishes simple prompt-to-app work from enterprise software, where reliable workflows need review, testing, bug fixing, refactoring, feature changes, maintainability, and standards. (05:17-06:53)
- Review and testing should not be only hindsight inside IDE or PR tools; they should act like a tech-lead red team during the work so generated code follows company best practices before the developer waits for a later AI review. (06:53-08:08)
- Confident vibe coding requires the right context plus workflows connected to agents; manual context collection is framed as too weak to be a game-changing workflow. (10:59-11:35)
- Qodo's example links review-collected best practices back into generation or IDE assistance so quality knowledge learned over time can shape later coding runs. (12:34-13:29)
- **Shifting left can mean manufacturing the artifact that review needs, not only running checks earlier.** Metronome's skills files make the agent flow synthetic usage into the platform during setup, because "what it means to test your initial setup is not just that you can see a contract… or see a customer provision but also you need to see usage." Without that, the earliest reviewable evidence of a correct pricing model would be a real customer's first invoice. The generalization: when a system's correctness only shows up in a derived artifact, moving review left requires generating the input that produces it. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 07:53-08:19)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI Code Quality Needs Full-SDLC Workflows](ai-code-quality-needs-full-sdlc-workflows.md)
- [AI Review Gates Turn Standards Into Executable Feedback](ai-review-gates-turn-standards-into-executable-feedback.md)
- [Context Quality Determines AI Code Review Trust](context-quality-determines-ai-code-review-trust.md)
- [Seed the Agent-Built Sandbox With Usage, Not Just Objects](seed-the-agent-built-sandbox-with-usage-not-just-objects.md)

Sources:
- [Vibe Coding with Confidence - Itamar Friedman, Qodo](../sources/20250806_n991Yxo1aOI.md), 05:17-08:08, 10:59-13:29
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 07:53-08:19
