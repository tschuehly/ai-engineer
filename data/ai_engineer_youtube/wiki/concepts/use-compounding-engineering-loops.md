# Use Compounding Engineering Loops

Summary: Compounding engineering is a loop where agent-assisted work leaves behind reusable context, tools, and prompts that make the next feature easier. The loop is plan, delegate, assess, and codify.

Use when:
- Turning repeated coding-agent lessons into shared organizational context.
- Designing prompts, subagents, slash commands, or repo guidance that should improve future work.

Details:
- The source defines compounding engineering as the opposite of traditional feature accumulation: each feature should make the next feature easier rather than harder. (08:35-09:11)
- The loop starts with detailed planning, then delegates implementation to an agent, then assesses through tests, trying the change, code review, or agent code review. (09:14-09:44)
- The codify step captures what was learned from planning, delegation, assessment, bug fixes, and plan repairs into `CLAUDE.md`-style files, subagents, slash commands, and shared prompt libraries. (09:44-10:29)
- Codified tacit knowledge can make onboarding faster because new hires inherit environment setup, commit conventions, and PR expectations through agent-readable files. (12:13-12:44)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Context development lifecycle treats context as an engineered artifact](context-development-lifecycle-treats-context-as-an-engineered-artifact.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Govern agent rules through feedback gatekeepers](govern-agent-rules-through-feedback-gatekeepers.md)

Sources:
- [Dispatch from the Future: building an AI-native Company - Dan Shipper, Every, AI & I](../sources/20251218_MGzymaYBiss.md), 08:35-12:44
