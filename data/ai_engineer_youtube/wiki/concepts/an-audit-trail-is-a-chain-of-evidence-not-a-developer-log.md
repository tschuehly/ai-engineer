# An Audit Trail Is a Chain of Evidence, Not a Developer Log

Summary: Engineers hear "audit trail" and picture application logs in a dashboard; the compliance frameworks enterprises actually answer to mean a complete, authorization-bearing record of every action and every data access, durable enough to stand as evidence if the decision were examined in court. The architecture that satisfies it is an immutable append-only event log as the system's single source of truth, which makes auditability a property of the storage model instead of something reconstructed after the fact.

Use when:
- A security or compliance team asks to see the audit trail for an agent and you are about to point at your observability vendor.
- Choosing the storage model for an agent that will operate in a regulated enterprise, before the first pipeline is built.
- Several agents run in parallel over the same records and you need one defensible account of what the system knew and did at a given moment.

Details:
- **The definitional gap is the trap.** "For programmers, an audit trail sounds very like a typical developer log you might have in DataDog. Surely it's … a similar kind of thing. But for security frameworks that … exist in the real enterprise world, like SOC 2, HITRUST, HIPAA, an audit trail is … a bit more than that. It has to contain a complete record of absolutely every action that the agent took … all of the places where the agent accessed data, all of the authorization by which the agent did something." Note the third element: authorization, not just action and access — a developer log almost never carries it. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 05:23-06:07)
- **The test to apply is legal, not operational.** "Say our agent's decisions came up in a court of law. Could we show a justifiable chain of evidence for why the particular actions were taken by a decision? And that's something that could easily happen within the health care context." This is a stricter bar than "can we debug it" and it is the one that decides whether a POC ships. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 06:09-06:27)
- **Borrow the finance transaction log.** The pattern is "an immutable record of events that store all of the transactions that happen throughout the system": append-only and timestamped, *complete* ("this is your source of truth for all of the data of the system"), and *unified* ("there's only one source of truth across all of the different agents that you might have running in parallel"). The unification claim is what rules out per-agent logs stitched together later. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 06:47-07:21)
- **Auditability then stops being a feature.** "Auditability becomes trivial. It falls out of your data storage paradigm that you've chosen. It sort of is impossible not to be able to roll back time and … see exactly the state of the system at a … particular point in time and be able to … provide that as an audit trail." The property you are buying is the same one behind [making regulated-data failures architecturally impossible](make-regulated-data-failures-architecturally-impossible.md): a system incapable of the failure beats a system that has a policy against it. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 07:21-07:44)
- **State the price.** With event sourcing, "writes become very easy. So, you just drop an event. Reads become more difficult because you have to read through all of the events in order to reconstruct a view of what happened." Caching and snapshots help, "but there always is more effort there." Choosing this model is choosing to pay on the read path forever. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 07:46-08:14)
- **In domains where the past gets reinterpreted, the read cost buys something back.** "You're going to want different interpretations of the raw data that your agents recorded after the fact… more events happened and that changes the interpretation of the healthcare journey, and you want a different view of the … source of truth at that particular time. And this pattern makes that easy because all of your views of the data are ephemeral computed projections of the event log." A system that stored the derived view instead of the events cannot do this at all. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 08:14-08:46)
- **Distinguish this from developer-facing replay.** Recording node-boundary inputs and outputs to [re-enter a failed run](record-and-replay-agent-runs-at-node-boundaries.md) serves debugging and is scoped to traces you chose to keep; the compliance ledger is the system's source of truth, covers every action including the successful ones, and carries the authorization for each. The same log can serve both, but only the second requirement forces completeness and immutability. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 05:23-07:44)
- **Why the systems that already do this well are the ones agents cannot build on.** Krieger, on agentic products in financial services: "a lot of the systems that were built to do the verifiability, auditability are almost by design not super flexible in terms of agentic workloads on top. So there's opportunity at both sides of the stack." The rigidity is a design consequence of the evidence guarantee, not an implementation gap, so an agent layer generally cannot be bolted onto an existing audit system — the architecture question becomes where to draw the cut line between the verified substrate and the free-form analysis generated over it. ([Krieger](../sources/20260827_qqrk7CtkuIw.md), 20:42-21:41)

Related topics:
- [Security](../topics/security.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Store Agent Data in Object Storage Beside the Event Log, Not Inside It](store-agent-data-in-object-storage-beside-the-event-log.md)
- [Let Evals Emerge From Your Architectural Primitives](let-evals-emerge-from-your-architectural-primitives.md)
- [Record and Replay Agent Runs at Node Boundaries](record-and-replay-agent-runs-at-node-boundaries.md)
- [Use immutable versioned state for agent handoffs](use-immutable-versioned-state-for-agent-handoffs.md)
- [First-Class Agent Users Need Identity, Scopes, and Audit Trails](first-class-agent-users-need-identity-scopes-and-audit-trails.md)
- [Make Regulated-Data Failures Architecturally Impossible](make-regulated-data-failures-architecturally-impossible.md)
- [Draw the Cut Line Between Verified Data and Free-Form Agent Analysis](draw-the-cut-line-between-verified-data-and-free-form-agent-analysis.md)

Sources:
- [Why Your Enterprise Tech Stack Isn't Ready for AI Agents — Christopher Lovejoy & Saul Howard](../sources/20260819_mav15aW9lLM.md), 05:23-08:46
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 20:42-21:41
