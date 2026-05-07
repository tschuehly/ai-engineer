# Server-Side Request Forgery Exfiltrates Agent Credentials

Summary: Agent tools that fetch URLs, repositories, schemas, or other remote resources can become SSRF channels when user-controllable strings make the server call attacker-controlled endpoints with internal credentials attached.

Use when:
- Reviewing tools that pull schemas, files, URLs, Git repositories, or other remote resources.
- Threat-modeling agent tools that run from inside a VPC or privileged backend.

Details:
- Casco frames SSRF as getting a tool to call an endpoint the service did not intend the attacker to call, then extracting information through that workflow. 12:31-13:00
- In the example, a database-creation agent pulled a database schema from a private GitHub repository, implying that the backend request carried Git credentials. 13:03-13:28
- Because the repository location was just a string, the attacker could point it at an attacker-controlled Git endpoint and observe the credentials attached to the outbound request. 13:28-13:46
- Those leaked Git credentials could then be used to download the private codebase. 13:46-13:53
- SSRF defenses for agents need input/output sanitization and explicit constraints on which internal or external endpoints tools may call. 14:10-14:41

Related topics:
- [Security](../topics/security.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [LLM guardrails need checkpoints at every untrusted boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Constrain sensitive file access with purpose-built tools](constrain-sensitive-file-access-with-purpose-built-tools.md)
- [Run agent-written API code inside programmable sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)

Sources:
- [How we hacked YC Spring 2025 batch's AI agents - Rene Brandel, Casco](../sources/20250730_kv-QAuKWllQ.md), 12:31-14:41
