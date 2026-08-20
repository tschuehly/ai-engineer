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

- The mirror-image placement of the same artifact: Matt Dailey (Ref) writes the decision log *before* the run and by humans, not during it and by the agent — "let's pull out all the decisions up front and agree to them and put them in a place that's durable." The two are complementary rather than competing, and the split is by discovery time: an up-front log records decisions someone knew were needed, an in-run log records the ones only reachable by doing the work. Relying on the in-run log alone carries the risk Dailey names — a later LLM summarizing the session and "maybe picking the wrong things." ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 17:41-18:05)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Collaborative plans become executable agent context](collaborative-plans-become-executable-agent-context.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Make the Doc the State and the Agent the Action](make-the-doc-the-state-and-the-agent-the-action.md)

Sources:
- [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../sources/20260422_XNtkiQJ49Ps.md), 08:39-11:29
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 17:41-18:05
