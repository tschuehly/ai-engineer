# Compute Truth in the Warehouse and Serve It as a Denormalized Profile

Summary: Split the context layer into a compute store and a serve store: the warehouse ingests every vendor feed and produces a small set of modeled, versioned entities on a batch cadence, and a key-value store publishes a denormalized, key-addressable profile that agents read in milliseconds with no joins. Key the generated unstructured artifacts to the same IDs so one read returns both halves.

Use when:
- Agents need account, user, or entity context on the critical path of a request and warehouse queries are too slow.
- Structured records and model-generated artifacts (summaries, research notes, rolling state) live in different stores and downstream systems have to stitch them.
- Deciding what "single source of truth" means operationally when the truth is computed from a dozen vendor systems.

Details:
- The split is stated as two verbs over the same noun. "Snowflake, which is our data warehouse, is where we compute this truth… DynamoDB is our key-value store and it's where we serve our truth." ([Liu](../sources/20260826_L4I7WgiEquo.md), 09:04-09:41)
- The compute side ingests "data from all the vendors in our GTM stack" and runs "daily transforms and in some cases real time to produce a small set of modeled, versioned entities": accounts, contacts, workspaces, eligibility, and facts, each with "clear ownership of what teams or tools they come from and timestamps." Smallness, versioning, provenance, and recency are all properties of the modeled layer rather than of the raw feeds. (09:11-09:36)
- **The serve side is shaped by the agent's read pattern, not the analyst's.** "We publish a denormalized, key-addressable profile that agents can quickly query in milliseconds with no joins" — the denormalization exists because an agent turn cannot afford a multi-table join. (09:41-09:49)
- Agent output is stored in the same place as agent input: "we also persist agent-generated artifacts — research snippets, summarized notes, rolling summaries — and these unstructured data are also keyed by the same IDs so that downstream systems can read all of this in one shot." Shared keys are what make the structured and unstructured halves one profile instead of two lookups. (09:49-10:07)
- The design answers a specific named failure: "every vendor added a hop and this lag was causing us to act on stale data, and that meant we were automating on yesterday's world." Consolidating ingestion and publishing a served profile removes the per-vendor hop from the decision path. (04:49-04:59)
- It also answers the structured/unstructured problem, because the facts that change what a rep should do — "the champion just left," "don't contact this customer again," "they're blocked in legal" — arrive as notes; the normalized entities are brought into the shared workspace "so that we could work with structured and unstructured data at the same time." (05:00-05:27, 10:10-10:35)
- **Limit.** "Milliseconds" is asserted, not measured, and no figure is given for freshness lag, entity count, write volume, or the cost of maintaining two stores. Which entities get real-time rather than daily transforms is not specified, so the staleness boundary that motivated the design is left undrawn. (09:11-09:49)
- **The same split, with a different serve shape, when the reader is an analysis rather than an account agent.** Cloudflare pre-computes into tables organized by time, organizational slice, and metric — wide for snapshots, long for trends — because "a big part of this is simplifying the data so that the AI agents can actually analyze the data in a very consistent and clean way." Notion's serve layer is keyed by entity ID for millisecond per-account reads; this one is keyed by period and slice for aggregate reasoning. Both move the joins and the definitions into batch, and the choice of serve shape follows from the question the agent is being asked, not from the storage technology. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 10:04-10:37)
- **What the compute half has to do before it can produce a modeled entity, from a source that buys its inputs.** Berry lists the admission requirements for the data layer: waterfall multiple vendors because none covers a field, run evals to rank them, choose which fields to refresh because "it's incredibly expensive to update data all the time, especially if you're purchasing it," absorb pushed signal data alongside pulled data, and resolve entities because "the actual representation of a single account in those different sources is going to be different." Notion's "small set of modeled, versioned entities" is the output of exactly this work; naming the inputs is what makes the versioning and the timestamps load-bearing rather than tidy. ([Berry](../sources/20260826_UhCY231d0FQ.md), 04:42-06:19)
- **A third serve shape, and the sharpest disagreement in this cluster.** Ramp runs the same compute half — "dbt, Snowflake, pulling everything into our warehouse, doing a lot of offline batch compute, and then piping that in via reverse ETL back into the same layer" — but serves from Postgres, chosen because it "enables us to maintain transactional guarantees, referential integrity between the entities that exist… between your CRM, between your product, between third parties." Denormalizing for join-free millisecond reads and keeping one authoritative relationship graph are opposite answers to the same question, and neither source argues against the other. See [Back the Served Context Layer With a Transactional Store for Referential Integrity](back-the-served-context-layer-with-a-transactional-store-for-referential-integrity.md). ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 06:28-07:03, 07:50-08:05)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Put Humans and Agents on the Same Substrate Instead of an AI Layer on Top](put-humans-and-agents-on-the-same-substrate-instead-of-an-ai-layer-on-top.md)
- [Reduce Every Workflow to Know, Decide, Act, and Learn](reduce-every-workflow-to-know-decide-act-and-learn.md)
- [Land the Data in One Governed Store So Agents Inherit Access Control](land-the-data-in-one-governed-store-so-agents-inherit-access-control.md)
- [Pre-Bake Transforms Too Heavy for the Real-Time Path](pre-bake-transforms-too-heavy-for-the-realtime-path.md)
- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](treat-go-to-market-as-a-live-model-of-your-world.md)
- [Do Not Cache Context Engine Answers as Durable Truth](do-not-cache-context-engine-answers-as-durable-truth.md)
- [Pre-Shape Analytics Data by Time, Slice, and Metric Before the Agent Reads It](pre-shape-analytics-data-by-time-slice-and-metric-before-the-agent-reads-it.md)
- [Waterfall Data Vendors and Run Evals to Decide Which to Trust](waterfall-data-vendors-and-run-evals-to-decide-which-to-trust.md)
- [Resolve Entities Across Vendors Before the Agent Reads the Record](resolve-entities-across-vendors-before-the-agent-reads-the-record.md)
- [Refresh Record Fields Selectively by Volatility and Price](refresh-record-fields-selectively-by-volatility-and-price.md)
- [Treat Tool-to-Tool Orchestration as a Data Engineering Problem](treat-tool-to-tool-orchestration-as-a-data-engineering-problem.md)
- [Run One Dormant, Long-Lived Agent Per Account](run-one-dormant-long-lived-agent-per-account.md)
- [Give Agents Their Own Fields in the System of Record](give-agents-their-own-fields-in-the-system-of-record.md)
- [Back the Served Context Layer With a Transactional Store for Referential Integrity](back-the-served-context-layer-with-a-transactional-store-for-referential-integrity.md)

Sources:
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 04:49-04:59, 09:04-10:35
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 10:04-10:37
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 04:42-06:19
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 06:28-08:05
