# Separate Agent Harnesses From Generated-Code Execution

Summary: Agent runtimes should separate the trusted harness that plans and controls work from the environment where generated code executes, because co-location turns agent mistakes or hostile code into direct harness compromise risk.

Use when:
- Designing a coding-agent, app-building agent, or sandbox that runs model-generated code.
- Reviewing whether an agent harness has enough execution isolation for production use.

Details:
- Ubl warns that agent-built applications require different infrastructure because agent-written code may be expected to run in production even when the human did not write it by hand. (13:48-14:10)
- He calls the security posture of current agent systems an early-stage problem and compares it to a period when most web systems were easy to compromise. (14:46-15:04)
- His concrete architecture critique is that many agent harnesses combine where the harness runs with where the generated code runs; he argues that separation is key. (15:10-15:36)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Run agent-written API code inside programmable sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Hackable agent runtimes need tight safety boundaries](hackable-agent-runtimes-need-tight-safety-boundaries.md)
- [Unified coding-agent harnesses combine models, tools, environments, and safety](unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md)

Sources:
- [The New Application Layer - Malte Ubl, CTO Vercel](../sources/20260420_XKup1pj-34M.md), 13:48-15:36
