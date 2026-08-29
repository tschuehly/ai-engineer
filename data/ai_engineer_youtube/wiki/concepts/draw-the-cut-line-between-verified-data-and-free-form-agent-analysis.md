# Draw the Cut Line Between Verified Data and Free-Form Agent Analysis

Summary: In regulated verticals the design question is not how much freedom to give the agent but *where the boundary goes*: a verified, provenance-carrying data substrate underneath, and free-form just-in-time analyses, dashboards, and workflows generated on top. Fully free-form is a recipe for confusion and is not what the buyers want; fully locked-down is what the incumbent audit systems already are, and it is why they cannot host agentic workloads.

Use when:
- Designing an agentic product for finance, healthcare, or another audited domain.
- Deciding which parts of a data pipeline an agent may generate versus consume.
- Judging whether an incumbent's compliance architecture is an asset or an obstacle for agent features.

Details:
- The blend, as stated: "the model having the flexibility to dive in and create just-in-time analyses or dashboards or workflows with some sense of what is the not immutable, but at least verified sort of set of data. And having all of that be totally free form is a recipe for confusion and is not what most companies in the financial services space want." Note the qualifier — the substrate is *verified*, not immutable, so it can still change through a governed path. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 20:42-21:10)
- The design work is naming the boundary, and the failure mode on each side is different: "finding that right cut line where you have verifiability and audit logging and data provenance here, but not in a way that constrains the kinds of applications that you can build on top, is a lot of the art that we're seeing in that space." Too low a cut line yields confident analyses over unverified inputs; too high a one yields a compliant system nobody can build on. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 21:10-21:24)
- Why this is an opening rather than a solved problem: "a lot of the systems that were built to do the verifiability, auditability are almost by design not super flexible in terms of agentic workloads on top. So there's opportunity at both sides of the stack." The rigidity of existing audit systems is a design consequence, not an implementation gap, so agent features are unlikely to be bolted onto them. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 21:28-21:41)
- The evaluation signal available in these verticals comes from outside the lab: "there's some good vertical specific finance startups that have done their own evals, which has been interesting to track. And it's not like we're playing to the eval, but it is a useful barometer around is this actually getting better at these finance use cases." A vertical eval owned by an application team is a progress barometer precisely because the lab did not write it — and the disclaimer is a stated intention with no mechanism behind it. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 20:28-20:42)
- Limits: directional and unmeasured. No finance product, dataset, eval, or customer is named, no cut line is actually drawn for a concrete workload, and the claim about what financial services companies want is asserted rather than sourced.
- **One way to make the line below the cut cheap: consolidate first, then inherit.** Snowflake's internal go-to-market assistant is built on a deliberate data-consolidation choice — "we bring all the first-party, the third-party data, all the Salesforce data, everything, the call transcripts, all together" — and the first payoff Izmit names is authorization rather than query performance: "these agents then can basically inherit a lot of the role-based access controls," which is what makes it defensible to "deploy these agents without writing a single line of code" and eventually to let business teams build their own. The cut line is drawn at the store boundary, so provenance and access control are properties of the substrate rather than of each agent. The cost is the consolidation itself, and it is not free even here: 60% of the system's data arrived in the six to seven months after launch. This is also the vendor describing its own platform. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 05:06-05:11, 19:26-20:19)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Business Intelligence](../topics/business-intelligence.md)
- [Agents](../topics/agents.md)

Related concepts:
- [An Audit Trail Is a Chain of Evidence, Not a Developer Log](an-audit-trail-is-a-chain-of-evidence-not-a-developer-log.md)
- [Target High-Value AI Verticals as Capability Matures](target-high-value-ai-verticals.md)
- [Enterprise Coding Agents Need Ownership, Auditability, and Action Controls](enterprise-coding-agents-need-ownership-auditability-and-action-controls.md)
- [Pre-Measure Everything and Build Runtime Knobs Before You Need Them](pre-measure-everything-and-build-runtime-knobs-before-you-need-them.md)
- [Land the Data in One Governed Store So Agents Inherit Access Control](land-the-data-in-one-governed-store-so-agents-inherit-access-control.md)

Sources:
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 20:18-21:41
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 05:06-05:11, 19:26-20:19
