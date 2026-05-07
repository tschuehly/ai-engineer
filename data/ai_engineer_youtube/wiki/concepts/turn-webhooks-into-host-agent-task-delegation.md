# Turn Webhooks Into Host-Agent Task Delegation

Summary: Event-driven business workflows can turn incoming webhooks into host-agent tasks, then delegate compact subtasks to specialist agents instead of sharing the entire event payload with every tool-using agent.

Use when:
- Building webhook-triggered LLM automations that need multiple downstream tools or agents.
- Keeping subagent context small while preserving a central decision point for sequencing.

Details:
- The workshop's target architecture triggers a multi-agent system from a webhook, then has agents work together through A2A and MCP-backed integrations. (01:47-02:35)
- The host agent should process the source event and decide which tasks to issue; it should not blindly forward the full meeting transcript or raw payload to every subagent. (54:35-55:34)
- A delegated task can be a compact instruction such as creating a GitHub issue with a repo, title, and description; the specialist agent then extracts the MCP call instructions, body, and title it needs. (55:42-56:05)
- The host should retain coordination decisions, including whether work can run in parallel or must be sequenced because one task needs another task's output, such as a GitHub URL before a Slack notification. (53:53-54:31)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Compose agents and workflows as interchangeable primitives](compose-agents-and-workflows-as-interchangeable-primitives.md)
- [Choose choreography or orchestration by complexity and autonomy](choose-choreography-or-orchestration-by-complexity-and-autonomy.md)
- [Treat agent APIs as asynchronous task lifecycles](treat-agent-apis-as-asynchronous-task-lifecycles.md)

Sources:
- [A2A & MCP Workshop: Automating Business Processes with LLMs - Damien Murphy, Bench](../sources/20250726_wXVvfFMTyzY.md), 01:47-02:35, 53:53-56:05

