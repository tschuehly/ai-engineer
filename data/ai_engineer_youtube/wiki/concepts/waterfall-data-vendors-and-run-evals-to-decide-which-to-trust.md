# Waterfall Data Vendors and Run Evals to Decide Which to Trust

Summary: When no single data provider covers a field for your whole population, fill it by layering providers in sequence until a value comes back, and decide the order by running evals against the providers rather than by reputation or price — coverage is the constraint, and per-provider accuracy is the tiebreak.

Use when:
- Building the enrichment layer under an agent system and finding a field populated for only part of your records.
- Choosing between buying one comprehensive data vendor and composing several.
- Deciding whether to run provider evals yourself or delegate them to an intermediary.
- Reviewing a pipeline that treats one external source as authoritative for a field.

Details:
- The coverage problem is stated as a property of the market, not of any one vendor: "within GTM, there is literally hundreds of vendors that you can turn to to get the data that you need, but none of those vendors is going to have a complete picture of all the information you desire." ([Berry](../sources/20260826_UhCY231d0FQ.md), 04:42-05:01)
- **The technique is named and demonstrated on one field.** "The key technique here is called waterfalling. This is where I'm going to actually go and look into multiple providers to try to fill in all the information that I need. If you see here, if I was just using Forager to get phone numbers for this set of countries, I'd only get halfway there. So, instead, what I need to do is layer on all of these other providers." (05:01-05:18)
- It is not a phone-number special case: "that's not only true for phone numbers, but for most the other data points that we care about within GTM." Any field whose values live outside your company is a candidate. (05:14-05:18)
- **The ordering mechanism is an eval, and the eval can be bought.** "Either you or the vendor that you're using needs to run evals against these data providers in order to obtain the most accurate information." That sentence contains the buy-versus-build decision for the whole data layer: the intermediary's real product is the eval, not the fan-out. (05:18-05:28)
- A waterfall is structurally the same shape as an LLM provider fallback chain and inherits the same hazard — see [Your Fallback Provider Is Under-Tested and Under-Provisioned](your-fallback-provider-is-under-tested-and-under-provisioned.md). The later rungs are exercised only on the records the earlier rungs missed, which is a biased, low-volume, and usually unmonitored slice; if provider four is quietly wrong, it is wrong specifically on the hard population you added it for.
- The waterfall answers coverage, not correctness. A value returned by the third provider is still one external system's claim, and [Treat Every External System of Record as Non-Authoritative](treat-every-external-system-of-record-as-non-authoritative.md) applies with extra force here, because agreement between two vendors who both resold the same upstream file is not independent confirmation.
- **Limit.** No eval method is given: no ground-truth source, no sample design, no per-field or per-segment metric, no cadence for re-running it as providers change. The "halfway there" figure is one field, one unspecified country set, and one chart from the speaker's own product. And the ground truth for a phone number is the same market the vendors are selling into, which is the hard part of the method the talk does not address. (04:42-05:28)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Refresh Record Fields Selectively by Volatility and Price](refresh-record-fields-selectively-by-volatility-and-price.md)
- [Resolve Entities Across Vendors Before the Agent Reads the Record](resolve-entities-across-vendors-before-the-agent-reads-the-record.md)
- [Treat Every External System of Record as Non-Authoritative](treat-every-external-system-of-record-as-non-authoritative.md)
- [Your Fallback Provider Is Under-Tested and Under-Provisioned](your-fallback-provider-is-under-tested-and-under-provisioned.md)
- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](treat-go-to-market-as-a-live-model-of-your-world.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Own the Context Layer and Rent Every Other Layer](own-the-context-layer-and-rent-every-other-layer.md)

Sources:
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 04:42-05:28
