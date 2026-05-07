# Embed Agent Tools in Existing Work Surfaces

Summary: Agent tools get more usage when they appear inside the surfaces where users already perform the work, such as an IDE, ticket, merge request, or support workflow. A separate playground can be useful for discovery but may fail as an adoption surface.

Use when:
- Deciding whether an internal AI tool should be a standalone app, MCP server, IDE integration, ticket action, or merge-request assistant.
- Debugging low usage of a tool that is technically useful but outside the user's normal workflow.

Details:
- Zapier's Autocode playground exposed useful APIs, but asking engineers to visit another web page for context and feedback created low engagement. (05:40-06:25)
- Diagnosis became valuable when support embedded it into the Zap that created Jira tickets from support issues, so the diagnosis appeared in the existing ticket workflow. (06:38-07:22)
- MCP let Zapier expose the same API tools inside engineers' Cursor workflow, reducing IDE context switching. (07:28-07:53)
- Scout moved from loose tools to an embedded agent loop: Zaps start the process, Jira receives diagnosis and routing context, GitLab CI/CD runs plan/execute/validate, and GitLab comments let support request another pass without pulling the merge request into an IDE. (10:09-12:39)
- A high-value tool can still fail when it is synchronous and slow; Zapier's diagnosis tool pushed the workflow toward asynchronous orchestration because users would not wait in the IDE. (07:53-08:15)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Treat agent APIs as asynchronous task lifecycles](treat-agent-apis-as-asynchronous-task-lifecycles.md)
- [Design coding-agent editors as review surfaces](design-coding-agent-editors-as-review-surfaces.md)

Sources:
- [Your Support Team Should Ship Code - Lisa Orr, Zapier](../sources/20251216_RmJ4rTLV_x4.md), 05:40-12:39
