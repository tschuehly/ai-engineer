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
- Production usage data corroborates the shift toward this surface: a Tailscale talk that watches every agent LLM call at the network layer reports that internally "bash dominates everything else" over structured/MCP tool calls — and frames "a lot of agents are moving away from tool calls and executing code" as the reason to instrument at the LLM layer rather than the MCP layer, since structured-tool traffic no longer captures what agents do. BM2JX9hqsVQ 22:54-23:11, 21:28-22:10

- **The CLI's advantage stated as a context-disposal property.** Uber projected its entire MCP catalog into commands, and the reason given is narrow and reusable: "we projected all of these MCPs into CLI pattern so that even the response doesn't eat up in your context" ([Medisetty](../sources/20260821_17-YSUHo6Lk.md), 05:06-05:21). That names what a CLI actually changes relative to a tool call — not the protocol and not the capability, but who decides what happens to the output. A tool result is pasted into the transcript whole; a command's output lands somewhere the agent can filter, page, or discard. It is the same tools with a different default disposal policy, which is why the projection was mechanical enough to apply to the whole catalog at once. See [Stage the MCP Token Tax Down](stage-the-mcp-token-tax-down-direct-omni-cli-then-code-mode.md).

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)
- [Run agent-written API code inside programmable sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Sandboxed code execution turns model reasoning into inspectable computation](sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md)
- [Shell-wrapped subagents can retrofit harness capabilities](shell-wrapped-subagents-can-retrofit-harness-capabilities.md)
- [Make the LLM Gateway the Agent Observability Chokepoint](make-the-llm-gateway-the-agent-observability-chokepoint.md)
- [Stage the MCP Token Tax Down: Direct, Omni, CLI, Then Code Mode](stage-the-mcp-token-tax-down-direct-omni-cli-then-code-mode.md)

Sources:
- [Claude Agent SDK [Full Workshop] - Thariq Shihipar, Anthropic](../sources/20260105_TqC1qOfiVcQ.md), 15:51-19:00
- [Code World Model: Building World Models for Computation - Jacob Kahn, FAIR Meta](../sources/20251217_sYgE4ppDFOQ.md), 06:55-08:05
- [Hacking Subagents Into Codex CLI - Brian John, Betterup](../sources/20251124_5eJqXtevlXg.md), 02:40-03:22, 08:09-08:57
- [What if the network was the sandbox? — Remy Guercio, Tailscale](../sources/20260601_BM2JX9hqsVQ.md), 21:28-23:11
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 05:06-05:21
