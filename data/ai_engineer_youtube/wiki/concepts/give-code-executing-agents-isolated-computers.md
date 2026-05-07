# Give Code-Executing Agents Isolated Computers

Summary: Code-executing agents should run in a dedicated container, VM, or OS sandbox and return reviewable artifacts rather than sharing the user's privileged machine environment.

Use when:
- Choosing where a coding agent should run commands, install dependencies, or edit files.
- Designing local and hosted Codex-style execution environments.

Details:
- OpenHands runs agents inside Docker containers by default so autonomous shell work is separated from the user's workstation and cannot delete or mutate the user's home directory. 06:44-07:05
- Container isolation does not solve external authority; when agents receive GitHub tokens, AWS access, or other third-party credentials, those credentials should be tightly scoped and least-privilege. 07:08-07:23
- The talk recommends giving the agent "its own computer" as the first safeguard, especially for local runs. Codex in ChatGPT is described as spinning up a fully isolated container and producing a PR at the end. 04:25-04:41
- Local Codex CLI-style agents still need appropriate sandboxing, such as containerization, app-level sandboxing, or OS-level sandboxing. 04:41-05:02
- Codex CLI examples include macOS Seatbelt policies and Linux sandboxing built with seccomp and Landlock to support unprivileged execution and reduce privilege-escalation risk. 06:09-07:42
- The isolated environment still needs the right dependencies and task access; isolation should not prevent validation, but it should limit second-order consequences outside the intended workspace. 06:09-08:24

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)

Related concepts:
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)
- [Run Agent-Written API Code Inside Programmable Sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Do Not Roll Your Own Agent Code Sandbox](do-not-roll-your-own-agent-code-sandbox.md)

Sources:
- [Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands](../sources/20250725_o_hhkJtlbSs.md), 06:44-07:23
- [OpenAI on Securing Code-Executing AI Agents - Fouad Matin (Codex, Agent Robustness)](../sources/20250730_w7IMuYsBNr8.md), 04:25-08:24
