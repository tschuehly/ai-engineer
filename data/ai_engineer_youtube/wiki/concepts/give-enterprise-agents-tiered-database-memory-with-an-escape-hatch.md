# Give Enterprise Agents Tiered Database Memory With an Escape Hatch

Summary: Coding agents keep memory as files on the operator's own disk; an enterprise agent cannot, so memory moves into a database for logical separation and splits into organization-level and user-level tiers. The tiers make repetitive enterprise work cheap to disambiguate, but persistent memory across chats and days introduces bias — it can steer a user into repeating yesterday — so every user needs a way to break out of it.

Use when:
- Porting a coding-agent-shaped harness into a multi-tenant or regulated enterprise deployment.
- Designing where agent memory physically lives and how it is scoped.
- Users report the agent assuming what they want instead of asking.
- Deciding whether personalization from usage history is a feature or a hazard for a given workflow.

Details:
- Storage location is a deployment constraint, not a preference: "cloud code or codex, they use local memory, they write to your desktop. In enterprise healthcare, we can't really do this, so we do memory in a database, just so we have that logical separation." (`UyyOoJmuATU`, 07:23-07:38)
- Two tiers are named: partner-level / organizational memory and user memory. Both exist because "we find people in multi-site health organizations, they tend to do the same thing day after day." (`UyyOoJmuATU`, 11:19-11:50)
- The payoff is intent disambiguation from very little input: if a user "mention[s] a few words — oh, they usually do eligibility and they usually do it within this context, they probably mean this," while another user with the same words probably means something else. (`UyyOoJmuATU`, 11:50-12:05)
- The hazard is steering: "as you introduce memory … persistent memory across chats, across days, you also introduce bias. So maybe that person doesn't want to do the exact same thing that they did yesterday and now you steer them to do the exact same thing they did yesterday. That's a problem." (`UyyOoJmuATU`, 12:06-12:24)
- The required mitigation is an escape hatch, not better ranking: "you want to strike a balance somewhere in there and you want to make sure that any user can break out of this." (`UyyOoJmuATU`, 12:24-12:33)
- Memory is placed inside the harness alongside tools, checks, permissions, handoffs, and evals, and is the mechanism used to sit between fully free agentic reasoning and a fully hardcoded system. (`UyyOoJmuATU`, 08:31-09:03, 11:13-11:19)
- This is a different failure mode from the memory concerns already in the wiki: [ranking memory by outcome utility](rank-agent-memory-by-outcome-utility-not-just-similarity.md) fixes retrieving the *wrong* memory, and [explicit context attachments](explicit-context-attachments-can-outperform-opaque-agent-memory.md) fix not knowing *which* memory was used; this one is about a correctly retrieved, correctly ranked memory narrowing the user's own options.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Rank Agent Memory by Outcome Utility, Not Just Similarity](rank-agent-memory-by-outcome-utility-not-just-similarity.md)
- [Explicit Context Attachments Can Outperform Opaque Agent Memory](explicit-context-attachments-can-outperform-opaque-agent-memory.md)
- [Decouple Agent Harnesses From Enterprise Data Layers](decouple-agent-harnesses-from-enterprise-data-layers.md)
- [Ambient Agents Need Self-Maintenance and Memory Hygiene](ambient-agents-need-self-maintenance-and-memory-hygiene.md)

Sources:
- [Healthcare's Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay](../sources/20260819_UyyOoJmuATU.md), 07:23-07:38, 08:31-09:03, 11:13-12:33
