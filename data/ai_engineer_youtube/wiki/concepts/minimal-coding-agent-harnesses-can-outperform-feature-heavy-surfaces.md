# Minimal coding-agent harnesses can outperform feature-heavy surfaces

Summary: A coding-agent harness does not need a large tool catalog or elaborate UI to be effective. Minimal surfaces can reduce context noise and leave the model with a clearer execution contract.

Use when:
- Designing a first version of a coding-agent harness or evaluating whether a feature belongs in the default surface.
- Choosing between terminal-first, file-tool-first, subagent-heavy, or plugin-heavy agent workflows.

Details:
- Zechner highlights Terminal-Bench as a minimal harness that gives the model a way to send keystrokes to a tmux session and read the output, with no file tools or subagents, yet it was one of the best-performing leaderboard harnesses in late 2025. (04:46-05:25)
- He argues current coding-agent harnesses are still experimental and that minimal cores can be preferable while the field discovers which abstractions actually help. (05:25-05:47)
- pi follows this pattern by stripping the harness down to provider abstraction, a simple agent loop with tool calling, compact tool definitions, and small system-prompt guidance rather than large default prompt payloads. (05:47-07:26)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)

Sources:
- [Building pi in a World of Slop - Mario Zechner](../sources/20260416_RjfbvDXpFls.md), 04:46-07:26
