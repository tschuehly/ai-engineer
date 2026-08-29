# Go To Market

## Overview

Go-to-market has become an AI engineering surface, and the useful reframe is that it is a data problem before it is a channel problem. Researching accounts, finding the right person at a company, deciding which segments exist, knowing when something changed with a customer, and building a demo are not separate automations — they are queries against an artifact most companies never build: a live, joined model of internal data (customers, colleagues, product usage) and external data (companies, people, news) that agents can read and act on. Build that substrate first, and the visible surfaces become readers of it.

Two surfaces recur once the substrate exists. The first is a market model built by classification rather than search: with embeddings over a large corpus, labelling every company in the addressable market is affordable, which converts segment definitions from anecdotes into a list that can be counted, re-sliced, and revenue-weighted. The second is an event layer over customer state — signup, usage surge, usage stop, watchlist arrival — where the most valuable trigger is the one that is an absence, because a stop produces no rows and cannot be caught by a threshold on observed activity.

The agent layer sits on top and is mostly unremarkable except for where it lives and who may call it: a shared fleet in the chat tool the team already works in, with broad read access to internal data, invoked by non-engineers who have been trained to operate tools rather than to build them. The sharp design question is permissions. An agent cloned from a high-access person cannot be shared at that person's privilege level, so bind the capability set to the caller — full read/write and full tools for the owner, drafts and a reduced tool set for everyone else — noting that drafting constrains authority and does nothing about what the assembled context can reveal.

Three cross-cutting decisions shape the stack. Agent-first requires API-first: internal dashboards and internal agents both fail without a programmatic surface over internal and external data, and the requirement extends to purchased systems, which is why buy-versus-build is better replaced by a single test of whether the system is arbitrarily customizable — a bought system of record with a good MCP server passes, and one with only a configuration screen does not. Not everything should be a chatbot: a use case someone runs repeatedly deserves a crystallized interface they can learn once, while open-ended questions belong to the flexible agent. And the staffing consequence is a forward-deployed group that both runs deals and builds the systems the deals run on, a collapse of two roles the speaker attributes directly to AI.

Two cautions run through this material. Almost none of it is measured — the strongest outcome claim in the anchor source is "very lean, but very productive" — and much of it is a vendor demonstrating its own product on its own market. The product-versus-distribution argument is treated as settled by conjunction rather than by evidence: you need both, and the new part is only that the distribution half is now engineerable by a small number of people.

## Key Concepts

- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](../concepts/treat-go-to-market-as-a-live-model-of-your-world.md) - the reframe that makes the rest of the stack follow: GTM tasks are queries against a joined internal/external model.
- [Classify the Whole Addressable Market Instead of Searching It Account by Account](../concepts/classify-the-whole-addressable-market-instead-of-searching-it.md) - exhaustive labelling is a different operation from per-account lookup, and embeddings over a corpus make it affordable.
- [Alert on Account Change Events, Including the Ones That Are Absences](../concepts/alert-on-account-change-events-including-absences.md) - the action layer is an event stream on state transitions, and one of the transitions produces no data.
- [Derive an Agent Persona From a Measured Corpus, Not a Described Tone](../concepts/derive-an-agent-persona-from-a-measured-corpus-not-a-described-tone.md) - measure voice off the person's own archive so the persona is checkable rather than aspirational.
- [Mine Chat History for Past Decisions and Turn Them Into Judgment Evals](../concepts/mine-chat-history-for-past-decisions-and-turn-them-into-judgment-evals.md) - the decision log nobody kept already exists in Slack and email, and it is an eval set.
- [Scope a Person-Cloned Agent by Caller, With Drafts as the Shared Capability](../concepts/scope-a-person-cloned-agent-by-caller-with-drafts-as-the-shared-capability.md) - bind permissions to who invokes the agent, not to the agent.
- [Replace Buy-Versus-Build With Arbitrary Customizability](../concepts/replace-buy-versus-build-with-arbitrary-customizability.md) - the procurement test is whether agents can change the system, which a bought system with an MCP server passes.
- [Crystallize the UI for Repeated Use Cases and Generate It for Novel Ones](../concepts/crystallize-the-ui-for-repeated-use-cases-and-generate-it-for-novel-ones.md) - repetition, not capability, decides whether an interface should be frozen.
- [Staff Forward-Deployed Engineers Who Run Deals and Build the Deal Tooling](../concepts/staff-forward-deployed-engineers-who-run-deals-and-build-the-deal-tooling.md) - AI collapsed the solutions-engineer and tooling-builder roles, while everyone else is trained to operate rather than build.
- [Distribution Is the New Bottleneck for Developer Tools](../concepts/distribution-is-the-new-bottleneck-for-devtools.md) - the diagnosis that motivates treating distribution as engineering work rather than as an afterthought to product.
- [Founder Personal Brand Is the GTM Moat](../concepts/founder-personal-brand-is-the-gtm-moat.md) - the personal complement to an engineered GTM stack, answering a different constraint.
- [AI Does Not Replace Shareable Product Marketing](../concepts/ai-does-not-replace-shareable-product-marketing.md) - generated content is not an attention strategy, whatever the pipeline behind it.
- [Treat Investor Outreach Like Specific Go-To-Market](../concepts/treat-investor-outreach-like-specific-go-to-market.md) - the same targeting discipline applied to a different counterparty.
- [Verify AI Call Summaries Before CRM Sync](../concepts/verify-ai-call-summaries-before-crm-sync.md) - the write path into the system of record needs a check, and agent tool access widens it.

## Open Questions

- What is the accuracy of an exhaustively classified market? Wang reports classifying "basically every possible company" in the TAM and attaching anticipated spend per account, with no sample, spot check, precision figure, or method for the spend estimate. Segment counts derived from a labelled market are only as good as the labels, and no source here measures them. ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 05:22-06:58)
- Does a decision-calibrated clone actually produce accepted output? The evals built from hundreds of past decisions are the strongest methodological claim in the anchor source and carry no pass rate, baseline, or held-out split, and nobody reports whether the drafts colleagues receive are sent, edited, or discarded. ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 09:10-09:27)
- Where does "arbitrarily customizable" run out for a bought system? An MCP server is a narrower surface than source code, and no source here describes a case where a purchased system's customizability was exhausted — which is exactly the evidence the criterion needs to be a decision rule rather than a preference. ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 11:56-13:16)
- Does the everyone-does-everything forward-deployed model survive growth? Eight or nine FDEs at ~115 people is reported as working, and the speaker's own answer to whether it scales is "probably not," with no account of what breaks first. ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 18:07-18:31)

## Sources

- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md)
- [GTM Is You - Victoria Melnikova, Evil Martians](../sources/20260707_G6IlDzj8OjA.md)
- [The AI Engineer's Guide to Raising VC - Dani Grant (Jam), Chelcie Taylor (Notable)](../sources/20250727_YYNXFsUutbM.md)
- [Contact Center Voice AI: Low-Latency Intelligence Extraction from Messy Audio Streams - Dippu Singh](../sources/20260408_IEF842ZEU5A.md)
