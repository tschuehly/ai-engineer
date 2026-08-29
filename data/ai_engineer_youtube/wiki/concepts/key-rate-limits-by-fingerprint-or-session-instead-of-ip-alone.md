# Key Rate Limits By Fingerprint Or Session Instead Of IP Alone

Summary: Rate limits are more robust when keyed by user session or client fingerprint rather than source IP alone, because automated clients can rotate addresses while retaining stable request characteristics.

Use when:
- Designing abuse limits for public web endpoints, forms, or scarce inventory flows.
- Investigating crawler traffic spread across many IPv4 or IPv6 addresses.

Details:
- Network and HTTP fingerprints can hash request characteristics such as TLS configuration or header patterns so a site can identify the same client across changing IP addresses. (16:56-18:04)
- JA4-style TLS fingerprints and HTTP request fingerprints can become rule keys for blocking or throttling high-volume clients across many IPs. (17:28-18:04)
- Rate limiting by source IP alone is weak because ordinary users' IPs change and malicious crawlers can rotate addresses; logged-in user session IDs and fingerprints are stronger quota keys. (18:10-18:41)
- Emerging HTTP message signatures and private access tokens aim to make client identity more verifiable, but adoption and value beyond existing IP verification are still uncertain. (15:34-16:50)
- **The internal-traffic version of the same problem is credential granularity, not client identity.** Inside an organization the callers are known, so the limit key is the credential — and the failure mode is a shared one. Manuja's rule is to "make sure that your API keys are segregated per route, per use case, to the most granular thing that you can imagine," because "having a noisy tenant can be one of the biggest problems here." The shared principle across both settings is that a rate limit is only as useful as the stability and specificity of the thing it is keyed on. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 13:24-13:48)

Related topics:
- [Security](../topics/security.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Layer Bot Detection Signals Instead Of Trusting One Header](layer-bot-detection-signals-instead-of-trusting-one-header.md)
- [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md)

Sources:
- [How to defend your sites from AI bots - David Mytton, Arcjet](../sources/20250730_Gi4V8viBGYQ.md), 15:34-18:41
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 13:24-13:48
