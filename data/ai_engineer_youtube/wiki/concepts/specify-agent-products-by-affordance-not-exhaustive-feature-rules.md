# Specify Agent Products by Affordance, Not Exhaustive Feature Rules

Summary: Agent product specs should define durable capabilities and affordances rather than enumerating every possible user-triggered feature path. Broad tool access and free-form prompts make exhaustive rule lists brittle, while affordances give agents composable boundaries.

Use when:
- Designing product requirements for an agent that can operate across collaboration tools, documents, tickets, messages, or other open-ended surfaces.
- Deciding whether to write one more edge-case feature rule or define the underlying capability the agent may use.

Details:
- Teammates' AI workers have ordinary collaboration identities such as Google Workspace and Slack accounts, which lets customers try workflows the product team did not explicitly design. (01:15-02:46)
- The Google Doc comment example shows the combinatorial problem: direct replies, access checks, thread context, unrelated commenters, Linear tickets, Figma comments, and LinkedIn posts quickly exceed a feature-by-feature specification. (04:36-05:40)
- The suggested product shift is to define affordances such as commenting, communication, email, and collaboration, then let the agent workflow plan within those affordances instead of treating every integration event as a separately specified feature. (06:02-06:42)

Related topics:
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Choose AI coworker form factors by interaction mode](choose-ai-coworker-form-factors-by-interaction-mode.md)
- [Court agent emergence with bounded play](court-agent-emergence-with-bounded-play.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)

Sources:
- [Shipping Products When You Don't Know What they Can Do - Ben Stein, Teammates](../sources/20250728_PthmdT92qNg.md), 01:15-06:42
