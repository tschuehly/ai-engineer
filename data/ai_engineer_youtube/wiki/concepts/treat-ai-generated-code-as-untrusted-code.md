# Treat AI-generated code as untrusted code

Summary: AI-generated code should be handled like unaudited code from an anonymous internet source, because hallucination, over-helpfulness, and prompt injection can all produce dangerous behavior without the model being intentionally malicious.

Use when:
- Designing any product feature that executes code written by an LLM or agent.
- Reviewing whether a generated-code workflow is relying on model intent instead of runtime boundaries.

Details:
- Running generated code directly in an application gives it the same filesystem, environment variable, network, database, and API-key access as the host process unless the runtime removes those capabilities. (01:45-02:59, 06:01-06:48)
- The baseline failure mode is not only malicious code: hallucinated imports, recursive functions without base cases, and infinite loops can crash services or consume compute. (03:08-04:01)
- Over-helpful generated code can read environment variables or secrets while trying to configure a database connection; the resulting sensitive-data exposure is still a security failure even when the model had no hostile intent. (04:01-04:54)
- Direct and indirect prompt injection can steer generated code toward exfiltration when user input, web pages, or documents become part of the prompt context. (04:57-05:58)
- A practical generated-code checklist includes default-deny network access, explicit capabilities, per-user sandboxing, resource limits, secrets outside the sandbox, cleanup, audit logs, and validation before execution. (33:00-35:24)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Run Agent-Written API Code Inside Programmable Sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)
- [LLM Attack Surfaces Span Prompts, Context, Retrieval, Tools, and Actions](llm-attack-surfaces-span-prompts-context-retrieval-tools-and-actions.md)

Sources:
- [Why, and how you need to sandbox AI-Generated Code? - Harshil Agrawal, Cloudflare](../sources/20260408_AHtGAgQ0Q_Q.md), 01:45-06:48, 33:00-35:24
