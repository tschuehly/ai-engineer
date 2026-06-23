# Settle Agent Payments Over HTTP With 402 and Checkout Protocols

Summary: Make agent payment programmatic over standard protocols instead of browser checkout. Tool calls are HTTP requests, so a server can answer with HTTP 402 ("payment required") plus an encoded payload of what, who, and how to pay; for richer e-commerce, a structured agent↔seller↔PSP exchange relays cart state each turn so purchase details are not mis-relayed.

Use when:
- Charging for ephemeral agent tool calls or API endpoints without pre-provisioned API keys.
- Building agent checkout where tax, quantity, shipping, and fulfillment details must be conveyed exactly.

Details:
- Tool calls are essentially HTTP requests, and HTTP requests should be payable; passing an API key is one option, but tool interactions can be ephemeral, so the Machine Payments Protocol (built with Tempo) uses an HTTP 402 status to signal payment-required, then supplies the credential. (08:54-09:33)
- Demo: a curl to a protected endpoint fails with a 402 and an encoded payload describing what is being bought, who is being paid, and the mechanism to pay; after paying, the response confirms the cost (a penny), the recipient, settlement in USD on the Tempo blockchain, and the transaction lands on-chain. (09:50-11:14)
- Not everything is an API call: e-commerce detail (tax, quantity restrictions, shipping) matters, and an agent proxy in the middle risks mis-relaying it into disputes and chargebacks, so the Agentic Commerce Protocol (built with OpenAI) standardizes a back-and-forth between agent, seller, and PSP. (11:18-12:12)
- In ACP the seller expresses a product catalog as JSON (images, descriptions, pricing) so the agent picks an item and initiates checkout instead of stumbling through links; each create-checkout / update-quantity / pick-shipping turn has the seller relay the latest cart state (line items, base price, applicable tax, fulfillment options) like a tool-call response, ending in payment via a shared payment token or otherwise. (12:16-14:33)
- The seller stays in control: it keeps the customer relationship and receives the signals and risk data needed to safely transact with agents, supporting crypto, cards, or any of hundreds of payment methods. (14:33-14:54)
- Stripe supports multiple networks (Base and Tempo): transaction data lives on the chain, and Stripe replicates a product view of it in its own system. (16:15-16:31)

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)
- [AI Monetization](../topics/ai-monetization.md)

Related concepts:
- [Expose Commerce Data Through Agent-Native Product APIs](expose-commerce-data-through-agent-native-product-apis.md)
- [Agentic Commerce Moves From Static Stores to Intent Infrastructure](agentic-commerce-moves-from-static-stores-to-intent-infrastructure.md)
- [Bound Agent Payments With Processor-Enforced Mandate Tokens](bound-agent-payments-with-processor-enforced-mandate-tokens.md)
- [Separate Non-Deterministic Discovery From Deterministic Payment Execution](separate-non-deterministic-discovery-from-deterministic-payment.md)

Sources:
- [Building safe Payment Infrastructure for the autonomous economy — Steve Kaliski, Stripe](../sources/20260606_KLSuFPj2ld0.md), 08:54-14:54, 16:15-16:31
