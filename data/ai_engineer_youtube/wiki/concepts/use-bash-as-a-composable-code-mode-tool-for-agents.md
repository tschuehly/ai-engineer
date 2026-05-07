# Use Bash as a composable code-mode tool for agents

Summary: Shell access can be a broad agent capability when it is paired with permissions and sandboxing. Bash lets an agent compose existing programs, files, scripts, package-manager commands, search, pipes, and verification steps instead of requiring a bespoke tool for every use case.

Use when:
- Choosing between many narrowly hand-authored tools and a sandboxed command-line surface.
- Designing coding or knowledge-work agents that need to transform, search, verify, or summarize local artifacts.

Details:
- The source calls Bash an early form of code mode because it lets the agent store tool results to files, store memory, generate and call scripts, and compose commands such as `tail` and `grep`. 15:51-16:25
- Existing software such as FFmpeg and LibreOffice can become agent capabilities through Bash without creating one custom tool per operation. 16:26-16:34
- For coding agents, Bash lets the model discover and run local project checks such as `npm run lint` instead of requiring a prebuilt linter tool. 16:36-17:13
- In a non-coding email example, saving search results, grepping prices, writing intermediate files with line numbers, and checking extracted values gives the agent a more inspectable path than reasoning over a raw pile of messages. 17:28-19:00
- CWM intentionally uses fewer tools than many coding-agent systems and emphasizes Bash so the model learns terminal commands, file mutation, code execution, and repository-level work in an engineer-like environment. 06:55-08:05
- A Codex CLI subagent prototype uses ordinary shell wrappers as a composable harness layer: the parent agent invokes a stable command, the wrapper launches a child `codex exec`, and stdout becomes the parent-visible result. 02:40-03:22, 08:09-08:57

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)
- [Run agent-written API code inside programmable sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Sandboxed code execution turns model reasoning into inspectable computation](sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md)
- [Shell-wrapped subagents can retrofit harness capabilities](shell-wrapped-subagents-can-retrofit-harness-capabilities.md)

Sources:
- [Claude Agent SDK [Full Workshop] - Thariq Shihipar, Anthropic](../sources/20260105_TqC1qOfiVcQ.md), 15:51-19:00
- [Code World Model: Building World Models for Computation - Jacob Kahn, FAIR Meta](../sources/20251217_sYgE4ppDFOQ.md), 06:55-08:05
- [Hacking Subagents Into Codex CLI - Brian John, Betterup](../sources/20251124_5eJqXtevlXg.md), 02:40-03:22, 08:09-08:57
