# Classify AI Bot Traffic By Intent And Benefit

Summary: AI bot defenses should distinguish search crawlers, training crawlers, user-triggered fetchers, and browser-like operator agents because each has different site-owner benefit and abuse risk.

Use when:
- Designing crawler and agent access policy for a public site.
- Separating legitimate user-delegated automation from bulk scraping or inventory abuse.

Details:
- Search-style AI crawlers can create citations and referral traffic, while training crawlers may consume bandwidth without direct site-owner benefit. User-triggered fetchers such as a chat product retrieving a URL occupy a middle ground because they may represent a real user's request. (05:02-06:16)
- Browser-like operator agents are harder to classify because they may act for a legitimate user in a real browser-like environment, or they may automate unwanted actions such as bulk ticket purchasing. (06:39-07:28)
- A binary good-bot/bad-bot taxonomy is too coarse for AI traffic; access rules should encode the site's desired outcomes and acceptable automation patterns. (03:48-04:47)

- The agent-platform side states the same taxonomy failure as a design gap rather than a policy choice: "the web was built to stop bad bots, but now there's good agents and bad bots. How do we delineate between the two?" — and concludes that classification cannot be resolved from traffic signals alone, because the missing piece is an issuer willing to vouch for an agent and its vendor. See [Agent Trust Needs a Certificate Issuer, Not a CAPTCHA](agent-trust-needs-a-certificate-issuer-not-a-captcha.md). ([Paul Klein IV](../sources/20260814_GqoNrUz8hEU.md), 12:37-13:39)

Related topics:
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Layer Bot Detection Signals Instead Of Trusting One Header](layer-bot-detection-signals-instead-of-trusting-one-header.md)
- [Agent Trust Needs a Certificate Issuer, Not a CAPTCHA](agent-trust-needs-a-certificate-issuer-not-a-captcha.md)

Sources:
- [How to defend your sites from AI bots - David Mytton, Arcjet](../sources/20250730_Gi4V8viBGYQ.md), 03:48-07:28
- [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../sources/20260814_GqoNrUz8hEU.md), 12:37-13:39
