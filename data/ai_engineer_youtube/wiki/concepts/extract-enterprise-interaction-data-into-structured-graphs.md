# Extract Enterprise Interaction Data Into Structured Graphs

Summary: LLMs can turn messy enterprise interaction records into structured graphs for attribution, analytics, and operational intelligence. The useful product is not raw data hoarding, but a structured map teams can query and act on.

Use when:
- Designing AI systems over sales, marketing, or customer-interaction records.
- Explaining why enterprise data products need extraction and graph structure before agents or analysts can reason over noisy records.

Details:
- Upside frames sales and marketing teams as storing large amounts of interaction data in systems such as Salesforce while still not knowing which outreach works. (11:20-12:08)
- The pitch proposes using LLMs to pull important details out of messy email records into structured form. (12:08-12:20)
- Upside compares this to search engines making sense of the unstructured web, but applied to raw enterprise data as a structured map of interactions. (12:20-12:34)
- The hiring focus names knowledge graphs, data analytics agents, graph analytics, and graph-learning models as the technical substrate. (13:27-13:39)

- **Induce the schema by sampling the corpus instead of designing it first.** Unblocked's open-source document query engine "runs over your GitHub repository, ingests your historical pull requests, and then synthesizes a schema based on the documents that it can sample," after which arbitrary queries run through agent chat. That inverts the usual order — pick an ontology, then extract against it — and suits a corpus whose useful fields are not known in advance, at the cost of a schema that shifts with the sample. It pairs with the review-relationship graph built from the same repository data, which is clustered into team labels and projected as an expert-coverage map. ([Werry](../sources/20260827_qdAkxLoYNI8.md), 15:10-16:44)

Related topics:
- [Business Intelligence](../topics/business-intelligence.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Start GenBI with certified assets before autonomous SQL](start-genbi-with-certified-assets-before-autonomous-sql.md)
- [Map expert decision taxonomies into knowledge graphs](map-expert-decision-taxonomies-into-knowledge-graphs.md)
- [Use Social and Expert Graphs to Personalize Coding-Agent Context](use-social-and-expert-graphs-to-personalize-coding-agent-context.md)

Sources:
- [The Next Unicorns: 7 Top AI startups from the HF0 Residency](../sources/20250821_L8-5ezsoI5A.md), 11:20-13:39
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 15:10-16:44
