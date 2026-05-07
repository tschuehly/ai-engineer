# Agent skills package progressive-disclosure context for repeatable workflows

Summary: Agent skills are context packages that expose a small trigger surface first, then let the agent load deeper instructions, references, or scripts only when the task calls for them.

Use when:
- Designing product-specific or domain-specific context for agents.
- Deciding how much workflow guidance belongs in the agent's initial context.

Details:
- A skill is described as a folder with instructions, files for repeatable workflows, custom information, and optional scripts; the required `SKILL.md` contains front matter such as a name and description. 03:17-04:22
- Progressive disclosure keeps the full skill content out of initial context: the agent receives enough metadata to decide when the rest of the skill is relevant. 04:25-05:24
- Reference files can hold deeper Markdown context and can link to other reference files, so a skill can behave like an index plus chapters rather than one large prompt. 05:21-06:24
- Anthropic's skills framing uses the same folder primitive: only metadata is shown at runtime until the agent decides to load `SKILL.md`, core instructions, directories, scripts, or other assets for the current task. 03:00-04:56
- Skill-like prompts can also implement advanced product workflows when loaded on demand through commands; Cursor used this pattern for worktree and parallel model comparison commands, with server-controlled prompts so the workflow could improve without a client update. 08:24-09:05
- API-specific skills can combine stable orientation with links to current Markdown documentation, reducing stale embedded context while still teaching the agent which models, agents, or workflows are available. 23:34-24:34

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Prompt-coded product behavior reduces code but weakens hard guarantees](prompt-coded-product-behavior-reduces-code-but-weakens-hard-guarantees.md)
- [Agent skills should point to current docs instead of embedding every API detail](agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md)
- [Treat complex skills like software artifacts](treat-complex-skills-like-software-artifacts.md)

Sources:
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md), 03:17-06:24
- [Don't Build Agents, Build Skills Instead - Barry Zhang & Mahesh Murag, Anthropic](../sources/20251208_CEvIs9y1uog.md), 03:00-04:56
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md), 08:24-09:05
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md), 23:34-24:34
