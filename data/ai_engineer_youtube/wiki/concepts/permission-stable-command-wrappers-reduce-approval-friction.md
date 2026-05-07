# Permission-stable command wrappers reduce approval friction

Summary: Agent harnesses that require per-command approval can reduce repeated prompts by keeping the executed command text stable and moving variable inputs into files. This improves ergonomics, but it makes the wrapper a security-sensitive boundary because the approved command can still execute different agent tasks based on file contents.

Use when:
- A shell-invoked agent helper receives different task text on each run.
- Approval systems key decisions on command shape or arguments.
- A wrapper needs to support repeated subagent calls without asking the user to approve every query.

Details:
- The Codex CLI demo writes the subagent name and user query to files, then runs the same wrapper command each time. 09:08-09:22
- Passing the agent name and query as command arguments would make the command look different on every invocation, causing repeated approval prompts. 09:22-10:03
- The wrapper also has to account for sandbox constraints: a child Codex process may need workspace write access for output files, access to copied Codex home credentials, and disabled rollout logging when parent sandboxing blocks writes outside the workspace. 03:26-04:51, 10:10-10:42
- The security tradeoff should be assessed explicitly: in a proprietary codebase, the child agent has private data access, can change state, and can communicate externally to the model API, so convenience does not remove risk. 05:00-06:15

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Layer agent permissions across model behavior, harness parsing, and sandboxing](layer-agent-permissions-across-model-behavior-harness-parsing-and-sandboxing.md)
- [Shell-wrapped subagents can retrofit harness capabilities](shell-wrapped-subagents-can-retrofit-harness-capabilities.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)

Sources:
- [Hacking Subagents Into Codex CLI - Brian John, Betterup](../sources/20251124_5eJqXtevlXg.md), 03:26-06:15, 09:08-10:42
