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
- **The specify-plan-task-implement loop is one step of an organization's lifecycle, not the lifecycle.** "I think this is how most of our coding agents actually are kind of shaped today. In reality that is not how it is composed, and at scale when you look at the organization complexity, this is just one step in the journey. This is like building a product increment." ([Touil](../sources/20260828_M05vON8i0aI.md), 02:32-03:20) The surrounding steps Touil enumerates — product strategy, discovery, data preparation and data-product delivery, platform engineering ops, launch, performance optimization and incident resolution — are where spec-driven tooling currently has no counterpart, and he adds that organizations run many such lifecycles rather than one: "it is not like a one workflow that can actually build anything you want for your organization" (04:43-05:09), with the whole diagram covering "probably 10, 20% of what it is." A framing argument, not a measurement.

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
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)

Sources:
- [Spec-Driven Development: Agentic Coding at FAANG Scale and Quality - Al Harris, Amazon Kiro](../sources/20260109_HY_JyxAZsiE.md), 03:32-06:26
- [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](../sources/20260628_IddXPepIAS4.md), 10:49-12:12
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 02:32-05:37

