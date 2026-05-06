# Expose Observability As Agent-Readable Feedback

Summary: Logs, metrics, traces, and deployment health signals should be available through machine-friendly surfaces so agents can verify outcomes and iterate without relying on human dashboards.

Use when:
- Designing observability for platforms or applications that coding agents need to debug.
- Defining success criteria for agent-executed deployment or provisioning work.

Details:
- The talk emphasizes that agents need precise instructions and explicit success criteria, including how they know they have completed the task. (11:14-11:32)
- Humans may verify deployments by reading graphical observability dashboards, but agents are unlikely to use those interfaces reliably as their primary feedback channel. (11:32-12:03)
- Platform teams should expose logs, metrics, traces, and other verification signals through APIs, CLIs, MCP servers, or similar machine-friendly surfaces so the agent can close the loop. (12:03-12:20)
- Platform-readiness changes should be measured before and after with delivery, reliability, support-load, or developer-experience metrics rather than assumed from AI adoption alone. (17:12-19:19)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Agent traces require specialized eval infrastructure](agent-traces-require-specialized-eval-infrastructure.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)

Sources:
- [Platforms for Humans and Machines: Engineering for the Age of Agents - Juan Herreros Elorza](../sources/20260408_cCRO3ChaYhM.md), 11:14-12:20, 17:12-19:19
