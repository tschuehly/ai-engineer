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
- **Caveat: domain and HTTP-method allow-lists only cover the HTTP path.** Deno's threat model is an agent that "can just spawn [psql] as a subprocess and start connecting to services" over a non-HTTP protocol, tunneling to a VPC-internal Postgres through an EKS endpoint — traffic an HTTP-layer rule never parses. The allow-list is still the right first control where the agent's egress is HTTP, but for an agent with subprocess access to production systems the enforcement point has to sit [below HTTP, parsing the wire protocol](enforce-agent-egress-policy-below-the-http-layer.md). ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 04:45-06:33, 07:40-09:58)

- **The reason to bother is stated as exfiltration, and the practical form is per-project or per-ticket scope with a prompt on anything new.** Superconductor frames egress control as the direction people forget: "it's not just, 'Hey, make sure they don't have the credentials that they shouldn't have.' It's also make sure they can't exfiltrate your code or your projects or your secrets or your content to somewhere they shouldn't be able to." Their sandbox names allowed and disallowed destinations and prompts on a new one — the given example is benign ("maybe you're trying to integrate a new vendor and you need documentation"), which is exactly why a prompt-on-new-destination flow trains toward approval; the same talk criticizes interactive approval as one of two bad camps minutes earlier. The stated goal is "we're not going to leak a bunch of important data by running agents in YOLO mode," which is the honest scope: an allowlist is what makes unattended execution tolerable, not what makes it safe. ([Arjun Singh](../sources/20260809_OL7kfezynJM.md), 11:24-12:13)
- **The per-automation form: the destination list is derived from the job, not from the organization.** GitHub Next's agentic workflows declare reachable destinations in each workflow's own front matter, and the list for a dependency-upgrade job is exactly what that job needs — "the NPM ecosystem cuz it's got to check for what's new, GitHub, and of course the Astro docs which I specified in my original prompt" — with the counter-example named directly: "it's not allowed to just go to bitcoin.com." Scoping the allow-list to the standing job rather than to the agent or the team is what keeps it tight enough to be meaningful, and it survives review because the justification for each entry is visible one paragraph above it in the same document. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 07:50-08:16)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)

Related concepts:
- [Browser agents sit in the prompt-injection lethal trifecta](browser-agents-sit-in-the-prompt-injection-lethal-trifecta.md)
- [LLM guardrails need checkpoints at every untrusted boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)
- [A Developer Laptop Is an Ambient-Credential Surface](a-developer-laptop-is-an-ambient-credential-surface.md)
- [Bound What an Unattended Automation May Emit, Including Emitting Nothing](bound-what-an-unattended-automation-may-emit.md)

Sources:
- [OpenAI on Securing Code-Executing AI Agents - Fouad Matin (Codex, Agent Robustness)](../sources/20250730_w7IMuYsBNr8.md), 05:02-09:47
- [Security Firewall for Agents — Ryan Dahl, Deno](../sources/20260817_MkRYPFIMCSA.md), 04:45-09:58
- [Multiplayer agentic engineering — Arjun Singh, Superconductor](../sources/20260809_OL7kfezynJM.md), 11:24-12:13
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 07:50-08:16
