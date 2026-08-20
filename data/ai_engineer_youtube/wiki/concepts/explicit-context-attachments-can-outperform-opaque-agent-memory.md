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

- Opacity is not hypothetical in shipped products. ChatGPT's synthesized profile enters every conversation but was not viewable in settings; Shlok Khemani read his own only by jailbreaking the model, and the June 2026 transparency update shows a summary of the profile rather than the profile — "which is weird because your profile is already an LLM generated summary of your conversations." Claude's design is the counter-example this page argues for: the raw profile is visible and user edits trigger a resynthesis. ([Lessons from Studying Every Memory System](../sources/20260812_5ZGyKWjQDr0.md), 06:29-06:56, 08:20-09:16, 09:33-09:58)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Personal knowledge bases become agent context substrates](personal-knowledge-bases-become-agent-context-substrates.md)
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Make the Memory Profile Visible and Editable](make-the-memory-profile-visible-and-editable.md)

Sources:
- [The End of Apps - Kitze, Sizzy.co](../sources/20260423_4fntwuOoedA.md), 15:35-17:30
- [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../sources/20260812_5ZGyKWjQDr0.md), 06:29-06:56, 08:20-09:58
