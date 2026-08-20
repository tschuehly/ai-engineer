# Use Repository Instructions To Ground Coding Agents

Summary: Repository-level instructions turn team conventions into durable model-visible context. They should explain the codebase foundation, stack, versions, tools, and working style that should apply across Copilot requests.

Use when:
- Setting up a repository so coding agents can follow local conventions without every prompt restating them.
- Reviewing whether agent guidance belongs in shared repo instructions, user settings, or a task-specific prompt.

Details:
- Copilot instructions live in `.github/copilot-instructions.md` and are included with agent, chat, and inline requests, making Markdown guidance part of the agent's default repository context. (38:14-39:22)
- Useful instructions start with core foundation knowledge such as stack, framework, version, and important project practices; stale or overly broad copied lint rules should be avoided because they turn shared context into noise. (39:22-40:58)
- The speakers distinguish "how" from "what": instructions should encode how the agent should work in this repository, while the current task prompt should state what to change. (45:09-45:14)

- The cost side of this file is easy to lose, and it argues for a specific shape. Khandelwal: "Don't overload your [CLAUDE.md] or your [AGENTS.md] file into like one big thing. You want to make sure that… it's a thin index that can point through the right files and that's what the agent gets in its like first prompt cuz that's what gets loaded when it starts to work." Because it is charged to every session before any work happens, the useful discipline is pointing rather than explaining, with the material it points at also reachable from the code itself. The corresponding check is a first-prompt token reading — his team treats roughly 20–25K as unavoidable overhead and 40–50K as a symptom. See [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md) and [Measure First-Prompt Context Burn to Test Progressive Disclosure](measure-first-prompt-context-burn-to-test-progressive-disclosure.md). ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 15:36-16:20)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md)
- [Measure First-Prompt Context Burn to Test Progressive Disclosure](measure-first-prompt-context-burn-to-test-progressive-disclosure.md)
- [Give coding agents the same engineering infrastructure humans need](give-coding-agents-the-same-engineering-infrastructure-humans-need.md)
- [Encode non-functional requirements as agent-visible context](encode-non-functional-requirements-as-agent-visible-context.md)
- [Configure Agent Modes, Rules, and Permissions as the Workflow Evolves](configure-agent-modes-rules-and-permissions-as-the-workflow-evolves.md)

Sources:
- [Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison](../sources/20250803_eOxOzcw70f0.md), 38:14-40:58, 45:09-45:14
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 15:36-16:20
