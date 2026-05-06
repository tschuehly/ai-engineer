# Guard AI-Assisted Platform Contributions With Policy and Context

Summary: AI can lower the barrier for developers to contribute to internal platforms, but platform owners need hard policies plus agent-readable contribution context to preserve security, compliance, standards, and maintainability.

Use when:
- Opening platform repositories to broader AI-assisted contributions.
- Deciding which contribution rules belong in policy enforcement versus `AGENTS.md`, skills, or documentation.

Details:
- The talk encourages platform teams to welcome contributions because AI agents can lower the entry barrier and help platform users contribute fixes or features. (15:19-15:52)
- That lower barrier is double-edged: the platform-owning team remains responsible for maintainability and must decide what contribution standards matter for security, compliance, and conventions. (15:52-16:24)
- Hard guardrails or policies should enforce outcomes that must never happen, while `AGENTS.md`, skills, and Markdown contribution guidance can tell agents how to build, test, deploy, verify, and follow platform conventions. (16:25-17:05)
- Agent-facing contribution context can be layered: general instructions can apply across systems, with repository- or project-specific files overriding or extending them for local workflows. (14:24-14:54)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use reviewer agents and lints to turn review lessons into guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)

Sources:
- [Platforms for Humans and Machines: Engineering for the Age of Agents - Juan Herreros Elorza](../sources/20260408_cCRO3ChaYhM.md), 14:24-17:05
