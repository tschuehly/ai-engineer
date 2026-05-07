# Compose Coding-Agent Workflows Through CLI Pipelines

Summary: A command-line interface can turn coding agents into composable workflow units because developers can run them in the background, pipe outputs, collect logs, and chain specialized generation, coverage, review, or custom agents.

Use when:
- Choosing between IDE-only, chat, CLI, MCP, or A2A surfaces for coding-agent workflows.
- Designing agent pipelines that need repeatable composition across multiple SDLC tasks.

Details:
- The talk argues that the CLI is useful for AI coding because it can issue commands to agents as team-member-like workers and support end-to-end flows outside the IDE. (03:15-04:21)
- CLI tools can be run in the background and embedded in workflows, which makes them easier to compose than an IDE plugin when logs, pipelines, or repeated automation are needed. (14:32-17:08)
- A practical pipeline can run code generation, then a coverage-specialized agent, then a review agent; this is not full agent-to-agent communication, but it demonstrates value from passing outputs between specialized agents. (17:08-17:35)
- A2A is presented as the next step when parallel agents need discovery, handshakes, and communication rather than a simple linear pipeline; the talk also notes that active A2A usage was still rare among the speaker group. (17:30-18:29)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)
- [A2A agent registries make deployed agents discoverable through agent cards](a2a-agent-registries-make-deployed-agents-discoverable-through-agent-cards.md)

Sources:
- [Vibe Coding with Confidence - Itamar Friedman, Qodo](../sources/20250806_n991Yxo1aOI.md), 03:15-04:21, 14:32-18:29
