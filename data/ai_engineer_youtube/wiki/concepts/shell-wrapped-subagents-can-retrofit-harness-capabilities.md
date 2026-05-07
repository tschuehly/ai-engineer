# Shell-wrapped subagents can retrofit harness capabilities

Summary: A coding-agent harness can add subagent-like behavior by exposing a stable shell command that launches another agent process and returns a compact result. This is a pragmatic way to reuse an existing CLI as a child agent when native subagents are unavailable, but it inherits the CLI's sandbox, credential, and execution-model constraints.

Use when:
- A CLI-based coding agent lacks native subagents but can run shell commands.
- The main agent needs context-isolated research, inspection, or small implementation tasks.
- A team wants to prototype subagent workflows without replacing the core agent harness.

Details:
- The demonstrated Codex CLI design uses a parent session, wrapper script, child `codex exec` process, child output file, and stdout handoff back to the parent. 02:40-03:22
- The child process acts as another instance of the main agent, so it can spend its own context budget and return only the answer that matters to the parent. 01:35-01:56, 02:40-02:49
- A lightweight agent catalog can define each subagent's name, reasoning effort, and prompt; `AGENTS.md` then tells the parent when to run subagents and what roles are available. 06:18-08:04
- This retrofit is not equivalent to native asynchronous subagents: the demo runs subagent calls serially, so long codebase inspections may need explicit timeouts and are slower than a parallel agent runtime. 11:26-12:54

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use subagents to isolate context-heavy subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Customize subagents by task, model, tools, and permissions](customize-subagents-by-task-model-tools-and-permissions.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)
- [Permission-stable command wrappers reduce approval friction](permission-stable-command-wrappers-reduce-approval-friction.md)

Sources:
- [Hacking Subagents Into Codex CLI - Brian John, Betterup](../sources/20251124_5eJqXtevlXg.md), 01:35-03:22, 06:18-08:04, 11:26-12:54
