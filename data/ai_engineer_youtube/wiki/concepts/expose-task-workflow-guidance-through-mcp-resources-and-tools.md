# Expose task workflow guidance through MCP resources and tools

Summary: MCP can expose both task-management guidance and task-management operations to coding agents. Resources teach the workflow and required fields, while tools let agents search, inspect, create, update, and complete work items without guessing command syntax.

Use when:
- Building an MCP server for an agent-facing project-management workflow.
- Deciding what belongs in MCP resources versus MCP tools.
- Teaching agents how to follow a repository-local task lifecycle.

Details:
- Backlog.md uses an MCP server to expose instructions and tools to AI agents; the transcript calls resources the most important part because they teach agents how to use the workflow. (05:40-06:02)
- The workflow overview resource explains what Backlog.md is and points to deeper resources for task creation, execution, and completion. (06:02-06:24)
- The task-creation guide tells agents how to create tasks and which fields are required or optional. (06:15-06:24)
- The task-execution guide tells an implementing agent to put a task in progress and assign it to itself, while the completion guide tells it to check acceptance criteria and the definition of done. (06:24-06:53)
- The MCP tools expose task operations such as search, view details, create, and update tasks so agents can check for duplicates and mutate task state through the intended interface. (06:54-07:29)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Design MCP servers as agent products](design-mcp-servers-as-agent-products.md)
- [Agent skills should point to current docs instead of embedding every API detail](agent-skills-should-point-to-current-docs-instead-of-embedding-every-api-detail.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)

Sources:
- [Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents - Alex Gavrilescu, Funstage](../sources/20251124_zMXKhhwiCIc.md), 05:40-07:29
