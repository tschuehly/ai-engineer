# Map the Agentic Commerce Protocol Stack by Layer

Summary: MCP, A2A, ACP, UCP, and AP2 are usually encountered as a pile of competing acronyms, but four of the five occupy different layers and compose: MCP advertises capabilities, A2A carries agent-to-agent messages, ACP and UCP supply the commerce vocabulary, and AP2 authorizes the money. Only ACP and UCP are genuine alternatives, and that is the one place a merchant must implement twice.

Use when:
- Deciding which agentic-commerce specifications your merchant or buyer integration actually has to implement.
- Reading a protocol announcement and needing to place it against what you already support.
- Explaining to a team why "we already have MCP" does not answer the checkout question.

Details:
- The layering, in Prio's words: MCP is "still the model context protocol, the way that the AI agent identifies the tool"; A2A "is how agents talk to each other. They're more of a spec"; "ACP, UCP are the primitives and AP2 is the agentic payment protocol scoped payment mandate." ([Prio](../sources/20260827_G7cgLjZtmMU.md), 06:18-06:56)
- The layers are observable in a single request. In the demo, one user turn produces an A2A message from the customer agent to the merchant agent, a completed-task A2A response, and *underneath it* an MCP `product_search` tool call that the merchant agent chose from the intent — "when I give her the intent that I want to find products, you should call the MCP tool call product search." A2A is the envelope between the two parties; MCP is how the merchant's own capabilities got named. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 11:20-12:20)
- MCP's merchant-side content is capability advertisement, not data transfer: showing "what products they have," "the details of a specific product," and loyalty, with "the only way to get access to the specific capabilities is through MCP tool calls." ([Prio](../sources/20260827_G7cgLjZtmMU.md), 06:56-07:11)
- A2A earns its place twice over. Inside one merchant it connects domain-specialized agents — payments, loyalty — that "need to talk to each other." Across the org boundary it connects "your customer agent and your merchant agent… They're both agents. Maybe we can use A2A." The second case is the one that has no alternative, because neither side controls the other's process. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 07:11-08:03)
- ACP (OpenAI) and UCP (Google) are the duplicated layer, and the duplication is not accidental — "Google and OpenAI separately came up with their own little primitives… which is basically talking about how you would actually talk to us." A merchant selling into both surfaces implements both, plus Meta's feed format, which is a third. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 04:53-05:00, 09:19-09:30)
- The cost of the duplication is smaller than the acronym count implies, because the *shape* is shared: running the identical add-to-cart-and-check-out sequence under ACP after UCP, "you can see the same checkout calls, just different schemas are being utilized, and the order goes through." That is an argument for an internal canonical checkout model with per-spec serializers rather than two parallel implementations. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 14:07-14:22)
- The maturity read as of the talk, which is the part to re-check rather than to reuse: adopted — "MCP is widely adopted, A2A is used, UCP ACP is out there"; still forming — "AP2 and actual usage of it, ACP versus UCP convergence, do we always have to do two different specs, identity consent standards, and multi-agent checkout delegation." The last item is the interesting gap: nothing yet says how authority is passed when more than two agents are in the chain. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 18:44-19:08)
- Caveat on the whole map: it is an orientation talk with no Best Buy implementation behind it, and every protocol statement is explicitly present-tense. Treat the layer assignment as durable and the support matrix as perishable.

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)
- [AI Monetization](../topics/ai-monetization.md)

Related concepts:
- [Choose A2A and MCP by Ownership Boundary](choose-a2a-and-mcp-by-ownership-boundary.md)
- [Model Agentic Checkout as an Explicit Session State Machine](model-agentic-checkout-as-an-explicit-session-state-machine.md)
- [Push a Product Feed, Because Per-Merchant Catalog Search Does Not Scale](push-a-product-feed-because-catalog-search-does-not-scale.md)
- [Bound Agent Payments With Processor-Enforced Mandate Tokens](bound-agent-payments-with-processor-enforced-mandate-tokens.md)
- [Settle Agent Payments Over HTTP With 402 and Checkout Protocols](settle-agent-payments-over-http-with-402-and-checkout-protocols.md)
- [Agentic Commerce Moves From Static Stores to Intent Infrastructure](agentic-commerce-moves-from-static-stores-to-intent-infrastructure.md)

Sources:
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 04:53-05:00, 06:18-08:03, 09:19-09:30, 11:20-12:20, 14:07-14:22, 18:44-19:08
