# Run Agent-Written API Code Inside Programmable Sandboxes

Summary: Agent-written code can be a compact and flexible tool plan, but it must run in an isolated environment with explicit controls over filesystem, secrets, network access, resource use, and API rate limits.

Use when:
- Letting an agent execute generated code against an API or SDK.
- Designing hosted agent runtimes, MCP clients, or code-mode tools that may run user- or model-written programs.

Details:
- The source names concrete generated-code risks: reading local files, accessing secrets, exfiltrating them through network requests, running infinite loops, consuming resources, or running unwanted workloads. (09:40-10:24)
- Cloudflare's dynamic worker example executes generated code in a backend worker rather than in the browser, and the worker cannot read environment secrets by default. (11:15-12:08)
- The sandbox can expose policy as configuration, such as enabling or disabling node compatibility, allowing or blocking outbound network access, and restricting access to specific domains. (12:00-13:00)
- Service APIs need rate limits and abuse protection because agent-written code can loop across many sandboxes and hammer endpoints faster than ordinary interactive users. (17:02-17:31)
- Saved mini-scripts turn generated code into reusable automation such as scheduled scraping jobs, but they introduce maintenance duties because agents may need to repair brittle scripts and resave them when the target changes. (19:04-19:44)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Sandboxed Code Execution Turns Model Reasoning Into Inspectable Computation](sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md)
- [Expose Large APIs Through Typed Code Mode](expose-large-apis-through-typed-code-mode.md)

Sources:
- [MCP = Mega Context Problem - Matt Carey](../sources/20260425_YBYUvGOuotE.md), 09:40-19:44
