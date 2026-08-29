# Classify the Whole Addressable Market Instead of Searching It Account by Account

Summary: Once you hold embeddings over a large corpus, exhaustive classification becomes a different and cheaper operation than repeated per-account search — so the market-understanding artifact can be a labelled list of every company in the addressable market rather than a research task run once per lead.

Use when:
- Deciding whether to build account research as an on-demand agent call or as a precomputed classification over the whole market.
- You have or can buy semantic coverage of a corpus and are still using it one query at a time.
- Defining an ICP and the team keeps arguing from anecdotes about which segments exist.

Details:
- The operation is stated as exhaustive rather than sampled: the internal ICP dashboard "answers the question, like what is our world? Like what is the world of customers and use cases that we care about," and the method is "we just classify basically like every possible company that is inside of our total addressable market," yielding "an understanding of literally like almost every company within those segments." ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 05:22-06:15)
- The output has two levels, and both are needed: a category breakdown of the market (in the demo: model providers, AI coding platforms "like say Cursor," go-to-market intelligence tools) with revenue attached per category, and a per-company deep dive carrying "how much annual spend we could anticipate them to have" plus company metadata. (05:56-06:28)
- The enabling condition is a corpus-wide representation, not a better search API: "we take the internet, we crawl it, we train embeddings to do web search really well… you can think about Exa as like embeddings over the internet. And when you have embeddings over the internet you have this like arbitrarily powerful semantic filtering and slicing and dicing of any type of data that you want." Search retrieves the top matches for a query; the same embeddings support partitioning the whole set. (06:29-06:58)
- The practical consequence is that segment definitions become falsifiable. A precomputed labelled market can be recounted, re-sliced, and revenue-weighted, where per-lead research produces answers that cannot be aggregated because each was scoped to one account.
- **Limits.** No accuracy claim accompanies "basically every possible company" — no sample, spot check, precision figure, or coverage estimate — and the method behind anticipated annual spend is never described. The revenue columns in the demo are deliberately blurred. The classification substrate is also the speaker's own product, so this is a demonstration of Exa by Exa. (05:56-06:58)
- **The step before classification, and the reason exhaustive labelling is not free.** Berry's data layer builds the population the classifier would run over — accounts and contacts enriched with "the account hierarchy, the firmographics that describe how big the company is and so forth, the technographics that describe what technology they're using" — and each of those attributes is waterfalled across vendors and resolved across their disagreeing representations. Embeddings make the labelling affordable; they do not make the features exist. A label computed over a record whose technographics came from the third provider in the waterfall inherits that provider's coverage bias, which is the accuracy question this page's open limit already flags. ([Berry](../sources/20260826_UhCY231d0FQ.md), 03:42-06:19)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](treat-go-to-market-as-a-live-model-of-your-world.md)
- [Neural Web Search Supports Semantic Agent Queries](neural-web-search-supports-semantic-agent-queries.md)
- [Treat Embeddings as Cached Compute Decided by Query Volume](treat-embeddings-as-cached-compute-decided-by-query-volume.md)
- [Alert on Account Change Events, Including the Ones That Are Absences](alert-on-account-change-events-including-absences.md)
- [Waterfall Data Vendors and Run Evals to Decide Which to Trust](waterfall-data-vendors-and-run-evals-to-decide-which-to-trust.md)
- [Resolve Entities Across Vendors Before the Agent Reads the Record](resolve-entities-across-vendors-before-the-agent-reads-the-record.md)

Sources:
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 05:22-06:58
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 03:42-06:19
