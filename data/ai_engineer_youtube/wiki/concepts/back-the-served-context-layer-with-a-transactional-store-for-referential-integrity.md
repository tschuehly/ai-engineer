# Back the Served Context Layer With a Transactional Store for Referential Integrity

Summary: When the entities an agent reads are stitched from a CRM, a product database, and third-party vendors, a relational store with transactional guarantees can be the right serving layer — chosen not for read latency but because referential integrity across systems, and provenance on every value, are what keep the joined model from silently drifting. This is the opposite tradeoff from a denormalized key-value profile, and the go-to-market cluster contains both.

Use when:
- Choosing the store that agents read customer, account, or entity context from.
- Cross-system relationships (contact belongs to account belongs to workspace) matter more than shaving milliseconds off a read.
- Deciding where provenance and recency metadata should live — on the row, or in a separate lineage system.

Details:
- **The choice and its reason, stated together.** Real-time events "like emails, you can go and pipe them onto a Kafka topic, consume them, and then funnel them back" into "a Postgres database that backs all of this," which "enables us to maintain transactional guarantees, referential integrity between the entities that exist… between your CRM, between your product, between third parties, and attribute everything to the right level of detail, which we found to be a pretty important problem." ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 06:28-07:03)
- **Provenance is a column, not a pipeline artifact.** Stored alongside the entities is "all the associated metadata around capturing like where did this come from? When did it come in?" — which is what makes a contradiction between two vendors resolvable at read time rather than a mystery. (07:05-07:09)
- **The unstructured half lives beside the structured half.** "So much sales data is just inherently unstructured — you have call transcripts, you have emails, you have notes, and the ability to search across that is really valuable," so the same layer carries embedded content addressable by the same entities. (07:09-07:24)
- **Two write paths converge on one read surface.** Online batch jobs "which are really just calling a lot of APIs" pre-compute enrichment across the addressable market, and an offline path — "dbt, Snowflake, pulling everything into our warehouse, doing a lot of offline batch compute" — returns "via reverse ETL back into the same layer." Convergence is the point: the agent reads one place regardless of which path produced the value. (07:24-08:05)
- **The direct contrast in this wiki.** Notion computes in Snowflake and serves from DynamoDB as "a denormalized, key-addressable profile that agents can quickly query in milliseconds with no joins" ([Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)). Both designs put batch compute behind a fast serving layer; they disagree on what the serving layer owes the reader. Denormalization buys join-free latency and pays with duplicated, eventually-consistent copies; a relational store keeps one authoritative relationship graph and pays with joins on the read path. Neither source acknowledges the other's tradeoff, so treat this as two defensible answers selected by which failure hurts more — a slow agent turn, or a rep shown a contact attached to the wrong account.
- **The failure this defends against is specific and already documented.** "Conflicting systems of record, wrong contacts tied to different accounts. One bad mapping was enough to lose trust for a sales rep" ([Liu](../sources/20260826_L4I7WgiEquo.md), 04:36-04:48). Referential integrity enforced by the store is a structural answer to exactly that failure; a denormalized profile can only answer it by being rebuilt correctly.
- **Limit.** No latency, volume, entity count, or write-rate figure is given, so there is no evidence about where the relational read path stops being fast enough — which is precisely the boundary a reader needs to choose between the two designs. Nor is it stated whether agents read Postgres directly or through a service. ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 06:28-07:09)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Context Engineering](../topics/context-engineering.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Resolve Entities Across Vendors Before the Agent Reads the Record](resolve-entities-across-vendors-before-the-agent-reads-the-record.md)
- [Hydrate a Trigger Event to Its Entity Once and Persist the Mapping](hydrate-a-trigger-event-to-its-entity-once-and-persist-the-mapping.md)
- [Treat Every External System of Record as Non-Authoritative](treat-every-external-system-of-record-as-non-authoritative.md)
- [Land the Data in One Governed Store So Agents Inherit Access Control](land-the-data-in-one-governed-store-so-agents-inherit-access-control.md)
- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](treat-go-to-market-as-a-live-model-of-your-world.md)
- [Treat Tool-to-Tool Orchestration as a Data Engineering Problem](treat-tool-to-tool-orchestration-as-a-data-engineering-problem.md)
- [Fan Out a Scheduled Per-Entity Agent Instead of Waiting for a Trigger](fan-out-a-scheduled-per-entity-agent-instead-of-waiting-for-a-trigger.md)
- [Own the Context Layer and Rent Every Other Layer](own-the-context-layer-and-rent-every-other-layer.md)

Sources:
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 05:44-08:05
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 04:36-04:48, 09:36-10:07
