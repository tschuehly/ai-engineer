# Model Airplanes Give Coding Agents Token-Efficient Exemplars

Summary: Thin example projects can show a coding agent the shape of a successful integration without carrying the complexity and token cost of full production apps.

Use when:
- A coding agent needs architectural examples across frameworks or languages.
- Full reference applications are too large, brittle, or distracting to place in agent context.

Details:
- PostHog maintains "model airplanes": lightweight projects with PostHog already implemented across multiple frameworks and languages. 05:27-05:43
- The examples are intentionally not complete production applications; auth may be simplified, but it remains auth-shaped so the agent can recognize where login or identity tracking belongs. 05:43-06:27
- The pattern gives the model the correct shape of an integration in a more token-efficient form and helps it complete a consistent implementation rather than inventing a strange architecture. 06:27-06:47
- In Q&A, Campos says the context service flattens these model airplanes into Markdown and includes them as references in skill files so the model can search and use them while working. 17:01-18:07

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Fresh Markdown context mitigates model rot in codegen](fresh-markdown-context-mitigates-model-rot-in-codegen.md)

Sources:
- [LLM codegen fails and how to stop 'em - Danilo Campos, PostHog](../sources/20260430_juoNbJiZUi0.md), 05:27-06:47, 17:01-18:07
