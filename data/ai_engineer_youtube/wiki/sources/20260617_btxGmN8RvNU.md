# Your Agent's Biggest Lie: "I Searched the Web"

Source: [Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data](https://www.youtube.com/watch?v=btxGmN8RvNU)
Uploaded: 2026-06-17
Transcript: `raw/20260617_btxGmN8RvNU/btxGmN8RvNU.en-orig.vtt`

## Summary

Rafael Levi (Bright Data) argues that the most damaging agent failure mode is silent: when an agent's web access is blocked by a CAPTCHA, an empty page, or anti-bot defenses, the model does not report the failure. Because LLMs are tuned to please, they fall back to stale training data or fabricate an answer and present it as current, which produces dead 404 citations and invented product links and prices. The talk frames the open web as actively adversarial to agents (Cloudflare blocks roughly 20% of the web to AI crawling by default and runs an "AI Labyrinth" that feeds detected bots fake data), and demos identical prompts with and without Bright Data's Web MCP across five anti-bot-heavy sites, where the no-MCP run fails all five and the MCP run succeeds. The mitigation is managed web-access infrastructure: residential IPs, human-like browser fingerprints, automatic CAPTCHA solving, scrape-to-markdown, batch search, parallel browser sessions, and pre-collected public datasets, scoped to public data only for legal safety, with the broad tool surface filtered down to the few tools a task needs.

## Extracted Concepts

- [Silent Web-Access Failure Produces Confident Hallucination](../concepts/silent-web-access-failure-produces-confident-hallucination.md) - blocked or empty web fetches are not reported, so the model fabricates instead of refusing.
- [The Open Web Is Adversarial to Agent Access](../concepts/the-open-web-is-adversarial-to-agent-access.md) - default crawling is blocked or poisoned, and prices vary by device, IP, and proxy.
- [Ground Agents With Managed Web-Access Infrastructure](../concepts/ground-agents-with-managed-web-access-infrastructure.md) - residential IPs, human-like browsers, CAPTCHA solving, scrape-to-markdown, batch search, and public datasets restore reliable retrieval.
- [MCP Tool Surfaces Need Default Context Budgets](../concepts/mcp-tool-surfaces-need-default-context-budgets.md) - a 66-69 tool web-access MCP should be filtered to the few tools a task needs.

## Topic Links

- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)
- [Evaluation](../topics/evaluation.md)
- [Security](../topics/security.md)

## Notes

- LLMs are "programmed to please" users, so the speaker would rather a model say "no, I can't," but it never does; it tries to make things up. (00:33-00:55)
- The web has fought robots and automations for years; CAPTCHAs are roughly a decade old, and now "AI is blocking AI," so web access is not as simple as it looks. (00:56-01:17)
- Cloudflare blocks AI crawling for about 20% of the web, so ~20% is not accessible by the default `fetch` built into AI. (01:43-01:53)
- Cloudflare's "AI Labyrinth" does not block a detected bot; it feeds it fake data, making results worse. (01:53-02:04, 10:04-10:15)
- The invisible failure mode: no error and no warning, just a wrong answer. The agent gets a CAPTCHA or even an empty page, does not say so, and makes something up, which is where most hallucinations come from. (02:07-02:23)
- Concrete symptoms: fabricated numbers, fake citations that 404, and product links where the URL and product do not exist; the speaker claims roughly 60% of ChatGPT citations are not working. (02:23-03:01)
- Demo design: identical prompts run with and without Bright Data's MCP, across five anti-bot-heavy sites (Rightmove property, LinkedIn, Instagram, Amazon, TikTok), using GPT-5, to "let the AI talk for itself." (03:15-04:24)
- Without MCP, the model has no live web data access and no browsing tools by default: zero success, five failed. (04:24-04:47)
- The MCP exposes 66-69 tools, including a search engine tool that runs real Google, Bing, and DuckDuckGo searches rather than the model's background "search the web." (04:56-05:14)
- "Scrape as markdown" curls any URL and returns markdown without HTML tags, so the agent does not waste tokens parsing HTML. (05:21-05:33)
- Search-engine batch sends ~100 keywords and returns 100 batched results for scale; "discover" exposes pre-built APIs for many sites. (05:33-05:50)
- The scraping browser is a remote browser the LLM can open and navigate; it solves CAPTCHA by itself, has a unique fingerprint, can run 100 browsers and multiple sessions in parallel without getting blocked. (05:50-06:11)
- With MCP, Rightmove, LinkedIn, Instagram, and Amazon all return real data; the LLM's own head-to-head comparison marks the no-MCP runs as failed (no live web access) and the MCP runs as successful. (06:13-06:27, 09:19-09:25)
- Legal posture: only public data, never behind-login data; logging in means accepting terms and conditions, which the speaker treats as illegal to scrape, and notes lawsuits (LinkedIn, Amazon) against scrapers. Using a public-data provider keeps the user from being sued. (06:50-08:42)
- IP quality matters: a datacenter or event-Wi-Fi IP is low quality and gets blocked, a home IP can reach maybe 5-10 profiles before a login wall, and the provider uses residential-quality access. (08:03-08:17)
- Pre-collected public datasets let the agent filter by criteria (for example, LinkedIn AI engineers in a region) instead of live scraping. (08:49-09:15)
- Anti-detection approach: rather than detecting Cloudflare Labyrinth, make the agent look like a human with pre-recorded mouse movement and human-like typing so it never triggers the block; misleading-data defenses (for example, Asian hotels showing different prices by device, IP, or proxy) are the toughest case, where the best bet is to look human and hope for the best. (10:51-11:53)
- Token efficiency: do not parse 10,000 pages with the LLM; have the LLM build a parser once and run it as a script, which the speaker says saves about 99% of tokens. A "skills" page can teach any agent to build such a scraper or pipeline. (12:38-13:38)
- Tool-budget caveat: the 66-69 tools are shown only for the demo; in production, filter to the few needed (for example, scrape-markdown plus search = two tools), otherwise you flood the context with irrelevant data. (13:41-14:03)
- Pricing: a free tier of 5,000 requests per month plus pay-as-you-go, framed as enough for an MVP or hackathon. (10:26-10:30, 15:07-15:32)
