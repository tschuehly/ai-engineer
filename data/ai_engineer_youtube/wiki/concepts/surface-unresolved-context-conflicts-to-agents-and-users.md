# Surface Unresolved Context Conflicts to Agents and Users

Summary: Context engines should resolve conflicts when they can, but explicitly surface unresolved contradictions instead of hiding them behind a guessed answer. The unresolved state becomes a learning point for human clarification and future context improvement.

Use when:
- Building retrieval over sources that may disagree, such as docs, code, Slack, tickets, and PR history.
- Designing agent handoff behavior for ambiguous or conflicting organizational knowledge.

Details:
- Large organizations can contain conflicting source material, so a context engine needs conflict-resolution behavior rather than treating all retrieved chunks as equally true. (11:23-11:56)
- The speaker describes unresolved truth as a gray area: when the system cannot resolve a conflict, it should tell the agent and learn from additional user input. (16:08-16:31)
- A reported implementation mistake was using naive strategies to resolve conflicts and not surfacing the ones that remained unresolved. (24:04-24:25)
- Graph RAG-style summarization can cross permission boundaries, so conflict and synthesis logic must also respect compartmentalized access. (37:37-37:55)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Enterprise agent failures often expose missing institutional knowledge](enterprise-agent-failures-expose-missing-institutional-knowledge.md)
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](demand-driven-context-pulls-knowledge-from-failed-work.md)
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)

Sources:
- [Mergeable by default: Building the context engine to save time and tokens — Peter Werry, Unblocked](../sources/20260503_5ID22ACI7IM.md), 11:23-11:56, 16:08-16:31, 24:04-24:39, 37:37-37:55
