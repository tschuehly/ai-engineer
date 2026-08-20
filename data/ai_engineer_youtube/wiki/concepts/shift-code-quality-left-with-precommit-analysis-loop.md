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
- **A second account of ACDC ten weeks later restates the argument on different grounds and updates the product state.** The reason to check inside the loop is no longer primarily latency but propagation: issues found during generation "can then be fixed immediately by the agent so they don't propagate into future agentic loops that are going to run in order to fully build out the software project." Latency argues for a faster check anywhere; propagation argues specifically for *inside the loop*, and it survives if CI ever gets fast — see [Fix Defects Inside the Agent Loop Before They Become Foundation](fix-defects-inside-the-agent-loop-before-they-become-foundation.md). The later talk also states that verification "needs to run in both the inner agentic loop and also in the outer loop for CICD," so the pre-commit layer is a way to reach the gate clean rather than a replacement for it. ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 17:41-17:59, 18:25-19:04)
- **The Guide stage has reversed on whole-codebase context, without either talk acknowledging the change.** Where the account above describes pushing the entire codebase into the LLM, the later talk says "you can't just throw your entire code base at the agent up front. It's going to spend a lot of time thrashing and exploring and burning tokens," and describes the tool as serving "the right context at the right time… rules, standards, patterns" plus "a knowledge graph representation of your code base." Take the narrower, later position as the current one and read the earlier bullet as superseded. ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 15:34-17:35)
- **Product state as of the later talk** (useful only for dating claims, and unverified beyond the speaker's word): SonarQube Advanced Security and the remediation agent are described as generally available, "Sonar Vortex" is named as the LLM-review layer built on the acquired Gitar technology, and the analysis layer is integrated with Cursor, Claude Code, Codex, and Antigravity. The remediation agent can be run all the way to "approve those fixes and merge those PRs completely automatically if you wanted to" — which is where the same vendor's zero-trust independence argument collapses for that change; see [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md). (14:20-14:49, 18:25-19:57)
- Caveat spanning both accounts: neither talk measures the shift-left layer. There is no defect-rate comparison against PR-time-only checking, no false-positive rate, and no cost for running analysis on every agent loop; the later demo was a pre-recorded video.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI Review Gates Turn Standards Into Executable Feedback](ai-review-gates-turn-standards-into-executable-feedback.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [AI Code Quality Needs Full-SDLC Workflows](ai-code-quality-needs-full-sdlc-workflows.md)
- [Measure Generated Code Quality Beyond Pass Rate](measure-generated-code-quality-beyond-pass-rate.md)
- [Fix Defects Inside the Agent Loop Before They Become Foundation](fix-defects-inside-the-agent-loop-before-they-become-foundation.md)
- [Choose Verification Layers by Defect-Class Coverage](choose-verification-layers-by-defect-class-coverage.md)
- [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md)

Sources:
- [Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](../sources/20260531_NuePCNMpWGc.md), 10:43-14:38
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 14:20-19:57
