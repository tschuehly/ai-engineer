# Ground Agent Actions in an Existing Domain Transaction Standard

Summary: When a regulated domain already has a strict public transaction standard, make that standard part of the agent harness rather than inventing your own schema: it confines the model to a small predictable value space, it gives a long multi-step pipeline something grounded to reject against, and because every action channel maps onto the same transaction, heterogeneous surfaces (an API feed, a phone call, a browser session) normalize into one representation.

Use when:
- Designing an agentic execution layer in a domain that already has an EDI, messaging, or filing standard (healthcare X12, financial messaging, regulatory submissions).
- Deciding whether the agent should emit a schema you designed or one the industry already publishes.
- A multi-step agent pipeline accumulates errors and you need a checkpoint that can reject an intermediate result.
- Agents reach the same external counterparty through several channels and you need one internal shape for all of them.

Details:
- The confinement argument: like older strict languages such as COBOL or a strict modern one such as TypeScript, "LLMs really thrive … when they're confined, they have clear limited values that they can predict, and X12 is exactly this" — the standard supplies "this contract between what you're trying to communicate and the insurance company." (`UyyOoJmuATU`, 09:04-09:40)
- The standard is treated as a harness component, not a serialization detail. Kearney's broad definition of harness is "all the different nuts and bolts that surround this agentic reasoning" — memory, tools, checks, permissions, handoffs, evals — "but also in the context of healthcare and claims, it's X12." (`UyyOoJmuATU`, 08:31-09:03)
- Why it pays off across steps: a claims objective can be "like 50 steps," and each mistake propagates downstream, so "it's very good to have something grounded that can be rejected to" — strict guardrails give you the authority to reject an incorrect intermediate result rather than carrying it forward. (`UyyOoJmuATU`, 09:44-10:25)
- Channel normalization is the non-obvious payoff. Calling a payer "boils down to a transaction, an X12 transaction": identifying the patient is an eligibility request (a 270), a claim-status request has its own grounding, an imaging attachment is a 275. So a phone call, a desktop agent, a browser agent, and an EDI feed are the same transaction emitted by different routes; only the bank/ACH leg falls outside X12, and that is still a structured transaction. (`UyyOoJmuATU`, 13:29-14:26)
- Public beats bespoke for both models and people: "this is not my schema. If you ask agents to make a schema for you you're going to get like all sorts of stuff. But now if we ground it in something standard you can look up all of these" — an engineer using Claude Code or Codex for research, and a new engineer joining the team, both start from documentation that already exists. (`UyyOoJmuATU`, 14:39-15:25)
- The standard covers the whole lifecycle, which is what lets it act as a spine: scheduling, treatment eligibility, documents, claim submission, and payment each have an X12 correspondence, and the post-submission progression runs submission → 999 syntax acknowledgement → status update → (optionally a verification phone call) → EOB/835 recording payment. (`UyyOoJmuATU`, 12:36-13:20, 18:28-18:55)
- The tradeoff it resolves: pure agentic reasoning over ~50 multimodal steps is expensive, slow, and multiplies error opportunities, while hardcoding the whole system "limits yourself or your code can explode to be just unmanageable," demanding "a giant engineering team." The domain standard is where the strictness is spent, leaving reasoning free elsewhere. (`UyyOoJmuATU`, 10:27-11:18)
- Caveat carried by the same talk: conforming to the standard says nothing about whether the content is true — see [Treat Every External System of Record as Non-Authoritative](treat-every-external-system-of-record-as-non-authoritative.md). Structure and truth are separate problems.
- **The advice holds even when you are the only party to the transaction.** Prio's closing recommendation to a merchant building an agent only for its own website is to adopt the public commerce primitives anyway: "I would advise maybe look into some of these primitives and trying to use them because they've been standardized across merchants. So, they have been well thought out, and also you could probably reuse them to sell externally as well." Two arguments, both independent of interoperability today — the standard already encodes distinctions you would otherwise rediscover by shipping bugs, and adopting it is what makes an internal surface externally sellable later without a rewrite. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 15:33-16:07)

Related topics:
- [Agents](../topics/agents.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Add structure where agent reliability fails](add-structure-where-agent-reliability-fails.md)
- [Treat Every External System of Record as Non-Authoritative](treat-every-external-system-of-record-as-non-authoritative.md)
- [Normalize Network Telemetry Into Agent-readable Schemas](normalize-network-telemetry-into-agent-readable-schemas.md)
- [Type-Safe Agent Schemas Make Refactoring and Validation Easier](type-safe-agent-schemas-make-refactoring-and-validation-easier.md)
- [Agent harnesses combine model, tools, prompts, filesystem, skills, hooks, and memory](agent-harnesses-combine-model-tools-prompts-filesystem-skills-hooks-and-memory.md)
- [Map the Agentic Commerce Protocol Stack by Layer](map-the-agentic-commerce-protocol-stack-by-layer.md)

Sources:
- [Healthcare's Agent Bytecode: X12 as the Harness for AI Agents — Vasant Kearney, Onlay](../sources/20260819_UyyOoJmuATU.md), 08:31-11:18, 12:36-15:25, 18:28-18:55
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 15:33-16:07
