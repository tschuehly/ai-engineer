# Resolve Entities Across Vendors Before the Agent Reads the Record

Summary: The moment a context layer draws on more than one external source, the same real-world entity arrives under different representations, so entity resolution is a precondition for the layer rather than a cleanup pass on top of it — nothing downstream, from waterfalling to per-account agents, is well defined until the records are merged.

Use when:
- Assembling a customer, company, or person model from several vendors, feeds, or acquired systems.
- An agent produced contradictory facts about one entity and each fact traces to a different source.
- Deciding what "one record" means before designing per-entity agents, alerts, or eligibility rules.

Details:
- The requirement falls out of the multi-vendor design rather than being a separate initiative: "because I'm using multiple third-party sources, the actual representation of a single account in those different sources is going to be different. So, I need to resolve the entities in between them." ([Berry](../sources/20260826_UhCY231d0FQ.md), 05:57-06:12)
- **It is listed as one of the things a data layer must do before the interesting work starts.** "A great data layer will tackle all of these things and allow me to move on to the more interesting work, but without this, it's really, really hard to execute automated GTM plays." Resolution is grouped with waterfalling, refresh selection, and first-party integration as a single admission requirement. (06:12-06:19)
- The entity is not stable either, which is what makes resolution ongoing rather than one-time. Accounts change from three directions simultaneously — the company acts ("a company gets acquired, opens offices, ships products"), you act on it ("you're marketing at them, you're selling towards them"), and it emits signals ("hiring people and firing people"). Acquisitions in particular change the identity itself, not a field on it. (03:00-03:42)
- **Resolution is what makes a waterfall coherent.** Layering providers to fill a field ([Waterfall Data Vendors and Run Evals to Decide Which to Trust](waterfall-data-vendors-and-run-evals-to-decide-which-to-trust.md)) presumes the providers are being asked about the same company; if the join is wrong, the waterfall does not fail loudly — it fills the field with a correct value about a different entity, which is worse than leaving it empty.
- It is also the precondition for the per-account agent architecture. [Run One Dormant, Long-Lived Agent Per Account](run-one-dormant-long-lived-agent-per-account.md) instantiates one persistent agent per account; a duplicate account is a duplicate agent working the same customer with half the state each, and a merge mid-cycle has no defined semantics in the talk.
- Notion's version of the same requirement is architectural rather than procedural: the warehouse produces "a small set of modeled, versioned entities" from every vendor feed, and the serve store publishes profiles "keyed by the same IDs," so resolution is the thing that produces the ID everything else addresses. ([Liu](../sources/20260826_L4I7WgiEquo.md), 09:11-10:07)
- **Limit.** No method at all — no matching strategy, blocking scheme, survivorship rule, confidence threshold, human review path, or error rate. The requirement is named in one sentence and dropped, which leaves the hardest part of the data layer as an assertion. (05:57-06:19)
- **A second resolution problem that vendor merging does not touch.** Even with one clean account record per company, the *events* that trigger workflows arrive keyed by attendee emails and meeting titles, and mapping them back is "a sneaky hard problem… because you have the same emails that can work on behalf of multiple businesses, so it's kind of like a fuzzy match." One person legitimately belonging to several accounts is a many-to-many relationship no survivorship rule resolves; the fix is to decide per event and persist the answer ([Hydrate a Trigger Event to Its Entity Once and Persist the Mapping](hydrate-a-trigger-event-to-its-entity-once-and-persist-the-mapping.md)). ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 09:41-10:11)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Waterfall Data Vendors and Run Evals to Decide Which to Trust](waterfall-data-vendors-and-run-evals-to-decide-which-to-trust.md)
- [Refresh Record Fields Selectively by Volatility and Price](refresh-record-fields-selectively-by-volatility-and-price.md)
- [Run One Dormant, Long-Lived Agent Per Account](run-one-dormant-long-lived-agent-per-account.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Treat Every External System of Record as Non-Authoritative](treat-every-external-system-of-record-as-non-authoritative.md)
- [Land the Data in One Governed Store So Agents Inherit Access Control](land-the-data-in-one-governed-store-so-agents-inherit-access-control.md)
- [Wait for the Background Sync Before Acting on a Record You Just Created](wait-for-the-background-sync-before-acting-on-a-record-you-just-created.md)
- [Hydrate a Trigger Event to Its Entity Once and Persist the Mapping](hydrate-a-trigger-event-to-its-entity-once-and-persist-the-mapping.md)
- [Back the Served Context Layer With a Transactional Store for Referential Integrity](back-the-served-context-layer-with-a-transactional-store-for-referential-integrity.md)

Sources:
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 03:00-03:42, 05:57-06:19
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 09:11-10:07
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 09:41-10:11
