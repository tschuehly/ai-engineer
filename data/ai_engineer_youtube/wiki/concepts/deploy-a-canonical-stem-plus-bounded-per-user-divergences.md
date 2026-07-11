# Deploy a Canonical Stem Plus Bounded Per-User Divergences

Summary: To make software adaptive per user without the brittleness of "millions of tangled AI code bases," deploy one canonical *stem* and let every user run a bounded, immutable, individually reversible *divergence* of it. The failure mode people fear is unmanaged divergence inside a single artifact; the containment comes from structure — isolated divergences whose blast radius is one user context and that roll back live with no deploy.

Use when:
- Designing per-user, runtime-adaptive, or agent-modified software and needing an architecture that contains rather than multiplies risk.
- Answering the objection "you want me to reason about a million AI-generated versions?"
- Deciding where the source of truth, provenance, and rollback boundaries live once there is no single frozen artifact.

Details:
- The architecture: "instead of one code base gated by flags and shipped to everyone, you deploy one canonical stem and every user runs her own divergence of it. Same origin, but individually adapted live" — moving "from the least[-worst] first version for everyone to the best version for anyone."
- The brittleness people picture "is a specific type of failure mode — unmanaged divergence inside a single artifact" (thousand-line files where "everything can touch everything else, no boundaries"); that is brittle "because there's no structure separating things," not because it is AI-generated. Stem-plus-divergences "is the opposite of that": divergences are "bounded, isolated, and individually reversible."
- Containment properties: "the blast radius of a change in the system is one context," and "any single divergence can roll back live with no deploy." A bad variant cannot silently corrupt the stem or reach another user — "the thing that you're afraid of is the thing that this architecture exists to prevent."
- Developer-set boundaries: the developer declares "what can and cannot be adapted." A form can be adapted to improve conversion, but specific fields "can never be dropped," and areas like auth or payments "should always be off limits for any sort of adaptation." Adaptation can be system-observed (a CRM stops surfacing fields the investor always skips, creates an intro path she always logs, reprioritizes deals she checks) or user-requested, and a user's request is implemented without going back to the developer only if it stays "within the boundaries the developer sets" and "within the spirit / purpose of the software."
- Source of truth: with no single artifact, "the software" is "the stem plus all the immutable divergences," and identifying "what is this user running and why?" becomes "a graph query versus a version number." A bug report "describes a program that exists for that specific user," so every divergence must be "immutable, inspectable, attributable" and traceable back to the signal and adaptation that produced it.
- Coordination across a million versions: "don't merge code, merge intent, merge outcome" — "everyone converges on the same goal through their own path," not the same commit.
- Where the hard work is: "Generation has become easy… the easy 80%." The business is "observability, validation, coordination" — "the substrate is stem plus divergences, provenance, validation." A correct change is not enough; you also need *desirability* (was it an uplift on the metric that matters — retention, churn, support tickets), because "anyone can make a code change now, but the hard part is knowing whether you actually found an improvement." Autonomy is framed as an earned-trust problem: "the challenge isn't building more control, it's winning enough trust that you don't have to."

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [The Frozen-Artifact Pipeline Is a Cost Constraint, Not a Law](frozen-artifact-pipeline-is-a-cost-constraint-not-a-law.md)
- [Branchable Cloud Workspaces Make Agent Actions Reversible](branchable-cloud-workspaces-make-agent-actions-reversible.md)
- [Constrain Agent Effects, Not Expression, With a Typed SDK](constrain-agent-effects-not-expression-with-a-typed-sdk.md)
- [Think Wider, Not Bigger: Compete on Breadth via User Extensibility](think-wider-not-bigger-compete-on-breadth-via-extensibility.md)

Sources:
- [The Pipeline Is Dead](../sources/20260707_bRnoEpoK5m4.md), 08:02-13:10, 13:40-18:25
