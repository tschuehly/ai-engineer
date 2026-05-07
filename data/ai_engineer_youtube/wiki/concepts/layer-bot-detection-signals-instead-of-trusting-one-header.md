# Layer Bot Detection Signals Instead Of Trusting One Header

Summary: Bot detection needs layered evidence because robots.txt is voluntary, user-agent strings are spoofable, IP reputation is noisy, and no single signal is fully accurate.

Use when:
- Building request admission rules for web apps exposed to crawlers, scrapers, and agents.
- Reviewing whether a bot-defense system will block spoofed or rotating automated clients.

Details:
- `robots.txt` is useful for expressing crawler policy and guiding cooperative clients, but malicious clients can ignore it or use it to discover disallowed paths. (07:42-08:37)
- User-agent strings help classify many crawlers and can be backed by open source user-agent lists, but they are just HTTP header strings that a client can set to anything. (08:40-09:33)
- Claimed identities from Apple, Bing, Google, OpenAI, and similar crawlers should be verified with source IP and reverse DNS checks before allow-listing. (09:36-10:23)
- IP metadata such as data-center origin, network operator, country, VPN, proxy, residential, and mobile classification is useful but imperfect because geolocation can be wrong and residential proxy services can disguise crawler traffic. (10:27-12:56)

Related topics:
- [Security](../topics/security.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Classify AI Bot Traffic By Intent And Benefit](classify-ai-bot-traffic-by-intent-and-benefit.md)
- [Key Rate Limits By Fingerprint Or Session Instead Of IP Alone](key-rate-limits-by-fingerprint-or-session-instead-of-ip-alone.md)

Sources:
- [How to defend your sites from AI bots - David Mytton, Arcjet](../sources/20250730_Gi4V8viBGYQ.md), 07:42-12:56
