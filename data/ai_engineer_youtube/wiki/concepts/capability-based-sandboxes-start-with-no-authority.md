# Capability-Based Sandboxes Start With No Authority

Summary: A code-mode runtime should begin as an execution environment with no external authority, then receive only the APIs, network access, and state needed for the current task.

Use when:
- Designing sandboxes for model-generated code that will call APIs or manipulate user data.
- Reviewing whether an agent runtime grants broad ambient authority instead of explicit task-scoped capabilities.

Details:
- Pai distinguishes this from wrapping a full container in security controls: start with an environment that can execute code but cannot fetch, call APIs, or access anything else until capabilities are granted. (12:33-13:08)
- Cloudflare's dynamic-worker example uses V8 isolates for fast startup and security hardening, but the transferable pattern is capability exposure rather than a specific JavaScript runtime. (13:08-14:15)
- Recommended defaults include no outgoing fetches, API-only capability exposure, fast ephemeral execution, and full observability into generated code and its actions. (13:30-14:15)
- The language is not the core constraint; JavaScript, Python, WASM, or Lisp-like runtimes still need events, sandboxing, capability-based security, and embeddability for fast ephemeral runs. (17:50-18:17)
- Agrawal states the capability rule as allow-list security: enumerate what generated code may access rather than trying to enumerate all operations it must not perform. If a capability is not granted, it should not exist for the generated code. (08:13-09:57)
- In a dynamic isolate pattern, the trusted worker can pass only specific bindings such as a restricted database query method or logger, set outbound networking to null, and avoid passing secrets into the sandbox. (15:24-18:44)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Run Agent-Written API Code Inside Programmable Sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Separate Agent Harnesses From Generated-Code Execution](separate-agent-harnesses-from-generated-code-execution.md)
- [Treat AI-generated code as untrusted code](treat-ai-generated-code-as-untrusted-code.md)
- [Choose isolates or containers by generated-code workload](choose-isolates-or-containers-by-generated-code-workload.md)

Sources:
- [Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare](../sources/20260419_8txf05vVVl4.md), 12:33-14:15, 17:50-18:17
- [Why, and how you need to sandbox AI-Generated Code? - Harshil Agrawal, Cloudflare](../sources/20260408_AHtGAgQ0Q_Q.md), 08:13-09:57, 15:24-18:44
