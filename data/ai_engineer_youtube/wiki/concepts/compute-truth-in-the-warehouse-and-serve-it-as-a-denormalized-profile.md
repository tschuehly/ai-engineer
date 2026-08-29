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

Sources:
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 04:49-04:59, 09:04-10:35
