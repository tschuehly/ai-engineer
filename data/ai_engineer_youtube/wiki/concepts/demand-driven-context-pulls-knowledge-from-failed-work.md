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

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Enterprise agent failures often expose missing institutional knowledge](enterprise-agent-failures-expose-missing-institutional-knowledge.md)
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Mine stuck-then-solved sessions for injectable fixes](mine-stuck-then-solved-sessions-for-injectable-fixes.md)

Sources:
- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md), 13:01-16:31
- [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](../sources/20260602_KA5kPbdkK2E.md), 07:55-10:27
