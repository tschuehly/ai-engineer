# Restrict Agent Internet Access With Allowlists

Summary: Network access is one of the highest-risk paths for prompt injection and data exfiltration in code-executing agents. Disable it when possible, and when it is needed, constrain domains, commands, and HTTP methods explicitly.

Use when:
- Letting agents read web docs, fetch GitHub issues, install packages, or call external APIs.
- Deciding between full-auto agent modes and interactive approval for networked actions.

Details:
- The talk identifies internet access as a high-probability vector for prompt injection and exfiltration because the agent may read untrusted docs, GitHub issues, or comments before acting inside a trusted code-execution loop. 05:02-05:31
- Codex CLI full-auto mode is described as allowing read/write only within the current directory and permitting network calls only for commands the user auto-approves. 07:53-08:24
- Hosted Codex network access can be enabled with configurable allowlists and HTTP method controls, giving teams both a maximum-security mode and a more flexible mode for docs or package installation. 08:24-08:56
- In the GitHub issue example, hostile issue text asks the agent to post repository data to a random URL; model-level detection can flag suspicion, but the decisive control is a system policy that prevents the outbound call. 09:00-09:47

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)

Related concepts:
- [Browser agents sit in the prompt-injection lethal trifecta](browser-agents-sit-in-the-prompt-injection-lethal-trifecta.md)
- [LLM guardrails need checkpoints at every untrusted boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)

Sources:
- [OpenAI on Securing Code-Executing AI Agents - Fouad Matin (Codex, Agent Robustness)](../sources/20250730_w7IMuYsBNr8.md), 05:02-09:47
