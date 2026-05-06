# Treat Prompts as Distributed Harness Surfaces

Summary: Agent guidance is not limited to the initial user prompt. Rules files, skills, lint errors, PR comments, reviewer agents, and tests can all inject task-specific guidance into the agent trajectory without changing model weights.

Use when:
- Auditing where an agent receives instructions during a coding workflow.
- Designing a harness that needs to refresh or reinforce context over long-running agent work.

Details:
- Lopopolo says teams should build with the expectation that context gets paged out over time, so the harness needs ways to continually refresh context as an agent works. (11:24-12:00)
- The talk lists `AGENTS.md`-style files, rules files, skills, lint error messages, reviewer-agent PR comments, and agent SDKs embedded into tests as prompt surfaces. (11:22-16:15)
- Reviewer-agent comments can be required before an agent proposes a change for merge, turning PR review feedback into an active instruction channel. (15:46-15:57)
- Prompting guidance can itself be packaged as a skill synthesized from prompting cookbooks, so agents can help author the prompts used elsewhere in the harness. (16:15-16:40)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Use agent hooks to automate session rituals](use-agent-hooks-to-automate-session-rituals.md)
- [Prompt-coded product behavior reduces code but weakens hard guarantees](prompt-coded-product-behavior-reduces-code-but-weakens-hard-guarantees.md)

Sources:
- [Harness Engineering: How to Build Software When Humans Steer, Agents Execute - Ryan Lopopolo, OpenAI](../sources/20260417_am_oeAoUhew.md), 11:22-16:40
