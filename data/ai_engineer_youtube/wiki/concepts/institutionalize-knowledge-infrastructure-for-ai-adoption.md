# Institutionalize Knowledge Infrastructure for AI Adoption

Summary: Team-level AI adoption stalls when only individual engineers learn how to prompt agents; organizations need shared knowledge infrastructure that captures codebase context, decisions, meetings, docs, task trackers, and successful agent memories.

Use when:
- Scaling coding-agent success from one engineer to a team.
- Diagnosing why AI tool rollout stalls despite strong individual results.

Details:
- The talk identifies the context or knowledge gap as the same blocker behind slow new-hire ramp-up and weak organization-wide AI adoption. 09:27-11:45
- The recommended starting point is to map existing knowledge sources such as Notion, Google Docs, GitHub, documentation, Linear, and codebase context, then fill critical meeting and decision gaps with meeting-intelligence capture. 12:28-13:24
- Tool familiarity is bidirectional: teams learn the AI tools, and the tools learn the organization's coding patterns, architecture decisions, and business logic through shared integrations and use. 13:27-13:58
- Successful memories and task lists should be shared across teams so individual AI workflows compound into reusable organizational practice. 13:59-14:48
- The source explicitly warns that this is not a call to make humans serve AI through documentation theater or organizational rebuilds; the goal is tools and systems that institutionalize knowledge infrastructure for humans and agents. 12:07-12:25
- **The gap has a named owner, and they are usually the org's agent skeptics.** The undocumented institutional knowledge this page wants captured sits with the engineers "holding together with their mental duct tape all the places that agents are not working well" — the same people who "end up being slowest to adopt because they see all the problem[s] first hand." Blum's proposal turns that into an enrolment path rather than an extraction problem: give them ownership of the roadmap for making agents safe in the codebase, since "their feedback is basically the road map," and the knowledge lands in verification infrastructure as a by-product of work they wanted done anyway. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 03:25-04:07, 11:57-12:33)
- **The same gap, located in industries where nobody has ever been asked to write it down.** Shenoy's list is deliberately non-technical: how to close the books when receipts are missing, how to scope a building for construction from a blueprint, how to coordinate vendors to fix a broken roof. "All of this knowledge lives in people's heads, in 20-year-old software, in the way that one senior person on one of these teams just knows how to do it. How do you make this information explicit and create tasks that you can actually learn from?" His extraction mechanism is to run agents alongside employees on real work and keep the traces — "tool calls, the hiccups, the papercuts, everything that goes wrong" — which makes the knowledge infrastructure a byproduct of the work rather than a documentation project. ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 10:13-11:08)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Enterprise Agent Failures Expose Missing Institutional Knowledge](enterprise-agent-failures-expose-missing-institutional-knowledge.md)
- [Surface existing company information before redesigning processes](surface-existing-company-information-before-redesigning-processes.md)
- [Use Compounding Engineering Loops](use-compounding-engineering-loops.md)
- [The Best Engineers Adopt Agents Last, and Their Objections Are the Roadmap](the-best-engineers-adopt-agents-last-and-their-objections-are-the-roadmap.md)
- [Operational Outcomes Are Eval Labels You Only See If You Own the Operation](operational-outcomes-are-eval-labels-you-only-see-if-you-own-the-operation.md)

Sources:
- [Mentoring the Machine - Eric Hou, Augment Code](../sources/20250724_Zniw5c9_jx8.md), 09:27-14:48
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 03:25-04:07, 11:57-12:33
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 10:13-11:08
