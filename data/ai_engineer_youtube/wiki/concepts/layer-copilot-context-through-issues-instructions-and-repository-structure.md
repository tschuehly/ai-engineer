# Layer Copilot Context Through Issues, Instructions, and Repository Structure

Summary: Copilot context is layered across the immediate prompt or issue, repository-wide instructions, task-specific instruction files, existing code structure, and environment setup. The less ambiguity left in those layers, the less likely an asynchronous coding agent is to return a plausible but unwanted implementation.

Use when:
- Writing a GitHub issue intended for Copilot Coding Agent.
- Encoding team coding standards for Copilot chat, agent mode, or background issue work.

Details:
- For asynchronous issue assignment, Harrison warns that the user may not know whether Copilot has everything it needs, so the issue should state both the desired outcome and known implementation approach when that is known. 30:36-31:58
- `copilot-instructions.md` is described as broadly supported by chat and coding-agent workflows, making it a durable repository-level context surface. 32:06-32:35
- Copilot can also consume task-specific instruction files: a Flask endpoint instruction file can describe endpoint expectations, unit tests, project notes, and prototype files. 37:34-38:47
- Instruction files can be scoped by `apply to` path patterns, so guidance for React components, TypeScript files, or test files can load only when matching files are involved. 38:49-39:45
- Existing code quality still matters as implicit context: clear code, comments, and project structure help Copilot explore the repository and infer the intended shape. 35:10-35:43

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Fresh Markdown context mitigates model rot in codegen](fresh-markdown-context-mitigates-model-rot-in-codegen.md)
- [Encode non-functional requirements as agent-visible context](encode-non-functional-requirements-as-agent-visible-context.md)

Sources:
- [Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft](../sources/20250726_DdaAABdAqZY.md), 30:36-32:35, 35:10-35:43, 37:34-39:45
