# Unified Coding-Agent Harnesses Combine Models, Tools, Environments, and Safety

Summary: A coding agent's capability comes from the model and from the harness that manages tool execution, environment setup, behavior evaluation, and safety boundaries.

Use when:
- Distinguishing raw model capability from a production coding-agent runtime.
- Designing an agent platform that must run commands, tests, code exploration, and integrations safely.

Details:
- The workshop describes Codex as more than a code-writing model: it can run commands, run tests, explore codebases, and work across app, IDE, CLI, Slack, GitHub, and integrations. 01:56-03:55
- The model layer improves through GPT-5.3 Codex, Spark, GPT-5.4, and smaller variants, but Codex also depends on a unified agent harness for behavior management, tool execution, environment setup, and safety. 02:18-03:12
- Serving and UX improvements are part of the agent system: websockets and fast mode are framed as token-speed improvements that make long-running agent work feel more usable. 06:11-06:55
- A future-proofing talk defines the harness as the model-facing layer for prompts, tools, multi-turn work, code interaction, and user interpretation; maintaining it also includes compaction, parallel tool calls, sandboxing, permissions, port management, MCP support, and image handling. 02:06-04:24, 08:31-10:04

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Prompt-coded product behavior reduces code but weakens hard guarantees](prompt-coded-product-behavior-reduces-code-but-weakens-hard-guarantees.md)
- [Use stable agent harnesses as model-evolution boundaries](use-stable-agent-harnesses-as-model-evolution-boundaries.md)
- [Prompt coding agents around learned model habits](prompt-coding-agents-around-learned-model-habits.md)

Sources:
- [OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman](../sources/20260429_MhHEGMFCEB0.md), 01:56-03:55, 06:11-06:55
- [Future-Proof Coding Agents - Bill Chen & Brian Fioca, OpenAI](../sources/20251205_wVl6ZjELpBk.md), 02:06-04:24, 08:31-10:04
