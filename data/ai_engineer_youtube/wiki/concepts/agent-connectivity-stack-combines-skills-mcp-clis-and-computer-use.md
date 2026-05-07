# Agent Connectivity Stack Combines Skills, MCP, CLIs, and Computer Use

Summary: Agent connectivity is a stack of complementary surfaces rather than a single protocol choice. Skills, MCP, CLIs, and computer use each fit different operational constraints around domain guidance, local execution, remote semantics, governance, and user interfaces.

Use when:
- Choosing how an agent should reach SaaS systems, shared drives, local tools, or domain guidance.
- Reviewing claims that one connectivity mechanism can replace every other tool surface.

Details:
- General knowledge-worker agents need to connect to multiple SaaS applications and shared drives, while coding agents are an unusually favorable case because they are local, verifiable, compiler-backed, and supervised by a developer. (03:51-05:06)
- Skills fit reusable domain knowledge and specific capabilities captured in simple files; CLIs fit local agents with shell access, sandboxing, code execution, and tools that models likely saw during pretraining. (05:28-06:31)
- MCP fits richer remote semantics: resources, long-running task UI, platform independence, authorization, governance, policy, MCP applications, and skills over MCP. (06:31-07:12)
- The talk argues that strong 2026 agents will combine skills, MCP, CLIs, and computer use rather than standardizing on only one connectivity path. (07:12-07:20, 17:49-18:01)
- Amazon Q Developer's CLI agent demonstrates the CLI-plus-MCP shape: from a terminal chat, it connects to an AWS documentation MCP server, asks for permission, and returns a response grounded in official docs. (05:23-06:27)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Agent Experience Prioritizes APIs, CLIs, and MCP Over Dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Discover Large API Tool Surfaces Progressively](discover-large-api-tool-surfaces-progressively.md)
- [Deploy Remote MCP Servers on Serverless Cloud Infrastructure](deploy-remote-mcp-servers-on-serverless-cloud-infrastructure.md)

Sources:
- [The Future of MCP - David Soria Parra, Anthropic](../sources/20260419_v3Fr2JR47KA.md), 03:51-07:20, 17:49-18:01
- [Building Agents at Cloud Scale - Antje Barth, AWS](../sources/20250802_WJjInLeaJjo.md), 05:23-06:27
