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
- **A later source reports the write-access version working.** Deno gives its incident agents (OpenClaw is named, "but other agents as well") read *and write* access to production Postgres, Kubernetes, ClickHouse, AWS, GitHub, and Slack against a real PagerDuty rotation, and the read half is justified in exactly the context-gathering terms above: "the agents can actually get all of the context. They can see traces in ClickHouse. They can look in the production Postgres database at what projects a user owns. They can look through Slack for communications, GitHub logs, etc." The reported outcome moves past RCA drafting — "the agents are actually able to solve quite a lot of incidences where we previously would have a human [SRE] in the loop." ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 00:36-02:16)
- **The precondition that comes with it.** Write access is what makes the agent able to close an incident and what makes a prompt injection consequential, and Deno's agents are reachable from outside because they are "connected to the support system." Dahl's stance is that the agent is untrusted software, so the control belongs outside it — see [enforcing egress policy at the wire protocol](enforce-agent-egress-policy-below-the-http-layer.md). Treat the deployment evidence and the security requirement as a package; the first is not reportable without the second. ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 02:16-03:58)

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
- [Security Firewall for Agents — Ryan Dahl, Deno](../sources/20260817_MkRYPFIMCSA.md), 00:36-03:58
