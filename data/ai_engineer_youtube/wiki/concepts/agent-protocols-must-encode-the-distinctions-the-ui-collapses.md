# Agent Protocols Must Encode the Distinctions the User Interface Collapses

Summary: A human interface deliberately hides distinctions the back-end system treats as structurally different — adding a second unit looks like one gesture to a shopper and is a second line item to a merchant. An agent protocol sits between the two systems, not in front of a human, so it has to carry the counterparty's vocabulary rather than the user's simplified one; this is the reason domain-specific specs exist on top of generic tool-calling.

Use when:
- Asking whether a generic tool or API surface is enough or a domain protocol is genuinely needed.
- Designing an agent-facing schema for a domain that already has internal operational semantics (commerce, ticketing, billing, logistics, scheduling).
- Diagnosing why an agent integration "works" in demos and produces wrong records downstream.

Details:
- The originating example, and the sentence the rest of the protocol argument rests on: "for some of you who are shopping on the other side as the customer, there is not much of a difference between adding an item to cart, adding a second quantity. But to us merchants, that's a second line item, buddy. That's not the same scale. So, if we don't talk about the nuances and the primitives of commerce and standardize it, things will just not work and will remain to be clunky." ([Prio](../sources/20260827_G7cgLjZtmMU.md), 05:00-05:26)
- The diagnostic shape is a *silent* failure, not an error. Both readings of "add another one" produce a plausible cart; only one produces the record the merchant's fulfillment, tax, and returns systems expect. A UI-shaped integration passes its own tests and corrupts the counterparty's state.
- This is why the layer above MCP is not redundant. MCP can express a tool named `add_to_cart` with a quantity argument; what it cannot supply is the agreement about which of the two operations that argument means, across merchants. ACP and UCP exist to fix the vocabulary, which is what Prio calls "the primitives of commerce." ([Prio](../sources/20260827_G7cgLjZtmMU.md), 04:53-05:00, 06:43-06:56)
- The generalization: when an agent replaces a human at an interface, the interface's simplifications stop being kindnesses and become lossy encodings. The right question for any agent-facing surface is not "can the agent drive this?" but "which distinctions did we remove for humans that the system on the other side still relies on?"
- The same principle explains a design choice elsewhere in the talk: the checkout session is exposed as explicit named states rather than as an implicit progression, because "ready for payment" versus "not ready for payment" is a merchant-side distinction a human buyer never sees as a state at all. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 13:04-13:26)
- It also predicts where browser-driving agents fail worst: a DOM-scraping agent can only ever recover the buyer-facing collapse, because that is all the page contains. No amount of model capability recovers a distinction the rendering deleted.
- Caveat: Prio gives one worked example. The claim that this generalizes across domains is an inference from the mechanism, not something the talk tests, and the counter-case — domains where the UI and the back end genuinely agree — is not discussed.

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Map the Agentic Commerce Protocol Stack by Layer](map-the-agentic-commerce-protocol-stack-by-layer.md)
- [Ground Agent Actions in an Existing Domain Transaction Standard](ground-agent-actions-in-an-existing-domain-transaction-standard.md)
- [Model Agentic Checkout as an Explicit Session State Machine](model-agentic-checkout-as-an-explicit-session-state-machine.md)
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)
- [Expose Site Capabilities to In-Browser Agents With WebMCP](expose-site-capabilities-to-in-browser-agents-with-webmcp.md)

Sources:
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 04:53-05:26, 06:43-06:56, 13:04-13:26
