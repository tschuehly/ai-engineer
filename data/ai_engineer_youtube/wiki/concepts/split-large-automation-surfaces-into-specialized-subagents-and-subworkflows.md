# Split Large Automation Surfaces Into Specialized Subagents and Subworkflows

Summary: As an automation agent gains more tools, split specialized capabilities into subagents or subworkflows so the top-level agent can route work without carrying every implementation detail directly.

Use when:
- Expanding a personal or business automation beyond one service domain.
- A single agent is accumulating too many unrelated tools.

Details:
- The n8n workshop suggests turning the email and calendar bot into a specialized subagent when adding many more tools, with the top-level agent calling specialized agents for domains such as calendar/email or GitHub issues. 01:17:43-01:18:14
- Subworkflows can also encapsulate operational logic such as confirmation handling and return simple values, such as approved or denied, to the calling tool. 01:15:30-01:16:08
- **A number for "too many tools," and a second reason to split that has nothing to do with routing.** Coyle's rule is that a subagent should "do one thing" with "maybe one or two tools available to it," argued from the functional-programming habit of small single-purpose functions and from a trades analogy — you hire the specialist, not the generalist carrying every toolkit. The second reason is context rather than routing: a forked subagent's tool calls and intermediate results never enter the parent's window, so splitting bounds what the top-level agent has to hold as well as what it has to know how to do ([Bound Context Twice: Fork the Subtask, Then Compact on a Token Threshold](bound-context-twice-fork-the-subtask-then-compact-on-a-token-threshold.md)). He gives no evidence for one-or-two specifically, so read it as a design bias toward narrow rather than a measured threshold. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 12:42-13:41)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)
- [Bound Context Twice: Fork the Subtask, Then Compact on a Token Threshold](bound-context-twice-fork-the-subtask-then-compact-on-a-token-threshold.md)

Sources:
- [Human-in-the-Loop Automation with n8n - Liam McGarrigle](../sources/20260502_tDArkCqjA-c.md), 01:15:30-01:18:14
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 12:42-13:41
