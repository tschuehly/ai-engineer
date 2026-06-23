# Ground Agents With Managed Web-Access Infrastructure

Summary: Reliable web grounding for agents needs an access layer that defeats anti-bot defenses rather than a raw fetch: residential-quality IPs, human-like browser fingerprints, automatic CAPTCHA solving, scrape-to-markdown, batch search, parallel sessions, and pre-collected public datasets. The strategy is to make the agent look like a human and avoid getting blocked, scoped to public data for legal safety.

Use when:
- Building agents whose answers depend on hard-to-reach public sites (marketplaces, social, listings) that block default crawlers.
- Choosing between a raw HTTP fetch, a self-run headless browser, and a managed web-access provider.

Details:
- A web-access tool surface bundles several primitives: a real search-engine tool (Google, Bing, DuckDuckGo) instead of the model's background "search the web," scrape-as-markdown that returns clean markdown so the agent does not waste tokens parsing HTML, batch search (about 100 keywords to 100 batched results), pre-built per-site APIs, and a remote scraping browser the LLM can open and navigate. (04:56-05:56)
- The scraping browser solves CAPTCHA by itself, carries a unique fingerprint, and can run 100 browsers and multiple sessions in parallel without getting blocked. (05:50-06:11, 09:28-09:44)
- The anti-detection strategy is to make the agent look like a human (pre-recorded mouse movement, human-like typing) rather than reverse-engineer each defense, so a system such as Cloudflare's labyrinth never even challenges it. (10:51-11:25)
- Pre-collected public datasets are an alternative to live scraping: the agent can filter a maintained dataset by criteria (for example, LinkedIn AI engineers in a region) when fresh-to-the-minute data is not required. (08:49-09:15)
- Legal posture is part of the design: only public data, never behind-login content, because logging in means accepting terms and conditions, and scrapers have faced lawsuits (LinkedIn, Amazon); a public-data provider keeps the user from being sued. (06:50-08:42)
- Token efficiency at scale: do not parse 10,000 pages with the LLM; have the LLM build a parser once and run it as a script, which the speaker claims saves about 99% of tokens versus per-page LLM parsing. (12:38-13:38)
- Even with the access layer, the broad tool catalog (66-69 tools in the demo) should be filtered to the few a task needs, or it floods the context with irrelevant data. (13:41-14:03)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Silent Web-Access Failure Produces Confident Hallucination](silent-web-access-failure-produces-confident-hallucination.md)
- [The Open Web Is Adversarial to Agent Access](the-open-web-is-adversarial-to-agent-access.md)
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Expose Search Controls For Agentic Retrieval](expose-search-controls-for-agentic-retrieval.md)

Sources:
- [Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data](../sources/20260617_btxGmN8RvNU.md), 04:56-09:44, 10:51-14:03
