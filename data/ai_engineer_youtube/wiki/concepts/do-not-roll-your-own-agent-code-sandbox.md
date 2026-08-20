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
- **What "buying it" actually covers, and what it does not.** Anthropic frames the decision as a checklist of six things production forces on you — hosting and scaling, session management, filesystem, execution isolation, credentials, observability — where execution isolation is one item among six that a platform answers together ([Decide the Agent Buy Boundary With Six Production Questions](decide-the-agent-buy-boundary-with-six-production-questions.md)). The useful correction to "just use a sandbox product" is in that list: a team that outsources isolation alone still owns session durability and credential handling, and those are the ones a prototype has never had. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 04:30-05:14)
- **Sandbox lifecycle is a design decision, not just a procurement one.** Anthropic ran the loop and the container as one unit first and found that the container blocked first token and that either half dying killed the run; splitting them let a dead sandbox be replaced mid-run — "the brain could just spin up a new sandbox and retry and then continue as it left off" ([Decouple the Agent Loop From the Tool Execution Environment](decouple-the-agent-loop-from-the-tool-execution-environment.md)). Whichever sandbox you buy, that boundary is yours to get right. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 11:16-12:52)
- **The case where the advice does not apply, from a team that hit it.** Codex runs on the user's own machine, so there is no container to buy: it uses Seatbelt on macOS, Bubblewrap on Linux, and on Windows — where no comparable primitive existed — OpenAI wrote its own ([Sandbox Primitives Are Per Operating System](sandbox-primitives-are-per-operating-system.md)). This does not overturn the guidance so much as scope it: "use a hardened sandbox product" presumes execution can move off the user's machine, and where it cannot, the choice is between an OS primitive, a custom sandbox, and no isolation at all. Reading it the other way round is the practical version — if you are contemplating writing a sandbox, first check whether the execution could be remote instead. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 11:06-11:57)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Run agent-written API code inside programmable sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Capability-based sandboxes start with no authority](capability-based-sandboxes-start-with-no-authority.md)
- [Separate agent harnesses from generated-code execution](separate-agent-harnesses-from-generated-code-execution.md)
- [Decide the Agent Buy Boundary With Six Production Questions](decide-the-agent-buy-boundary-with-six-production-questions.md)
- [Decouple the Agent Loop From the Tool Execution Environment](decouple-the-agent-loop-from-the-tool-execution-environment.md)
- [Sandbox Primitives Are Per Operating System](sandbox-primitives-are-per-operating-system.md)

Sources:
- [How we hacked YC Spring 2025 batch's AI agents - Rene Brandel, Casco](../sources/20250730_kv-QAuKWllQ.md), 08:13-12:24
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 04:30-05:14, 11:16-12:52
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 11:06-11:57
