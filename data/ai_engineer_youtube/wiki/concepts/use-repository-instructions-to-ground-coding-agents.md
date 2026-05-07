# Use Repository Instructions To Ground Coding Agents

Summary: Repository-level instructions turn team conventions into durable model-visible context. They should explain the codebase foundation, stack, versions, tools, and working style that should apply across Copilot requests.

Use when:
- Setting up a repository so coding agents can follow local conventions without every prompt restating them.
- Reviewing whether agent guidance belongs in shared repo instructions, user settings, or a task-specific prompt.

Details:
- Copilot instructions live in `.github/copilot-instructions.md` and are included with agent, chat, and inline requests, making Markdown guidance part of the agent's default repository context. (38:14-39:22)
- Useful instructions start with core foundation knowledge such as stack, framework, version, and important project practices; stale or overly broad copied lint rules should be avoided because they turn shared context into noise. (39:22-40:58)
- The speakers distinguish "how" from "what": instructions should encode how the agent should work in this repository, while the current task prompt should state what to change. (45:09-45:14)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Give coding agents the same engineering infrastructure humans need](give-coding-agents-the-same-engineering-infrastructure-humans-need.md)
- [Encode non-functional requirements as agent-visible context](encode-non-functional-requirements-as-agent-visible-context.md)
- [Configure Agent Modes, Rules, and Permissions as the Workflow Evolves](configure-agent-modes-rules-and-permissions-as-the-workflow-evolves.md)

Sources:
- [Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison](../sources/20250803_eOxOzcw70f0.md), 38:14-40:58, 45:09-45:14
