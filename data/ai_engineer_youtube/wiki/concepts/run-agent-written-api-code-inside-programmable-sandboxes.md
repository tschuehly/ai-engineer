# Run Agent-Written API Code Inside Programmable Sandboxes

Summary: Agent-written code can be a compact and flexible tool plan, but it must run in an isolated environment with explicit controls over filesystem, secrets, network access, resource use, and API rate limits.

Use when:
- Letting an agent execute generated code against an API or SDK.
- Designing hosted agent runtimes, MCP clients, or code-mode tools that may run user- or model-written programs.

Details:
- Code mode shifts work from model-tool back-and-forth into executable programs, so sandbox design becomes part of the agent interface rather than an optional deployment detail. (02:04-02:43, 11:46-12:28)
- A safe execution space should expose capabilities explicitly, control outgoing fetches and network connections, and preserve enough observability to reconstruct why a generated program took an action. (12:19-13:58)
- Long-running generated workflows that persist for days, months, or years need state plus the same task-scoped capability controls as one-shot API scripts. (14:16-14:38)
- The source names concrete generated-code risks: reading local files, accessing secrets, exfiltrating them through network requests, running infinite loops, consuming resources, or running unwanted workloads. (09:40-10:24)
- Cloudflare's dynamic worker example executes generated code in a backend worker rather than in the browser, and the worker cannot read environment secrets by default. (11:15-12:08)
- The sandbox can expose policy as configuration, such as enabling or disabling node compatibility, allowing or blocking outbound network access, and restricting access to specific domains. (12:00-13:00)
- Service APIs need rate limits and abuse protection because agent-written code can loop across many sandboxes and hammer endpoints faster than ordinary interactive users. (17:02-17:31)
- Saved mini-scripts turn generated code into reusable automation such as scheduled scraping jobs, but they introduce maintenance duties because agents may need to repair brittle scripts and resave them when the target changes. (19:04-19:44)
- Agrawal expands the threat model to five sandbox questions: can generated code read secrets, make outbound requests, read files or other tenants' data, affect other users' execution, or consume unbounded CPU and memory. (11:38-12:58)
- When generated code needs authenticated APIs, proxy the request through trusted application code that adds credentials and returns the response; do not pass API keys into the sandbox environment. (27:13-28:37)
- Container sandboxes need lifecycle controls such as `try finally` cleanup, maximum lifetimes, and execution logs because idle sandboxes cost money and remain a security surface. (28:40-35:09)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Sandboxed Code Execution Turns Model Reasoning Into Inspectable Computation](sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md)
- [Expose Large APIs Through Typed Code Mode](expose-large-apis-through-typed-code-mode.md)
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)
- [Treat AI-generated code as untrusted code](treat-ai-generated-code-as-untrusted-code.md)
- [Choose isolates or containers by generated-code workload](choose-isolates-or-containers-by-generated-code-workload.md)

Sources:
- [Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare](../sources/20260419_8txf05vVVl4.md), 02:04-14:38
- [MCP = Mega Context Problem - Matt Carey](../sources/20260425_YBYUvGOuotE.md), 09:40-19:44
- [Why, and how you need to sandbox AI-Generated Code? - Harshil Agrawal, Cloudflare](../sources/20260408_AHtGAgQ0Q_Q.md), 11:38-12:58, 27:13-35:09
