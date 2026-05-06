# Maintain Ubiquitous Language for AI Coding

Summary: AI coding workflows benefit from a shared domain language that humans, code, and agents all use consistently. A glossary or domain model gives the agent compact terms for planning and implementation instead of forcing every conversation through verbose ad hoc translation.

Use when:
- An agent is verbose, misaligned, or using domain terms differently from the team.
- Planning a feature whose domain vocabulary should appear consistently in prompts, code, tests, and documentation.

Details:
- Pocock maps the "AI is too verbose" failure mode to a language gap like the one between developers and domain experts. (07:22-08:17)
- Domain-driven design's ubiquitous language gives developers, code, domain experts, and AI a common set of terms derived from the same domain model. (08:17-08:57)
- A practical version can be a Markdown glossary of terminology extracted from the codebase, kept open during planning and passed into the agent as shared context. (08:57-09:24)
- Shared language can make planning and model reasoning less verbose because the agent can use agreed terms instead of repeatedly restating concepts. (09:24-09:33)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use PRDs to align agents on the design concept](use-prds-to-align-agents-on-the-design-concept.md)
- [Collaborative plans become executable agent context](collaborative-plans-become-executable-agent-context.md)

Sources:
- ["Software Fundamentals Matter More Than Ever" - Matt Pocock](../sources/20260423_v4F1gFy-hqg.md), 07:22-09:33
