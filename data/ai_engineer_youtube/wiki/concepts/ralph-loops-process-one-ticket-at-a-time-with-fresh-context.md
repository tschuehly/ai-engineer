# Ralph loops process one ticket at a time with fresh context

Summary: A Ralph loop is a deliberately simple coding-agent workflow that repeats one small unit of work at a time. It is useful when tickets are accessible to the agent, completion criteria are concrete, and each run can validate and hand off its result before the next run starts.

Use when:
- You want a coding agent to work through a queue without designing a complex multi-agent orchestration graph.
- You need a repeatable pattern for small code changes, ticket status updates, tests, and commits.

Details:
- The minimal loop is: choose or specify one ticket, implement it, run the relevant checks, mark the ticket complete, and repeat for the next ticket. 09:20-10:28, 28:34-30:26
- Tickets can live in flat files under `doc/tickets`, Beads, Linear, Jira, or another system, as long as the agent can read the work queue and update status. 49:22-49:53
- A useful loop prompt can constrain the agent to act as one engineer in a relay team, do exactly one change, then drop context and stop so the next iteration starts cleanly. 50:03-50:20
- Large upfront dependency graphs and many parallel agents can fail when agents cannot reliably know what is done, what is blocked, and where work items contend with each other. 23:20-25:18

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)

Sources:
- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md), 09:20-10:28, 23:20-25:18, 28:34-30:26, 49:22-50:20
