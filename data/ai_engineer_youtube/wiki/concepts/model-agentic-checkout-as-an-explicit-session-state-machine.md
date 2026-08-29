# Model Agentic Checkout as an Explicit Session State Machine

Summary: Agentic checkout specs expose the cart as a named session state rather than as an implied sequence of calls: not-ready-for-payment, ready-for-payment, completed, with payment-method selection as the transition that arms the session. Because ACP and UCP share that shape and differ mainly in schema, one internal state machine plus per-spec serializers is a cheaper implementation than two parallel integrations.

Use when:
- Implementing ACP, UCP, or any agent-facing checkout, booking, or multi-turn transaction API.
- Deciding how much of a transaction's progress an agent should have to infer versus be told.
- Planning to support more than one competing commerce specification.

Details:
- The contract: "the checkout APIs will have state, and the three different states are not ready for payment, ready for payment, and then completed." ([Prio](../sources/20260827_G7cgLjZtmMU.md), 13:04-13:26)
- The transition is explicit and separates cart assembly from payment authorization: "it's added to cart, but it's not ready for payment. I have to pick what I want to pay with. I say credit card and debit card. And this is where I issue the AP2 token… and then it went from ready for payment to complete." Adding items does not arm the session; naming a payment instrument does. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 13:26-14:07)
- Why a named state beats an inferred one for an agent: the model does not have to reason about whether the cart is complete, and a wrong guess is rejected by the API rather than silently charged. This is the checkout-shaped version of keeping the money path deterministic while discovery stays non-deterministic.
- The call sequence sits below A2A and MCP, not beside them: in the demo an MCP `create_checkout` tool call is what drives the UCP checkout-session endpoints, so the state machine is the protocol's model of the transaction and MCP is how the agent reaches it. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 13:26-13:48)
- The dual-spec finding is the practically useful one. Rerunning the identical flow under ACP: "you can see the same checkout calls, just different schemas are being utilized, and the order goes through." Two specs, one state machine — which makes an internal canonical session model with ACP and UCP serializers the natural implementation, and makes "which spec do we pick?" a smaller question than the ecosystem noise suggests. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 14:07-14:22)
- The payment leg is where the specs are genuinely, not cosmetically, different, because the accepted instrument differs by surface: "in ChatGPT, payments only happen through a shared payment token right now, and Gemini UCP, the payments are only being accepted through Google Pay." Serializing the cart is portable; the payment step is not. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 10:03-10:11)
- Caveat: the states shown are the happy path only. The talk demonstrates no cancellation, expiry, partial-fulfillment, price-change-mid-session, or out-of-stock transition — and a stale feed makes the last two likely — so the three states should be read as the minimum the spec exposes, not as the full state machine a production merchant needs.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Separate Non-Deterministic Discovery From Deterministic Payment Execution](separate-non-deterministic-discovery-from-deterministic-payment.md)
- [Map the Agentic Commerce Protocol Stack by Layer](map-the-agentic-commerce-protocol-stack-by-layer.md)
- [Agent Protocols Must Encode the Distinctions the User Interface Collapses](agent-protocols-must-encode-the-distinctions-the-ui-collapses.md)
- [Bound Agent Payments With Processor-Enforced Mandate Tokens](bound-agent-payments-with-processor-enforced-mandate-tokens.md)
- [Settle Agent Payments Over HTTP With 402 and Checkout Protocols](settle-agent-payments-over-http-with-402-and-checkout-protocols.md)

Sources:
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 10:03-10:11, 13:04-14:22
