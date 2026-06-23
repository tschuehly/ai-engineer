# Move Agent Access Control to the Network Layer So the Sandbox Holds No Credential

Summary: "Sandbox" conflates two separable problems — execution isolation (the boundary) and access control (the permissions). You can perfectly isolate a runtime and still hand the agent a credential it can exfiltrate, misuse, or escalate over a long loop. Moving authentication and authorization to the network layer, so every connection carries verified identity, lets the agent in the box hold a placeholder instead of a real key — there is nothing to steal and revocation can't be routed around.

Use when:
- Designing how an agent or sandboxed coding bot gets access to LLM providers, internal APIs, or MCP servers.
- Reviewing whether "isolating the runtime" has actually removed the credential the agent is holding.

Details:
- The framing: a sandbox is a boundary (a thing in, a thing out) plus a set of permissions/identity. The VM-vs-container debate is only about the boundary; the credential problem is the other, usually-ignored half. (00:46-01:46)
- Both common permission patterns put the credential *inside* the box: API keys (you pay full price; doesn't separate authN from authZ — "here's a key, it lets you have access"; even a synthetic key gets misused because "models are very clever at doing things with keys they shouldn't, especially if you run them in a loop for a very long time"), and OAuth/OIDC (cheaper and handles real permissions, but the agent still logs in and the account sits inside the box). Either way "the agent has access to its own permissions." (01:52-03:18)
- The network-layer answer: WireGuard gives keys to every node on a network, and Tailscale layers verified identity on top. Each direct connection (container, GPU server, laptop, phone) carries the logged-in user, SCIM-synced groups, or a tag / set of tags (e.g. "the PR review bot for this project"). You can both govern network access by that identity ("you can't even talk to something if you don't have a certain set of permissions") and give the receiving side the full identity — replacing "IP address plus an API key" with a connection that *is* an identity. (03:18-05:30)
- The payoff for the sandbox: with a gateway (Aperture) holding the only real provider key, the sandboxed agent gets a placeholder — a literal dash — instead of a key. "There's actually no key... no key to accidentally exfil or share or do something with." (05:42-07:10)
- A GitHub Actions runner gets access via GitHub's federated OIDC: on spin-up it joins the tailnet and receives a tag, and "that tag is what determines what it is able to do." Ephemeral compute is authorized by attested identity rather than a shipped secret. (06:05-06:55)
- Network-layer revocation can't be worked around: "the moment you say no," the agent can't fail over to another endpoint because there is no working credential — "it's just a dash," not "the key no longer works, let me try this other thing... I would want to be very helpful here." Contrast with a still-valid key that an over-helpful model reroutes. (11:13-11:46)
- tsnet (open-source Go library) exposes the same identity primitives so teams can build internal-only MCP servers or API endpoints that read "who made this request?" and force that identity downstream — without "thinking about OAuth or opening it up to everybody." Aperture was deliberately built only on public primitives so it is reproducible. (15:35-16:55)
- Permissions configure in two places: a gateway "grants" surface (model access, quotas, MCP access, hooks, roles) and the Tailscale ACL/policy file; "application capabilities" attach arbitrary control-plane-guaranteed metadata to an identity, editable as JSON for GitOps. (17:03-18:46)

Related topics:
- [Security](../topics/security.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Make the LLM Gateway the Agent Observability Chokepoint](make-the-llm-gateway-the-agent-observability-chokepoint.md)
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)
- [Treat Agents As Users For Authorization](treat-agents-as-users-for-authorization.md)
- [Authenticate Agents With URL-Based PKI Identities](authenticate-agents-with-url-based-pki-identities.md)
- [Server-Side Request Forgery Exfiltrates Agent Credentials](server-side-request-forgery-exfiltrates-agent-credentials.md)

Sources:
- [What if the network was the sandbox? — Remy Guercio, Tailscale](../sources/20260601_BM2JX9hqsVQ.md), 00:46-07:10, 11:13-11:46, 15:35-18:46
