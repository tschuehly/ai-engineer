# Wire Issue-Filing Authority Before Giving Agents a Tracker

Summary: Wiring an issue tracker into the repo so agents can close the loop also gives every agent write access to the team's work queue. Without an explicit answer to which agents may file, under what conditions, and against what, the backlog fills faster than anyone can read it — one team reached hundreds of open issues in a couple of weeks.

Use when:
- Connecting agents to GitHub Issues, a board, or any queue humans are expected to triage.
- Adding a second or third agent that can report findings.
- Diagnosing a backlog that grew past the point of usefulness after agents were introduced.

Details:
- The reported failure: "There are too many issues. Like when we started… we blew up to like 4 or 500 issues… within like a couple of weeks, which is a crazy number for like a repo. And then… there are so many like different agents all trying to create issues cuz they've not been wired correctly." ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 11:54-12:11)
- The cause he names is wiring, not model behavior. Each agent was individually behaving reasonably — noticing something and filing it — and the aggregate was unusable. Write access to a shared queue is a permission that has to be scoped per agent, the same way filesystem or network access is.
- It arrived as a side effect of a good idea. Closing the loop is one of the talk's four principles: "you need to have a pipeline and a way to close the loop to remove the slop, to detect it, and to be able to like self-heal the system," implemented as "we wired issues and boards into the repo. Like we added CICD. We added [agentic] reviews. We have like a code gardener." The tracker is the shared surface all of those write to, which makes it the first thing to saturate. (08:03-08:19, 10:32-10:53)
- What a wiring decision has to specify, from the shape of the failure: which agents may file at all; whether a finding must survive a dedup or severity check first; whether the agent may file against code it did not touch; and what closes an issue nobody triaged. None of this is described in the talk — the failure is reported, the fix is not.
- The failure is structurally the same one recorded in [Clusters Are Not Issues](clusters-are-not-issues.md) from the production-monitoring side: a mechanism that can generate candidate problems is not an issue tracker, because an issue tracker's value comes from every entry being worth a human's attention. Agent-filed issues and machine-derived clusters both violate that by construction, and both need a filter between generation and the queue.
- It also sharpens a related caveat the wiki already holds. [AI-Generated Security Reports Need Maintainer Triage](ai-generated-security-reports-need-maintainer-triage.md) covers unsolicited reports arriving from outside; this is the internal version, where the team wired the firehose to itself and the triage cost lands on the same people who were supposed to be freed up.
- Caveat on the count: the captions render "4 or 500 issues" (400–500) while the channel-authored video description says "roughly 4,500 open issues in a couple of weeks." The order of magnitude is unresolved; the failure mode does not depend on which reading is right. No other figure — issues per agent, triage rate, how many were valid — appears anywhere.

Related topics:
- [Workflows](../topics/workflows.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Clusters Are Not Issues](clusters-are-not-issues.md)
- [AI-Generated Security Reports Need Maintainer Triage](ai-generated-security-reports-need-maintainer-triage.md)
- [Run Parallel Issue Agents in Sandboxes With Review and Merge Loops](run-parallel-issue-agents-in-sandboxes-with-review-and-merge-loops.md)
- [Repo-local Markdown tasks give agents durable scoped work units](repo-local-markdown-tasks-give-agents-durable-scoped-work-units.md)
- [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md)
- [Automation Loops Convert Repeated Review and Triage Into Factory Improvements](automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md)

Sources:
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 08:03-08:19, 10:32-10:53, 11:54-12:11
