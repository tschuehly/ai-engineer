# Design an Agent-First Signup and Login Flow

Summary: Once a browser agent can operate a site, the binding constraint stops being capability and becomes access: how it logs in on the user's behalf. Software vendors should design the agent's signup and login path deliberately, because agents will use the product either way — and the three improvised paradigms in use today (share the human's password, run a service account, gate on human approval) each trade security against friction.

Use when:
- Building a SaaS product and deciding whether agents get a supported entry path or are left to reuse human credentials.
- Planning an enterprise computer-use deployment and finding that the blocker is credentials, not the model.
- Choosing between password sharing, service accounts, and delegated authorization for an agent that must reach an internal system.

Details:
- The gating claim, stated plainly: "the biggest gate to building agents that actually can work in prod is going to be the systems it has access to. And authentication is something that needs to be solved in our industry to make this possible." Klein ranks it above the harness problems that make up the rest of his talk — "authentication for agents is the next thing to be solved once you solve the harnessing capability problems." ([Paul Klein IV](../sources/20260814_GqoNrUz8hEU.md), 11:45-12:20)
- The three paradigms currently in use, with the cost he attaches to each:
  - **Give the agent your password** — "doing that securely can be very challenging." It also destroys attribution, since every action lands in the audit log as the human.
  - **Create a service account with limited access** — the running cost is permission churn: "you constantly have to give it new permissions."
  - **Human-in-the-loop approval on sensitive actions** — "doing that securely where you can have a human [in the] loop approve certain actions on a website is going to be a major challenge for unlocking computer use for the enterprise." (11:39-12:03)
- A discovery-layer proposal exists: WorkOS shipped an `auth.md`-style convention (name garbled in the captions; capability described clearly) as "a new way for your agent that goes to a website to find how to sign up on that website and get its own accounts." This is the authentication analogue of `llms.txt` — a published, machine-findable answer to "how do I get an identity here?" rather than an agent guessing at a signup form. (12:20-12:31)
- The advice to builders is framed as inevitability, not opportunity: "if you're building software now, you should think about what is my agent-first sign up and login flow look like because agents are going to be using your software whether you like it or not. It's best to let them use it securely." The alternative to a designed path is not "no agents"; it is agents using the human path badly. (12:31-12:37)
- Where this meets the wiki's existing authorization material: the *third-party site* case here is harder than the enterprise-integration case those pages cover. [Treating agents as users for authorization](treat-agents-as-users-for-authorization.md) and [first-class agent users with identity, scopes, and audit trails](first-class-agent-users-need-identity-scopes-and-audit-trails.md) assume the platform chose to model agents; [cross-app access](cross-app-access-centralizes-mcp-authentication-through-the-identity-provider.md) and [scoped OAuth token flows](move-production-mcp-from-api-keys-to-scoped-oauth-token-flows.md) assume an identity provider both sides accept. A browser agent on an arbitrary website has neither, which is why password sharing persists despite being the worst option.
- Pairs with the trust problem rather than solving it: an agent getting its own account answers "can it get in?", not "should this site let it in" — see [Agent Trust Needs a Certificate Issuer, Not a CAPTCHA](agent-trust-needs-a-certificate-issuer-not-a-captcha.md). Klein names both as the two unsolved halves of the agent-facing web.

Related topics:
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Agent Trust Needs a Certificate Issuer, Not a CAPTCHA](agent-trust-needs-a-certificate-issuer-not-a-captcha.md)
- [Treat Agents As Users For Authorization](treat-agents-as-users-for-authorization.md)
- [First-Class Agent Users Need Identity, Scopes, and Audit Trails](first-class-agent-users-need-identity-scopes-and-audit-trails.md)
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Authorization Propagation Is the Hard Part of Enterprise Agent Workloads](authorization-propagation-is-the-hard-part-of-enterprise-agent-workloads.md)

Sources:
- [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../sources/20260814_GqoNrUz8hEU.md), 11:25-12:37
