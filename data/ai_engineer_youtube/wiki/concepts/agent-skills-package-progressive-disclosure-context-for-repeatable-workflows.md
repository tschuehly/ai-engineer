# Agent skills package progressive-disclosure context for repeatable workflows

Summary: Agent skills are context packages that expose a small trigger surface first, then let the agent load deeper instructions, references, or scripts only when the task calls for them.

Use when:
- Designing product-specific or domain-specific context for agents.
- Deciding how much workflow guidance belongs in the agent's initial context.

Details:
- A skill is described as a folder with instructions, files for repeatable workflows, custom information, and optional scripts; the required `SKILL.md` contains front matter such as a name and description. 03:17-04:22
- Progressive disclosure keeps the full skill content out of initial context: the agent receives enough metadata to decide when the rest of the skill is relevant. 04:25-05:24
- Reference files can hold deeper Markdown context and can link to other reference files, so a skill can behave like an index plus chapters rather than one large prompt. 05:21-06:24

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)

Sources:
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md), 03:17-06:24
