# Ship Production Software in Minutes, Not Months - Eno Reyes, Factory

Source: [Ship Production Software in Minutes, Not Months - Eno Reyes, Factory](https://www.youtube.com/watch?v=iheWKg2Tkrk)
Uploaded: 2025-07-25
Transcript: `raw/20250725_iheWKg2Tkrk/iheWKg2Tkrk.en-orig.vtt`

## Summary

Eno Reyes frames enterprise agent-native development as more than code generation: agents need centralized context, planning and design artifacts, action tools, parallel execution infrastructure, incident-response context, and enterprise controls so engineers can move from inner-loop coding toward orchestration, review, and operational learning.

## Extracted Concepts

- [Agent-Native SDLC Platforms Need Context, Reliability, and Parallelism](../concepts/agent-native-sdlc-platforms-need-context-reliability-and-parallelism.md) - this source defines agent-native development as platform-supported delegation across the software lifecycle.
- [Agent Planning Should Mine Feedback Before Producing PRDs and Tickets](../concepts/agent-planning-should-mine-feedback-before-producing-prds-and-tickets.md) - this source describes using meeting transcripts, architecture context, and customer feedback to create PRDs, roadmaps, and parallel tickets.
- [Incident Agents Turn Alerts Into RCA and Operational Memory](../concepts/incident-agents-turn-alerts-into-rca-and-operational-memory.md) - this source shows how Sentry incidents, logs, runbooks, Slack discussions, and past incidents can become RCA and mitigation plans.
- [Enterprise Coding Agents Need Ownership, Auditability, and Action Controls](../concepts/enterprise-coding-agents-need-ownership-auditability-and-action-controls.md) - this source warns that enterprise agent adoption must answer security, audit log, responsibility, and high-risk command questions.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)

## Notes

- The talk argues that the full AI unlock comes when teams delegate a majority of software-lifecycle tasks to agents through task-management interfaces, centralized engineering context, reliable agents, and infrastructure for thousands of parallel agents. (01:56-02:27)
- Vibe coding is presented as inadequate for hard enterprise problems such as legacy Java systems that support critical banking transactions; agents should amplify human engineering expertise rather than replace it. (03:03-03:42)
- A coding-agent task should ground itself in the environment, inspect codebase state, recent changes, branch context, machine capabilities, and organizational memories before returning a plan and asking clarifying questions. (03:52-04:35)
- The source frames many AI failures as missing-context failures rather than model-intelligence failures, citing meetings, whiteboards, transcripts, and cross-system organizational context as material agent inputs. (04:52-06:28)
- In the planning example, Factory combined months of user transcripts, architecture context, meeting notes, and a knowledge agent to find customer-feedback patterns and technical constraints before iterating toward a PRD. (08:27-09:24)
- The PRD-to-roadmap workflow can create Linear or Jira tickets, dependencies, and parallelizable work for multiple code agents when the platform has the relevant action tools. (09:26-09:56)
- Process artifacts such as PRDs, design docs, RCA templates, roadmaps, and meeting transcripts become a knowledge base and map for future developers and AI systems when their rationale is captured. (09:59-10:46)
- Incident-response agents can gather Sentry incidents, logs, metrics, runbooks, past incidents, and Slack discussion into RCA and mitigation plans, but the speaker explicitly avoids claiming all SRE/RCA work can be automated today. (10:57-11:55)
- RCA outputs can feed runbook generation, response workflow updates, and team-memory capture, turning incidents into a larger operational learning cycle. (12:29-13:41)
- Enterprise deployment needs questions about security, audit logs, ownership, responsibility, indemnification, and destructive command controls; the talk cautions that broad YOLO mode is not a strong enterprise default. (15:09-15:49)
