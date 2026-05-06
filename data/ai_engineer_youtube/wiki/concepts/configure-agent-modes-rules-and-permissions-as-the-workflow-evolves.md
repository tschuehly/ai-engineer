# Configure agent modes, rules, and permissions as the workflow evolves

Summary: Agent workflows should expose configurable roles, rules, skills, tools, workspace boundaries, and approval policies that can change as the team learns what is safe. The configuration is part of the engineering workflow, not a one-time setup detail.

Use when:
- Setting up a coding-agent workspace for a repository.
- Deciding which tools or actions an agent can use without approval.

Details:
- Specialized modes help separate responsibilities: ask mode can be read-only research, architect mode can plan, and code mode can implement. (13:45-14:06, 17:44-18:01)
- AGENTS.md-style files are becoming the always-on project readme for agents, holding repository rules and project details that must be written down before agents can follow them. (18:03-18:26, 19:37-19:58)
- Rules should be tuned as the workflow reveals real behavior: whether to run multiple agents, whether to use worktrees, how to merge work back locally, and which operations deserve auto-approval. (18:28-18:52)
- Permission choices should distinguish autonomous reads, workspace boundaries, test execution, and actions requiring human approval. (18:52-19:15)
- Short commands and context tools can make common workflow transitions faster, such as starting a new task, condensing context, or adding a selected code region into the agent context. (21:28-22:01)
- Agent invocation surfaces are expanding beyond the IDE into CLI, mobile, cloud agents, and Slack, which makes consistent rules and permissions more important across environments. (22:13-22:43)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Customize subagents by task, model, tools, and permissions](customize-subagents-by-task-model-tools-and-permissions.md)
- [Repository skills and AGENTS.md encode repeatable web-agent workflows](repository-skills-and-agents-md-encode-repeatable-web-agent-workflows.md)
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)

Sources:
- [Agentic Engineering: Working With AI, Not Just Using It - Brendan O'Leary](../sources/20260407_BEKc4P87XKo.md), 13:45-22:43
