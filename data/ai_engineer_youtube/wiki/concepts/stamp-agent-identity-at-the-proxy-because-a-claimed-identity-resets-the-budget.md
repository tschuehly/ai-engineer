# Stamp Agent Identity at the Proxy, Because a Claimed Identity Resets the Budget

Summary: Every other agent control — quotas, rate limits, approvals, trip wires, ownership, audit rows — is keyed on who the caller is. If the caller supplies that key, an agent that hits a limit can change the header and start over, and the limit was never a limit. Identity has to be stamped by a proxy that holds the real credentials and already knows who the agent is, and the stamp has to propagate to whatever the agent spawns.

Use when:
- Building any per-agent quota, budget, audit trail, or approval rule, before building the rule itself.
- An agent's actions currently appear in logs under a human's token or a shared service account.
- Deciding where session attribution comes from in a fleet where many agent sessions run concurrently.

Details:
- **The attack, which requires no cleverness.** If the agent can set its own identity in a header, then on hitting a limit "what's the easiest fix from an agent's point of view? It'll just change the header… instead of sachin, sachin2, and voila, you just have a fresh budget to work with. Now, in this case, you technically don't have a rate limit. You just have a suggestion." Note that this is not adversarial behavior — an agent optimizing to complete its task finds this the same way it finds any other workaround. ([Malhotra](../sources/20260822_rbjWzZK2LU0.md), 18:01-18:22)
- **The fix.** "With the proxy in the path, the agent never gets to say who it is. The proxy already knows. It's the thing that's holding real credentials and it stamps every call with the identity that it already knows, not the one that agent claims." Deployment shape: "every agent session has its own proxy running right next to it," and "every outbound call goes through the proxy." (16:42-16:59, 18:23-18:34)
- **The stamp propagates; the proxy does not follow.** "If the agent is trying to launch a bunch of jobs in a Kubernetes cluster, the proxy is not following it. What is following is the stamp itself… the cluster would write the stamp onto the job as a label, and every child job or anything that's happening afterwards simply inherits the same identity." This is the part that makes the model work for agents that spawn asynchronous work: the enforcement point is at the boundary, but the attribution travels into everything the boundary let through. (17:00-17:26)
- **One key, every control.** "Every safeguard that is there in the rest of our systems… whether it's ownership, whether it's quotas, rate limits, approvals, trip wires, whatever it is, they're all keyed on the same stamp and the agent never got to touch it." This is why the talk calls it the one rule: "identity has to come from the infrastructure, not from the request. If you get that one rule right, everything else is just tuning." (17:26-17:42, 19:22-19:32)
- **Provenance is taken away from the agent on purpose.** For audit rows on skip and unskip operations, "the agent itself is not responsible for writing the row or the audit trail itself. There is a proxy in the middle… responsible for stamping the caller's main identity on every call… the agent technically never holds the pen on its own provenance." An audit trail the agent writes is a record of what the agent chose to record. (08:07-08:24)
- **Per-session IDs fall out of it for free.** "Because the proxy is the one that is stamping, you also get this per session ID so that you're able to differentiate different sessions that are running… and see which one's overreacting or which one's not acting as it's supposed to be." Fleet-level debugging is a side effect of doing attribution correctly rather than a separate observability project. (18:35-18:47)
- **The agent gets its own identity, not the operator's.** In the flag-rollout workflow: "every action that the agent is taking is stamped with its own identity and not mine. And that stamp is basically what ties the whole thing together." This is the enforcement mechanism behind the wiki's existing position that agents should be [first-class users with identity, scopes, and audit trails](first-class-agent-users-need-identity-scopes-and-audit-trails.md) — that page describes the model, this one describes what makes it true at runtime rather than by convention. It also answers the incident that opened the talk, where the agent acted under the operator's token and so was indistinguishable from him in every downstream system. (14:18-14:25, 03:06-03:26)
- **What it does not cover, and the talk does not say.** No mechanism is given for how the proxy authenticates the agent process next to it, what stops a process from bypassing the proxy and reaching the API directly, or what happens when the proxy is unavailable. That last is the question the wiki's guardrail-as-dependency page insists on — [fail open or fail closed](enforce-deterministic-guardrails-around-sensitive-tool-calls.md) — and a per-session sidecar in the path of every outbound call is a dependency of exactly that kind. The bypass flag described elsewhere in the same talk detects "am I in an agent session" in band, which is the weaker form of the same problem this page solves.
- **Evidence limits.** The design is described, not measured. No incident is reported in which an agent actually rewrote its identity header, so the attack is stated as an obvious consequence rather than an observation; there is no report of proxy overhead, availability, or operational cost, and no description of how the label-inheritance is enforced on the cluster side rather than merely conventional.

Related topics:
- [Security](../topics/security.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Replace the Token's Boolean With a Budget on Four Dimensions](replace-the-token-boolean-with-a-budget-on-four-dimensions.md)
- [Rate-Limit Every Write With a Ceiling That Refills](rate-limit-every-write-with-a-ceiling-that-refills.md)
- [Keep Policy in Text for Intent and in Infrastructure for Bounds](keep-policy-in-text-for-intent-and-in-infrastructure-for-bounds.md)
- [First-Class Agent Users Need Identity, Scopes, and Audit Trails](first-class-agent-users-need-identity-scopes-and-audit-trails.md)
- [Identify the Human Subject Behind Agent Actions](identify-the-human-subject-behind-agent-actions.md)
- [Preserve Authorization Chain of Custody Across Agent Hops](preserve-authorization-chain-of-custody-across-agent-hops.md)
- [An Audit Trail Is a Chain of Evidence, Not a Developer Log](an-audit-trail-is-a-chain-of-evidence-not-a-developer-log.md)
- [Decrypt Agent Credentials Only at Tool Execution Time](decrypt-agent-credentials-only-at-tool-execution-time.md)

Sources:
- [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../sources/20260822_rbjWzZK2LU0.md), 08:07-08:24, 14:18-14:25, 16:42-19:32
