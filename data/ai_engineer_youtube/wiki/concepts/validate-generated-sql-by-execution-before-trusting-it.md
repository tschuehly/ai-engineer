# Validate Generated SQL by Execution Before Trusting It

Summary: A model-generated query that parses and runs can still be wrong: valid SQL that returns zero rows, or that silently omits status filters, looks correct but misleads. Run every generated query and confirm it returns sensible data before hardcoding it into a durable artifact.

Use when:
- Building a text-to-SQL or NL-to-analytics agent whose queries get frozen into dashboards, widgets, or reports.
- Worried that a wrong generated query becomes accepted business truth that nobody re-checks.

Details:
- Studio always runs a generated Snowflake query and validates that it gets data back before hardcoding it into a widget, because a syntactically valid query that returns zero rows is a real and useless failure mode the agent must notice. (11:59-12:24)
- This execution check is a pre-deployment gate: the agent pre-validates its own work before it is baked into a self-serve dashboard, rather than trusting that compiling SQL means correct SQL. (12:18-12:24)
- The most common semantic miss is forgetting filter columns — pulling all entities instead of only active-status or non-deleted ones, or doing a plain count/group-by without the consistency filters the data assumes. Embedding those data-consistency rules into the tool context prevents most of these errors. (15:02-15:34)
- Governance framing: an audience member's fear is that a wrong query becomes a "truth" everyone believes and no one verifies; the answer is a high hit rate plus context-encoded guardrails, with the residual errors tending to be large and obvious rather than subtle. (14:26-15:43)
- Evals run in both staging and production and are treated the same, so the team developing the tool experiences the same validation behavior as the teammates using it. (12:25-12:43)
- **Where the silently-omitted-filter bug goes when the filters are engineered up front.** Cloudflare removes the class from the model's reach — "the embedding of the logic of how you would filter this data to even analyze it, as well as the logical aggregations the business want to see is all engineered up front" — which relocates it rather than eliminating it. A wrong status filter in a transform job is testable once and applies everywhere, instead of needing per-query execution checks; the cost is that the error is now shared by every consumer of that table and invisible to anyone reading the generated prose. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 10:37-10:49)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Business Intelligence](../topics/business-intelligence.md)

Related concepts:
- [Compile Natural-Language Analytics Into Reusable Deterministic Widgets](compile-natural-language-analytics-into-reusable-deterministic-widgets.md)
- [Inject Tool Context Just-in-Time During Agent Sequencing](inject-tool-context-just-in-time-during-agent-sequencing.md)
- [Start GenBI with certified assets before autonomous SQL](start-genbi-with-certified-assets-before-autonomous-sql.md)
- [Make Validation Fast, Local, Deterministic, and Actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Pre-Shape Analytics Data by Time, Slice, and Metric Before the Agent Reads It](pre-shape-analytics-data-by-time-slice-and-metric-before-the-agent-reads-it.md)

Sources:
- [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](../sources/20260611_iUWwcG-C8OU.md), 11:59-12:43, 14:26-15:43
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 10:37-10:49
