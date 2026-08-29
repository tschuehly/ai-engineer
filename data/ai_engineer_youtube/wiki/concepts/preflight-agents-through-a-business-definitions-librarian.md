# Preflight Agents Through a Business-Definitions Librarian

Summary: Before an analytics agent acts on a business question, route it through a "librarian" service that injects just-in-time definitions and prior-failed-query knowledge. Left alone, the agent silently guesses what business terms mean (a calendar quarter, "pipeline") and returns a confident wrong answer; the librarian gives it the organization's real definitions and citations first, so it stops discovering the wrong interpretation for itself.

Use when:
- Building a natural-language analytics or GTM agent over data whose terms are organization-specific (fiscal calendars, stage definitions, metric semantics).
- An agent produces answers that look right but rest on an unstated wrong assumption about what a term means.
- You want a shared, reusable definitions layer consulted at query time rather than stuffing all definitions into every prompt.

Details:
- Failure mode: asked "How much pipeline did we create in Q1?", a naive agent assumes "quarter means January to March, I'll just look at created date" — "and that is probably not correct." The wrongness is invisible in the output. (12:23-12:38)
- The fix is to consult the librarian *first*, before the agent queries the data. (12:38-12:43)
- The librarian has access to three things: documentation, a "library of knowledge items about your company," and "the schema of prior failed queries." (12:43-12:50)
- It gives the agent "a just-in-time memory of all the important things" — e.g. the fiscal year is actually February through April, and "pipeline" means only records at stage two or later. (12:50-13:03)
- Output is "a nice trustworthy answer with citations back rather than something that you discovered for the first time." (13:03-13:10)
- The librarian ("radiant librarian") is a shipped feature inside Upside's product, presented as a design pattern any agent should consult before acting. (12:12-12:23)
- This is a preflight / just-in-time context-injection pattern applied to *definitions*: it is the human analogue of onboarding a new hire so they understand your business before they answer, and it complements execution-based query validation that catches valid-but-wrong queries after the fact.
- **Where the definitions live when the store is the governed layer, and what happens when they outgrow the prompt.** Snowflake's internal assistant encodes business meaning in 15 semantic views over 85 tables and 3,000 columns rather than in a retrieval-time librarian, and started with the process knowledge inline: "a nine-page long agent instructions." That does not hold — "we were creating all these business processes and workflows. We couldn't fit them into the agent instructions anymore. And then the skills came, and we were like, perfect, let's build a skill library" — and when orchestration instructions for five to six MCP connections pushed past the instruction limit, the answer was progressive disclosure. The durable point for a definitions layer: it grows monotonically with the business, so it needs a retrieval mechanism rather than a prompt slot, whichever artifact holds it. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 05:14-05:31, 12:11-13:08)
- **The static alternative, and what it trades away.** Cloudflare puts the same class of knowledge — business definitions tied to the data, plus the recurring question shapes — inside role-specific skill files loaded up front, and moves the riskiest definitions (which rows count, how they roll up) out of the model entirely into pre-engineered transforms. That removes the librarian service and its latency, at the cost of the librarian's two live properties: just-in-time selection of only the relevant definitions, and accumulated knowledge of prior failed queries. A static file cannot learn from the query that just went wrong. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 06:47-07:53, 10:37-10:49)

Related topics:
- [Business Intelligence](../topics/business-intelligence.md)
- [Retrieval](../topics/retrieval.md)
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Seller knowledge bases let agents pull business context at action time](seller-knowledge-bases-let-agents-pull-business-context-at-action-time.md)
- [Inject tool context just-in-time during agent sequencing](inject-tool-context-just-in-time-during-agent-sequencing.md)
- [Demand-driven context pulls knowledge from failed work](demand-driven-context-pulls-knowledge-from-failed-work.md)
- [Validate generated SQL by execution before trusting it](validate-generated-sql-by-execution-before-trusting-it.md)
- [Compile natural-language analytics into reusable deterministic widgets](compile-natural-language-analytics-into-reusable-deterministic-widgets.md)
- [Stage the Internal Agent Roadmap From Answers to Automation to Team-Built Tooling](stage-the-internal-agent-roadmap-from-answers-to-automation-to-team-built-tooling.md)
- [Put the Business Question Set Inside the Skill File, Not Just the Schema](put-the-business-question-set-inside-the-skill-file-not-just-the-schema.md)
- [Pre-Shape Analytics Data by Time, Slice, and Metric Before the Agent Reads It](pre-shape-analytics-data-by-time-slice-and-metric-before-the-agent-reads-it.md)

Sources:
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](../sources/20260711_YZQsWVeN3rE.md), 12:12-13:10
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 05:14-05:31, 12:11-13:08
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 06:47-07:53, 10:37-10:49
