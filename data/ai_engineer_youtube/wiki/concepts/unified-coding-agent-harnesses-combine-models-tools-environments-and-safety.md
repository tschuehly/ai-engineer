# Unified Coding-Agent Harnesses Combine Models, Tools, Environments, and Safety

Summary: A coding agent's capability comes from the model and from the harness that manages tool execution, environment setup, behavior evaluation, and safety boundaries.

Use when:
- Distinguishing raw model capability from a production coding-agent runtime.
- Designing an agent platform that must run commands, tests, code exploration, and integrations safely.

Details:
- OpenHands frames a coding agent as a loop between an LLM and the external world: the model chooses a next action such as reading a file, editing code, running a command, or inspecting a webpage, then the harness returns the result for the next turn. 03:50-04:30
- Brennan decomposes the harness into core software-engineering tools: diff or find-and-replace editing to avoid whole-file rewrites, terminal control for long-running and parallel commands, browser context via accessibility trees or Markdown rather than raw HTML, labeled screenshots for interaction, and sandboxing for autonomous execution. 04:33-07:23
- The workshop describes Codex as more than a code-writing model: it can run commands, run tests, explore codebases, and work across app, IDE, CLI, Slack, GitHub, and integrations. 01:56-03:55
- The model layer improves through GPT-5.3 Codex, Spark, GPT-5.4, and smaller variants, but Codex also depends on a unified agent harness for behavior management, tool execution, environment setup, and safety. 02:18-03:12
- Serving and UX improvements are part of the agent system: websockets and fast mode are framed as token-speed improvements that make long-running agent work feel more usable. 06:11-06:55
- A future-proofing talk defines the harness as the model-facing layer for prompts, tools, multi-turn work, code interaction, and user interpretation; maintaining it also includes compaction, parallel tool calls, sandboxing, permissions, port management, MCP support, and image handling. 02:06-04:24, 08:31-10:04
- **What changes when the harness is the user's choice rather than yours.** Every decomposition above describes a harness a vendor owns end to end. A platform hosting other people's harnesses cannot own the loop, the tools, or the safety model, and Abdalla's account is that supporting several by delegation fragments the product — "your experience with working with Claude is different from working with Codex versus a custom harness." What the platform keeps instead is narrow and specific: conversation state it can store and rehydrate, and artifacts (PRs, issues, generated files) structured identically regardless of which harness produced them. That is the minimum below-the-line set, and it implies the harness decomposition on this page is the part that stays heterogeneous. See [Support Many Harnesses by Owning Conversation State and Artifacts](support-many-harnesses-by-owning-conversation-state-and-artifacts.md). ([Abdalla](../sources/20260822_L173Z8DpaJg.md), 05:28-06:24)

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
- [Support Many Harnesses by Owning Conversation State and Artifacts](support-many-harnesses-by-owning-conversation-state-and-artifacts.md)

Sources:
- [Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands](../sources/20250725_o_hhkJtlbSs.md), 03:50-07:23
- [OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman](../sources/20260429_MhHEGMFCEB0.md), 01:56-03:55, 06:11-06:55
- [Future-Proof Coding Agents - Bill Chen & Brian Fioca, OpenAI](../sources/20251205_wVl6ZjELpBk.md), 02:06-04:24, 08:31-10:04
- [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../sources/20260822_L173Z8DpaJg.md), 05:28-06:24
