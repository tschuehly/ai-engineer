# Use Decision Logs to Keep Uncertain Agents Moving

Summary: When an agent hits uncertainty inside a large work tree, it can make a reversible decision, record the assumption, and keep working instead of blocking the whole run. The human then reviews the decision log with enough context to reverse or refine choices.

Use when:
- Designing elicitation for long-running agents.
- Avoiding chat threads full of low-context clarification questions.
- Making agent assumptions reviewable after autonomous work.

Details:
- Upfront planning gives the human a chance to align on the approach, but it cannot anticipate special cases the agent only discovers after reading the underlying documents or data. 08:39-09:24
- The suggested pattern is to tell the agent: if uncertain, decide enough to unblock the work, write the choice into a decision log, and let the human review or reverse decisions later. 10:35-11:13
- Decision-log UX should avoid dumping dozens of questions into a linear chat because the human may lack the local context needed to answer them all at once. 11:15-11:29

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Collaborative plans become executable agent context](collaborative-plans-become-executable-agent-context.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)

Sources:
- [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../sources/20260422_XNtkiQJ49Ps.md), 08:39-11:29
