# Custom Agent Modes Encode Repeatable Coding Workflows

Summary: Custom modes package a repeated coding workflow into reusable agent behavior. A mode can narrow tools, prompts, and process expectations so a team can invoke TDD, planning, review, or other workflows consistently.

Use when:
- A team repeatedly asks an agent to follow the same implementation discipline.
- A workflow should be shared after it has proven useful in personal experiments.

Details:
- The Copilot demo creates a test-driven-development mode that first understands the problem, writes failing tests, asks for user confirmation, implements, and repeatedly runs tests until they pass. (45:24-47:49)
- The speakers frame user-scoped modes as a place to experiment and repository-scoped modes as the right place for high-confidence team workflows. (45:24-47:49)
- For mature workflows, modes and prompts work best when the repository also has configured tasks, linting, tests, and instructions that let the agent execute the process instead of merely describing it. (01:17:21-01:18:16)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Configure Agent Modes, Rules, and Permissions as the Workflow Evolves](configure-agent-modes-rules-and-permissions-as-the-workflow-evolves.md)
- [Review coding-agent work at task, plan, and code checkpoints](review-coding-agent-work-at-task-plan-and-code-checkpoints.md)
- [Shift review and testing left for confident vibe coding](shift-review-and-testing-left-for-confident-vibe-coding.md)

Sources:
- [Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison](../sources/20250803_eOxOzcw70f0.md), 45:24-47:49, 01:17:21-01:18:16
