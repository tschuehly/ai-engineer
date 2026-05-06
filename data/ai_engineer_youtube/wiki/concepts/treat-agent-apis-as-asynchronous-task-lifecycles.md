# Treat Agent APIs as Asynchronous Task Lifecycles

Summary: Agent APIs should expose long-running work as task lifecycles rather than one-shot chat completions. Applications need stable task identifiers, status transitions, result retrieval, continuation, and error handling around the agent's execution.

Use when:
- Designing an API wrapper around an autonomous agent that may browse, execute code, ask follow-up questions, or take longer than one request.
- Integrating an agent into Slack, email, dashboards, or workflow tools where the caller needs progress and final-result delivery.

Details:
- Manus task creation returns a task ID, task title, and task URL; the task ID is the durable handle for retrieving state, sending feedback, and keeping later messages attached to the same execution context (17:15-17:50).
- The workshop describes a status lifecycle with `running`, `pending`, `completed`, and `error`, which lets the host application decide whether to wait, poll again, surface a question, show the result, or handle failure (22:00-22:20).
- Polling is presented as the simplest starting pattern for prototypes, while webhooks are introduced for pushing final results back into an integration without continuously polling (21:57-22:10, 61:53-62:11).
- A useful agent task response includes operational metadata such as credits used, returned messages, and agent responses, not only final text (20:58-21:12).

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use durable execution for production agent loops](use-durable-execution-for-production-agent-loops.md)
- [Treat long waits as logical workflow state](treat-long-waits-as-logical-workflow-state.md)
- [Server-side interaction state simplifies branching conversational agents](server-side-interaction-state-simplifies-branching-conversational-agents.md)

Sources:
- [Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)](../sources/20251230_xz0-brt56L8.md), 17:15-22:39
