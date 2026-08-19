# Hold Unregulated Intimate Data to the Professional-Privilege Bar

Summary: Some consumer AI products collect data at least as sensitive as anything a regulator covers, in a category no regulator covers. When the legal floor is "whatever your privacy policy says," the usable bar is the one the corresponding profession applies to a human — privilege — imported voluntarily, because otherwise the disclosures land in the same infrastructure as search history.

Use when:
- Designing storage, logging, analytics, or training pipelines for a product that receives intimate disclosures — relationships, grief, money, addiction, sexuality, family conflict.
- Your compliance review comes back "not HIPAA-covered, not GDPR-special-category, we're fine," and you need a different question to ask.
- Deciding whether conversation data may enter training pipelines, product analytics, or a shared data lake.
- Setting an internal standard that survives a growth team asking for more instrumentation.

Details:
- **Inventory the data before arguing about the category.** What a user tells an AI relationship coach in the very first conversation: "the fight from an hour ago. The thing your partner did that you've never told anyone. Financial secrets, affairs, mental health history, sometimes your kids' names." Cockrell's assessment — "that is without exaggeration some of the most sensitive data a human being generates" — is an observation about the content, and it holds regardless of which regulation applies. ([Clay Cockrell](../sources/20260819_yoONZwV2smc.md), 10:35-11:00)
- **The default destination is ordinary consumer infrastructure.** That data "sits in training pipelines, server logs, and product analytics built by teams optimizing for engagement, not confidentiality," so "your most vulnerable disclosures about your relationship may be sitting in the same data infrastructure as your search history and your shopping cart. And that should bother you." The mechanism is not malice; it is that nothing in the stack was told this data is different. ([Clay Cockrell](../sources/20260819_yoONZwV2smc.md), 11:00-11:29)
- **The asymmetry with the human version of the same service.** "In my office, what you tell me is privileged. There's a legal and ethical framework built over decades governing exactly what I can and can't do with it. Consumer AI products have no equivalent." A user moving from a counselor to an app experiences continuity of service and a silent discontinuity of protection. ([Clay Cockrell](../sources/20260819_yoONZwV2smc.md), 11:08-11:20)
- **The bar, stated as a decision rule.** "We treat what you tell Maxine the way I treat what you tell me in my office, as privileged. That's the bar we hold ourselves to. Not is this legally defensible, the bar is would I be comfortable if this were my own marriage on the line, because a lot of our users it is." The first half names the source of the standard (the profession's, borrowed); the second is a test any engineer on the team can apply to a proposed log line, feature, or dataset without a lawyer. ([Clay Cockrell](../sources/20260819_yoONZwV2smc.md), 13:02-13:21)
- **This is the unregulated branch of a pattern the wiki documents on the regulated side.** Hinge Health strips PHI at the pipeline boundary so "the PHI was never there," and Anterior separates the event log from object storage so engineers can debug an agent without reading the records — both are architectural answers to a *compelled* requirement, and both are the right implementations here too. What this concept adds is the case where nothing compels you: the requirement has to be adopted, which means it competes with engagement instrumentation rather than overriding it, and the only thing holding it in place is a stated bar. Adopt the architecture *and* the bar; the architecture is what makes the bar survive the next roadmap.
- **The honest limit of the claim.** The talk describes the standard the team holds itself to and does not describe the mechanism — no retention policy, training-data exclusion, encryption scheme, or audit is specified, and privilege in the legal sense is a protection a private company cannot actually grant a user (a court can still reach the records). Treat "privileged" here as an internal handling bar, not as a legal status you can promise.

Related topics:
- [Security](../topics/security.md)
- [Product Strategy](../topics/product-strategy.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Make Regulated-Data Failures Architecturally Impossible](make-regulated-data-failures-architecturally-impossible.md)
- [Store Agent Data in Object Storage Beside the Event Log, Not Inside It](store-agent-data-in-object-storage-beside-the-event-log.md)
- [Aggregated Personal Context Creates Mosaic and Exfiltration Risk](aggregated-personal-context-creates-mosaic-and-exfiltration-risk.md)
- [High-Consequence Data Changes Vendor Trust Requirements](high-consequence-data-changes-vendor-trust-requirements.md)
- [Agreeableness Is a Failure Mode When the Product's Job Is to Change the User](agreeableness-is-a-failure-mode-when-the-job-is-to-change-the-user.md)

Sources:
- [AI is the World's largest Relationship Therapist — Clay Cockrell & Tony Fabrikant, CoupleWork AI](../sources/20260819_yoONZwV2smc.md), 10:35-11:39, 13:02-13:21
