# Product Work Graphs Coordinate Agents and Humans

Summary: Product-development systems can become coordination substrates for agents when issues, projects, feedback, related work, owners, and communication threads form a structured work graph. Agents can then act in the same context humans already use instead of relying on disconnected chat prompts.

Use when:
- Designing agent platforms around ticket trackers, project systems, or product-feedback stores.
- Deciding whether agent context should live in a collaboration tool rather than a separate assistant UI.

Details:
- Linear frames itself as an operating system for engineering and product teams, then extends that surface so agents live where human communication and work tracking already happen (00:44-01:10, 09:39-10:17).
- Product intelligence builds a relationship map from each issue to related issues and explains why they are related, then uses that graph for suggested labels, assignees, possible duplicates, and project matches (06:27-07:22).
- Customer feedback becomes part of the work graph when requests from many channels are analyzed into project splits and candidate features (07:26-08:19).
- Video bug reports can be turned into reproduction steps and issue drafts, preserving customer evidence while reducing manual translation work (09:09-09:33).
- The same issue thread can coordinate coding agents, feature-flag agents, PM agents, and support agents, making agent output reviewable in the team's normal work surface (10:29-13:49).

- **A work graph whose contents are constraints rather than tasks, with a write rule attached.** AIDAChip's "system of intent" holds "all the constraints of the system… all the decisions," plus the stakeholders bound by each, and agents are "not allow[ed] to touch it except with human in the loop approval for specific changes." Because the dependents are edges, three behaviours fall out that a ticket graph does not naturally give: a sign-off automatically notifies "the next stakeholders of what they should do," a value outside its constraint is flagged without anyone querying for it, and an approved change "echoes in the whole system" to everyone holding the old one. The distinction worth noting is that Linear's graph is a substrate for *work in flight* and this one is a substrate for *what the work must satisfy* — the second is why it is write-gated and the first is not. This is a pre-release product demo with no reported rates. ([Mohamed](../sources/20260822_0I6aoPSRzVc.md), 05:46-06:19, 08:03-10:15)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Retrieval](../topics/retrieval.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Embed agent tools in existing work surfaces](embed-agent-tools-in-existing-work-surfaces.md)
- [Show Retrieved Chunks Inside Agent Workflows](show-retrieved-chunks-inside-agent-workflows.md)
- [Agentic coding collapses coordination tax for small valuable changes](agentic-coding-collapses-coordination-tax-for-small-valuable-changes.md)
- [Keep a Living Intent Graph That Agents Read but Cannot Write](keep-a-living-intent-graph-that-agents-read-but-cannot-write.md)

Sources:
- [Building the platform for agent coordination - Tom Moor, Linear](../sources/20250728_UG9IAdmi2Dg.md), 06:27-13:49
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 05:46-06:19, 08:03-10:15
