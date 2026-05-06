# Agent skills should point to current docs instead of embedding every API detail

Summary: Skills should carry enough stable guidance for an agent to choose the right workflow, then link to current documentation for fast-changing API details. This reduces stale embedded context while preserving a useful trigger and orientation surface.

Use when:
- Packaging SDK, model, or API guidance for coding agents.
- Deciding what belongs inside a skill versus an external reference.

Details:
- The presenters recommend creating skills for things a model cannot do reliably or for user-specific workflow preferences, such as which test runner to use. 23:16-23:33
- Their Interactions API skill includes available Gemini models and high-level agent guidance because agents were otherwise prone to using outdated model names such as Gemini 1.5. 23:34-23:50
- The skill intentionally does not embed all API documentation; it links to Markdown documentation so agents with web-fetch tools can retrieve details when needed. 23:50-24:06
- Keeping volatile API details in documentation instead of the skill avoids forcing every skill user to update their local package for each new API feature. 24:06-24:34

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Package reusable context as skills, libraries, and registries](package-reusable-context-as-skills-libraries-and-registries.md)
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)

Sources:
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md), 23:16-24:34
