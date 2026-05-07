# Agent Planning Should Mine Feedback Before Producing PRDs and Tickets

Summary: Agent planning is strongest when agents first mine customer feedback, meetings, architecture context, and assumptions before drafting a PRD or issue plan. The output can then become a roadmap of dependent tickets that multiple coding agents can execute in parallel.

Use when:
- Turning ambiguous product direction into agent-ready implementation work.
- Deciding what context should feed PRD generation, roadmap creation, and ticket decomposition.

Details:
- The planning workflow delegates groundwork and research to agents, then uses a collaborative surface for human-agent exploration rather than asking for a design doc in one shot. (07:16-07:38)
- Factory's example combined months of customer transcripts, architecture context, and meeting notes, then asked a knowledge agent to find patterns in feedback, map them to assumptions, and highlight technical constraints. (08:27-09:14)
- Intermediate research documents become the basis for iterating on a final PRD, not the final answer by themselves. (09:14-09:24)
- With access to Linear or Jira, the PRD can become epics, tickets, dependency relationships, and work parallelizable across multiple coding agents. (09:26-09:48)
- Process artifacts such as PRDs, design docs, RCA templates, roadmaps, and meeting transcripts become a knowledge base for future agents when they preserve the why behind decisions. (09:59-10:46)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use PRDs to Align Agents on the Design Concept](use-prds-to-align-agents-on-the-design-concept.md)
- [Collaborative plans become executable agent context](collaborative-plans-become-executable-agent-context.md)
- [Plan coding-agent work through feature inventories and dependency graphs](plan-coding-agent-work-through-feature-inventories-and-dependency-graphs.md)

Sources:
- [Ship Production Software in Minutes, Not Months - Eno Reyes, Factory](../sources/20250725_iheWKg2Tkrk.md), 07:16-10:46
