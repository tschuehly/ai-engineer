# Split Large Automation Surfaces Into Specialized Subagents and Subworkflows

Summary: As an automation agent gains more tools, split specialized capabilities into subagents or subworkflows so the top-level agent can route work without carrying every implementation detail directly.

Use when:
- Expanding a personal or business automation beyond one service domain.
- A single agent is accumulating too many unrelated tools.

Details:
- The n8n workshop suggests turning the email and calendar bot into a specialized subagent when adding many more tools, with the top-level agent calling specialized agents for domains such as calendar/email or GitHub issues. 01:17:43-01:18:14
- Subworkflows can also encapsulate operational logic such as confirmation handling and return simple values, such as approved or denied, to the calling tool. 01:15:30-01:16:08

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)

Sources:
- [Human-in-the-Loop Automation with n8n - Liam McGarrigle](../sources/20260502_tDArkCqjA-c.md), 01:15:30-01:18:14
