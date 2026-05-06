# Choose isolates or containers by generated-code workload

Summary: Sandbox technology should match the generated-code workload: isolates are best for fast, constrained functions, while containers are better for full application builds that need filesystem, processes, package installation, and servers.

Use when:
- Selecting a runtime for AI-generated functions, plugins, skills, code interpreters, or app-building workflows.
- Deciding whether a generated-code task needs lightweight isolation or a full operating-system-like environment.

Details:
- V8-style isolates fit short-lived generated functions because they start quickly, run in separate memory and execution contexts, and can expose only specific bindings such as a restricted database interface or logger. (10:28-11:18, 15:24-18:44)
- Isolates are intentionally constrained: they lack ordinary filesystem and process models, cannot run arbitrary binaries, and require state or persistence to be routed through explicit bindings such as databases, durable objects, or KV stores. (19:52-21:05)
- Containers fit generated application workflows that need `git clone`, package installation, build steps, long-running dev servers, real file IO, process management, networking, and preview URLs. (21:12-26:13)
- Container sandboxes should isolate by user, keep files and packages inside the container rather than the host worker, and destroy idle or finished sandboxes because they continue to consume resources and remain a security surface. (25:20-29:45)
- The decision is per workflow step, not permanent: use isolates for quick tool calls, plugins, data transformations, and code interpreters; use containers for app building, package installation, and server execution. (32:40-37:15)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)
- [Run Agent-Written API Code Inside Programmable Sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Separate Agent Harnesses From Generated-Code Execution](separate-agent-harnesses-from-generated-code-execution.md)

Sources:
- [Why, and how you need to sandbox AI-Generated Code? - Harshil Agrawal, Cloudflare](../sources/20260408_AHtGAgQ0Q_Q.md), 10:28-11:29, 15:24-21:05, 21:12-29:45, 32:40-37:15
