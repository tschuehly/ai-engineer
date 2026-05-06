# Explicit Context Attachments Can Outperform Opaque Agent Memory

Summary: For personal agents, explicit context selection can be more reliable than hoping an opaque memory system retrieves the right facts. Nested topic descriptions and user-attached documents, knowledge bases, passwords, and skills make the context contract visible.

Use when:
- Designing agent memory for personal workspaces, support workflows, or project assistants.
- Debugging failures where an agent retrieved the wrong personal or project context.

Details:
- The speaker says he does not trust generic agent memory to "solve memory" and instead uses nested topics whose parent descriptions are injected into the first prompt for a scoped conversation (15:35-16:19).
- In the example tree `work -> projects -> Benji -> Benji customer support`, the agent receives descriptions for the parent topics so it knows the work context, project, product, and support behavior before responding (15:44-16:11).
- The workspace also supports explicit mentions of Markdown documents, knowledge bases, passwords, and skills so the user can attach the exact context needed for a task instead of relying only on automatic retrieval (17:03-17:30).
- This pattern is a challenge to broad memory claims: visible topic context and selected attachments can be easier to inspect, debug, and revise than a hidden memory lookup (15:35-17:30).

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Personal knowledge bases become agent context substrates](personal-knowledge-bases-become-agent-context-substrates.md)
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)

Sources:
- [The End of Apps - Kitze, Sizzy.co](../sources/20260423_4fntwuOoedA.md), 15:35-17:30
