# Turn Tool Errors Into Agent Self-Healing Recovery

Summary: Every error an agent hits costs retry and reasoning tokens, so a tool's error surface should be designed so the agent recovers on its own without a human. Error recovery is a spectrum: actionable error messages, proactive detours that counteract model priors, and diagnostic-playbook skills.

Use when:
- Designing the error/failure responses of an MCP server or agent-facing tool.
- An agent gets stuck, loops, or escalates to a human on recoverable tool failures.
- Auditing why an interface is token-expensive even when individual calls succeed.

Details:
- Efficiency is useless if the agent gets stuck; every error forces a retry plus reasoning about what happened, so error design is part of interface fuel efficiency. (Chrome DevTools, 13:14-13:34)
- Actionable error messages enable self-heal: adding the missing fact to a vague message ("Unable to navigate back in currently selected page" → add "no previous page in history to navigate") let the agent fix itself instead of needing a human to intervene. Useful error messages sound obvious but most tools don't have them, and getting them right took several iterations. (13:46-14:20)
- Proactive detours counteract the model's training-data priors: when a model is biased toward the wrong tool for a goal, steer it — e.g. detour performance profiling to the start-performance-trace tool rather than the Lighthouse audit it would otherwise reach for. (14:20-14:50)
- Diagnostic-playbook skills handle recurring setup failures: a `troubleshooting` skill kicks in to help both the human and the agent fix common mistakes (e.g. misconfiguring the Chrome DevTools MCP server), increasing the resilience of the whole harness. (14:50-15:16)
- This is the recovery side of interface design; the prevention side is discoverability (clear tool descriptions and the right tool set) so the agent doesn't error in the first place.

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Measure Agent Interface Efficiency With Tokens Per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)
- [Use Tool Names and Descriptions as Operational Prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Expose task workflow guidance through MCP resources and tools](expose-task-workflow-guidance-through-mcp-resources-and-tools.md)
- [Let an Agent Build and Maintain Self-Healing Scrapers](let-agents-build-and-maintain-self-healing-scrapers.md)

Sources:
- [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](../sources/20260605__B4Pv9ttFgY.md), 13:14-15:16
