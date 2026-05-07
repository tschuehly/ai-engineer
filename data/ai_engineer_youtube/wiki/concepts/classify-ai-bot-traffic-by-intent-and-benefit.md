# Classify AI Bot Traffic By Intent And Benefit

Summary: AI bot defenses should distinguish search crawlers, training crawlers, user-triggered fetchers, and browser-like operator agents because each has different site-owner benefit and abuse risk.

Use when:
- Designing crawler and agent access policy for a public site.
- Separating legitimate user-delegated automation from bulk scraping or inventory abuse.

Details:
- Search-style AI crawlers can create citations and referral traffic, while training crawlers may consume bandwidth without direct site-owner benefit. User-triggered fetchers such as a chat product retrieving a URL occupy a middle ground because they may represent a real user's request. (05:02-06:16)
- Browser-like operator agents are harder to classify because they may act for a legitimate user in a real browser-like environment, or they may automate unwanted actions such as bulk ticket purchasing. (06:39-07:28)
- A binary good-bot/bad-bot taxonomy is too coarse for AI traffic; access rules should encode the site's desired outcomes and acceptable automation patterns. (03:48-04:47)

Related topics:
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Layer Bot Detection Signals Instead Of Trusting One Header](layer-bot-detection-signals-instead-of-trusting-one-header.md)

Sources:
- [How to defend your sites from AI bots - David Mytton, Arcjet](../sources/20250730_Gi4V8viBGYQ.md), 03:48-07:28
