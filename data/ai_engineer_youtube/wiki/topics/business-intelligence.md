# Business Intelligence

## Overview

GenBI applies agent and retrieval patterns to governed enterprise analytics. The safest starting point is not open-ended SQL over messy warehouses; it is a staged workflow that understands business context, retrieves certified reports or dashboards, and only then expands toward SQL generation or data pivoting when the system has enough metadata, expert validation, and access controls. This preserves trust because early answers point to assets the organization already knows how to govern.

Enterprise BI-agent programs should also be funded as incremental bets. Metadata enrichment, report discovery, data-owner discovery, and light pivoting can each be useful products before the full analytics copilot exists. In messy go-to-market systems, LLM extraction can also turn emails and CRM records into structured interaction graphs before teams attempt attribution or agentic analytics. That gives leadership visible business value, reusable benchmarks, and stop/go control while the team learns what accuracy, governance, and user expertise are required.

A second design pattern takes the opposite stance on autonomous SQL when the warehouse can be described. WorkOS's internal Studio lets any employee ask questions against Snowflake, Linear, and Notion in natural language; rather than routing to certified assets, it generates SQL directly and reaches a reported high hit rate using no RAG store at all, because LLMs read self-descriptive table schemas well when a hand-written context block encodes join quirks and entity representations. The durable output is not the answer but a "widget" the model writes once as declarative JavaScript that calls the data sources itself, so every later run is deterministic, cheap, and LLM-free and can be shared for self-serve use. Three things make the generation trustworthy: preflight sequencing with just-in-time tool-context injection, a layered prompt that distrusts the model's stale product knowledge in favor of primary sources, and execution-based query validation that catches valid SQL returning zero rows — most often from a forgotten active-status or non-deleted filter. The governance worry that a wrong query becomes accepted truth is answered by encoding those consistency filters into context plus the observation that residual errors tend to be large and obvious.

## Key Concepts

- [Fund enterprise AI through incremental productizable bets](../concepts/fund-enterprise-ai-through-incremental-productizable-bets.md) - keeps uncertain analytics-agent research tied to short, measurable business deliverables.
- [Start GenBI with certified assets before autonomous SQL](../concepts/start-genbi-with-certified-assets-before-autonomous-sql.md) - treats certified reports and dashboards as the first trusted answer surface.
- [Evaluate BI agents with real metadata and expert feedback](../concepts/evaluate-bi-agents-with-real-metadata-and-expert-feedback.md) - validates metadata, schema context, and answer quality against realistic enterprise data and expert review.
- [Extract enterprise interaction data into structured graphs](../concepts/extract-enterprise-interaction-data-into-structured-graphs.md) - converts messy outreach and CRM records into graph-backed attribution and analytics context.
- [Compile Natural-Language Analytics Into Reusable Deterministic Widgets](../concepts/compile-natural-language-analytics-into-reusable-deterministic-widgets.md) - the model writes a query tool once as declarative code so later runs are deterministic and shareable.
- [Validate Generated SQL by Execution Before Trusting It](../concepts/validate-generated-sql-by-execution-before-trusting-it.md) - run a generated query and confirm it returns data before freezing it into a dashboard.

## Open Questions

- Which BI questions can be answered by routing to certified assets, and which require generated SQL, joined data, or human analyst review? (Northwestern Mutual starts from certified assets; WorkOS generates SQL directly with context blocks and execution validation — when does each approach win?)
- Which metadata fields most improve LLM performance on enterprise analytics tasks?
- Which sales and marketing interaction fields should be extracted before graph analytics or attribution agents can be trusted?

## Sources

- [Small Bets, Big Impact Building GenBI at a Fortune 100 - Asaf Bord, Northwestern Mutual](../sources/20251223_LU9KgcZDRfY.md)
- [The Next Unicorns: 7 Top AI startups from the HF0 Residency](../sources/20250821_L8-5ezsoI5A.md)
- [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](../sources/20260611_iUWwcG-C8OU.md)
