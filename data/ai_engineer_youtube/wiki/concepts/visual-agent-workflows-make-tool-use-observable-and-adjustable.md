# Visual Agent Workflows Make Tool Use Observable and Adjustable

Summary: Visual workflow builders can make agent behavior easier to inspect by representing triggers, model calls, memory, tools, approval waits, and downstream actions as explicit nodes.

Use when:
- Designing agent automations that need non-developers or operators to see what happened.
- Debugging why an agent did or did not call a tool.

Details:
- The n8n workshop frames the competitive value of an agent builder as the ability to see what an agent can do, know what it is doing, inspect what went wrong, and tweak the workflow rather than treating the agent as a black box. 02:37-03:05
- A basic n8n agent can be assembled from a chat or Slack trigger, a chat model, memory, and service nodes exposed as tools, then expanded into scheduled or Slack-based operation. 12:07-14:20, 17:26-19:41, 22:06-22:27, 01:05:06-01:07:53
- Workflow executions can enter a waiting state for review and later resume, and execution metadata can be queried or aggregated for audit logging. 01:04:14-01:04:54

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)

Sources:
- [Human-in-the-Loop Automation with n8n - Liam McGarrigle](../sources/20260502_tDArkCqjA-c.md), 02:37-03:05, 12:07-14:20, 17:26-19:41, 22:06-22:27, 01:04:14-01:04:54, 01:05:06-01:07:53
