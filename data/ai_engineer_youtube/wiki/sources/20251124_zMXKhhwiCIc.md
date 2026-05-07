# Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents - Alex Gavrilescu, Funstage

Source: [Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents - Alex Gavrilescu, Funstage](https://www.youtube.com/watch?v=zMXKhhwiCIc)
Uploaded: 2025-11-24
Transcript: `raw/20251124_zMXKhhwiCIc/zMXKhhwiCIc.en-orig.vtt`

## Summary

Backlog.md presents a repo-local task-management workflow for coding agents: large features are split into Markdown task files with metadata, descriptions, acceptance criteria, implementation plans, and status, then agents use MCP resources and tools or CLI commands to create, execute, and complete tasks while humans review task intent, plan direction, and final code.

## Extracted Concepts

- [Repo-local Markdown tasks give agents durable scoped work units](../concepts/repo-local-markdown-tasks-give-agents-durable-scoped-work-units.md) - this source supports using versioned Markdown task files as compact context and state for coding-agent work.
- [Expose task workflow guidance through MCP resources and tools](../concepts/expose-task-workflow-guidance-through-mcp-resources-and-tools.md) - this source shows MCP resources teaching agents the workflow and MCP tools letting them search, create, update, and complete tasks.
- [Review coding-agent work at task, plan, and code checkpoints](../concepts/review-coding-agent-work-at-task-plan-and-code-checkpoints.md) - this source identifies three review moments before trusting implementation output.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Backlog.md is framed as a way to avoid agents running in the wrong direction or exhausting context by dividing a large feature into smaller Markdown tasks. (00:00-00:23)
- Tasks are stored as Markdown files in the repository with front matter metadata such as task ID, title, labels, and other fields, followed by description and acceptance criteria. (03:14-04:22)
- The workflow uses acceptance criteria as the first review checkpoint: the human can verify whether the agent understood the requested feature before implementation begins. (04:04-04:35)
- The agent is asked to produce an implementation plan after reading the task, documentation, and existing codebase; reviewing that plan lets a senior engineer catch wrong direction before code is written. (04:38-08:12)
- Backlog.md exposes MCP resources for workflow overview, task creation, task execution, and completion guidance, plus MCP tools for searching, viewing, creating, and updating tasks. (05:40-07:29)
- The demo describes execution as implementing all acceptance criteria and moving the task to done when the definition of done is fulfilled. (08:21-08:49)
- Atomic tasks act as context engineering: they limit how much an agent implements in one run, reduce unwanted extra features, and make rollback or spec revision easier when a task goes wrong. (11:08-12:15)
- The workflow's three review checkpoints are task creation, implementation plan, and final code review; independent tasks can be run in parallel with Git worktrees when there are no dependencies. (12:15-12:48)
