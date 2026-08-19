# Spec-driven development turns prompts into requirements, design, and tasks

Summary: Spec-driven development converts an initial coding prompt into a chain of reviewable artifacts before implementation: requirements, acceptance criteria, design, system properties, and task lists. The spec becomes both a point-in-time natural-language representation of the system and the workflow seed for agent execution.

Use when:
- Turning vague coding-agent requests into implementation plans that can be reviewed before code changes.
- Designing an agent workflow that needs reproducible delivery rather than one-shot prompt-to-code generation.

Details:
- The Kiro flow takes a prompt, turns it into requirements, derives a design, defines system properties, builds a task list, and then runs that task list. (05:32-05:45)
- The source frames a spec as artifacts representing system state at a point in time, a structured workflow through requirements, design, and execution, and a tool layer for reproducible delivery. (06:00-06:26)
- Requirements and acceptance criteria are represented in EARS, a structured natural-language syntax intended to make desired behavior easier to state and reuse. (03:32-03:48)
- Spec artifacts can be edited before implementation, so UI wireframes, extra data in requirements, or design changes can be resolved while the human and agent are still aligned upfront. (15:35-17:41)
- Fresh task sessions can be seeded with the spec and a single selected task, which keeps each task bounded but means context is not automatically shared across task sessions. (46:47-47:21)
- The Kiro requirements phase asks clarifying questions before generating (with a "quick plan" mode to generate all documents at once from the Q&A), the design phase carries mermaid/ASCII diagrams and can be started before requirements, and the human should stop and edit each doc with their own taste before code because "it's only as good as what you put in." (IddXPepIAS4 10:49-12:12)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use PRDs to align agents on the design concept](use-prds-to-align-agents-on-the-design-concept.md)
- [Use research-plan-implement loops for coding agents](use-research-plan-implement-loops-for-coding-agents.md)
- [Collaborative plans become executable agent context](collaborative-plans-become-executable-agent-context.md)
- [Spec-driven development is a tool-portable pattern, not a single product](spec-driven-development-is-a-tool-portable-pattern.md)
- [Reorder the generated task list to ship an MVP first](reorder-the-generated-task-list-to-ship-an-mvp-first.md)
- [Spec-Driven Development Without a Feedback Loop Is Waterfall](spec-driven-development-without-a-feedback-loop-is-waterfall.md)

Sources:
- [Spec-Driven Development: Agentic Coding at FAANG Scale and Quality - Al Harris, Amazon Kiro](../sources/20260109_HY_JyxAZsiE.md), 03:32-06:26
- [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](../sources/20260628_IddXPepIAS4.md), 10:49-12:12

