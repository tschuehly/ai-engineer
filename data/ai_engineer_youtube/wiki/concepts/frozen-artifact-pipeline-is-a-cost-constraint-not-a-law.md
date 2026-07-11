# The Frozen-Artifact Pipeline Is a Cost Constraint, Not a Law

Summary: The one-way software distribution stack (CI, packagers, registries, container images, app-store review) exists only to move a *frozen artifact* to every machine once, and "one version for everyone" was never a fact about software — it was a consequence of change-production being expensive and rare. As that cost collapses toward zero and production can happen at runtime on the server, client, or in the user's live session, the boundary between development and distribution dissolves.

Use when:
- Deciding whether "we build once and ship the same version to everyone" is a requirement or just an inherited default.
- Evaluating per-user, runtime-generated, or agent-modified software and needing the economic argument for why it is newly viable.
- Reasoning about what parts of a system must be frozen at build time versus produced live in front of the user.

Details:
- The whole distribution stack solves exactly one problem: get a frozen artifact "from machine where it was built to the machine where it runs, safely, reproducibly, once." Every production guarantee (reproducibility, previewability, rollback) "flows from one fact: there is one artifact and it doesn't change after we ship it."
- The one-way pipeline "is not arbitrary; it's the direct consequence of production of software being expensive and risky." Because a correct, scoped change took skilled humans hours or days, teams "did it rarely… verified it and froze it… and shipped that frozen thing to everyone."
- A per-user version "never had to win an argument" and was never rejected in a meeting — it "just wasn't an option," because giving users different software "meant forking the code base and hand-maintaining both," which doesn't scale. So teams treated one-version-for-everyone "as a fact about software like gravity" when it was "a fact about cost and budget and the economics."
- The load-bearing shift is not that AI writes code ("table stakes"); it is *where and how cheap*: "the cost of producing a correct and scoped change is collapsing towards zero," and "the production of the software no longer has to happen in one place up front before anyone runs it" — part on the server, part on the client, part in the user's live session, placed "wherever it makes most sense, including right in front of the user."
- Consequence: "when the agent is the runtime, when the thing that runs your software can also modify it, development and distribution stop being two phases… the boundary blurs and it's gone." The pipeline "didn't fail because it didn't work anymore, but the constraint it was built for went away."
- Demand for per-user software is decades old and was only gated by cost — the forward-deployed engineer / professional-services industry, developers rebuilding dotfiles and editor config by hand on every machine, and Excel as "millions of people that all build their own programs on top of it." Feature flags, segmentation, and A/B testing were the forced predecessors that could only make software diverge into "buckets and segments that you declare in advance."
- Historical analogy for the skepticism: a bank with no branches "sounded reckless," and "a decade later the branch is the weird part"; an engineer once "used to fight with engineers about why you need builds and CI."

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Deploy a Canonical Stem Plus Bounded Per-User Divergences](deploy-a-canonical-stem-plus-bounded-per-user-divergences.md)
- [Rescope Ambition Down a Tier as Models Improve](rescope-ambition-down-a-tier-as-models-improve.md)
- [Think Wider, Not Bigger: Compete on Breadth via User Extensibility](think-wider-not-bigger-compete-on-breadth-via-extensibility.md)

Sources:
- [The Pipeline Is Dead](../sources/20260707_bRnoEpoK5m4.md), 00:07-05:02, 06:47-08:00, 18:25-19:43
