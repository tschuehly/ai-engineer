# Code-backed content can replace fragile CMS workflows for agents

Summary: For agent-managed operational data, keeping structured content in code can make the agent's source of truth easier to inspect, diff, and update than a separate CMS workflow.

Use when:
- Deciding whether conference schedules, catalogs, docs, or product content should live in a CMS, spreadsheet, database, or repository.
- Giving coding agents authority over structured content while preserving reviewable provenance.

Details:
- Swyx describes the AI Engineer conference as a data-management problem spanning speakers, sponsors, attendees, and changing needs. (07:55-08:13)
- The team found an unlock by dropping the CMS and committing the schedule/content data into code, using that code as the source of truth for a coding agent to manage. (08:23-08:40)
- This let speaker-change requests be handed to Devin with minimal additional instruction, because the agent could update the same code-backed schedule that powered the site. (08:40-09:05)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Context development lifecycle treats context as an engineered artifact](context-development-lifecycle-treats-context-as-an-engineered-artifact.md)
- [Package reusable context as skills, libraries, and registries](package-reusable-context-as-skills-libraries-and-registries.md)

Sources:
- [Agents for Everything Else - swyx](../sources/20260501_zepu8Kk6FBQ.md), 07:55-09:05
