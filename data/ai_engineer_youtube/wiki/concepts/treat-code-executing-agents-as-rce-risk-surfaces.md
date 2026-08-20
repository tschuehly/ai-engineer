# Treat Code-Executing Agents as RCE-Risk Surfaces

Summary: When an agent can decide to write and execute code, its useful capability resembles a remote-code-execution surface. Security design should start from that risk rather than from the model's helpful intent.

Use when:
- Giving an agent shell, local code execution, package installation, or filesystem mutation.
- Reviewing whether agent autonomy is being evaluated only by capability and not by the operations it can perform.

Details:
- The talk argues that every agent is moving toward becoming a code-executing agent because code helps models achieve objectives efficiently, including non-SWE tasks such as OCR or image cropping. 01:05-02:29
- Simpler agent designs can let the reasoning model choose when to call tools, write code, and run code instead of relying on complex hand-coded routing loops. 02:29-03:09
- Security teams should treat that power like RCE: the system is intentionally letting a model write and execute programs, so prompt injection, exfiltration, mistakes, vulnerable code, malicious packages, privilege escalation, and sandbox escape are core risks. 03:09-03:55
- **The same remote-command-execution outcome, reached without the agent.** A poisoned LiteLLM release installed "a credential harvester that would steal your API keys, your SSH keys, your crypto keys, and also install a backdoor that lets them do remote command execution." No prompt injection, no model behavior, no tool call — just a dependency the AI stack installs, executing at install time as the developer or CI runner. The sandbox boundaries this page argues for are drawn around the agent process, and a package install sits outside all of them. Worth checking that whatever isolation you built for agent-run code also covers `pip install` and `npm install` on the same host. See [An AI-Infrastructure Package Is a High-Yield Credential Target](an-ai-infrastructure-package-is-a-high-yield-credential-target.md). ([Rizwan](../sources/20260807_CoEIs6Xm8m8.md), 04:17-05:19)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Security](../topics/security.md)

Related concepts:
- [Treat AI-generated code as untrusted code](treat-ai-generated-code-as-untrusted-code.md)
- [Layer agent permissions across model behavior, harness parsing, and sandboxing](layer-agent-permissions-across-model-behavior-harness-parsing-and-sandboxing.md)
- [Unified Coding-Agent Harnesses Combine Models, Tools, Environments, and Safety](unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md)
- [An AI-Infrastructure Package Is a High-Yield Credential Target](an-ai-infrastructure-package-is-a-high-yield-credential-target.md)

Sources:
- [OpenAI on Securing Code-Executing AI Agents - Fouad Matin (Codex, Agent Robustness)](../sources/20250730_w7IMuYsBNr8.md), 01:05-03:55
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 04:17-05:19
