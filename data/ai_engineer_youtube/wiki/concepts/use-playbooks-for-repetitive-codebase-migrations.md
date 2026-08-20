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
- **A playbook can be a checked-in document that a scheduler runs, not only a procedure a human replays.** GitHub's agentic workflows keep the migration procedure as Markdown in the repository — prose steps in the body, a declarative manifest of permissions, tools, and network destinations in the front matter — compiled into a CI workflow. Gazit's dependency-upgrade job was authored as roughly three lines, "something a lot like a Slack message that I'd send to a junior developer," and expanded into the full sequence he never wrote: check for a new release, read the changelog and upgrade guide, apply it, open a PR. The demonstrated run crossed two major versions of Astro, fixed the broken call sites, verified the build, and separately listed the manual steps it could not take. Two properties matter for playbook design here: expansion was codebase-aware ("because it sees my codebase, it was able to infer what it even needs to check"), so the playbook did not have to enumerate the project's specifics; and the durable artifact is the English, since "if you don't like the way that the automation works, just edit the English" ([the Markdown workflow is the source](the-markdown-workflow-is-source-the-yaml-is-a-compiled-artifact.md)). Caveat: one successful upgrade on a personal site, with no failure cases shown. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 04:55-06:58, 09:35-10:35)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Manual migration seeds teach agents the hidden constraints](manual-migration-seeds-teach-agents-the-hidden-constraints.md)
- [Agentic coding transforms existing software](agentic-coding-transforms-existing-software.md)
- [Skills turn procedural feedback into transferable agent memory](skills-turn-procedural-feedback-into-transferable-agent-memory.md)
- [The Markdown Workflow Is the Source; the YAML Is a Compiled Artifact](the-markdown-workflow-is-source-the-yaml-is-a-compiled-artifact.md)

Sources:
- [Devin 2.0 and the Future of SWE - Scott Wu, Cognition](../sources/20250725_MI83buT_23o.md), 03:34-06:25
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 04:55-06:58, 09:35-10:35
