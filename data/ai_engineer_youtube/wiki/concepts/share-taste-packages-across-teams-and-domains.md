# Share taste packages across teams and domains

Summary: Learned coding taste can be treated as a shareable package that steers a preferred LLM toward a developer, team, library, design, or enterprise convention set.

Use when:
- A team wants a coding agent to apply another expert's specialized style or domain judgment without copying a whole repository into context.
- An organization needs project- or enterprise-level conventions to travel across agent runs and developers.

Details:
- Awais presents taste as usable with any preferred LLM: the LLM provides generative capability while the taste layer supplies learned choices and intentions. (14:25-14:39, 17:36-18:05)
- Taste can be shared with a team and applied by scope: React code could use a React expert's taste, front-end work could borrow a design engineer's taste, and enterprise projects could encode organization-specific conventions. (16:14-17:22, 18:17-18:40)
- The possible packaging surface is still unsettled in the talk, but the current form is described as transparent Markdown or another dump of the learned neuro-symbolic preference space; the example command is `npx taste` to install a CLI taste. (18:42-19:35)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Package reusable context as skills, libraries, and registries](package-reusable-context-as-skills-libraries-and-registries.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Treat complex skills like software artifacts](treat-complex-skills-like-software-artifacts.md)

Sources:
- [Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL - Ahmad Awais, CommandCode](../sources/20251124_kWOQS3XPZ10.md), 14:25-14:39, 16:14-17:22, 17:36-19:35
