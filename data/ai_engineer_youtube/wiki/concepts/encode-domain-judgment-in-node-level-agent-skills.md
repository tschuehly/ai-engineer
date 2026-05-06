# Encode Domain Judgment in Node-Level Agent Skills

Summary: Skills can put human judgment into specific recurring nodes of an agent's work tree, including special-case contingencies that are hard to anticipate during upfront planning. This makes skills a control mechanism, not only a context-loading convenience.

Use when:
- A workflow has recurring decision points that need domain-specific handling.
- Upfront planning misses special cases discovered during execution.
- Deciding whether to encode guidance in a skill, plan, or artifact UI.

Details:
- The talk describes complex agent work as a tree or DAG where root-level planning gives limited control because the human can only steer before the agent discovers local details. 07:53-08:36
- Skills improve control by encoding human judgment into nodes of work, such as how to review confidentiality or termination clauses. 09:49-10:05
- Skills can cover contingencies discovered during execution, such as a special EU law affecting a termination clause; unlike a static plan, the skill is available when the relevant node is reached. 10:05-10:23
- Progressive discovery helps skills stay available without requiring the human to preload every special case, but the talk notes that teams will not have skills for everything. 10:23-10:33

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)

Sources:
- [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../sources/20260422_XNtkiQJ49Ps.md), 07:53-10:33
