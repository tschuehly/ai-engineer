# Delegate Agentic Commerce Transactions With Explicit Payment Authority

Summary: When software buys on a user's behalf, checkout needs explicit authority design rather than assuming a human clicked the final button. Practical bridges include virtual cards, delegated authentication to a user's existing card, and tightly bounded agent-owned spending instruments.

Use when:
- Designing agentic checkout, procurement, travel booking, purchasing, or payment workflows.
- Evaluating whether an agent should hold payment credentials, request step-up approval, or use delegated payment authority.

Details:
- Behrens identifies the first agentic commerce challenge as software clicking the buy button during checkout. (05:01-05:25)
- One existing bridge is for the software provider or chat product to check out with the user, issue a virtual card, and buy from the merchant on the user's behalf. (05:32-05:52)
- A cleaner pattern in the talk is delegated authentication, where the agent can use the user's actual credit card and complete the merchant checkout flow for the user. (05:53-06:08)
- In Q&A, Behrens says stablecoins and crypto have a conceptual case as AI-native payment rails because agents can live inside wallets, but credit cards are the practical consumer bridge today. (17:33-17:54)
- Another possible pattern is for the agent itself to own a persistent card or spending instrument that the user tops up, which makes spend limits and authorization boundaries part of the agent product. (17:54-18:01)
- **The spend-side primitive named by a billing vendor: give the agent its own wallet.** Garvin's answer to "agents can run away with spend" is authority scoped to the agent identity — "having agents have a wallet that only they can spend from and having controls at that level" — rather than a limit on the account the agent is acting within. The consequence is a containment property: a looping or compromised agent exhausts an allocation that was sized for it, and the failure is visible as a depleted wallet rather than as a surprise on the organization's invoice. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 03:13-03:37)
- **What each surface actually accepts, and the four questions the delegated case needs answered.** As of Prio's talk the bridges are narrow and surface-specific: "in ChatGPT, payments only happen through a shared payment token right now, and Gemini UCP, the payments are only being accepted through Google Pay." AP2, an extension of UCP, is the specification written for delegated authority, and its content is four questions — "who authorized the agent, what exactly can it buy, and what's the max amount that should be able to haggle with, maybe, and then the revocation URL, and the user consent proof." Revocation and consent proof are the two the virtual-card and delegated-authentication bridges on this page have no answer for. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 10:03-10:40)

Related topics:
- [Security](../topics/security.md)
- [AI Monetization](../topics/ai-monetization.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Bound Agent Payments With Processor-Enforced Mandate Tokens](bound-agent-payments-with-processor-enforced-mandate-tokens.md)
- [Authorize High-Impact Agent Actions Transactionally](authorize-high-impact-agent-actions-transactionally.md)
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Preserve Authorization Chain of Custody Across Agent Hops](preserve-authorization-chain-of-custody-across-agent-hops.md)
- [Separate Agent as Product, Agent as Buyer, and Agent as User](separate-agent-as-product-buyer-and-user.md)
- [Model Agentic Checkout as an Explicit Session State Machine](model-agentic-checkout-as-an-explicit-session-state-machine.md)

Sources:
- [Machines of Buying and Selling Grace - Adam Behrens, New Generation](../sources/20250723_zlZz0mDF2eg.md), 05:01-06:08, 17:33-18:01
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 03:13-03:37
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 10:03-10:40
