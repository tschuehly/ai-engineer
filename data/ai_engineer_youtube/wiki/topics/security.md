# Security

## Overview

AI security includes the controls that keep agents, model calls, generated code, private inference, and public web surfaces from turning useful automation into abuse or data exposure. For public sites, AI-era traffic makes the old good-bot/bad-bot split insufficient: search crawlers, training crawlers, user-triggered fetchers, and browser-like operator agents have different incentives and site-owner benefits. Defenses therefore need policy, identity verification, economic friction, and request-shaping layers rather than one universal block rule.

Bot defense is a layered infrastructure problem. `robots.txt` expresses cooperative crawler policy but does not stop adversarial clients. User-agent rules catch many honest crawlers but must be paired with IP or reverse-DNS verification before a claimed crawler identity is trusted. IP reputation, data-center detection, proxy and VPN signals, country metadata, and residential/mobile classification add useful context, but they are noisy and can be gamed through residential proxy networks. When traffic remains suspicious, CAPTCHA or proof-of-work challenges can shift cost onto the requester, but they should be evaluated against attack incentives, accessibility, and legitimate-user friction.

Rate limiting also needs better keys than source IP alone. Automated clients can rotate IPs across large address pools while retaining stable TLS, HTTP, or browser characteristics, so fingerprints and authenticated session IDs are often stronger quota keys. Emerging approaches such as HTTP message signatures and private access tokens point toward more verifiable automated-client identity, but they still need adoption and should be treated as part of a layered design.

These same defenses look different from the agent-builder's side, where the open web is an adversarial environment for retrieval rather than a resource to protect. A default agent fetch cannot reach roughly 20% of the web that blocks AI crawling, and some defenses (for example Cloudflare's AI Labyrinth) poison rather than block by serving fake data to detected bots. The agent-side countermeasures mirror the defender stack in reverse: residential-quality IPs to escape datacenter-IP reputation, human-like browser fingerprints and behavior to avoid challenges, and automatic CAPTCHA solving. That symmetry is why bot policy is hard to win permanently, and why teams scraping the public web also carry a legal boundary, restricting collection to public, non-login data because logging in accepts terms and conditions and has drawn lawsuits.

Agent tool access has a separate identity problem. Long-lived API keys in MCP config files are not a durable security model for large agent fleets; OAuth can move agent access toward short-lived scoped tokens, but the OAuth roles should stay clean. MCP servers are safer and easier to operate when they behave as resource servers that verify tokens while a separate authorization server handles login, consent, token issuance, and policy. Enterprise MCP servers also need ordinary SaaS security controls: SSO, lifecycle management, provisioning, access controls, audit logs, abuse controls, input validation, and DLP. Gateways add a practical enforcement point when many internal agents need remote MCP access: they can keep user credentials away from every service, constrain outbound external connectivity, and centralize audit, policy, malicious-server blocking, and content classification over standardized MCP messages. Future agent systems need verified agent identities, transaction-specific permissions for high-impact actions, and chain-of-custody when one agent, MCP server, or upstream API delegates to another. The hard part is not only hosting the MCP workload, but propagating enforceable authorization through background agents, service accounts, MCP servers, and A2A-style delegation without relying on model obedience as the security boundary. Agentic commerce makes transaction authority especially concrete: a shopping agent may use a virtual card, delegated authentication to a user's existing card, or an agent-owned spending instrument, but each option needs explicit authorization boundaries because software is initiating purchases that move money and create merchant obligations.

Agent application security is broader than prompt injection and OAuth. Red-team evidence from live startup agents shows ordinary web and infrastructure bugs becoming agent bugs: IDOR appears when tools accept user IDs or document IDs without per-object authorization, service-level backend permissions let an agent traverse data beyond the represented user, code sandboxes can expose files, metadata services, service tokens, and customer data, and SSRF can leak credentials when tools fetch user-controlled repositories or URLs from privileged infrastructure.

Code-executing agents add another security boundary because the useful capability is also RCE-shaped. A reasoning model that can decide when to write and run code may simplify agent loops, but it also needs isolated execution, default-limited filesystem access, network restrictions, dependency checks, and reviewable outputs. Prompt injection is especially dangerous when untrusted web or GitHub issue content enters the same loop that can read a repository and make outbound requests. Model-level suspicion helps, but deterministic system controls such as sandbox policy, network allowlists, HTTP method restrictions, and human review of sensitive operations carry the hard security boundary.

OpenHands reinforces that sandboxing is only one layer. Docker containers can separate autonomous shell work from the user's workstation, but credentials such as GitHub tokens or AWS access still need least-privilege scoping because they grant authority outside the container.

Enterprise coding-agent rollouts also need an accountability layer around ordinary development actions. Security review should ask where audit logs live, who owns an agent's actions, how destructive commands are constrained, and what responsibility model applies when a codebase-changing agent acts on behalf of a team.

Regulated consumer AI also needs output-integrity controls, not only access controls. In tax explanations, legal and privacy risk make it important that LLM text does not hallucinate numbers or unsupported advice; authoritative values should come from tax engines, and guardrails should inspect raw model responses before users see them.

## Key Concepts

- [Vet MCP Servers As Action-Capable Extensions](../concepts/vet-mcp-servers-as-action-capable-extensions.md) - MCP servers connected to coding agents can access data and act for users, so trust and scope are security decisions.
- [Classify AI Bot Traffic By Intent And Benefit](../concepts/classify-ai-bot-traffic-by-intent-and-benefit.md) - access rules should distinguish search, training, user-triggered, and operator-style AI traffic.
- [Layer Bot Detection Signals Instead Of Trusting One Header](../concepts/layer-bot-detection-signals-instead-of-trusting-one-header.md) - bot identity needs multiple request, IP, and reputation signals.
- [Treat CAPTCHA And Proof Of Work As Economic Friction](../concepts/treat-captcha-and-proof-of-work-as-economic-friction.md) - challenges deter by changing economics, not by proving humanity perfectly.
- [Key Rate Limits By Fingerprint Or Session Instead Of IP Alone](../concepts/key-rate-limits-by-fingerprint-or-session-instead-of-ip-alone.md) - limits should follow stable client or user identity where possible.
- [The Open Web Is Adversarial to Agent Access](../concepts/the-open-web-is-adversarial-to-agent-access.md) - the agent-builder side of bot defense: blocked, poisoned, and device-variant pages degrade web grounding.
- [Model MCP Servers as OAuth Resource Servers](../concepts/model-mcp-servers-as-oauth-resource-servers.md) - MCP authorization should keep token issuance separate from tool-serving logic.
- [Enterprise MCP Requires SaaS Security Controls](../concepts/enterprise-mcp-requires-saas-security-controls.md) - production MCP needs SSO, provisioning, audit, DLP, abuse prevention, and access controls.
- [MCP Gateways Create an Enterprise Root of Trust](../concepts/mcp-gateways-create-an-enterprise-root-of-trust.md) - gateway policy points can reduce decentralized credential, network, audit, and malicious-server risk.
- [Dynamic Client Registration Pressures MCP Auth Stacks](../concepts/dynamic-client-registration-pressures-mcp-auth-stacks.md) - MCP client registration can overwhelm ordinary application-management surfaces.
- [Authorization Propagation Is the Hard Part of Enterprise Agent Workloads](../concepts/authorization-propagation-is-the-hard-part-of-enterprise-agent-workloads.md) - background agents need enforceable scopes and access context across MCP, A2A, and service-account boundaries.
- [Authenticate Agents With URL-Based PKI Identities](../concepts/authenticate-agents-with-url-based-pki-identities.md) - agent clients need verifiable identity when they act without a human delegation flow.
- [Authorize High-Impact Agent Actions Transactionally](../concepts/authorize-high-impact-agent-actions-transactionally.md) - sensitive actions need amount-, budget-, or action-specific authorization rather than broad standing scopes.
- [Preserve Authorization Chain of Custody Across Agent Hops](../concepts/preserve-authorization-chain-of-custody-across-agent-hops.md) - authorization context should survive MCP-to-API and agent-to-agent delegation.
- [Treat Agents As Users For Authorization](../concepts/treat-agents-as-users-for-authorization.md) - agent tools need requester-scoped authorization rather than service-level trust.
- [Do Not Roll Your Own Agent Code Sandbox](../concepts/do-not-roll-your-own-agent-code-sandbox.md) - code execution boundaries can become arbitrary execution and lateral movement.
- [Server-Side Request Forgery Exfiltrates Agent Credentials](../concepts/server-side-request-forgery-exfiltrates-agent-credentials.md) - privileged agent fetch tools can leak tokens to attacker-controlled endpoints.
- [Treat Code-Executing Agents as RCE-Risk Surfaces](../concepts/treat-code-executing-agents-as-rce-risk-surfaces.md) - shell and code execution should be designed as an intentional remote-code-execution risk.
- [Give Code-Executing Agents Isolated Computers](../concepts/give-code-executing-agents-isolated-computers.md) - agent execution should happen in a dedicated container, VM, or OS sandbox with reviewable outputs.
- [Restrict Agent Internet Access With Allowlists](../concepts/restrict-agent-internet-access-with-allowlists.md) - network access should be disabled or constrained by explicit domains, commands, and HTTP methods.
- [Keep Human Review on High-Risk Agent Operations](../concepts/keep-human-review-on-high-risk-agent-operations.md) - LLM monitors help, but sensitive commands, dependency changes, and diffs still need accountable review.
- [Enterprise Coding Agents Need Ownership, Auditability, and Action Controls](../concepts/enterprise-coding-agents-need-ownership-auditability-and-action-controls.md) - enterprise agent security needs audit logs, responsibility boundaries, and controls for destructive actions.
- [Human Ownership Keeps Agent Pull Requests From Bypassing Review](../concepts/human-ownership-keeps-agent-pull-requests-from-bypassing-review.md) - agent PR identity should not bypass second-human review or leave failures ownerless.
- [Delegate Agentic Commerce Transactions With Explicit Payment Authority](../concepts/delegate-agentic-commerce-transactions-with-explicit-payment-authority.md) - commerce agents need bounded payment authority before buying for users.
- [Ground Regulated Explanations in Deterministic Engines](../concepts/ground-regulated-explanations-in-deterministic-engines.md) - high-liability answers should keep authoritative calculations outside the model and check generated text for invented values.

## Open Questions

- Which HTTP message signature and private access token patterns will get enough crawler, browser, and site adoption to become practical for general bot policy?
- Which agent identity and attestation patterns will become practical enough for open MCP ecosystems without recreating brittle pre-registration workflows?
- How should code-executing agent products balance full-auto sandboxed work against approval fatigue for commands that are low-risk individually but high-risk in aggregate?

## Sources

- [Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft](../sources/20250726_DdaAABdAqZY.md)
- [How to defend your sites from AI bots - David Mytton, Arcjet](../sources/20250730_Gi4V8viBGYQ.md)
- [How to Secure Agents using OAuth - Jared Hanson (Keycard, Passport.js)](../sources/20250730_blmAkayzE8M.md)
- [(possible dupe but better sound) What does Enterprise Ready MCP mean? - Tobin South, WorkOS](../sources/20250627_0MqYA52iWQU.md)
- [How we hacked YC Spring 2025 batch's AI agents - Rene Brandel, Casco](../sources/20250730_kv-QAuKWllQ.md)
- [OpenAI on Securing Code-Executing AI Agents - Fouad Matin (Codex, Agent Robustness)](../sources/20250730_w7IMuYsBNr8.md)
- [Remote MCPs: What we learned from shipping - John Welsh, Anthropic](../sources/20250619_0NHCyq8bBcM.md)
- [Ship Production Software in Minutes, Not Months - Eno Reyes, Factory](../sources/20250725_iheWKg2Tkrk.md)
- [Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands](../sources/20250725_o_hhkJtlbSs.md)
- [Machines of Buying and Selling Grace - Adam Behrens, New Generation](../sources/20250723_zlZz0mDF2eg.md)
- [How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit](../sources/20250723__zl_zimMRak.md)
- [Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data](../sources/20260617_btxGmN8RvNU.md)
