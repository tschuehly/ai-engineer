# Move Mandatory Brittle Tool Steps Outside the Agent Loop

Summary: When a workflow always requires the same brittle or sensitive step, call the needed tool functions deterministically before the agent starts. This keeps secrets, authentication mechanics, and repetitive setup out of the agent's reasoning burden.

Use when:
- Every agent run must perform a fixed setup step such as login, environment preparation, or tenant selection.
- The step involves secrets or client-specific mechanics that should not be improvised by the model.

Details:
- The demo performs login before creating and invoking the agent; only after deterministic login does the agent receive control of the browser workflow. 34:02-34:29
- Login was moved out of the agent loop because real products may need to authenticate into multiple client systems, each with different mechanics and secrets. 34:33-35:07
- The implementation still reused MCP-provided browser operations, but called them directly as functions and injected JWT tokens into local storage rather than asking the agent to discover and execute login. 35:12-36:11
- Removing mandatory setup from the model's context can simplify the task and avoid burdening the agent with clunky operations that have no useful decision point. 36:11-36:30

- **Moving a brittle step to a provider is a third option beside code and the loop.** This page's usual move is to lift a fragile mandatory step into deterministic code around the agent. A web-access source shows the same relief obtained by relocating it entirely: the browser that made a shopping agent "slow, expensive and unreliable" was not scripted, it was pushed behind a REST call that "runs a full browser under the hood" when needed, so the brittleness stays in the system but leaves the agent's cost, latency, and retry envelope. The evaluation question that follows is whose failure rate you are now exposed to and whether it is reported honestly, which is why the contract in [Fail Loudly and Bill Only for Successful Results](fail-loudly-and-bill-only-for-successful-results.md) matters more once a step is outsourced than when you own it. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 01:33-02:11, 10:29-11:54)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Split Large Automation Surfaces Into Specialized Subagents and Subworkflows](split-large-automation-surfaces-into-specialized-subagents-and-subworkflows.md)
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Adapt Third-Party MCP Servers to the Agent Workflow](adapt-third-party-mcp-servers-to-the-agent-workflow.md)
- [Assign a Web-Access Primitive Per Pipeline Stage](assign-a-web-access-primitive-per-pipeline-stage.md)
- [Fail Loudly and Bill Only for Successful Results](fail-loudly-and-bill-only-for-successful-results.md)

Sources:
- [Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz](../sources/20260408_U00AOI1eJUE.md), 32:49-36:30
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 01:33-02:11, 10:29-11:54
