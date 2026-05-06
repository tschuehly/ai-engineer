# Claude Agent SDK [Full Workshop] - Thariq Shihipar, Anthropic

Source: [Claude Agent SDK [Full Workshop] - Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=TqC1qOfiVcQ)
Uploaded: 2026-01-05
Transcript: `raw/20260105_TqC1qOfiVcQ/TqC1qOfiVcQ.en-orig.vtt`

## Summary

Thariq Shihipar frames the Claude Agent SDK as a reusable harness built from Claude Code's production lessons: agents build their own context and trajectory, but reliable products still need scoped harness primitives, filesystem-based context, composable shell tools, layered permissions, hooks, and verification.

## Extracted Concepts

- [Agent harnesses combine model, tools, prompts, filesystem, skills, hooks, and memory](../concepts/agent-harnesses-combine-model-tools-prompts-filesystem-skills-hooks-and-memory.md) - this source defines the reusable runtime pieces Anthropic kept rebuilding around agents.
- [Use Bash as a composable code-mode tool for agents](../concepts/use-bash-as-a-composable-code-mode-tool-for-agents.md) - this source argues that shell access can replace many bespoke tools by letting agents use existing software, files, pipes, scripts, and checks.
- [Layer agent permissions across model behavior, harness parsing, and sandboxing](../concepts/layer-agent-permissions-across-model-behavior-harness-parsing-and-sandboxing.md) - this source describes layered guardrails for powerful Bash and filesystem-enabled agents.
- [Use hooks for deterministic agent verification and live context injection](../concepts/use-hooks-for-deterministic-agent-verification-and-live-context-injection.md) - this source positions hooks as event-driven controls that can verify state or insert changed context.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Agents are described as systems that build their own context, decide their own trajectories, and work autonomously rather than only following rigid workflows. 03:08-03:27
- The Agent SDK is built on Claude Code because Anthropic repeatedly rebuilt the same harness parts: tools, prompts, filesystem context, skills, subagents, web search, compaction, hooks, and memory. 04:01-05:52
- Context is not only prompt text; the agent's usable files, scripts, and tools are also context. 05:16-05:31
- Workflow-like automations can still need an agent harness when the middle steps require flexible repository exploration, Docker tests, and structured output. 11:29-12:34
- Bash is treated as a broad code-mode tool: it can store tool results in files, generate and call scripts, compose `tail` and `grep`, use software such as FFmpeg and LibreOffice, run package-manager checks, and verify work. 15:51-19:00
- Guardrails for Bash-enabled agents should be layered: model alignment, harness permissions and AST parsing, and sandboxing for network and filesystem operations. 12:42-14:39
- Hooks can perform deterministic verification, insert live user changes after tool calls, or give feedback such as requiring a script or requiring the agent to read data before acting. 01:47:08-01:50:20
- For very large codebases, the source cautions that semantic search can be brittle because the model is not trained on the bespoke index; practical scoping still relies on good `CLAUDE.md` files, starting in the right directory, verification steps, hooks, and links. 01:50:33-01:51:54
