# Works in Dev, Passes Tests, and Survives Reality Are Three Different Systems

Summary: For any component whose dependency is an adversary rather than an API — live web retrieval, anti-bot-defended targets, changing page layouts — passing your own tests proves nothing about production, because the environment reacts to you. Patricija Žemaitytė's team hit a sub-second search target in under two weeks, then got blocked live on the demo call with the client, and had to start over.

Use when:
- Grounding an agent or RAG pipeline on live web data, search results, or any target that actively defends against automated clients.
- Deciding how much confidence a green test suite or a successful staging benchmark should buy for a launch date.
- Explaining to stakeholders why a working prototype is not a shippable data pipeline.

Details:
- The concrete failure: after a rebuild reached ~650 ms P90 against a 4-second baseline in under two weeks, "we're sitting on a call with the client getting ready to test out our new product, and while we were on the call, we got blocked. And we got blocked really bad." Nothing worked afterward; the team started over. (09:24-10:10)
- The lesson she draws is the three-way split: "there is a difference between system that works in development, system that works in a test, and system that actually survives reality." (09:52-10:01)
- The second iteration was the hardest because reality forced an unwanted dependency back in: they "had to rely a lot on browsers," and browsers are "slow, expensive, complex, and deeply incompatible with dreams about low latency" — the client wanted sub-second, reality needed browsers, and browsers wanted four seconds. (10:10-10:49)
- The adversary is not static, so this is not a one-time hardening cost: "the targets change, layouts change, detection changes, market itself changes, client needs changes… this is not a build-once business. This is an adapt-forever business." (17:11-17:34)
- The generalizable posture is to treat the messy maintenance underneath — reaching the open web, collecting reliably, dealing with anti-bot systems, handling browsers when needed, structuring and delivering data — as a standing operational load someone must carry, whether that is your team or a vendor. (16:24-17:11)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md)
- [Let an Agent Build and Maintain Self-Healing Scrapers](let-agents-build-and-maintain-self-healing-scrapers.md)
- [Silent Web-Access Failure Produces Confident Hallucination](silent-web-access-failure-produces-confident-hallucination.md)
- [Layer Bot Detection Signals Instead of Trusting One Header](layer-bot-detection-signals-instead-of-trusting-one-header.md)
- [Realistic Traffic, Not Volume, Is the Hard Part of Load Testing](realistic-traffic-not-volume-is-the-hard-part-of-load-testing.md)

Sources:
- [How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs](../sources/20260814_1UmZHb_E_SM.md), 09:24-10:49, 16:24-17:34
