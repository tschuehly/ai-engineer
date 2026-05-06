# Keep critical code inside human understanding and review capacity

Summary: Agent-generated code should be limited by the human ability to understand, evaluate, and own the resulting system. Non-critical scoped tasks can be delegated more freely, but critical code needs direct human reading and decision ownership.

Use when:
- Deciding which coding tasks can run autonomously and which need a human in the loop.
- Reviewing proposals to scale agent output with many parallel agents, long context windows, or reviewer agents.

Details:
- Zechner warns that many agents can compound errors faster than humans can review them, and that delayed pain appears when the codebase becomes too large or inconsistent for either humans or agents to repair confidently. (12:59-16:01)
- He argues reviewer agents catch some issues but do not remove the human bottleneck because agents inherit complexity from internet-trained examples and do not learn from project pain the way humans do. (13:23-15:24)
- Good agent tasks are scoped so the agent can find all required context, have an evaluation function for the result, or are non-mission-critical work such as reproductions, boring chores, research, and rubber-ducking. (16:13-16:53)
- The final guidance is to slow down, build fewer features, keep generated code volume inside review capacity, allow more freedom for non-critical code, and read every line of critical code. (16:51-17:58)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)

Sources:
- [Building pi in a World of Slop - Mario Zechner](../sources/20260416_RjfbvDXpFls.md), 12:59-17:58
