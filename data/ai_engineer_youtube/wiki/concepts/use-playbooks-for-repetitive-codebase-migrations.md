# Use Playbooks for Repetitive Codebase Migrations

Summary: Repetitive codebase migrations are a strong early coding-agent fit when they have clear steps but still need judgment at each file. A playbook can encode the migration procedure so the agent reliably follows the same steps across many files.

Use when:
- Migrating a large codebase through framework, language, or dependency upgrades.
- Deciding whether a task needs an agent, deterministic codemod, or human-led refactor.

Details:
- Wu names JavaScript-to-TypeScript migrations, Angular upgrades, and Java-version upgrades as examples where a massive codebase must be changed file by file.
- These migrations are not always routine enough for a classical deterministic program, but they often have a clear sequence from docs or prior examples that an agent can follow.
- Cognition built playbooks so users could outline a clear set of steps and have Devin execute them step by step; this fit migration work better than open-ended software design.
- Human feedback during repeated runs can become memory or knowledge so future migration attempts remember recurring caveats such as "do X when this pattern appears."

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Manual migration seeds teach agents the hidden constraints](manual-migration-seeds-teach-agents-the-hidden-constraints.md)
- [Agentic coding transforms existing software](agentic-coding-transforms-existing-software.md)
- [Skills turn procedural feedback into transferable agent memory](skills-turn-procedural-feedback-into-transferable-agent-memory.md)

Sources:
- [Devin 2.0 and the Future of SWE - Scott Wu, Cognition](../sources/20250725_MI83buT_23o.md), 03:34-06:25
