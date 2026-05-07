# Treat Code-Executing Agents as RCE-Risk Surfaces

Summary: When an agent can decide to write and execute code, its useful capability resembles a remote-code-execution surface. Security design should start from that risk rather than from the model's helpful intent.

Use when:
- Giving an agent shell, local code execution, package installation, or filesystem mutation.
- Reviewing whether agent autonomy is being evaluated only by capability and not by the operations it can perform.

Details:
- The talk argues that every agent is moving toward becoming a code-executing agent because code helps models achieve objectives efficiently, including non-SWE tasks such as OCR or image cropping. 01:05-02:29
- Simpler agent designs can let the reasoning model choose when to call tools, write code, and run code instead of relying on complex hand-coded routing loops. 02:29-03:09
- Security teams should treat that power like RCE: the system is intentionally letting a model write and execute programs, so prompt injection, exfiltration, mistakes, vulnerable code, malicious packages, privilege escalation, and sandbox escape are core risks. 03:09-03:55

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Security](../topics/security.md)

Related concepts:
- [Treat AI-generated code as untrusted code](treat-ai-generated-code-as-untrusted-code.md)
- [Layer agent permissions across model behavior, harness parsing, and sandboxing](layer-agent-permissions-across-model-behavior-harness-parsing-and-sandboxing.md)
- [Unified Coding-Agent Harnesses Combine Models, Tools, Environments, and Safety](unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md)

Sources:
- [OpenAI on Securing Code-Executing AI Agents - Fouad Matin (Codex, Agent Robustness)](../sources/20250730_w7IMuYsBNr8.md), 01:05-03:55
