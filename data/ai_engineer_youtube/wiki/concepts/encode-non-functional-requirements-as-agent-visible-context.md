# Encode Non-Functional Requirements as Agent-Visible Context

Summary: Coding agents need the team's quality expectations written down where the harness can expose them. Documentation, ADRs, QA-plan guidance, review history, and persona-oriented notes turn implicit judgment about maintainability, reliability, security, and product fit into reusable context.

Use when:
- Agents produce plausible code that misses local quality expectations.
- A team wants expert review knowledge to improve every agent trajectory instead of appearing only in repeated PR comments.

Details:
- Lopopolo says a single patch can require hundreds of small decisions around underspecified non-functional requirements, so agents need those expectations specified in durable, visible form. (08:28-09:26)
- Breadcrumbs, documentation, ADRs, persona-oriented documentation, historical tickets, and code reviews are described as process evidence that helps agents reproduce how the team reached its current product and code. (06:54-07:25)
- Having teammates document their domain judgment, such as what makes a good QA plan, lets every engineer driving agents benefit from that expertise without waiting for low-signal review loops. (10:09-11:01)
- The source ties agent legibility to context efficiency: structures should be native to agents, respect scarce context, and make required tokens predictable. (07:25-07:59)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent-legible codebases reduce generated-code entropy](agent-legible-codebases-reduce-generated-code-entropy.md)
- [Maintain ubiquitous language for AI coding](maintain-ubiquitous-language-for-ai-coding.md)
- [Collaborative plans become executable agent context](collaborative-plans-become-executable-agent-context.md)

Sources:
- [Harness Engineering: How to Build Software When Humans Steer, Agents Execute - Ryan Lopopolo, OpenAI](../sources/20260417_am_oeAoUhew.md), 06:54-11:01
