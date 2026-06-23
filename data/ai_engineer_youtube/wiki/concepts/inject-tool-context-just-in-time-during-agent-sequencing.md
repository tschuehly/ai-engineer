# Inject Tool Context Just-in-Time During Agent Sequencing

Summary: A data-and-tool agent stays reliable by sequencing a preflight checklist before acting and injecting each tool's heavy schema/usage context only at the moment that tool is invoked, layered on a base prompt that tells the model to distrust its own stale knowledge and consult primary sources.

Use when:
- Building an agent over sprawling enterprise tools (warehouses, trackers, docs) whose per-tool context is large.
- Deciding when to load tool schemas and instructions so the context window stays clean.

Details:
- Sequencing: when a new question arrives, the agent runs preflight checks (are all tools connected, is there enough context to answer, otherwise ask clarifying questions) and works through a checklist to decide which tools it should actually use before invoking anything. (10:07-10:32)
- Just-in-time injection: the per-tool context is injected at the moment the tool is invoked, not upfront. For Snowflake this block is long because it encodes the database schema and how to connect teams to environments and resources, so loading it eagerly for every tool would blow out the context window. (10:32-11:13)
- This is the runtime, single-agent counterpart to MCP tool-budget discipline: rather than choosing which of many tools to expose, it defers the cost of each tool's instructions until that tool is chosen. (11:05-11:13)
- Layering: a base Studio prompt provides defaults, org-level rules add per-tool context, and that context is preserved when a user edits a tool, so customizations are not lost across sessions. (11:14-11:32)
- Primary-source grounding: the prompt explicitly tells the model to distrust its own knowledge of the fast-moving product because training data is outdated, and instead look up docs and other primary sources rather than relying on what the model "knows." (11:32-11:58)
- No RAG store is needed for schema understanding: LLMs interpret self-descriptive table schemas well, so a hand-written context block describing join quirks (e.g. a relationship four joins deep) and entity representations is enough — "we're just invoking tools with just context on top." (12:57-14:12)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)

Related concepts:
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Context blocks turn monolithic enterprise knowledge into reusable agent context](context-blocks-turn-monolithic-enterprise-knowledge-into-reusable-agent-context.md)
- [Wrap generic tool descriptions with use-case guidance](wrap-generic-tool-descriptions-with-use-case-guidance.md)
- [Validate Generated SQL by Execution Before Trusting It](validate-generated-sql-by-execution-before-trusting-it.md)

Sources:
- [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](../sources/20260611_iUWwcG-C8OU.md), 10:07-11:58, 12:57-14:12
