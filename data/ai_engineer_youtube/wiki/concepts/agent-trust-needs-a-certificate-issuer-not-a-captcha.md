# Agent Trust Needs a Certificate Issuer, Not a CAPTCHA

Summary: The web's bot defenses were built to answer "is this a human?", but the live question is now "is this a *trusted* agent acting for a real user?" CAPTCHAs cannot answer it, signed-request identity schemes answer only half of it, and the missing piece is an institution willing to vouch for agents and agent vendors — a role no one has taken.

Use when:
- Designing site access policy for a web that will carry both delegated user agents and abusive automation.
- Building an agent that needs to be *allowed* through defenses rather than to defeat them.
- Evaluating agent-identity proposals and asking what they actually establish.

Details:
- The reframed problem: "the web was built to stop bad bots, but now there's good agents and bad bots. How do we delineate between the two?" The taxonomy change is the point — the defense's original binary no longer maps onto the traffic. ([Paul Klein IV](../sources/20260814_GqoNrUz8hEU.md), 12:37-12:53)
- The incumbent tool is spent: "the CAPTCHA has been the tool in our tool chest for a very long time, but as we all know, CAPTCHAs are not as effective as we think against agents." The wiki's attacker-side account agrees in detail — Turnstile, an image challenge, and a drag puzzle each fell to ordinary inference cost, and only a round *timer* forced any architectural change. See [Treat CAPTCHA And Proof Of Work As Economic Friction](treat-captcha-and-proof-of-work-as-economic-friction.md). (12:53-12:59)
- Signed-identity work exists and is not sufficient by itself: "there's been a lot of cool frameworks and work done on things like [Web Bot Auth] and in more authenticated ways to say this is my agent, it's coming from me, and you can follow me along on the web, but I still don't think we've solved the issue yet." A signature establishes *who* is calling; it does not establish that the caller deserves access. (12:59-13:17)
- The missing institution, named by analogy: "there needs to be almost like a Verisign moment for web agents where who can be the certificate issuer in saying my agent is trusted [and] this agent vendor is trusted? Nobody's come out and done that yet." Note the two levels — the individual agent and the vendor behind it — which is what makes it a PKI-shaped problem rather than a per-request one. (13:17-13:39)
- The interim substitute being built is commercial rather than institutional: a platform requirement is "somebody who's going to go out and negotiate with the anti-bot providers of the world and say, we are the platform for trusted agents and we are the ones that can help broker the access for your agents as you use the web." A brokered allowlist between two vendors is a workable bridge and an explicit admission that no neutral issuer exists. (14:24-14:35)
- How this sits against the wiki's defender-side pages: [classifying bot traffic by intent and benefit](classify-ai-bot-traffic-by-intent-and-benefit.md) is the policy a site would apply *if* it could identify the caller, and [layering detection signals](layer-bot-detection-signals-instead-of-trusting-one-header.md) is what sites do in the absence of that identity. A certificate authority would convert a probabilistic detection problem into a credential-checking one — which also relocates the failure mode, since a compromised or over-permissive issuer becomes the whole ecosystem's weak point.
- Adjacent mechanism, not a replacement: [URL-based PKI identities for agents](authenticate-agents-with-url-based-pki-identities.md) covers proving control of an identifier in OAuth-style flows. That is the cryptographic substrate this concept says is already partly available; the gap is the trust root and the willingness of site defenses to honor it.

Related topics:
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Treat CAPTCHA And Proof Of Work As Economic Friction](treat-captcha-and-proof-of-work-as-economic-friction.md)
- [Classify AI Bot Traffic By Intent And Benefit](classify-ai-bot-traffic-by-intent-and-benefit.md)
- [Layer Bot Detection Signals Instead Of Trusting One Header](layer-bot-detection-signals-instead-of-trusting-one-header.md)
- [Authenticate Agents With URL-Based PKI Identities](authenticate-agents-with-url-based-pki-identities.md)
- [The Open Web Is Adversarial to Agent Access](the-open-web-is-adversarial-to-agent-access.md)
- [Design an Agent-First Signup and Login Flow](design-an-agent-first-signup-and-login-flow.md)

Sources:
- [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../sources/20260814_GqoNrUz8hEU.md), 12:37-13:39, 14:24-14:35
