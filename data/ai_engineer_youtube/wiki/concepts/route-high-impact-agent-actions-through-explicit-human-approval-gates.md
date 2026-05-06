# Route High-Impact Agent Actions Through Explicit Human Approval Gates

Summary: Agent workflows should route sensitive or high-impact actions through explicit approval steps that the model cannot bypass.

Use when:
- Giving an agent access to email, calendar, HR, finance, or other state-changing tools.
- Designing approval flows for chat, Slack, webhooks, or subworkflows.
- Deciding when a coding agent should pause before privileged filesystem, server, or network exposure actions.

Details:
- The workshop adds human-in-the-loop control to a Gmail and Google Calendar management agent so useful automation remains observable and controllable. 01:10-01:25
- Approval routing can use the trigger's user or channel metadata for ordinary replies, but should send sensitive requests such as vacation-day actions to the relevant decision maker or channel for approve/deny handling. 01:10:41-01:11:07
- The approval step is described as a hard human-review boundary: letting the LLM decide whether approval occurred would defeat the purpose of the control. 01:13:56-01:15:00
- When the built-in approval surface does not fit, confirmation logic can be implemented as a subworkflow with an if-node branch and exposed back to the agent as a tool. 01:15:30-01:16:08
- Guardian approvals are presented as a safer alternative to all-access coding-agent operation: privileged actions such as deleting directories, running servers, or exposing files should trigger review logic instead of being granted by default. 49:50-51:40

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Grow personal-agent permissions incrementally from recurring pain](grow-personal-agent-permissions-incrementally-from-recurring-pain.md)
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)
- [Customize subagents by task, model, tools, and permissions](customize-subagents-by-task-model-tools-and-permissions.md)

Sources:
- [Human-in-the-Loop Automation with n8n - Liam McGarrigle](../sources/20260502_tDArkCqjA-c.md), 01:10-01:25, 01:10:41-01:11:07, 01:13:56-01:16:08
- [OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman](../sources/20260429_MhHEGMFCEB0.md), 49:50-51:40
