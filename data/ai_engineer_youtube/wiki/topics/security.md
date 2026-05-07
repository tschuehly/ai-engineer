# Security

## Overview

AI security includes the controls that keep agents, model calls, generated code, private inference, and public web surfaces from turning useful automation into abuse or data exposure. For public sites, AI-era traffic makes the old good-bot/bad-bot split insufficient: search crawlers, training crawlers, user-triggered fetchers, and browser-like operator agents have different incentives and site-owner benefits. Defenses therefore need policy, identity verification, economic friction, and request-shaping layers rather than one universal block rule.

Bot defense is a layered infrastructure problem. `robots.txt` expresses cooperative crawler policy but does not stop adversarial clients. User-agent rules catch many honest crawlers but must be paired with IP or reverse-DNS verification before a claimed crawler identity is trusted. IP reputation, data-center detection, proxy and VPN signals, country metadata, and residential/mobile classification add useful context, but they are noisy and can be gamed through residential proxy networks. When traffic remains suspicious, CAPTCHA or proof-of-work challenges can shift cost onto the requester, but they should be evaluated against attack incentives, accessibility, and legitimate-user friction.

Rate limiting also needs better keys than source IP alone. Automated clients can rotate IPs across large address pools while retaining stable TLS, HTTP, or browser characteristics, so fingerprints and authenticated session IDs are often stronger quota keys. Emerging approaches such as HTTP message signatures and private access tokens point toward more verifiable automated-client identity, but they still need adoption and should be treated as part of a layered design.

Agent tool access has a separate identity problem. Long-lived API keys in MCP config files are not a durable security model for large agent fleets; OAuth can move agent access toward short-lived scoped tokens, but the OAuth roles should stay clean. MCP servers are safer and easier to operate when they behave as resource servers that verify tokens while a separate authorization server handles login, consent, token issuance, and policy. Future agent systems also need verified agent identities, transaction-specific permissions for high-impact actions, and chain-of-custody when one agent, MCP server, or upstream API delegates to another.

## Key Concepts

- [Classify AI Bot Traffic By Intent And Benefit](../concepts/classify-ai-bot-traffic-by-intent-and-benefit.md) - access rules should distinguish search, training, user-triggered, and operator-style AI traffic.
- [Layer Bot Detection Signals Instead Of Trusting One Header](../concepts/layer-bot-detection-signals-instead-of-trusting-one-header.md) - bot identity needs multiple request, IP, and reputation signals.
- [Treat CAPTCHA And Proof Of Work As Economic Friction](../concepts/treat-captcha-and-proof-of-work-as-economic-friction.md) - challenges deter by changing economics, not by proving humanity perfectly.
- [Key Rate Limits By Fingerprint Or Session Instead Of IP Alone](../concepts/key-rate-limits-by-fingerprint-or-session-instead-of-ip-alone.md) - limits should follow stable client or user identity where possible.
- [Model MCP Servers as OAuth Resource Servers](../concepts/model-mcp-servers-as-oauth-resource-servers.md) - MCP authorization should keep token issuance separate from tool-serving logic.
- [Authenticate Agents With URL-Based PKI Identities](../concepts/authenticate-agents-with-url-based-pki-identities.md) - agent clients need verifiable identity when they act without a human delegation flow.
- [Authorize High-Impact Agent Actions Transactionally](../concepts/authorize-high-impact-agent-actions-transactionally.md) - sensitive actions need amount-, budget-, or action-specific authorization rather than broad standing scopes.
- [Preserve Authorization Chain of Custody Across Agent Hops](../concepts/preserve-authorization-chain-of-custody-across-agent-hops.md) - authorization context should survive MCP-to-API and agent-to-agent delegation.

## Open Questions

- Which HTTP message signature and private access token patterns will get enough crawler, browser, and site adoption to become practical for general bot policy?
- Which agent identity and attestation patterns will become practical enough for open MCP ecosystems without recreating brittle pre-registration workflows?

## Sources

- [How to defend your sites from AI bots - David Mytton, Arcjet](../sources/20250730_Gi4V8viBGYQ.md)
- [How to Secure Agents using OAuth - Jared Hanson (Keycard, Passport.js)](../sources/20250730_blmAkayzE8M.md)
