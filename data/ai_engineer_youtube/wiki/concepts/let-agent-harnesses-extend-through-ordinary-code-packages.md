# Let agent harnesses extend through ordinary code packages

Summary: Agent harness extension can use ordinary code modules and package managers instead of bespoke marketplaces or core forks. This keeps experimental capabilities installable, hot-reloadable, and outside the default context surface.

Use when:
- Adding optional capabilities such as subagents, plan mode, MCP support, memory, custom compaction, or custom providers.
- Deciding whether an agent feature belongs in core, a plugin, a skill, or a normal package-manager distribution path.

Details:
- pi treats extensions as TypeScript modules that can be loaded by the harness and pointed to from disk. (07:53-08:16)
- The extension API can expose tools and slash-command shortcuts, listen to events, react to harness activity, store session state for agent or analysis tools, customize compaction, and change providers. (08:16-08:48)
- Zechner argues extensions should be bundled and published through existing package managers such as npm or GitHub rather than through new siloed marketplaces. (08:48-09:04)
- During extension development, pi supports hot reload so the agent and user can iterate inside the same session and immediately see the effect of changes. (09:04-10:08)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Plugin architectures let agent systems absorb experiments](plugin-architectures-let-agent-systems-absorb-experiments.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)

Sources:
- [Building pi in a World of Slop - Mario Zechner](../sources/20260416_RjfbvDXpFls.md), 07:53-10:25
