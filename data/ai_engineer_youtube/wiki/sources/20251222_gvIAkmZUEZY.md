# Amp Code: Next Generation AI Coding - Beyang Liu, Amp Code

Source: [Amp Code: Next Generation AI Coding - Beyang Liu, Amp Code](https://www.youtube.com/watch?v=gvIAkmZUEZY)
Uploaded: 2025-12-22
Transcript: `raw/20251222_gvIAkmZUEZY/gvIAkmZUEZY.en-orig.vtt`

## Summary

Beyang Liu presents Amp Code as an opinionated coding-agent system shaped around a small core loop, task-tuned tools, subagents that isolate context-heavy subtasks, and review-first editor and terminal interfaces. The durable lessons are that generic MCP surfaces can confuse coding agents when their tools are not tuned to the workflow, subagents can preserve the main agent's context window, and agent-heavy coding shifts the editor from a writing surface toward a guided review surface.

## Extracted Concepts

- [Task-tuned tool sets beat generic integration surfaces for core coding loops](../concepts/task-tuned-tool-sets-beat-generic-integration-surfaces-for-core-coding-loops.md) - supports the claim that coding-agent core tools should be optimized for feedback loops rather than inherited wholesale from generic MCP servers.
- [Use subagents to isolate context-heavy subtasks](../concepts/use-subagents-to-isolate-context-heavy-subtasks.md) - explains subagents as separate context windows for search, reasoning, library lookup, and codemod work.
- [Design coding-agent editors as review surfaces](../concepts/design-coding-agent-editors-as-review-surfaces.md) - frames agent-era editor UX around reviewing diffs, streamed commands, diagnostics, and change tours.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)

## Notes

- Amp describes an agent as a loop around a model and tool calls, with the practical levers being model choice, tool descriptions, and how the model iterates with tools. (03:58-04:30)
- The talk argues that Amp focused on custom core tools because agents need refined tools that close workflow feedback loops; generic MCP server authors do not know the local agent's task, and irrelevant tools increase context confusion. (04:40-05:58)
- Tool calls themselves consume context: a coding agent can spend so much context grepping and reading files that little remains for editing, while simply telling it to read less can cause repeated under-contextualized retries. (06:00-06:42)
- Amp uses subagents as separate context windows that return only relevant results to the main agent; examples include a finder for codebase search, an oracle for deeper reasoning, a librarian for external library/framework context, and an experimental codemod agent for large refactors. (06:44-09:06)
- Amp avoids exposing model selection as the primary UX choice and instead offers agent modes such as a slower smart agent for complex asynchronous work and a faster rush agent for tight inner-loop edits. (09:11-10:38)
- The editor experience treats the editor as a reader: the agent panel drives changes, while a custom review surface supports arbitrary commit ranges, file-level diffs, editable diffs, code navigation, and a guided tour of which files to read first. (11:21-12:35)
