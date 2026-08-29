# Automate the Security Review Path Because Deals Stall There

Summary: Security review is where deals go quiet and die, and most of it is document retrieval and questionnaire filling that can be self-served. Publish a trust portal with an auto-signed NDA, self-serve pen-test and security documentation, and machine-filled questionnaires — then make the buyer justify the call rather than defaulting to one.

Use when:
- Deals reach security review and then stop moving, with no clear owner or next date.
- A buyer's security team opens with a request for a two-hour call and a spreadsheet.
- Selling an AI product into organizations whose review process was written for conventional software.
- Deciding what to build or buy for the non-product half of the sales cycle.

Details:
- **The diagnosis.** "Security is where deals tend to stall out and die over time." Unlike a lost deal, a stalled security review produces no decision and no signal — which is why it is under-managed relative to its cost. ([Rosenthal](../sources/20260826_wdTRsfw0KG0.md), 08:15-08:33)
- **What is automatable, specifically.** "There's so many wonderful tools on the market to build these trust portals where companies can come in and they can auto sign an NDA. They can self-serve for your pen test and security documentation. There's AI products that can auto fill out your security questionnaires. So, automate as much of the security as you can." Three distinct pieces: a gated document store, an NDA that executes without a lawyer in the loop, and generated answers to a bespoke questionnaire. (08:33-08:51)
- **The behavioral half is the part teams skip.** "Most companies will tell you, 'Oh, I need to get on a call. I need to talk for 2 hours.' Push back on that. Push them towards your trust portal and then make them come to you and say, 'Here's what I couldn't find. Here's what wasn't available. Here's why I need a call.'" The portal only saves time if the default is inverted — the call becomes an exception the buyer has to justify with a specific gap, which also converts an open-ended review into a short list of named items. (08:51-09:06)
- **This is the one place the homework rule reverses, and the reason is instructive.** [Never Send the Buyer Away With Homework](never-send-the-buyer-away-with-homework.md) says never hand the buyer a task. Here you deliberately do — read the portal, come back with what is missing. The difference is that security review is the buyer's own governance obligation, which you cannot perform for them; what you can do is make their side cheap and bounded. The invariant holds: you are still removing work, not adding it.
- **The AI-specific caveat the talk does not cover.** A questionnaire written for conventional SaaS asks about data residency, encryption, and access control; an AI product also faces questions about training on customer data, subprocessor model providers, prompt and output retention, and what an agent is permitted to act on. Autofill from a document corpus answers the first category well and the second only as well as your written policy on it. The wiki's adjacent pages describe what a serious buyer will ask about the agent surface itself — see [Enterprise MCP Requires SaaS Security Controls](enterprise-mcp-requires-saas-security-controls.md) and [First-Class Agent Users Need Identity, Scopes, and Audit Trails](first-class-agent-users-need-identity-scopes-and-audit-trails.md) — and those answers have to exist before they can be automated.
- **A machine-filled questionnaire is a set of assertions you are on the hook for.** Nothing in the source addresses review of generated answers, and a wrong answer to a security questionnaire is a contractual representation, not a marketing claim. Treat autofill as a drafting step with a named human approver, in the same shape the wiki recommends for other high-consequence generated artifacts — see [Verify AI Call Summaries Before CRM Sync](verify-ai-call-summaries-before-crm-sync.md) for the same pattern on a lower-stakes write path.
- **The counterparty is also automating.** The security questionnaire exchange is converging on a machine writing questions and a machine answering them, which raises the value of primary artifacts a buyer's reviewer can verify — a current pen-test report, a certification, an architecture description — over prose that satisfies a form. The talk does not raise this; treat it as a reason to invest in the portal's contents rather than only in the autofill.
- **Limits.** No figures: no measured reduction in cycle time, no stall rate before or after, no named tools on either the trust-portal or the questionnaire-autofill side. The "push back on the two-hour call" advice also assumes leverage a small vendor selling into a regulated buyer may not have.

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Security](../topics/security.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Never Send the Buyer Away With Homework](never-send-the-buyer-away-with-homework.md)
- [Treat a Pilot as a Second Sales Process You Run for Free](treat-a-pilot-as-a-second-sales-process-you-run-for-free.md)
- [Enterprise MCP Requires SaaS Security Controls](enterprise-mcp-requires-saas-security-controls.md)
- [First-Class Agent Users Need Identity, Scopes, and Audit Trails](first-class-agent-users-need-identity-scopes-and-audit-trails.md)
- [High-Consequence Data Changes Vendor Trust Requirements](high-consequence-data-changes-vendor-trust-requirements.md)
- [Verify AI Call Summaries Before CRM Sync](verify-ai-call-summaries-before-crm-sync.md)
- [Build the Automated Motion First and Hire Into Its Bottlenecks](build-the-automated-motion-first-and-hire-into-its-bottlenecks.md)
- [Distribution Is the Bottleneck, Not the Idea](distribution-is-the-bottleneck-not-the-idea.md)

Sources:
- [Reverse-Engineering the AI Buyer — Aliisa Rosenthal, Acrew Capital](../sources/20260826_wdTRsfw0KG0.md), 08:15-09:06
