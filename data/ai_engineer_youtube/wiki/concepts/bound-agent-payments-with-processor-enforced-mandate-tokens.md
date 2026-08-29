# Bound Agent Payments With Processor-Enforced Mandate Tokens

Summary: Instead of handing an agent or seller a raw card number, share a payment token that carries a mandate — currency, amount, time window, and a specific seller — that the payment processor (not the seller) enforces. This bounds the blast radius even when the agent was duped by a domain or mis-parsed the amount.

Use when:
- An agent needs to pay a seller but should not hold or transmit unrestricted payment credentials.
- You want spend limits enforced independently of whether the agent or the seller behaves correctly.

Details:
- Stripe's Shared Payment Tokens let an agent collect a payment credential and share it with a seller across hundreds of payment-method types, encoding a "mandate" (like a smart contract) that limits how that credential can be used by a particular seller. (04:51-05:32)
- Limits can be scoped to specific currencies, amounts, time windows, and one seller — so even if the agent landed on a look-alike domain or mis-parsed the amount, the mandate still caps what can be charged. (05:32-05:52)
- Enforcement lives at the processor, not the seller: in the demo, a $25 / 30-day / seller-scoped token rejects a $50 charge because the requested amount exceeds the mandate; lowering the charge within the limit succeeds. (06:38-08:39)
- The seller is not hidden from the transaction: brand, last-four, and credit type still flow through so the seller can run its existing risk and fraud analysis — the goal is a minimized blast radius, not secrecy. (07:31-08:02)
- The mechanism is scoped-to-seller, processor-enforced, payment-method-agnostic, and auditable. (05:54-06:01)
- Recurring or subscription spend works like giving a business a card permitted to spend a periodic amount on the same credential, modeled on an OAuth-style access/refresh flow for subsequent usage; for larger budgets you raise the number or mint many seller-scoped tokens. (16:37-17:30)
- Stripe Projects is described as a product built on shared payment tokens plus product expression and the recurring/monthly layer. (17:37-17:58)
- **The same primitive arriving as an open specification, with revocation added.** The AP2 mandate rendered to a user in Prio's demo carries "the max amount…, the currency…," a revocation path ("if you want to revoke it, you can"), and "it's also a single time usage." Against Stripe's shared payment tokens the field set is close — amount, currency, scope, time — with one addition worth noting: an explicit revocation URL, so authority can be withdrawn after issuance rather than only expiring. AP2 is also the layer Prio flags as least settled: "what's still forming though is AP2 and actual usage of it." ([Prio](../sources/20260827_G7cgLjZtmMU.md), 10:14-10:40, 14:37-14:52, 18:44-19:08)

Related topics:
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)
- [AI Monetization](../topics/ai-monetization.md)

Related concepts:
- [Delegate Agentic Commerce Transactions With Explicit Payment Authority](delegate-agentic-commerce-transactions-with-explicit-payment-authority.md)
- [Authorize High-Impact Agent Actions Transactionally](authorize-high-impact-agent-actions-transactionally.md)
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Separate Non-Deterministic Discovery From Deterministic Payment Execution](separate-non-deterministic-discovery-from-deterministic-payment.md)
- [Map the Agentic Commerce Protocol Stack by Layer](map-the-agentic-commerce-protocol-stack-by-layer.md)

Sources:
- [Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe](../sources/20260606_KLSuFPj2ld0.md), 04:51-08:39, 16:37-17:58
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 10:14-10:40, 14:37-14:52, 18:44-19:08
