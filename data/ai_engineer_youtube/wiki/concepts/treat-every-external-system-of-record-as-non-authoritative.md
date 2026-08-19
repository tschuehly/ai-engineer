# Treat Every External System of Record as Non-Authoritative

Summary: When an external counterparty exposes several surfaces — an API or EDI feed, a portal, a phone line — none of them is ground truth: they are often built by different teams or different contractors, so they can contradict each other *and* can agree on the wrong answer together. Normalize all of them into one internal representation held as correct only until downstream evidence proves otherwise, and track which surface is reliable per counterparty.

Use when:
- An agent reads the same fact from multiple external systems and you must decide which one wins.
- Designing state for a workflow whose external inputs can be revised after the fact.
- A pipeline "verified" a precondition through several channels and still failed downstream.
- Deciding whether cross-channel agreement counts as confirmation.

Details:
- The surfaces have independent provenance: a payer's web portal, phone system, X12 layer, and FHIR layer may each have been built by a different team, "could be even a different company … that the insurance company contracts out." Conformance to the standard does not make the payload true — "it doesn't mean that when an insurance company gives you an X12, it's true." (`UyyOoJmuATU`, 15:30-16:12)
- Agreement is not confirmation. "They can all actually agree on the wrong information as well": all three surfaces say the patient is covered, you call, you check the portal, you check the X12; you treat the patient; the claim comes back denied because the patient was not covered at that time. (`UyyOoJmuATU`, 16:12-16:33)
- Reliability is per counterparty and learned, not global: "you'll learn some idiosyncrasies of these different payers that some of these systems are more reliable than others." That is an operational fact to record, not a static architecture decision. (`UyyOoJmuATU`, 16:33-16:41)
- The normalization rule: "regardless of if it originates as an X12 or not, you can boil all those transactions down to your own internal semi-correct X12. Correct until downstream evidence proves it otherwise to be incorrect." The internal representation is a working belief with an expiry condition, not a cache of truth. (`UyyOoJmuATU`, 16:42-17:10)
- Corollary for state design: "any of the information coming from the insurance company, any time can be wrong. It can be updated later" — so downstream artifacts must be revisable when a later transaction contradicts an earlier one. (`UyyOoJmuATU`, 17:01-17:10)
- This is the truth-side complement to [grounding agent actions in an existing domain transaction standard](ground-agent-actions-in-an-existing-domain-transaction-standard.md): the standard buys you a predictable shape and a rejection point for malformed intermediates, but nothing about semantic correctness. Structure and authority are separate guarantees.
- It also generalizes the caching caution in [Do Not Cache Context-Engine Answers as Durable Truth](do-not-cache-context-engine-answers-as-durable-truth.md) from generated answers to *retrieved* ones: an external system's answer ages and can be revised for the same reason a model's answer can.

Related topics:
- [Healthcare Operations](../topics/healthcare-operations.md)
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Ground Agent Actions in an Existing Domain Transaction Standard](ground-agent-actions-in-an-existing-domain-transaction-standard.md)
- [Do Not Cache Context-Engine Answers as Durable Truth](do-not-cache-context-engine-answers-as-durable-truth.md)
- [Prefer outcome verifiers over ground-truth path checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md)
- [Prevent Revenue Cycle Denials Upstream](prevent-revenue-cycle-denials-upstream.md)

Sources:
- [Healthcare's Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay](../sources/20260819_UyyOoJmuATU.md), 15:30-17:10
