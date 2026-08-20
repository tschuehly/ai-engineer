# Give Unowned Operational Work a Trigger

Summary: The operational work that reliably gets done is the work with a ceremony attached — a page has a receiver, an incident has a bridge. The long tail has neither, so it survives on someone remembering. Automating it starts by supplying the missing trigger: a schedule, an event stream, or a message.

Use when:
- Choosing the first background agent to build and looking for work that nothing currently fires for.
- Auditing what your team is accountable for but has no mechanism to initiate.
- Distinguishing "we should alert on this" from "we should look at this regularly."

Details:
- The distinction is between work with a ceremony and work without one: "on-call you've got a page that goes off. You know somebody's going to receive that. Incidents you create a bridge, you invite people in. That's great. Um, but there's just a long tail of other things that we are accountable for that doesn't have sort of a thing that's going to show up in your sort of job description of like this is what you're going to be responsible for" (09:04-09:25).
- The examples are specific and recognizable: "watching deploys that go out and make sure that they're actually getting out healthy"; "a morning report, incident digest of just like what's the state of my system today so that we're all on the same page"; "hey that P99 drift kind of came back. Is somebody looking at that or not?"; "produce the capacity report… this is maybe a company goal this quarter. Are we tracking against that?"; "the recurring health check… not waiting for a customer to come complain first" (09:25-10:08).
- The P99 case names why paging is not the answer: "this may not be paging, right? Because we're not going to alert on everything" (09:46-09:50). The work is real and the signal is below the threshold at which anyone can justify waking a human — which is exactly why it has no trigger.
- The category summary: "this work doesn't have like an obvious like, oh, this now needs to go be done. But it's work that we end up having to do" (10:08-10:16).
- Three trigger types cover the tail (11:15-12:18):
  - **Schedule** — "maybe it's a weekly event. We do an on-call handover every Thursday, and so a lot of the work that our agent does is sort of prepare what are the kind of interesting trends from the last week that the next on-caller needs to sort of understand as they pick up the rotation."
  - **Event stream** — "deployments go through a CI/CD pipeline… there's other sort of Slack-based, we get a lot of Slack messages coming through… 'Oh, if this event happens, let me sort of understand what that event is and go do some work.'"
  - **Message** — "I can just tell it, 'Hey, go do some work.' And it will go do some work."
- A schedule can be time-boxed so the job retires itself: "I made a change in part of our system. I'm worried about this third-party service that I'm kind of interacting with. Let me just kind of set an agent to kind of watch that maybe for the next week just to make sure everything is kind of stable and then that agent can sort of stop [its] job" (15:23-15:39). A standing job created for a bounded worry should carry its own end condition, or it becomes another thing nobody owns.
- The runtime assumptions that make a trigger dependable: "Always runs. It's in the cloud. So if you close your laptop, it's okay. Runs inside of a sandbox, so it has kind of a file system underneath it. This allows it to sort of self-organize a lot of its work" (12:19-12:33). A trigger tied to a workstation is not a trigger.
- The reason this tail is growing is the same volume argument made about coding agents: more change is reaching production — "AI is creating a lot more issues in production… it's not clear we have the right sort of structures in place to deal with the amount of kind of changes that are coming through" (02:37-02:49) — against a background where "70% of the time from an engineer is actually not focused just on writing code. It's actually spent on actually running the code that is actually shipped into production" (01:47-02:00).
- Caveats: the 70% figure is attributed only as "this was a survey study done," with no publisher, sample, or year. The workloads are offered as "very basic primitives" that customers have extended, but no adoption, catch-rate, or time-saved figures are given for any of them.

Related topics:
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Proactive Agent Systems Need Observation, Personalization, Timing, and Workflow Embedding](proactive-agent-systems-need-observation-personalization-timing-and-workflow-embedding.md)
- [Turn Unfiled Conversation Into Concrete Prototypes](turn-unfiled-conversation-into-concrete-prototypes.md)
- [Watch the Change Paths That Bypass Your Deployment Pipeline](watch-the-change-paths-that-bypass-your-deployment-pipeline.md)
- [Ambient Agents Need Self-Maintenance and Memory Hygiene](ambient-agents-need-self-maintenance-and-memory-hygiene.md)
- [Amend a Recurring Agent Task by Replying to Its Output](amend-a-recurring-agent-task-by-replying-to-its-output.md)

Sources:
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 01:47-02:49, 09:04-10:16, 11:15-12:33, 15:23-15:39
