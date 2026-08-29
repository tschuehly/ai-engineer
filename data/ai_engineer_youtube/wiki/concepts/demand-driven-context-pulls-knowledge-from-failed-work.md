# Demand-Driven Context Pulls Knowledge From Failed Work

Summary: Demand-driven context builds an agent knowledge base by assigning real tasks, watching where agents fail or ask questions, and documenting the missing knowledge needed to solve those tasks.

Use when:
- Growing enterprise agent context without guessing every prerequisite up front.
- Turning agent failures, questions, and blocked work into documentation requirements.

Details:
- The workflow favors a pull strategy over a push strategy: give agents work items and let them pull missing information from humans and systems, 13:01-14:17.
- One cycle starts with a problem, observes the agent's first-attempt failure, captures the checklist of missing information, satisfies those gaps, and curates the new knowledge for future reuse, 14:48-15:45.
- The talk compares the loop to TDD: failed tasks play the role of failing tests, and context is added until the task can pass, 15:49-16:31.
- Lovable runs a production-scale automated instantiation of the same pull strategy at ~200,000 projects/day: an LLM judge detects "stuck → solved" transitions, the system asks "what should we have injected at the start of this query?", clusters similar cases so the captured knowledge generalizes, eval-verifies the fix, and a lightweight model injects the entry into future runs — making this loop a continuous learning system rather than a one-time documentation pass (Lovable 07:55-10:27).
- **The people holding the missing context have the least incentive to write it down.** Figma's hardest-to-replace engineers "have all the institutional [context] that ha[s] never [been] written down in their head and they get so much burden and become bottlenecks and get[] really frustrated" — and they are also the slowest to adopt agents, because they see every failure first. That is the incentive problem this page's loop routes around: pulling knowledge out of observed agent failures does not require the bottleneck to volunteer anything, it only requires that the failures be captured. Volunteering, by contrast, asks someone to dissolve the position that makes them indispensable. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 03:25-04:07)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Enterprise agent failures often expose missing institutional knowledge](enterprise-agent-failures-expose-missing-institutional-knowledge.md)
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Mine stuck-then-solved sessions for injectable fixes](mine-stuck-then-solved-sessions-for-injectable-fixes.md)
- [The Best Engineers Adopt Agents Last, and Their Objections Are the Roadmap](the-best-engineers-adopt-agents-last-and-their-objections-are-the-roadmap.md)

Sources:
- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md), 13:01-16:31
- [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](../sources/20260602_KA5kPbdkK2E.md), 07:55-10:27
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 03:25-04:07
