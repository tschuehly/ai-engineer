# Social Context Dashboards Keep Agentic Teams Oriented

Summary: As agentic development increases the speed and volume of work, teams need summarized social context from sessions, issues, PRs, and conversations to stay aligned without reading every raw event.

Use when:
- Designing dashboards for teams running many agentic work streams.
- Deciding how agent systems should surface teammate activity and ownership context.

Details:
- ACE includes session summary blocks that show recent changes from both the user and collaborators, helping people switch between parallel sessions without losing orientation. 09:02-09:19
- The dashboard can suggest unfinished work to resume, summarize teammates' recent activity, and show a raw feed of issues and PRs with a more useful natural-language summary. 13:09-14:10
- The talk frames code-adjacent conversations as a social information fabric that agents can use to orient users, surface decisions, and pull relevant owners into conversations. 14:13-14:47
- This pattern turns disconnected terminal instances into a shared environment where people and agents retain common workspace context. 14:47-15:00
- **Stated later as a requirement separable from multiplayer itself.** "It's not just enough to have real-time multiplayer, I also want to be ambiently aware of what everybody's going on about" — a per-teammate view of who is working on what, shown alongside the sessions. Filing the two as one feature hides a design choice: a shared session tells you about the work you joined, and an awareness surface tells you about the work you did not. The talk also names the unsolved half of the same surface: "how do automations surface themselves in this? If I want to talk with my automation… when an agent wants to tap me on the shoulder and ask me a question." Once scheduled jobs are producing work in the background, they compete for the same awareness channel as colleagues, and no design for that is offered. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 18:37-19:21)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use social and expert graphs to personalize coding-agent context](use-social-and-expert-graphs-to-personalize-coding-agent-context.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Bound What an Unattended Automation May Emit, Including Emitting Nothing](bound-what-an-unattended-automation-may-emit.md)

Sources:
- [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment - Maggie Appleton, GitHub](../sources/20260426_ClWD8OEYgp8.md), 09:02-09:19, 13:09-15:00
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 18:37-19:21
