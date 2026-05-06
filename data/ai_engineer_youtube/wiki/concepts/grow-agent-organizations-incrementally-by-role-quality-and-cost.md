# Grow Agent Organizations Incrementally By Role Quality and Cost

Summary: Large agent organizations should be grown agent by agent, with role-specific instructions, model choices, skills, budgets, and quality checks before adding more parallel agents.

Use when:
- Evaluating whether to import a large preset agent organization or start from a small team.
- Routing frontier and cheaper models across an agent organization.

Details:
- The talk warns against starting with huge templates of dozens or hundreds of agents unless the operator has crafted behavior expectations for each role.
- A recommended pattern is to start with only the agents needed, verify quality, then fan out when the work actually requires additional roles.
- Expensive frontier models need not back every agent; high-intelligence roles may justify Claude, Codex, or other frontier systems, while lower-stakes roles can use cheaper model routes such as OpenRouter through OpenCode when quality is sufficient.
- Agent instructions should evolve from observed failures: if an agent blocks without a useful diagnosis or writes too broad a test suite, update its role instructions and feed repeated skill-use failures to a skill consultant or similar meta-agent.

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Customize subagents by task, model, tools, and permissions](customize-subagents-by-task-model-tools-and-permissions.md)
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)

Sources:
- [Paperclip: Open Source Human Control Plane for AI Labor - Dotta Bippa](../sources/20260415_h403btjldDQ.md), 16:27-18:23, 20:10-21:18
