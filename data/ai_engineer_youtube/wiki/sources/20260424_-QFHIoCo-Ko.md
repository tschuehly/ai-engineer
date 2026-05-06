# Full Walkthrough: Workflow for AI Coding - Matt Pocock

Source: [Full Walkthrough: Workflow for AI Coding - Matt Pocock](https://www.youtube.com/watch?v=-QFHIoCo-Ko)
Uploaded: 2026-04-24
Transcript: `raw/20260424_-QFHIoCo-Ko/-QFHIoCo-Ko.en-orig.vtt`

## Summary

Matt Pocock presents an AI coding workflow that turns ambiguous requirements into shared planning artifacts, slices work into testable implementation units, and then moves from sequential agent work into sandboxed parallel issue execution. The durable lesson is that classic software engineering practices still matter: clarify the design concept, keep permanent context small, use PRDs as alignment tools rather than stale source truth, design module interfaces and tests before delegating implementation, and review or merge parallel agent outputs through explicit loops.

## Extracted Concepts

- [Use PRDs to align agents on the design concept](../concepts/use-prds-to-align-agents-on-the-design-concept.md) - this source frames PRDs as destination documents that summarize shared understanding before implementation.
- [Retire completed planning docs before they become agent doc rot](../concepts/retire-completed-planning-docs-before-they-become-agent-doc-rot.md) - this source warns that old PRDs can mislead later agents when code, file structure, names, or requirements change.
- [Delegate implementations behind reviewed module interfaces](../concepts/delegate-implementations-behind-reviewed-module-interfaces.md) - this source recommends humans retain codebase shape and behavioral contracts while agents fill in module internals.
- [Run parallel issue agents in sandboxes with review and merge loops](../concepts/run-parallel-issue-agents-in-sandboxes-with-review-and-merge-loops.md) - this source describes a planner, per-issue sandbox implementers, commit review, and a merge agent.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

## Notes

- Software engineering fundamentals remain useful with AI coding: the workshop argues that practices used to coordinate humans also help coordinate agents. (01:12-01:25)
- A coding-agent session tends to move through system prompt, exploration, implementation, and testing; large always-loaded system context can push the model into less useful behavior before it starts working. (07:52-08:17)
- The speaker prefers more structure than a pure Ralph loop: specify the destination with a PRD, then ask the agent for small changes that move toward it. (06:56-07:16)
- Subagents can explore in isolated context windows, spend many tokens on discovery, and report only the important summary back to the parent agent. (17:37-18:33)
- The PRD is treated as a destination document summarizing the current design concept; useful fields include problem statements, solution, user stories, implementation decisions, and testing decisions. (30:24-32:28)
- The workflow is not pure "specs to code": after forming the idea, the agent and human inspect the codebase and propose modules to modify so implementation stays grounded in the current system. (32:46-33:31)
- Delegating more code can make engineers lose codebase understanding; the mitigation is to preserve ownership of big shapes, module interfaces, and behavior while delegating implementation details. (19:43-21:07)
- End-to-end module tests can make difficult systems more tractable for agents; in the example, wrapping a browser video editor flow in a testable module improved the agent's ability to make changes. (22:16-23:02)
- Completed PRDs can become doc rot when names, file structure, requirements, and user learnings change; the speaker prefers closing or removing stale planning artifacts instead of keeping them as current context. (24:19-25:05)
- Parallel agent execution can use a planner over the backlog, dependency phases, per-issue sandboxes and branches, implementers, commit review, and a merge agent that resolves type and test failures. (30:58-32:15)
