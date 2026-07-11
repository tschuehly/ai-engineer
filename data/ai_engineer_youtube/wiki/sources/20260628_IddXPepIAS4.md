# Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS

Source: [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](https://www.youtube.com/watch?v=IddXPepIAS4)
Uploaded: 2026-06-28
Transcript: `raw/20260628_IddXPepIAS4/IddXPepIAS4.en-orig.vtt`

## Summary

Erik Hanchett (Senior Developer Advocate, AWS) gives an introductory case for spec-driven development: write requirements, design, and task markdown before any code, because coding assistants behave like over-eager "AI interns" that go off the rails without guidance and because more structured context steers them better than a bare prompt. He frames spec-driven development as a tool-portable *pattern* — runnable manually with any assistant, via GitHub's open-source Spec Kit, or via a purpose-built tool like Kiro (AWS's spec-mode IDE and plan-mode CLI, GA'd in late 2025) — whose durable value is the reviewable artifact chain plus the human staying in the loop as the accountable code reviewer. He adds concrete operational tips: keep the AGENTS.md/steering context in a "Goldilocks zone," use skills alongside the flow, ask the agent to reorder the generated task list into a top-four MVP so you can see something working first, generate property-based tests (fast-check) against the requirements/design, and pull ticket/requirement context from Jira/Asana via MCP into the spec generation step. The flow works for greenfield and legacy projects and for in-depth features, while trivial changes can still be vibe-coded.

## Extracted Concepts

- [Spec-driven development is a tool-portable pattern, not a single product](../concepts/spec-driven-development-is-a-tool-portable-pattern.md) - Hanchett explicitly lays out running the same requirements→design→tasks pattern manually, via Spec Kit, or via Kiro.
- [Reorder the generated task list to ship an MVP first](../concepts/reorder-the-generated-task-list-to-ship-an-mvp-first.md) - his quick tip to pull the top four tasks into an MVP so you can see it working before full implementation.
- [Spec-driven development turns prompts into requirements, design, and tasks](../concepts/spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md) - corroborates the requirements/design/tasks artifact chain, EARS format, and clarifying-question front-end.
- [Translate structured requirements into property-based tests](../concepts/translate-structured-requirements-into-property-based-tests.md) - corroborates generating fast-check property tests against the requirements and design documents.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

## Notes

- Definition: spec-driven development means structured specifications — markdown requirements and a design document — are created before any code is written, which works well with LLM coding assistants. (00:30-01:02)
- Rationale: treat coding assistants as "AI interns" that need to be pushed the right way; given a little leeway "they will go off the rails," and specs guide them. Frontier models keep improving but are "still not perfect," so more context steers them, especially as software/requirements/paradigms change. (01:14-03:42)
- Some harnesses now add a thinking/planning mode before writing code, but "there's nothing better than actually having those documents created and having you be in the middle" before code generation. (03:22-03:46)
- Context discipline: an AGENTS.md/CLAUDE.md (Kiro calls these "steering docs") should hit a "Goldilocks zone" — enough rules and guidelines, not too much or too little. (04:06-04:46)
- Skills (on-demand instruction files triggered by keywords or `/skill`) can be used in parallel with the spec flow, e.g. during design or implementation. (04:49-05:23)
- Human-in-the-loop: everything in the flow is the human's responsibility — you are the code reviewer of all generated code and must interactively review the design and requirements docs, "because if something goes wrong, you are the person that are going to be blamed for it, not the agent." Team code reviews and AI review tools still apply on top. (05:26-06:22)
- Origin of Kiro: AWS saw customers hand-rolling a "bespoke pattern" of agent-generated requirements + design documents, and productized it. Kiro GA'd late 2025 as an AI IDE plus a CLI (the speaker notes people are shifting toward CLIs over IDEs); its differentiator is vibe mode vs spec mode. It went viral (tens of thousands of downloads, a preview gate people routed around) and is now public at kiro.dev. (06:25-08:24)
- Tool-portable pattern: you can run spec-driven development without Kiro — manually with any assistant (ask for user requirements, review, then design, review, then implementation/task list), via GitHub's open-source Spec Kit ("Spec It"), or in Kiro's IDE spec mode / CLI plan mode. (08:28-09:49)
- Greenfield vs legacy: the pattern is not just for greenfield; existing years-old apps carry "dozens and dozens" of spec files. Best for in-depth features needing upfront planning and complex projects; there is even a spec mode for bug fixes, though trivial changes may be better vibe-coded. (10:02-10:46)
- Requirements phase uses EARS format with an introduction, requirements, and user stories, and asks clarifying questions before generating; a new "quick plan" mode can generate all documents at once from the Q&A. (10:49-11:24)
- Design phase is a higher-level document with mermaid diagrams / ASCII art; you can start from design or requirements, or combine them. Stop and edit it with your own knowledge, taste, and expertise — "it's only as good as what you put in" — and review markdown for inconsistencies, hallucinations, and errors. (11:26-12:12)
- Implementation phase is a task list, optionally with property-based tests written against the requirements and design documents to confirm tasks are implemented correctly. (12:13-12:34)
- MVP tip: after the task list is generated, tell it "please take the top four tasks, put them at the top, and create an MVP for me first" so you can see it working; in the demo Kiro reordered tasks and reframed requirements so tasks 1-4 delivered a working browsable movie grid with search, genre filtering, sorting, and theme. (12:35-12:52, 16:29-17:00)
- MCP integration: pull tickets and requirement docs from Jira/Asana or any project-management service into the spec-generation step (e.g. a PM's requirements doc), directed either via a steering/AGENTS.md rule or specified in the first prompt. MCP is "still maturing" with a long road (especially security), not dead. (12:55-14:41)
- Demo used fast-check in the TypeScript/Node world for property tests that run "dozens if not hundreds of times with different values"; example property: for any movie dataset, the extracted genre list must contain exactly a sorted set of unique genres. (15:44-16:04, 17:17-17:27)
