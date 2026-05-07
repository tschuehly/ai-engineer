# Hacking Subagents Into Codex CLI - Brian John, Betterup

Source: [Hacking Subagents Into Codex CLI - Brian John, Betterup](https://www.youtube.com/watch?v=5eJqXtevlXg)
Uploaded: 2025-11-24
Transcript: `raw/20251124_5eJqXtevlXg/5eJqXtevlXg.en-orig.vtt`

## Summary

Brian John shows a lightweight way to retrofit subagent behavior into Codex CLI by letting a parent Codex session call a wrapper script, which launches a child `codex exec` run, captures its answer through a file, and returns only the compact result to the parent. The talk is most useful as a harness-design pattern: subagents can preserve the parent context window, but practical wrapper implementations must handle sandbox permissions, credential access, approval friction, timeouts, and the security risk of a code-writing agent that can see proprietary code and communicate externally.

## Extracted Concepts

- [Shell-wrapped subagents can retrofit harness capabilities](../concepts/shell-wrapped-subagents-can-retrofit-harness-capabilities.md) - this source gives a concrete Codex CLI pattern for implementing subagents through ordinary scripts and child agent processes.
- [Permission-stable command wrappers reduce approval friction](../concepts/permission-stable-command-wrappers-reduce-approval-friction.md) - this source explains why writing inputs to files can keep an approved command shape stable across subagent invocations.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

## Notes

- Subagents are framed as context-management tools: the parent gives a task to a child agent, the child spends its own tokens, and only the answer comes back to the parent context. 01:35-01:56
- The prototype design uses a parent Codex session, a wrapper script that selects the agent and builds the prompt, a child `codex exec` process, an output file, and stdout back to the parent session. 02:40-03:22
- Running nested Codex under ordinary sandbox permissions was difficult; the child needed workspace write access for its output file and a way to reach Codex credentials outside the workspace. 03:26-04:51
- The security note maps the pattern against agent risks: proprietary code makes private data relevant, and the child can both change local state and communicate with the OpenAI API, so "lower risk" is not "no risk." 05:00-06:15
- Agent definitions in the demo include a name, reasoning effort, and prompt, while `AGENTS.md` tells Codex when to invoke subagents and which ones are available. 06:18-08:04
- The wrapper writes the agent name and user query to files rather than passing them as command arguments, so the shell command looks the same each time and can be approved once. 09:08-10:03
- The demo notes a tradeoff versus native asynchronous subagents: the wrapper runs serially in Codex CLI, and larger codebase tasks may require long timeouts. 11:26-12:54
