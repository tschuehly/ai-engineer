# Purpose-Built Agent Workspaces Make Orchestration Visible

Summary: Personal-agent workspaces should expose orchestration state directly: topics, conversations, tool calls, scheduled messages, active agent identity, model choice, capabilities, and stop controls. Generic chat apps hide too much of this state and force users into workaround structures.

Use when:
- Designing a UI for multi-agent personal assistants or task-first workspaces.
- Evaluating whether Discord, Telegram, Slack, or a terminal is the right shell for an agent workflow.

Details:
- The source contrasts generic messaging surfaces with a UI designed for multi-agent orchestration across multiple topics and conversations (14:14-15:31).
- Visible tool calls matter: the speaker wants collapsible tool-call rows, loading states, and stop controls instead of slash-command-only control or invisible execution (16:20-16:31).
- Scheduled agent messages should be labeled and should read the relevant conversation so the user can tell where the message came from and why the agent is acting (16:31-16:41).
- Agent management should be present in the workflow: when chatting in a topic, the user should see which agent is active, which model and capabilities it has, and be able to remove unneeded capabilities (16:41-16:58).

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)
- [Single-chat personal agents collapse mixed life domains](single-chat-personal-agents-collapse-mixed-life-domains.md)

Sources:
- [The End of Apps - Kitze, Sizzy.co](../sources/20260423_4fntwuOoedA.md), 14:14-16:58
