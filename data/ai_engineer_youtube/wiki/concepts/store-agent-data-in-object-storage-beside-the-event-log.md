# Store Agent Data in Object Storage Beside the Event Log, Not Inside It

Summary: If the sensitive payload lives inside the agent's event log, then anyone who can read what the agent did can also read the regulated data it did it to. Putting the payload in schema-driven, immutable object storage and letting events carry only references splits "what happened" from "what it touched" — which buys PHI-free debugging, a place to enforce zero trust at the point of use, and an architectural answer to the lethal trifecta.

Use when:
- Designing storage for an agent that handles PHI, PII, or any data your engineers are not cleared to read.
- Developers need to retrace an agent's steps in production but cannot be granted access to the records involved.
- You want a structural, not prompt-level, answer to "could this agent hold data A and reach data B in the same process?"
- The customer will not let their data leave their own environment.

Details:
- **Let the data's shape pick the storage.** The stated characteristics of healthcare data: complicated and not strictly hierarchical, "sometimes unstructured and … sometimes structured," potentially very large ("one piece of health care data can easily be over a megabyte in size or … much more"), under strict role-based access control "both for humans and … then for agents downstream of that," and sometimes not permitted to leave the customer's premises at all — "customers where they're not willing to have their health care data leave their own environment, leave their on prem VPC," so the vendor has only "tangential access." Schema-driven object storage fits that list; a relational schema or an in-log blob does not. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 09:28-10:32)
- **The events hold references, nothing more.** Object storage "matches well with the choice of using event logging because you can separate the two. So, the events … only contain references to the schema driven blobs that are the storage of the actual health care data itself." The blobs are stored immutably too, "so that you can always go back in time and reconstruct what data the agent had access to at that particular point in time" — the reference is worthless as evidence if the target can be edited. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 10:25-11:03)
- **The first payoff is debugging without exposure.** Developers "go back and debug and have observability over what happened, what particular steps the agent took, why it did that, and … retrace the agent's steps without having access to the personal health information itself." The schema is what makes this workable rather than blind: "because of the schema driven, they can see the shape of that data," even though they cannot see its content and "often won't be able to be given access" to it. Generalized: "you can separate out observability and orchestration and instrumentation from the health care data itself." ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 11:04-11:52)
- **The second payoff is a zero-trust enforcement point.** "The object storage becomes a place where you can apply zero trust principles. Your agents can bear tokens and use those tokens to access the data at the point of use and not allow data to flow around the system as it likes." A single boundary that every read passes through is what makes per-read authorization checkable — and it is where the authorization half of a compliance [audit trail](an-audit-trail-is-a-chain-of-evidence-not-a-developer-log.md) comes from. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 11:52-12:14)
- **The third payoff turns the lethal trifecta into a constraint you can solve.** The framing is architectural rather than behavioral: "can I solve for the constraint if I have an agent at point A with access to this data? Is it possible within my architecture for the agent to be also accessing data over here?" With tokens borne by agents and "object storage segregated from the event stream that has your orchestration logic … it won't be possible for the agent to access data within the same process that … you've given it the … previous data." This is a different mitigation class from the [prompt-injection defenses used by browser agents](browser-agents-sit-in-the-prompt-injection-lethal-trifecta.md), which assume the injection lands and add tagging, allow-lists, and user confirmation; here the exfiltration target is simply unreachable from the compromised process. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 12:15-12:56)
- **Contrast with strip-at-ingestion.** Hinge Health's answer to the same problem is to [delete the regulated data at the pipeline boundary](make-regulated-data-failures-architecturally-impossible.md) so there is nothing downstream to leak. Anterior's agents must reason over the record itself, so the data has to survive; the separation moves the boundary from *whether the data exists downstream* to *which process can dereference it*. Both refuse to make redaction the control. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 08:47-12:56)
- **Access necessity is scoped per journey, not per role alone.** "You cannot have your agent, just as you cannot have humans, accessing and reading and utilizing healthcare data that they don't absolutely have a necessity to use at that … point in time for that particular journey." Point-of-use tokens are the mechanism that makes a per-journey necessity rule enforceable rather than aspirational. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 08:47-09:27)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [An Audit Trail Is a Chain of Evidence, Not a Developer Log](an-audit-trail-is-a-chain-of-evidence-not-a-developer-log.md)
- [Let Evals Emerge From Your Architectural Primitives](let-evals-emerge-from-your-architectural-primitives.md)
- [Make Regulated-Data Failures Architecturally Impossible](make-regulated-data-failures-architecturally-impossible.md)
- [Browser agents sit in the prompt-injection lethal trifecta](browser-agents-sit-in-the-prompt-injection-lethal-trifecta.md)
- [Aggregated Personal Context Creates Mosaic and Exfiltration Risk](aggregated-personal-context-creates-mosaic-and-exfiltration-risk.md)

Sources:
- [Why Your Enterprise Tech Stack Isn't Ready for AI Agents — Christopher Lovejoy & Saul Howard](../sources/20260819_mav15aW9lLM.md), 08:47-12:56
