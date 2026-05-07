# Scope bug-hunting rules to specific defect classes

Summary: Coding-agent rules for bug hunting should name concrete security and logic defect classes and require fix validation. Vague instructions to "find bugs" encourage noisy reports and weak fixes.

Use when:
- Writing repository rules, IDE-agent instructions, or review prompts for defect discovery.
- Turning security standards into agent-visible guidance.

Details:
- The talk recommends adding scoped rules for security and logic bugs to the agent's rules file so the model considers those failure modes while reading code. (02:10-02:23)
- OWASP-style guidance and explicit defect classes can prime the agent better than a generic repository-wide bug search. Named examples include auth bypasses, prototype pollution, and SQL injection. (03:03-03:59)
- Bug-hunting rules should require fix validation: the agent should write tests, get them passing, and verify that the reported bug is actually fixed before the change enters the codebase. (04:01-04:10)
- Structured rules reduce vague "check for bugs" requests that produce alert fatigue and can improve output quality. (04:10-04:24)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use repository instructions to ground coding agents](use-repository-instructions-to-ground-coding-agents.md)
- [Shift review and testing left for confident vibe coding](shift-review-and-testing-left-for-confident-vibe-coding.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)

Sources:
- [How to Improve your Vibe Coding - Ian Butler](../sources/20250803_g03m-WFEu1U.md), 02:10-04:24

