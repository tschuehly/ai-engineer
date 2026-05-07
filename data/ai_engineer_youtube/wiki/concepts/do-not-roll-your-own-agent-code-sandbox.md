# Do Not Roll Your Own Agent Code Sandbox

Summary: Agent code execution is a high-risk infrastructure boundary because small file read/write permissions can become arbitrary code execution, sandbox escape, lateral movement, or credential theft.

Use when:
- Adding code execution, calculators, generated scripts, or notebook-like tools to an agent.
- Deciding whether to build a custom sandbox or use a hardened sandbox provider.

Details:
- Many agents generate code on demand, and the tool path often reaches another container where arbitrary compute is available. 08:13-08:43
- A code tool that looked constrained to Python file write and file read operations still allowed filesystem exploration, discovery of `app.py`, and inspection of hidden write/execute endpoints. 09:21-10:12
- Because security checks lived in files the tool could overwrite, attackers could remove protections and gain arbitrary execution inside the container. 10:17-10:48
- Once inside a container, attackers can discover metadata services, service endpoints, network resources, service tokens, project names, token scopes, and customer data; this turns code execution into lateral infrastructure movement. 10:48-11:52
- The recommended posture is to avoid custom code sandboxes and use hardened sandbox products with observability, fast startup, and agent-friendly integration surfaces such as MCP. 11:54-12:24

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Run agent-written API code inside programmable sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Capability-based sandboxes start with no authority](capability-based-sandboxes-start-with-no-authority.md)
- [Separate agent harnesses from generated-code execution](separate-agent-harnesses-from-generated-code-execution.md)

Sources:
- [How we hacked YC Spring 2025 batch's AI agents - Rene Brandel, Casco](../sources/20250730_kv-QAuKWllQ.md), 08:13-12:24
