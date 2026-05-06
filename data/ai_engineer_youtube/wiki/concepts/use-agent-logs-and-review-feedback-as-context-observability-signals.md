# Use Agent Logs and Review Feedback as Context Observability Signals

Summary: Agent logs, PR feedback, and production failures reveal whether context is missing, misunderstood, or stale. Durable context workflows should mine those signals and turn repeated failures into shared context improvements.

Use when:
- Building feedback loops for team-maintained prompt, skill, or context libraries.
- Diagnosing repeated agent mistakes that survive local prompting and appear in review or production.

Details:
- Agent logs can show when an agent says it is missing information or fails to use available context, giving teams a feedback channel for shared context maintenance (17:54-19:21).
- PR review comments on agent-generated work are also feedback on the context that shaped the PR; the durable fix is often to improve context so the next iteration avoids the same defect (19:24-19:47).
- Production failures from AI-generated code can be converted into test cases and then into context improvements, closing the loop between runtime observation and future agent behavior (19:49-20:29).
- The organizational version of the loop is to publish reusable fixes so multiple teams benefit from one context improvement rather than each team rediscovering the same missing instruction (22:38-23:39).

Related topics:
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](demand-driven-context-pulls-knowledge-from-failed-work.md)

Sources:
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md), 17:54-23:39
