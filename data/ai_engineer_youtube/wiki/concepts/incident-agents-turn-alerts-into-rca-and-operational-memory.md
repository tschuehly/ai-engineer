# Incident Agents Turn Alerts Into RCA and Operational Memory

Summary: Incident agents can turn alerts into root-cause analysis and mitigation artifacts by gathering scattered operational context. The longer-term value comes when those RCAs update runbooks, workflows, and team memory so repeated incidents become easier to predict and prevent.

Use when:
- Designing observability-to-agent workflows for production incidents.
- Deciding how incident traces should become durable operational context.

Details:
- The talk cautions that it is not realistic to automate all SRE and RCA work today, but argues that agent-driven incident response changes the context-gathering step. (10:57-11:11)
- A Sentry incident can be combined with system logs, metrics, past incidents, Notion or Confluence runbooks, and Slack discussions to produce an RCA and mitigation plan. (11:11-11:55)
- Immediate context can condense search effort from hours to minutes and move time-to-act closer to the moment an incident triggers. (11:45-12:08)
- User- and organization-level memory helps model team response patterns and common issues, turning RCAs into new runbooks, response workflow updates, and automatically shared team knowledge. (12:10-12:46)
- The source reports that teams using this pattern can reduce incident response time and repeat incidents because repeated patterns become visible across operational history. (12:56-13:41)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Observability-to-PR agents turn incidents into reviewable fixes](observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md)
- [Analyze operational health over time slices before invoking repair agents](analyze-operational-health-over-time-slices-before-invoking-repair-agents.md)
- [Record Workflow History for Agent Debugging and Compliance](record-workflow-history-for-agent-debugging-and-compliance.md)

Sources:
- [Ship Production Software in Minutes, Not Months - Eno Reyes, Factory](../sources/20250725_iheWKg2Tkrk.md), 10:57-13:41
