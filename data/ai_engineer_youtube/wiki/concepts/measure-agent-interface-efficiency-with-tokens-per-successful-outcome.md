# Measure Agent Interface Efficiency With Tokens Per Successful Outcome

Summary: The fuel efficiency of an agent-facing tool interface should be measured as tokens per successful outcome — token cost conditioned on the agent actually completing the user journey — and compared within a task class rather than globally, so optimization targets the interface, not just the model.

Use when:
- Deciding which tools, descriptions, or output formats to optimize next on an MCP server or agent interface.
- Replacing gut-driven "this tool feels heavy" decisions with a measurable efficiency signal.
- Reviewing an interface whose tools fit the context window but still take many turns to finish a task.

Details:
- Treat the agent as a separate user class with its own non-functional requirements (efficiency, discoverability, security, stability); the interface, not just the model, has a measurable cost. (Chrome DevTools, 05:25-06:05, 21:32-21:50)
- The metric combines two axes: effectiveness (did the agent complete the entire user journey / is the functional intent fulfilled, yes/no) and efficiency (token cost, tool calls, duration). (08:18-08:45)
- It is deliberately "tokens per **successful** outcome," not "tokens per outcome": fuel economy is worthless if the agent can't reach the destination, so always measure effectiveness alongside cost — a cheap run that guesses or fails is not efficient. (08:45-09:03)
- Do not compare globally. Token usage differs enormously by user journey / task class — web scraping is relatively cheap, while debugging why a responsive layout breaks is intricate and uses more tokens, and that's fine — so compare within a journey. (09:10-10:00)
- Operationalize with a per-use-case view (e.g. a bar per tool or journey where shorter bars = less effective for that case); the short bars are where to focus optimization next. Even an imperfect measurement beats gut-driven decisions because it enables data-informed ones. (10:02-11:03)
- This is the design-time counterpart to model-comparison loop metrics: where loop evals rank models by correctness + cost + latency + steps, tokens per successful outcome ranks the *interface* the model is calling, per journey.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Design MCP Servers as Agent Products](design-mcp-servers-as-agent-products.md)
- [Turn Tool Errors Into Agent Self-Healing Recovery](turn-tool-errors-into-agent-self-healing-recovery.md)

Sources:
- [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](../sources/20260605__B4Pv9ttFgY.md), 05:25-11:03, 21:32-22:15
