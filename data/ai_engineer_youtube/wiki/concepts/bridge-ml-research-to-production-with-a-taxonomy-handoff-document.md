# Bridge ML Research to Production With a Taxonomy Handoff Document

Summary: Make an ML research prototype legible to production engineers and PMs by writing a "research prototype taxonomy" document — a software-engineering technical design doc / RFC adapted for machine learning — before the productionization handoff, so the baton pass between paper-fluent researchers and production-grade engineers is a systems-and-process artifact rather than an ad-hoc conversation.

Use when:
- An ML researcher has a proven prototype that platform/back-end/infra engineers (unfamiliar with CV or LLM-training methodology) must now stand up in production.
- You want to raise the velocity of an R&D-to-production pipeline and diagnose where it stalls.
- You need to onboard software engineers, AI engineers, and PMs onto a research initiative and make it obvious where each should concentrate and which tasks to pluck off.

Details:
- The gap is a two-sided handoff, not a modeling problem: production engineers know robust code but not CV/LLM-training research; researchers track the latest papers but have not owned production-grade APIs. Treat closing it as a systems-and-process problem (01:16-02:40).
- The RPT is "just a technical design document from software engineering with some specific twists" for ML, kept in any written doc (the team uses Notion). It follows the established practice (cited via a Pragmatic Engineer blog) of writing tech-design docs / RFCs / specs before building to align scaling teams (03:37-04:30).
- ML-specific sections come first: (1) **domain context and novel data representations** — the domain lingo and data shapes a newcomer must know (a party diagram, a graph for a home's circulation, embedding/latent-space representations); framed as "picture a software engineer we just hired from JP Morgan — what do they need to know?"; (2) **business goal** — why solving this matters and the value of the ML tool (04:30-05:23).
- Conventional TDD sections follow: (3) the **type contract** between the core product repo and the ML repo and how those types stay in sync; (4) the **persistence layer**, deliberately *not* where the researcher should sink time — mapping how far they got is a good first entry point for software-engineering help; (5) the **system architecture / anatomy** (is it a workflow, a chaining of workflows, external LLM calls?); (6) the **merge/decompose plan** (05:23-06:38).
- The document is also the input to decomposition: its mapped layers, architecture, persistence, and types "inform your decomposition strategy" when the prototype is sliced into stacked PRs (12:14-12:31).
- Diagnostic for this lever: when new staff join a research initiative, is it obvious where they should concentrate and clear which tasks to pluck off to productionize? Ambiguity is the signal to revisit the RPT process (12:53-13:21).

Related topics:
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Structure the ML Codebase as Decoupled Per-Researcher Microservices](structure-the-ml-codebase-as-decoupled-per-researcher-microservices.md)
- [Use the Agent to Surface Your Own Unknowns](use-the-agent-to-surface-your-own-unknowns.md)
- [Spec-Driven Development Turns Prompts Into Requirements, Design, and Tasks](spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md)

Sources:
- [Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc](../sources/20260628_OXMMN-XbxwA.md), 01:16-06:38, 12:14-13:21
