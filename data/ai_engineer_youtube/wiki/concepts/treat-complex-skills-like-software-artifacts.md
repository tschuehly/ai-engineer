# Treat Complex Skills Like Software Artifacts

Summary: Skills start as folders and Markdown instructions, but once they include scripts, binaries, assets, dependencies, and runtime assumptions, they need software-like testing, versioning, dependency metadata, and lineage.

Use when:
- Building skills that contain executable tools, assets, or dependencies.
- Reviewing whether a shared or enterprise skill is maintainable enough for production use.

Details:
- Skills can remain simple `SKILL.md` prompt files, but the ecosystem already includes skills packaging software, executables, binaries, files, code, scripts, assets, and other maintained artifacts. 07:28-08:04
- Complex skills need tests and evals that check whether agents load and trigger them for the right task, and whether the output quality is appropriate for the intended workflow. 10:38-11:14
- Versioning should track both skill changes and resulting agent behavior over time, because skill edits change the runtime instructions and tools an agent applies. 11:14-11:26
- Dependency metadata should let a skill refer to other skills, MCP servers, packages, or environment capabilities so runtime behavior is more predictable across agent products. 11:26-11:57

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Package reusable context as skills, libraries, and registries](package-reusable-context-as-skills-libraries-and-registries.md)
- [Evaluate agent skills with task scenarios and comparative conditions](evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md)
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)

Sources:
- [Don't Build Agents, Build Skills Instead - Barry Zhang & Mahesh Murag, Anthropic](../sources/20251208_CEvIs9y1uog.md), 07:28-08:04, 10:38-11:57
