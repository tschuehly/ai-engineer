# Agent Experience Means Autonomous Access, Understanding, and Operation

Summary: Agent experience is the ease with which agents can access, understand, and operate in a digital environment to complete a user-defined goal, with autonomy as the important extra constraint.

Use when:
- Designing products, devtools, or runtime environments whose primary users may be agents.
- Auditing whether a tool still depends on humans to click buttons, read logs, debug setup, or bridge missing machine interfaces.

Details:
- Burazin frames agent experience as the successor to user, customer, and developer experience, focused on whether agents can access, understand, and operate within digital environments to achieve the user's goal. 02:04-02:45
- He argues that the missing test is autonomy: if an agent always falls back to a human to log in, click buttons, debug errors, or type into terminals, the tool has not really solved agent experience. 05:35-06:29, 14:00-14:27
- The baseline agent-facing surface includes authentication handoff, clean Markdown documentation such as `.md` doc views and `llms.txt`, and API-first access to key product functionality. 03:07-05:23
- He cautions that API-first and readable docs are necessary but not sufficient; the stronger question is whether the agent can complete the task end to end without a human acting as an operational adapter. 05:23-06:29, 14:30-15:02
- Lajili (Poolside) frames this as the engineer's new job — the "AIX engineer": "focus less on the product and more on trying to make the AI work on the product" by building tools, improving the codebase so it is easier to work on, and improving knowledge bases, in whatever form fits (CLI, skill, or MCP). ([Your agent is blindfolded](../sources/20260708_iRcX54EO5g8.md), 05:51-07:02)
- His oxygen-mask investment argument: "put the mask on the AI first" — make it self-served *before* you build features, because "even if it slows you down right now, it's an investment that pays off as soon as you start multiplying agents and running things over time"; velocity without this "self-serve" scaffolding just compounds errors. ([Your agent is blindfolded](../sources/20260708_iRcX54EO5g8.md), 06:38-07:29)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Treat agents as embodied action systems](treat-agents-as-embodied-action-systems.md)
- [Give Your Agent Eyes With a Product-Specific Observation Tool](give-your-agent-eyes-with-a-product-specific-observation-tool.md)
- [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md)

Sources:
- [AX is the only Experience that Matters - Ivan Burazin, Daytona](../sources/20250724_e9sLVMN76qU.md), 02:04-06:29, 14:00-15:02
- [Your agent is blindfolded — Johan Lajili, Poolside AI](../sources/20260708_iRcX54EO5g8.md), 05:51-07:29
