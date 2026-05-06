# Use PRDs to Align Agents on the Design Concept

Summary: A PRD can be an agent-alignment artifact: it captures the shared destination, product intent, implementation decisions, and testing decisions before code generation starts. Its value is less the final document shape and more the process of turning vague requirements into a shared design concept.

Use when:
- Converting ambiguous feature requests into agent-ready implementation context.
- Deciding what a planning artifact should contain before a coding agent starts work.

Details:
- The source frames the PRD as a "destination document" that summarizes the design concept reached through exploration and user questioning, not as a substitute for reading the codebase. (30:24-31:09)
- Useful PRD content includes problem statements, the user's problem, the proposed solution, user stories, implementation decisions, and testing decisions. (31:49-32:28)
- The workflow can start with a "grilling" or interview stage, then produce the PRD after the agent and human have clarified open product and technical questions. (31:34-31:55)
- Optimizing the PRD indefinitely has diminishing returns; the stronger use is getting alignment with the AI early, then spending more effort on QA. (01:26:35-01:27:39)
- A follow-up source sharpens this into a failure mode: if the human and AI do not share the design concept, the agent may satisfy the written artifact while building something different from the user's intent. (04:42-05:50)
- The "Grill Me" pattern asks the agent to interview the human through dependent design decisions before creating the PRD or issue set, countering plan modes that rush to produce an asset. (05:50-07:18)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Collaborative plans become executable agent context](collaborative-plans-become-executable-agent-context.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Maintain ubiquitous language for AI coding](maintain-ubiquitous-language-for-ai-coding.md)

Sources:
- [Full Walkthrough: Workflow for AI Coding - Matt Pocock](../sources/20260424_-QFHIoCo-Ko.md), 30:24-32:28
- ["Software Fundamentals Matter More Than Ever" - Matt Pocock](../sources/20260423_v4F1gFy-hqg.md), 04:42-07:18
