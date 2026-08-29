# Last-Mile Domain Context Beats Model Chasing

Summary: In vertical AI applications, stronger models can establish a useful baseline, but the final performance gap often depends on customer-specific domain context and workflow interpretation. The durable advantage is a system that keeps translating expert insight into model-usable context.

Use when:
- Deciding whether a specialized AI product needs more model work or more domain-context infrastructure.
- Explaining why vertical AI products need workflow-specific context and expert iteration after general reasoning is good enough.

Details:
- Anterior frames the core bottleneck as whether the model understands the specific industry, customer, and workflow, not merely whether the base model can reason, 01:19-01:55.
- The clinical example shows that a seemingly simple policy question hides domain ambiguity around what qualifies as conservative therapy, what counts as unsuccessful treatment, and how much documentation can be inferred, 02:25-05:02.
- The talk reports that model and pipeline work reached a strong baseline around 95%, while the adaptive domain-intelligence loop pushed performance toward 99% by adding customer and domain context, 05:29-06:33.
- The structural reason this gap keeps appearing, from a different source: digital work is "millions of these micro worlds," each with "its unique local physics, like different structures, constraints, affordances, and dynamics that you have to learn," and "even if you're using the same software, every company configure it differently" ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 05:25-06:24). On that account Anterior's last five points are not a property of clinical review — they are what a general model structurally cannot hold, so the same gap should be expected in any vertical.
- The complementary framing for what the domain loop is actually supplying: intelligence "solves the problem through the context" it was handed, while expertise "will bring you the right context. Given any problem, we know what context [to] bring in are important" ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 09:20-09:49). Anterior's expert loop is a mechanism for acquiring that selection policy, which is why it keeps paying after the base model improves.

- **The same argument made about a production environment rather than a professional domain.** Justin Smith (Resolve AI) grants the base capability outright — "models have gotten incredibly capable over the last year, but especially over the last like 6 months or so" — and places the gap in per-customer environment knowledge: "truly understanding your environment and the way that your services interact and where the hotspots are, keeping track of all of that sort of understanding is incredibly difficult," which is why "every company is a unique place. That's why we spend so much time on our knowledge system." Two differences from the Anterior case are worth noting: the context here is about a system's topology rather than a profession's ambiguity, and it decays continuously ("grow as your system evolves"), so the loop cannot converge the way an expert-labelling loop can. No accuracy numbers are offered — this is the claim without Anterior's 95%-to-99% evidence. ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 03:00-03:12, 06:36-07:32, 23:09-23:28)
- **The blunt statement of why the last mile is the whole distance: "the exceptions are the job."** Shenoy contrasts the way LLM tasks are usually pictured — "it's a slope. You got a bike. And there's clear sight to success" — with the terrain of real services work: "there are hills and ravines. There's death by a thousand paper cuts. But that's what real work looks like. That's the entire job. The exceptions are the job. That's the demo. That's the actual job." He decomposes the residual into three axes rather than one: customization per company ("every company does things very differently"), per user ("the way each user does their work is very unique"), and per client ("the way you work with every client is different"). Each multiplies the others, which is why a single domain-context loop does not converge the way a single-customer one does. ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 12:40-13:43)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Build Domain-Specific Workflow Wrappers Around Models](build-domain-specific-workflow-wrappers-around-models.md)
- [Resolve AI Capability Risk Before Product Surface Commitment](resolve-ai-capability-risk-before-product-surface-commitment.md)
- [Digital Work Is Millions of Microworlds With Local Physics](digital-work-is-millions-of-microworlds-with-local-physics.md)
- [Expertise Compresses the Search; Intelligence Expands It](expertise-compresses-the-search-intelligence-expands-it.md)
- [Separate Execution From the Production Context That Judges It](separate-execution-from-the-production-context-that-judges-it.md)
- [Co-Design In Person Because Remote Channels Filter the Requirements](co-design-in-person-because-remote-channels-filter-the-requirements.md)

Sources:
- [Make your LLM app a Domain Expert: How to Build an Expert System - Christopher Lovejoy, Anterior](../sources/20250728_MRM7oA3JsFs.md), 01:19-06:33
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 03:00-03:12, 06:36-07:32, 23:09-23:28
- [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 05:25-06:24, 09:20-09:49
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 12:40-13:43
