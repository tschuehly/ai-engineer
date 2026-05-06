# Layer agent permissions across model behavior, harness parsing, and sandboxing

Summary: Powerful agent tools need multiple defensive layers because no single prompt, model policy, or sandbox catches every failure. A Bash-enabled harness should combine model behavior, runtime permissioning, command parsing, and network/filesystem sandboxing.

Use when:
- Reviewing whether an agent should receive shell or filesystem access.
- Designing guardrails for an agent that can execute code, mutate files, or touch the network.

Details:
- The source frames guardrails for Bash access as layered defenses: model alignment, harness-level permissioning and prompting, command parsing, and sandboxing. 12:42-14:19
- The harness can parse Bash with an AST-style pass so it can inspect what a command is actually doing before execution. 13:55-14:14
- Sandboxing should limit what a compromised agent can do, including network requests and filesystem operations outside the intended workspace. 14:17-14:36
- The source names the dangerous combination as code execution, filesystem mutation, and code or data exfiltration, making broad shell access a security architecture problem rather than only a model behavior problem. 14:36-14:49

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Capability-based sandboxes start with no authority](capability-based-sandboxes-start-with-no-authority.md)
- [Treat AI-generated code as untrusted code](treat-ai-generated-code-as-untrusted-code.md)
- [LLM guardrails need checkpoints at every untrusted boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Constrain sensitive file access with purpose-built tools](constrain-sensitive-file-access-with-purpose-built-tools.md)

Sources:
- [Claude Agent SDK [Full Workshop] - Thariq Shihipar, Anthropic](../sources/20260105_TqC1qOfiVcQ.md), 12:42-14:49
