# Pre-Shape Analytics Data by Time, Slice, and Metric Before the Agent Reads It

Summary: An agent asked to analyze business performance gives more consistent answers when the filtering logic, the aggregations, and the trend detection are engineered up front, so the model reads a small table already organized along the dimensions the analysis uses — time, organizational slice, and metric — rather than deriving that organization itself on every run.

Use when:
- Building a recurring automated analysis whose output must not wobble between runs.
- Deciding how much of an analytics pipeline belongs in SQL or a transform job versus in the prompt.
- Debugging an agent that reaches different conclusions from the same warehouse on different days.

Details:
- The stated motivation is determinism, not cost: "a big part of this is simplifying the data so that the AI agents can actually analyze the data in a very consistent and clean way." ([Joyce](../sources/20260826_Qw_tC68KKes.md), 10:04-10:14)
- **The three axes are named and they are the axes the narrative is written along.** "We transform the data by the dimension of time, also slice of the logical part of the business, which is manager, theater, and finally the metric." Time gives the comparison, the organizational slice gives the accountable unit, and the metric gives the subject — which is exactly the sentence structure a performance summary produces. (10:14-10:26)
- Layout is chosen per consumer rather than fixed: the demo table is wide, "you could also go from wide to long," and the trend feed is long. Wide reads as one row per entity for a snapshot; long reads as one row per (entity, period, metric) for a trend, and both are materialized rather than pivoted by the model. (10:26-10:32)
- **The judgment is moved out of the model, deliberately and completely:** "the embedding of the logic of how you would filter this data to even analyze it, as well as the logical aggregations the business want to see is all engineered up front." Which rows count and how they roll up are the two decisions where a model's silent guess produces a confident wrong answer, and neither is left to it. (10:37-10:49)
- Trend identification is also pre-computed — "we do some pre-processing on that data to then highlight trends" — so the model is describing detected movement rather than deciding what counts as movement. (10:32-10:37)
- **The claimed coverage is high and the escape hatch is retained:** "this handles 80 or plus percent of the requests is just getting information about the performance of the teams and how they're doing. You can always go down to the raw data," with raw access routed through the self-service workspace rather than through the automated summary. (10:49-11:03)
- This is the analytics-narrative sibling of the entity-serving split in [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md): both move work into a batch layer so the agent's read is cheap and join-free, but the shape differs — a denormalized per-entity profile serves per-account agent reads, while a slice-by-metric-by-period table serves aggregate analysis.
- **Limit.** The 80%-plus figure is a recollection with no denominator, and the cost of the approach is unstated: every new question outside the engineered slices requires a data change rather than a prompt change, and no source here reports how often that happened or how long it took.

Related topics:
- [Business Intelligence](../topics/business-intelligence.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Start GenBI With Certified Assets Before Autonomous SQL](start-genbi-with-certified-assets-before-autonomous-sql.md)
- [Preflight Agents Through a Business-Definitions Librarian](preflight-agents-through-a-business-definitions-librarian.md)
- [Compile Natural-Language Analytics Into Reusable Deterministic Widgets](compile-natural-language-analytics-into-reusable-deterministic-widgets.md)
- [Validate Generated SQL by Execution Before Trusting It](validate-generated-sql-by-execution-before-trusting-it.md)
- [Split a Generated Narrative Into Drafter, Fact-Checker, and Tone Agents](split-generated-narrative-into-drafter-checker-and-tone-agents.md)
- [Stage Complex AI Applications Into Inspectable Deterministic and Agentic Steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)

Sources:
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 10:04-11:03
