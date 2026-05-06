# Zero-Bug Policies Turn Bug Inflow Into Immediate Work

Summary: A zero-bug policy treats each reported bug as immediate prioritized work instead of backlog inventory. The point is not that every report is worth fixing, but that triage and fix-or-close decisions happen before defects accumulate.

Use when:
- Designing AI-assisted bug triage and repair workflows.
- Comparing delayed bug-backlog cleanup with immediate assignment and resolution.

Details:
- Linear's policy assigns a reported bug immediately, increasingly with agent help to identify the likely owner or area, and makes it the assigned engineer's highest priority. (16:39-17:04)
- The policy still allows a conscious decision not to fix a low-impact, unusually hard issue; zero-bug means no passive backlog, not mandatory repair of every report. (17:04-17:18)
- Artman argues bug inflow is roughly constant, so delaying fixes creates the same repair work later plus a worse product in the meantime; Linear initially paused new feature work for about three weeks to reach zero and now usually fixes bugs within seven days, often in hours. (17:23-19:16)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ralph loops process one ticket at a time with fresh context](ralph-loops-process-one-ticket-at-a-time-with-fresh-context.md)
- [Automation loops convert repeated review and triage into factory improvements](automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md)

Sources:
- [Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer](../sources/20260421_wjk0ulMAkbc.md), 16:39-19:42
