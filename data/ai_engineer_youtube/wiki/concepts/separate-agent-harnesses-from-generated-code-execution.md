# Separate Agent Harnesses From Generated-Code Execution

Summary: Agent runtimes should separate the trusted harness that plans and controls work from the environment where generated code executes, because co-location turns agent mistakes or hostile code into direct harness compromise risk.

Use when:
- Designing a coding-agent, app-building agent, or sandbox that runs model-generated code.
- Reviewing whether an agent harness has enough execution isolation for production use.

Details:
- Ubl warns that agent-built applications require different infrastructure because agent-written code may be expected to run in production even when the human did not write it by hand. (13:48-14:10)
- He calls the security posture of current agent systems an early-stage problem and compares it to a period when most web systems were easy to compromise. (14:46-15:04)
- His concrete architecture critique is that many agent harnesses combine where the harness runs with where the generated code runs; he argues that separation is key. (15:10-15:36)
- **Three non-security reasons for the same split, from a team that shipped the coupled version first.** Anthropic's managed-agent design originally put the agent loop and the tool container in one box and hit problems that have nothing to do with hostile code: "the container was blocking the agent being able to start its model reasoning," and "if one part of this component went down, the entire box of the agent would go down." Splitting them moved container setup off the first-token path (a reported 60% P50 and over 90% P95 improvement in time to first token, internal figures with no stated methodology), contained failures to one half, and made the container allocatable on demand rather than at session start. Recorded as [decouple the agent loop from the tool execution environment](decouple-the-agent-loop-from-the-tool-execution-environment.md). Two independent arguments converging on the same boundary is the strongest reason to treat it as structural. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 11:16-12:52, 23:15-24:12)
- **The security property the split unlocks.** Because tool execution is not in the model's process, credentials can be "decrypted only when needed at tool execution runtime… the model never sees your security tokens" — an exposure class that a co-located harness cannot close by policy. See [decrypt agent credentials only at tool execution time](decrypt-agent-credentials-only-at-tool-execution-time.md). ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 22:25-22:47)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Run agent-written API code inside programmable sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Hackable agent runtimes need tight safety boundaries](hackable-agent-runtimes-need-tight-safety-boundaries.md)
- [Unified coding-agent harnesses combine models, tools, environments, and safety](unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md)
- [Decouple the Agent Loop From the Tool Execution Environment](decouple-the-agent-loop-from-the-tool-execution-environment.md)
- [Decrypt Agent Credentials Only at Tool Execution Time](decrypt-agent-credentials-only-at-tool-execution-time.md)

Sources:
- [The New Application Layer - Malte Ubl, CTO Vercel](../sources/20260420_XKup1pj-34M.md), 13:48-15:36
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 11:16-12:52, 22:25-22:47, 23:15-24:12
