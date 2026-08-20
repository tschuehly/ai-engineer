# Use Subagents to Isolate Context-Heavy Subtasks

Summary: Subagents can act as separate context windows for bounded subtasks, letting the main agent preserve its working context while specialists search, reason, inspect dependencies, or prepare large mechanical edits.

Use when:
- A coding agent burns too much context on search and reading before it begins editing.
- A task needs deep reasoning or external library lookup without slowing every main-loop step.
- A large refactor needs codemod-style exploration that should not pollute the main agent context.

Details:
- Amp identifies a context exhaustion failure mode where good coding agents grep and read many files, leaving too little context for later editing. (06:00-06:24)
- Simply prompting the agent to read less can create a "doom loop" where it lacks enough context, retries the same edits, and fails to discover what it needs. (06:24-06:42)
- The proposed solution is subagents as subroutine-like calls: a subagent does context-heavy work in its own window and returns only relevant results to the main agent. (06:42-07:05)
- Amp's named examples include a finder for codebase search with a limited tool set and smaller model, an oracle for slower deep reasoning, a librarian for dependency/framework context, and a codemod-oriented agent for large refactors. (07:30-09:06)
- The pattern qualifies generic subagent guidance: role-specific model, tool, and permission choices matter, but context isolation is also a first-order reason to introduce a subagent.
- A Codex CLI retrofit shows the same context-isolation pattern can be approximated with a wrapper script that launches a child agent process and returns only the child answer to the parent session. 01:35-03:22
- Aditya Bhargava (Etsy) reaches the same conclusion from the tool-selection side: agents fail not only from context bloat but from "too many unrelated concepts in their context" and "too many tools that are unrelated," which makes it hard to pick the right tool. Grouping tools under sub-agents makes selection cleaner — the top agent just "picks the sub-agent you want to call" and each sub-agent owns a coherent tool set. In his framing a sub-agent is "just another function" you call like a tool (its own LLM call, its own tools, callable in parallel), so context isolation adds capability "without bloating context." ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 21:29-25:21)
- **What the parent can still do to a running child, which the subroutine framing hides.** Calling a subagent "just another function" implies fire-and-return; Codex instead exposes spawn, send input, wait, and shut down as four separate tools over a handle, on the grounds that async actions are "things that are happening while the agent has to continue to do work" ([Model Async Agent Work as Spawn, Send, Wait, Shut Down](model-async-agent-work-as-spawn-send-wait-shut-down.md)). The isolation argument on this page is unaffected — the child still has its own window — but the interface question is separate from it, and a one-shot call cannot express mid-run steering or cancellation of a specialist that has gone the wrong way. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 07:04-08:08)
- **Isolation alone does not bound the parent, which is why it is usually paired.** Coyle describes the identical fork — a "scan all the logs for error" task runs in a separate thread "where whatever the agent does and thinks and adds tokens to does not come back and pollute the main context," and only "that summation without all the other stuff" re-enters — and then insists on a second control, because the summaries themselves accumulate: "you want to isolate your subtask output, *and* you want to compact long sessions," with compaction fired on a measured token count ([Bound Context Twice](bound-context-twice-fork-the-subtask-then-compact-on-a-token-threshold.md)). His analogy for the fork is shared-memory concurrency — "keep the little threads independent. Keep your agents independent" — which captures the isolation but not the failure mode, since the risk here is dilution and cost rather than a data race. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 05:23-05:52, 15:40-17:08)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Customize subagents by task, model, tools, and permissions](customize-subagents-by-task-model-tools-and-permissions.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Shell-wrapped subagents can retrofit harness capabilities](shell-wrapped-subagents-can-retrofit-harness-capabilities.md)
- [Model Async Agent Work as Spawn, Send, Wait, Shut Down](model-async-agent-work-as-spawn-send-wait-shut-down.md)
- [Bound Context Twice: Fork the Subtask, Then Compact on a Token Threshold](bound-context-twice-fork-the-subtask-then-compact-on-a-token-threshold.md)

Sources:
- [Amp Code: Next Generation AI Coding - Beyang Liu, Amp Code](../sources/20251222_gvIAkmZUEZY.md), 06:00-09:06
- [Hacking Subagents Into Codex CLI - Brian John, Betterup](../sources/20251124_5eJqXtevlXg.md), 01:35-03:22
- [What if the harness mattered more than the model? - Aditya Bhargava, Etsy](../sources/20260707_2e9ANoOEn28.md), 21:29-25:21
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 07:04-08:08
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 05:23-05:52, 15:40-17:08
