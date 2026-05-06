# Use Subagents to Isolate Context-Heavy Subtasks

Summary: Subagents can act as separate context windows for bounded subtasks, letting the main agent preserve its working context while specialists search, reason, inspect dependencies, or prepare large mechanical edits.

Use when:
- A coding agent burns too much context on search and reading before it begins editing.
- A task needs deep reasoning or external library lookup without slowing every main-loop step.
- A large refactor needs codemod-style exploration that should not pollute the main agent context.

Details:
- Amp identifies a context exhaustion failure mode where good coding agents grep and read many files, leaving too little context for later editing. (06:00-06:24)
- Simply prompting the agent to read less can create a "doom loop" where it lacks enough context, retries the same edits, and fails to discover what it needs. (06:24-06:42)
- The proposed solution is subagents as subroutine-like calls: a subagent does context-heavy work in its own window and returns only relevant results to the main agent. (06:42-07:05)
- Amp's named examples include a finder for codebase search with a limited tool set and smaller model, an oracle for slower deep reasoning, a librarian for dependency/framework context, and a codemod-oriented agent for large refactors. (07:30-09:06)
- The pattern qualifies generic subagent guidance: role-specific model, tool, and permission choices matter, but context isolation is also a first-order reason to introduce a subagent.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Customize subagents by task, model, tools, and permissions](customize-subagents-by-task-model-tools-and-permissions.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)

Sources:
- [Amp Code: Next Generation AI Coding - Beyang Liu, Amp Code](../sources/20251222_gvIAkmZUEZY.md), 06:00-09:06
