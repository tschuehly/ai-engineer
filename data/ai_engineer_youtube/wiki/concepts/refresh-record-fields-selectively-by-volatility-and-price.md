# Refresh Record Fields Selectively by Volatility and Price

Summary: Once the context layer is assembled from purchased data, freshness stops being a schedule and becomes a budget: you cannot refresh every field on every record, so choose which fields update and how often, using how fast each field actually changes as the ranking signal.

Use when:
- Designing the refresh policy for an enrichment or context layer whose inputs are metered or paid per record.
- An agent acted on stale data and the proposed fix is "refresh everything more often."
- Deciding what belongs in a real-time path versus a daily, weekly, or monthly batch.

Details:
- The cost constraint is stated plainly and tied to purchasing: "it's also incredibly expensive to update data all the time, especially if you're purchasing it. So, I can't just update all the fields. I need to kind of selectively choose which fields to update." ([Berry](../sources/20260826_UhCY231d0FQ.md), 05:38-05:50)
- **The ranking signal is per-field volatility, and the spread is large.** "Some data points like employee count change all the time. Other data points like headquarters location change very rarely." A single record-level refresh cadence is therefore wrong in both directions at once — it overpays for the stable fields and is stale on the volatile ones. (07:44-07:54)
- Cadence heterogeneity also comes from the consumer, not only the field: "some systems need kind of like real-time updates one record at a time. Other systems are going to need hundreds of thousands of records, maybe updated once a day. I might need to schedule updates on a monthly or weekly basis depending on the data I'm using." The refresh policy is a cross product of field volatility and destination need. (07:19-07:44)
- Pull is not the only inbound path, which changes what the schedule is responsible for: "if I'm running a signals program, information that I need is getting pushed to me all the time as well." Pushed events cover the fields you cannot afford to poll, which is a reason to treat the signal layer and the refresh budget as one design rather than two. (05:50-05:57)
- **This is the price-side half of a rule the wiki states elsewhere on correctness grounds.** [Do Not Cache Context-Engine Answers as Durable Truth](do-not-cache-context-engine-answers-as-durable-truth.md) resolves stored context with "cache what you can re-derive and date-stamp; recompute what you concluded." Berry's constraint is that re-derivation has a per-call invoice, so the date stamp needs a companion: an expiry chosen per field, not per record, and priced against how much a wrong value costs the action it feeds.
- The rule interacts with waterfalling: each refresh of a waterfalled field may cost several provider calls, not one, so the fields that are hardest to cover are also the most expensive to keep fresh. See [Waterfall Data Vendors and Run Evals to Decide Which to Trust](waterfall-data-vendors-and-run-evals-to-decide-which-to-trust.md).
- **Limit.** No prices, no field-level change rates, no policy, and no worked example of which fields Clay refreshes at which cadence. The reasoning is presented as obvious rather than measured, and the failure mode it prevents — acting on a stale field — is not quantified anywhere in the talk. (05:38-07:54)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Context Engineering](../topics/context-engineering.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Waterfall Data Vendors and Run Evals to Decide Which to Trust](waterfall-data-vendors-and-run-evals-to-decide-which-to-trust.md)
- [Do Not Cache Context-Engine Answers as Durable Truth](do-not-cache-context-engine-answers-as-durable-truth.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Frequency, Not Volume, Drives Web-Context Cost](frequency-not-volume-drives-web-context-cost.md)
- [Treat Tool-to-Tool Orchestration as a Data Engineering Problem](treat-tool-to-tool-orchestration-as-a-data-engineering-problem.md)
- [Treat Embeddings as Cached Compute Decided by Query Volume](treat-embeddings-as-cached-compute-decided-by-query-volume.md)
- [Resolve Entities Across Vendors Before the Agent Reads the Record](resolve-entities-across-vendors-before-the-agent-reads-the-record.md)

Sources:
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 05:38-05:57, 07:19-07:54
