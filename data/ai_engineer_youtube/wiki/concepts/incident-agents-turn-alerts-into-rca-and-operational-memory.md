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

- **What the tool set and environment look like when built as a hosted agent.** Anthropic demos an "SRE Investigator" over a dashboard showing P99 latency "10x over baseline," and the shape is worth noting because it is unglamorous: the tools are bash, grep, and glob over uploaded logs, plus an MCP tool set for deploys and metrics. The investigation runs grep → metrics → deploy list → onset time → the code diff → root cause, which is the context-gathering step above done with ordinary file tools rather than a specialized retrieval layer. The environment carries the safety property: an "SRE sandbox" "with the networking limited and allowed hosts only being the MCP server," which "effectively stops Claude from doing things that you didn't intend." Note this is explicitly "a semi-interactive demo" — staged incident, staged logs — so it evidences the wiring, not diagnostic ability. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 17:14-21:36)
- **The operational-memory half has a proposed mechanism now.** The same talk describes an organization-scale memory holding "the team's runbooks and details," updated by a periodic batch pass over session transcripts — which is the "RCAs become runbooks" claim on this page given an implementation shape. It is announced rather than evaluated; see [rewrite agent memory in a periodic batch pass over session logs](rewrite-agent-memory-in-a-periodic-batch-pass-over-session-logs.md) for the hazards, particularly that nothing in the source says who may edit shared memory or what happens when the rewrite is wrong. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 27:28-28:44)

- **The work this page covers is the part that has a ceremony; a vendor in the same space argues the larger cost is the part that does not.** Resolve AI ships the pattern on this page — an on-call agent where "for every alert that comes in, we can do a triage of that alert. We can do kind of a full root cause investigation," plus incident agents for when "a single page" becomes "a much larger incident across many different teams" — and then spends the talk on background agents instead, because "on-call you've got a page that goes off. You know somebody's going to receive that. Incidents you create a bridge, you invite people in. That's great. Um, but there's just a long tail of other things that we are accountable for" with no trigger at all. Alert-driven RCA is the well-served case; see [Give Unowned Operational Work a Trigger](give-unowned-operational-work-a-trigger.md). ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 04:53-05:54, 09:04-09:25)
- **The operational-memory half is named as the hard part by a fourth source, still without a mechanism.** Smith grants that "models have gotten incredibly capable" and locates the difficulty in the knowledge layer: "truly understanding your environment and the way that your services interact and where the hotspots are, keeping track of all of that sort of understanding is incredibly difficult," and it has to "grow as your system evolves." The system is asserted — reflection after each task, transfer across tasks, "this sort of shared knowledge system works across all the different tasks" — with no storage model, retrieval, staleness policy, or evaluation, and nothing in that talk is measured. ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 06:36-07:32, 12:34-12:58)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Observability-to-PR agents turn incidents into reviewable fixes](observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md)
- [Analyze operational health over time slices before invoking repair agents](analyze-operational-health-over-time-slices-before-invoking-repair-agents.md)
- [Record Workflow History for Agent Debugging and Compliance](record-workflow-history-for-agent-debugging-and-compliance.md)
- [Rewrite Agent Memory in a Periodic Batch Pass Over Session Logs](rewrite-agent-memory-in-a-periodic-batch-pass-over-session-logs.md)
- [Model a Managed Agent as Agent, Environment, and Session](model-a-managed-agent-as-agent-environment-session.md)
- [Give Unowned Operational Work a Trigger](give-unowned-operational-work-a-trigger.md)
- [Separate Execution From the Production Context That Judges It](separate-execution-from-the-production-context-that-judges-it.md)

Sources:
- [Ship Production Software in Minutes, Not Months - Eno Reyes, Factory](../sources/20250725_iheWKg2Tkrk.md), 10:57-13:41
- [Security Firewall for Agents — Ryan Dahl, Deno](../sources/20260817_MkRYPFIMCSA.md), 00:36-03:58
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 17:14-21:36, 27:28-28:44
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 04:53-05:54, 06:36-07:32, 09:04-09:25, 12:34-12:58
