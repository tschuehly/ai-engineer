# Context Development Lifecycle Treats Context as an Engineered Artifact

Summary: Context should be managed through a repeatable lifecycle instead of as one-off prompt text. The reusable loop is generate, evaluate, distribute, observe, adapt, and regenerate context from feedback.

Use when:
- Designing a team process for maintaining prompts, skills, rules, memory, or context packages.
- Explaining why context updates need ownership, tests, distribution, and observability like code changes.

Details:
- Debois argues that as coding shifts from direct code edits to agent instructions, context becomes a primary work product that needs a consistent development lifecycle (02:37-03:18).
- The proposed loop generates context, tests it, distributes it to colleagues or other organization areas, observes whether it works, then adapts and regenerates it from those observations (03:18-03:45).
- Generated context can include handwritten prompts, reusable instruction files such as `agent.md`, current library documentation, repository or ticket context, and spec-driven prompts that agents break into plans (03:50-06:03).
- Context can also absorb workflow logic that would be difficult to encode as product code, such as asking an agent to inspect a user's package manager and ecosystem before guiding installation steps (01:41-02:35).

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](demand-driven-context-pulls-knowledge-from-failed-work.md)

Sources:
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md), 01:41-06:03
