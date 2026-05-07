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

Related topics:
- [Security](../topics/security.md)
- [AI Monetization](../topics/ai-monetization.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Authorize High-Impact Agent Actions Transactionally](authorize-high-impact-agent-actions-transactionally.md)
- [Prevent AI Billing Surprises With Caps, Notifications, and Rate Limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Preserve Authorization Chain of Custody Across Agent Hops](preserve-authorization-chain-of-custody-across-agent-hops.md)

Sources:
- [Machines of Buying and Selling Grace - Adam Behrens, New Generation](../sources/20250723_zlZz0mDF2eg.md), 05:01-06:08, 17:33-18:01
