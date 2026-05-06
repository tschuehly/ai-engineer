# Map External Conversation Threads to Agent Task IDs

Summary: Chat and collaboration integrations should map each external thread to the agent task or conversation that owns its context. This keeps follow-up messages in Slack, email, or another channel from starting unrelated agent runs.

Use when:
- Building a Slack, Teams, email, or ticketing bot backed by a long-running agent API.
- Preserving user-visible thread continuity while the agent provider owns the deeper task state.

Details:
- The Manus Slack bot stores task metadata such as task ID, task URL, Slack channel, thread timestamp, Slack user, and current status so later events can be routed correctly (56:30-57:25).
- A thread timestamp is mapped to a Manus task; when the same Slack thread receives a follow-up message, the integration pushes that message to the existing task ID rather than creating a fresh task (57:45-58:34, 59:34-61:46).
- The pattern lets external conversations keep context in one agent task while still showing the user progress reactions, task links, and final replies inside the original Slack thread (59:34-62:11).
- The same design generalizes beyond Slack: external systems need their own correlation record when their thread, ticket, or message IDs differ from the agent provider's task IDs.

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Treat agent APIs as asynchronous task lifecycles](treat-agent-apis-as-asynchronous-task-lifecycles.md)
- [Server-side interaction state simplifies branching conversational agents](server-side-interaction-state-simplifies-branching-conversational-agents.md)
- [Use resumable streams as the UI boundary for durable agents](use-resumable-streams-as-the-ui-boundary-for-durable-agents.md)

Sources:
- [Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)](../sources/20251230_xz0-brt56L8.md), 56:30-62:11
