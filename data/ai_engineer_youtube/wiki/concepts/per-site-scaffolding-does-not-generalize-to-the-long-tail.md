# Per-Site Scaffolding Does Not Generalize: The Bitter Lesson for Web Agents

Summary: Every wrapper, selector map, or site-specific adapter you write buys exactly one website. The capability that transfers to the other 200 million is the one the web was actually designed for — a general agent that looks at the rendered page and acts on it. Scaffolding is worth building as an optimization on sites you visit often; it is not worth mistaking for the path to coverage.

Use when:
- Choosing between building N site adapters and investing in one general computer-use loop.
- Deciding how much of a browser agent's competence may live in per-site artifacts (skills, selector maps, recorded scripts).
- Justifying why a system that works on the ten sites you tested collapses on the eleventh.

Details:
- **The claim, in the speaker's framing.** "In a way this is the bitter lesson for web agents — the more you end up writing scaffolds around existing websites, it doesn't actually generalize to the long tail of the web. The thing that generalizes is the thing that it was designed for, which is the most general solution: just pixels in." ([Dhruv Batra](../sources/20260814_Ki980nV0__0.md), 12:24-12:53)
- **What "general" buys, concretely.** The capability test he offers is a possibility claim rather than a reliability claim: "if you can do it on your browser, this model can accomplish it in principle. In practice, of course, there are accuracy gaps… whereas in a lot of earlier cases, even in principle that task may not be solvable." The example is validating a discount code whose constraints (specific product, date window, minimum cart threshold) are described in natural language — "there is no API for this. The way to do it is just like a human can: you go to that website, you find the product… you apply the discount code, and you check whether the claim of 22% off was met or not," 20-40 steps. (13:10-14:16)
- **Generality is a floor, not a ceiling.** The same talk immediately qualifies the pixels-in position: "just because for the long tail you need to have a capability does not mean that is the only way you should do it." The next Navigator version writes JavaScript in the page when that is faster — the working rule being "click buttons when you have to, write code when you have to, and look at the result through pixels." See [Pair Clicking With Generated Code and Replayed Network Requests](pair-clicking-with-generated-code-and-replayed-network-requests.md). (14:16-15:23)
- **The boundary against the wiki's per-site knowledge pages, which this does *not* refute.** [Per-site skills fetched before navigation](publish-per-site-skills-so-agents-do-not-rediscover-a-website.md) and [self-healing scrapers](let-agents-build-and-maintain-self-healing-scrapers.md) are both site-specific by construction, and both are defended on repeat-visit economics: you visit the same site many times, so paying discovery once is cheap. That argument is orthogonal to coverage. The two positions are compatible under one rule — *scaffolding may make a known site cheaper, but the agent's competence must not depend on it*, or the first unseen site is a hard failure rather than a slow success. Note the asymmetry in who each is written for: a platform serving arbitrary user tasks lives on the long tail; a team automating twelve known vendor portals does not.
- **Why this is not the usual "scaffolding is brittle" complaint.** The standard argument against site adapters is maintenance (selectors change, so the adapter rots). This argument is about *reach*: even a perfectly maintained adapter set covers only the sites someone wrote adapters for, against a tail of roughly 200 million active sites that no team will enumerate — see [The Long Tail of the Web Will Not Ship APIs](the-long-tail-of-the-web-will-not-ship-apis.md). Both arguments hold; they fail differently and need different remedies.
- **The countervailing evidence the wiki already holds.** Several sources argue the opposite emphasis for *today's* systems — that the harness, not the model, is what is missing ([Fix the Browser-Agent Runtime Interface](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)) and that a thick harness is correct early and thins later ([Keep the Harness Thick Early and Thin It as the Model Improves](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md)). Batra is a model builder, and his "bitter lesson" is the training-side statement of the same trajectory: harness work that is *general* (an action space, a verification channel, a page representation) survives model improvement, while harness work that is *per site* is the part the model is expected to absorb.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Models](../topics/models.md)

Related concepts:
- [The Long Tail of the Web Will Not Ship APIs](the-long-tail-of-the-web-will-not-ship-apis.md)
- [Rendered State Is Not in the HTML](rendered-state-is-not-in-the-html.md)
- [Publish Per-Site Skills So Agents Do Not Rediscover a Website](publish-per-site-skills-so-agents-do-not-rediscover-a-website.md)
- [Pair Clicking With Generated Code and Replayed Network Requests](pair-clicking-with-generated-code-and-replayed-network-requests.md)
- [Keep the Harness Thick Early and Thin It as the Model Improves](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md)
- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)

Sources:
- [Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](../sources/20260814_Ki980nV0__0.md), 12:24-15:23
