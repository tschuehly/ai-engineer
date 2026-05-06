# OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman

Source: [OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman](https://www.youtube.com/watch?v=MhHEGMFCEB0)
Uploaded: 2026-04-29
Transcript: `raw/20260429_MhHEGMFCEB0/MhHEGMFCEB0.en-orig.vtt`

## Summary

This workshop frames Codex as a full software engineering agent system rather than only a code generator: model capability is paired with an agent harness, multiple product surfaces, plugins, automations, worktrees, code review, subagents, approvals, hooks, and security-oriented integrations. The durable engineering lessons are that long-running coding agents need isolated work streams, composable context/tool bundles, scoped specialist subagents, explicit privilege boundaries, and event hooks that automate repeated session rituals without turning every action into an unchecked approval.

## Extracted Concepts

- [Unified coding-agent harnesses combine models, tools, environments, and safety](../concepts/unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md) - supports the idea that agent capability comes from both frontier models and the surrounding execution harness.
- [Isolate parallel coding work with project worktrees](../concepts/isolate-parallel-coding-work-with-project-worktrees.md) - shows native worktree support as a way to run multiple feature, bug, and Q&A threads without task interference.
- [Customize subagents by task, model, tools, and permissions](../concepts/customize-subagents-by-task-model-tools-and-permissions.md) - demonstrates specialist subagents for review, docs, security, backlog triage, and other decomposed work.
- [Use agent hooks to automate session rituals](../concepts/use-agent-hooks-to-automate-session-rituals.md) - describes start, tool-use, and stop hooks for repeatable agent lifecycle actions.
- [Route high-impact agent actions through explicit human approval gates](../concepts/route-high-impact-agent-actions-through-explicit-human-approval-gates.md) - adds Guardian approvals as a coding-agent privilege-control pattern.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Codex is presented as a software engineering agent that can run commands, run tests, explore codebases, and operate across app, IDE, CLI, Slack, GitHub, and tool integrations. 01:56-03:55
- The system description separates model progress from the unified agent harness that manages behavior, tool execution, environment setup, and safety. 02:18-03:12
- Worktrees let a project hold multiple simultaneous feature, bugfix, or Q&A threads without those tasks interfering with one another. 07:51-08:24
- Plugins bundle skills, apps, MCP servers, prompts, and related context so the model can use a coherent capability package instead of separately wiring every piece. 10:28-14:25
- Automations are positioned as scheduled or recurring Codex work, such as daily briefs from calendar context or Slack/Gmail summarization. 08:40-09:10, 18:53-21:06
- Codex code review can run through GitHub PR integration, the CLI `/review` command, or review of uncommitted local changes. 27:57-31:57
- Subagents decompose a master task into parallel independent tasks; examples include documentation reviewers, test-case creators/runners, accessibility reviewers, architects, and security reviewers. 32:39-35:24
- Custom subagents can specify model choice, reasoning effort, sandbox mode, MCP access, and skills; review and security subagents should typically be read-only, while docs-writing agents may need write access. 41:40-43:58
- Guardian approvals are described as a safer alternative to all-access "yolo mode" for privileged actions such as deleting directories, running servers, or exposing files to the internet. 49:50-51:40
- Hooks can run on session start, after tool use, and on session stop; examples include pulling the latest repo state, documenting tool use, and asking a long-running agent to perform one more validation pass before stopping. 52:54-55:32
