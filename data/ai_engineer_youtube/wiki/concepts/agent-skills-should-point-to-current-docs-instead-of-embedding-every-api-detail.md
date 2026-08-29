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
- **Freshness has a second, non-correctness reason to exist.** Pointing at current docs assumes the docs get updated when something changes. Jarmak adds a maintenance obligation that a correctness-driven process never generates: "even if your stuff hasn't changed in 2 years, which would be shocking. Even if it hasn't, keep everything up-to-date and fresh because that is how they have their relevance algorithm." Recency is an input to what an assistant retrieves and ranks, decoupled from whether the content is still true — so a stable API's docs can go quietly unfindable. See [Stale Product Content Compounds Through Newer Models](stale-product-content-compounds-through-newer-models.md). ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 11:53-12:12)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Package reusable context as skills, libraries, and registries](package-reusable-context-as-skills-libraries-and-registries.md)
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Stale Product Content Compounds Through Newer Models](stale-product-content-compounds-through-newer-models.md)

Sources:
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md), 23:16-24:34
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 11:53-12:12
