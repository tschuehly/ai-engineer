# Publish Per-Site Skills So Agents Do Not Rediscover a Website

Summary: A browser agent that starts every run by exploring the page pays the discovery cost again each time. Attaching skills and memory *per website* — what tasks the site supports, how they are performed, what the selectors or tool calls are — lets the agent arrive already knowing, which is both a reliability and a token argument.

Use when:
- The same agent visits the same handful of sites repeatedly and re-derives the same navigation each run.
- Deciding what to persist between browser-agent runs: raw traces, a compact site skill, or nothing.
- Designing a browser-agent platform and choosing where site knowledge lives (in the agent, in a shared registry, or published by the site itself).

Details:
- The principle: "doing these things repeatedly, you want to benefit from things like memory and skills… Your agent doesn't have to discover something in the first place if it's done it before. It can use its memory and its skills to actually make it better." ([Paul Klein IV](../sources/20260814_GqoNrUz8hEU.md), 07:59-08:36)
- One shipped shape is a registry of site skills: Browserbase's `browser.sh` (as spoken) "publishes skills for websites. So before your agent even goes to the website, it can observe what types of tasks it can do." The knowledge is fetched *before* navigation, which is what makes it a planning input rather than a recovery aid. (08:04-08:18)
- WebMCP is treated as a supply of the same knowledge from the other side of the wire: "WebMCP is very useful for this. It's part of pulling in existing knowledge to optimize a website." A site that publishes its own tool list removes the need to learn it by exploration — see [Expose Site Capabilities to In-Browser Agents With WebMCP](expose-site-capabilities-to-in-browser-agents-with-webmcp.md). (08:18-08:26)
- Skills are not tied to pixel control. "If your agent is using CLIs to control websites like the Playwright CLI, you could actually give it skills and context to be more effective there" — the skill carries domain procedure regardless of whether the action layer is a click, a CLI, or a tool call. (08:26-08:36)
- The token argument is the reason to compress rather than cache raw pages: "if you're throwing everything on the page to a model, you're going to get sub-par results and it's going to cost you a lot. The right harness should not only present the right tools, but present an optimized amount of tokens that are compressed to get exactly the right repeatable result every single time." Note the claim about *quality*, not only cost — dumping the page degrades results, it does not merely make them expensive. (08:36-08:54)
- Relationship to the wiki's general skills material: [agent skills package progressive-disclosure context](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md) and [repository skills and AGENTS.md encode repeatable web workflows](repository-skills-and-agents-md-encode-repeatable-web-agent-workflows.md) both keep the skill next to the *repository*. Keying the skill to the *external site* is the variant this source adds, and it changes the maintenance question: the artifact goes stale when someone else's site changes, so it needs the same self-repair posture as a scraper ([Let an Agent Build and Maintain Self-Healing Scrapers](let-agents-build-and-maintain-self-healing-scrapers.md)).
- Ownership caveat worth stating: a site skill published by a third party is an assertion about someone else's product. It is durable knowledge only as far as the site is stable, which is why the observability-fed improvement loop matters — see [Expose Observability As Agent-Readable Feedback](expose-observability-as-agent-readable-feedback.md).

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Repository skills and AGENTS.md encode repeatable web-agent workflows](repository-skills-and-agents-md-encode-repeatable-web-agent-workflows.md)
- [Expose Site Capabilities to In-Browser Agents With WebMCP](expose-site-capabilities-to-in-browser-agents-with-webmcp.md)
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Give Browser Agents a Compact Whole-Page Representation](give-browser-agents-a-compact-whole-page-representation.md)
- [Let an Agent Build and Maintain Self-Healing Scrapers](let-agents-build-and-maintain-self-healing-scrapers.md)

Sources:
- [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../sources/20260814_GqoNrUz8hEU.md), 07:59-08:54
