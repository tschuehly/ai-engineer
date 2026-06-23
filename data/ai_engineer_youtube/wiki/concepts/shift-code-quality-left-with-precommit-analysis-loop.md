# Shift Code Quality Left With a Pre-Commit Analysis and Remediation Loop

Summary: Instead of trusting LLM-generated code and catching defects late in CI or review, move static analysis to before the commit and gate an auto-remediation agent on regression checks. Sonar frames this as the ACDC ("agent-centric development cycle") — Guide, Verify, Solve — where fast pre-commit analysis (1-5 seconds vs 1-5 minutes in CI) feeds issues back to the coding agent, and a remediation agent only presents fixes that re-pass analysis and compilation.

Use when:
- Designing where quality checks run in an agentic coding pipeline (generation time, pre-commit, PR, or CI).
- Building an auto-fix or remediation agent that must not introduce regressions.
- Wanting fast quality feedback inside the coding agent loop rather than after a slow CI cycle.

Details:
- ACDC has three stages with an inner and outer loop: Guide, Verify, Solve. (10:43-11:06)
- Guide stage: Sonar Context Augmentation pushes the entire codebase into the LLM as context, and Sonar Sweep (private beta) treats the training/codebase data so problematic data does not become problematic generated code. (11:06-11:42)
- Verify stage: SonarQube Agentic Analysis (open beta) runs over the generated code through an MCP built into Claude/Codex/Gemini CLI, analyzing pre-commit in 1-5 seconds versus a 1-5 minute CI run; it surfaces issues so the agent fixes them before the developer commits. (11:42-12:40)
- Solve stage: the SonarQube Remediation Agent handles issues that slip through to the PR (and can batch tech debt selected from the dashboard) by creating one PR per issue, generating the fix, re-running analysis and compilation, and discarding any fix that introduces a regression — only passing fixes reach the developer for review and merge. (12:40-14:05)
- The operating principle is "the LLM generates the code but we are not trusting it" — assurance is a separate, verifiable loop rather than an assumption baked into the generation prompt. (14:05-14:38)
- This complements PR-time review gates by pulling the same kind of executable standard earlier (pre-commit) and shrinking the feedback latency a coding agent experiences.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI Review Gates Turn Standards Into Executable Feedback](ai-review-gates-turn-standards-into-executable-feedback.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [AI Code Quality Needs Full-SDLC Workflows](ai-code-quality-needs-full-sdlc-workflows.md)
- [Measure Generated Code Quality Beyond Pass Rate](measure-generated-code-quality-beyond-pass-rate.md)

Sources:
- [Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](../sources/20260531_NuePCNMpWGc.md), 10:43-14:38
