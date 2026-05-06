# Agent experience prioritizes APIs, CLIs, and MCP over dashboards

Summary: As agents and bots become primary product users, products need machine-friendly control surfaces such as APIs, CLIs, and MCP servers, not only human dashboards.

Use when:
- Designing product interfaces for agentic users or deciding whether a dashboard is enough.
- Prioritizing API, CLI, MCP, or embedded UI work for a service that agents need to operate.

Details:
- Swyx cites a conference keynote claim that a large share of Vercel's users are now bots or agents, then infers that dashboards matter less than APIs, CLIs, and MCP surfaces for those users. (12:48-13:06)
- He links this to "agent experience": products may need to ship UI or capabilities into someone else's app, and the primary user may be an agent rather than a human clicking through a custom dashboard. (13:06-13:28)
- In his own workflow, Figma was useful less as a dashboard destination than as an artifact handed into an agentic workflow that produced implementation output. (13:29-13:38)
- Ubl gives the direct Vercel observation behind this pattern: more than 60% of Vercel page views over the prior seven days were AI agents, and platform usage is shifting from dashboard clicking toward APIs and CLIs. (13:00-13:26)
- He says feature proposals should answer how the feature is automated and how an agent uses it, treating CLI design as a first-class product question rather than an afterthought to UI. (13:27-13:38)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Separate agent harnesses from generated-code execution](separate-agent-harnesses-from-generated-code-execution.md)

Sources:
- [Agents for Everything Else - swyx](../sources/20260501_zepu8Kk6FBQ.md), 12:48-13:38
- [The New Application Layer - Malte Ubl, CTO Vercel](../sources/20260420_XKup1pj-34M.md), 13:00-13:38
