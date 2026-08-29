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
- **A trained recovery policy is the other half.** Amazon AGI Lab reports that standard RL practice resets the environment on an infra error, which produces a model that has never recovered from one; their change is to "pass it to the model and… expect the model to recover from it using native tool use, native actions like… refresh, backtrack, compare, wait, abandon, escalate to the user." Good error messages help a model that knows what to do with them; a trained recovery policy still needs the error to reach the context window instead of being swallowed by infrastructure. See [Make Recovery a Native Model Action, Not an Infra Reset](make-recovery-a-native-model-action-not-an-infra-reset.md). ([From RL to IRL](../sources/20260814_Cc0_nyxROBA.md), 09:22-09:48)
- **The same principle stated as a vendor's product-development policy, with an org consequence.** Garvin: "this is nothing new but our perspective is to have much more verbose and clear errors so that the agent can self-correct" — and then the part that is not obvious, which is who does the work. "Our developer experience teams are working on finding more failure cases like that and being able to help guide especially in the initialization and setup." Error-surface quality becomes a staffed, ongoing discovery activity aimed at a specific phase, rather than a property you get right once when the endpoint is written. Note that no recovery-rate measurement is offered; a single error code is shown on screen. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 06:47-07:12)

- **The step before an actionable error is an error at all.** This page assumes the failure surfaces; a web-access source supplies the case where it does not. A blocked fetch returns HTTP 200 with a plausible body, so a tool that forwards it has not produced a bad error message — it has produced a successful-looking response the agent must spend input tokens to classify. The contract Šteimantas asks for is that the tool assert what it already knows: "in case of captures or other blocks the request would fail with an explicit error message. So I know not to include it when sending to a large language model." The costs of skipping each step differ usefully — an unhelpful error wastes a retry, a swallowed error wastes the whole payload and quietly biases the result set. See [Fail Loudly and Bill Only for Successful Results](fail-loudly-and-bill-only-for-successful-results.md). ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 08:39-09:01, 10:29-11:54)

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Measure Agent Interface Efficiency With Tokens Per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)
- [Use Tool Names and Descriptions as Operational Prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Expose task workflow guidance through MCP resources and tools](expose-task-workflow-guidance-through-mcp-resources-and-tools.md)
- [Let an Agent Build and Maintain Self-Healing Scrapers](let-agents-build-and-maintain-self-healing-scrapers.md)
- [Make Recovery a Native Model Action, Not an Infra Reset](make-recovery-a-native-model-action-not-an-infra-reset.md)
- [Seed the Agent-Built Sandbox With Usage, Not Just Objects](seed-the-agent-built-sandbox-with-usage-not-just-objects.md)
- [Fail Loudly and Bill Only for Successful Results](fail-loudly-and-bill-only-for-successful-results.md)
- [Validate Retrieved Content Before Spending Tokens on It](validate-retrieved-content-before-spending-tokens-on-it.md)

Sources:
- [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](../sources/20260605__B4Pv9ttFgY.md), 13:14-15:16
- [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../sources/20260814_Cc0_nyxROBA.md), 09:22-09:48
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 06:47-07:12
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 08:39-09:01, 10:29-11:54
