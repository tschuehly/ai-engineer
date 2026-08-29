# Keep Geolocation Consistent Across Pipeline Stages

Summary: Many sites serve different content by visitor location — stock, sizes, prices, currency, availability — so an agent's apparent location is a correctness parameter, not just an anti-blocking one. If the stage that discovers and verifies an item and the stage that acts on it exit from different locations, the pipeline validates one world and transacts in another, and the mismatch surfaces at the last and most expensive step.

Use when:
- Building an agent that reads a page to establish a fact and later acts on that fact through a different fetch path.
- Debugging an agent that verifies availability and then fails at checkout, or reports a price the user never sees.
- Configuring proxies, regions, or a managed browser across a multi-stage web pipeline.

Details:
- **The observed failure.** In the browser-driven original, "even if it worked, items ended up being unavailable at checkout because in the discovery phase he was not able to use geolocation capabilities, and a lot of e-commerce websites take the user's location into account when displaying stock, options, sizes and so forth." The agent's earlier stages were not wrong about *a* store; they were right about a different store than the one it eventually reached. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 06:08-06:30)
- **The fix is stated as a consistency property, not as a feature.** The scraper used for verification "supports geolocation options. So I can localize my results and get relevant content," and the browser used for checkout carries "a geolocation capability. So my results are localized the same way as in the verification stage." The phrase that matters is *the same way as* — either stage alone being geo-aware does not help. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 11:07-11:30, 12:58-13:20)
- **Why it hides until the end.** Every earlier stage returns a well-formed, valid, non-blocked page. There is no error, no empty result, and nothing for a validity check to catch — the content is real, it is just addressed to someone else. This makes locale drift invisible to the checks recommended in [Validate Retrieved Content Before Spending Tokens on It](validate-retrieved-content-before-spending-tokens-on-it.md), which asks whether a page is genuine rather than whether it is *yours*.
- **The same phenomenon, read two other ways in this wiki.** Bright Data's Rafael Levi frames it as ambiguity — hotel sites serving different prices "by device, computer, or proxy," so "the same query returns three different correct answers and the agent cannot tell which is real" ([The Open Web Is Adversarial to Agent Access](the-open-web-is-adversarial-to-agent-access.md)). Payment-side sources frame it as a money risk: prices "drift across regions, currencies, and taxes, so a number parsed off a page may not be the real charge" ([Separate Non-Deterministic Discovery From Deterministic Payment Execution](separate-non-deterministic-discovery-from-deterministic-payment.md)). This page adds the engineering handle the other two lack: the variation is not noise to be tolerated, it is a parameter to be pinned, and pinning it identically across stages converts an unanswerable "which price is real" into "the one for the location we transacted from."
- **Design consequence.** Locale belongs in the pipeline's configuration alongside credentials and timeouts, propagated to every fetch path, and it is a real constraint on using different vendors per stage: two providers that both support geolocation may not resolve the same nominal region to the same exit behaviour. That is a compatibility question to ask before splitting stages across providers, and neither the talk nor this wiki has evidence on how closely providers agree.
- **Scope.** The evidence here is e-commerce, where location dependence is universal and consequential. The failure generalizes to any locale-sensitive surface — regional pricing pages, licensing and content availability, localized search rankings, region-gated documentation — but the specific vanishing-at-checkout instance is retail.
- **Caveat.** Vendor talk; geolocation support is a stated product capability with no measurement of how often the mismatch caused the original failures.

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [The Open Web Is Adversarial to Agent Access](the-open-web-is-adversarial-to-agent-access.md)
- [Separate Non-Deterministic Discovery From Deterministic Payment Execution](separate-non-deterministic-discovery-from-deterministic-payment.md)
- [Assign a Web-Access Primitive Per Pipeline Stage](assign-a-web-access-primitive-per-pipeline-stage.md)
- [Validate Retrieved Content Before Spending Tokens on It](validate-retrieved-content-before-spending-tokens-on-it.md)
- [Hold the Browser Environment Constant Across Runs](hold-the-browser-environment-constant-across-runs.md)
- [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md)
- [Rendered State Is Not in the HTML](rendered-state-is-not-in-the-html.md)
- [Keep a Protocol Boundary So the Browser Backend Stays Swappable](keep-a-protocol-boundary-so-the-browser-backend-stays-swappable.md)
- [Agentic Commerce Moves From Static Stores to Intent Infrastructure](agentic-commerce-moves-from-static-stores-to-intent-infrastructure.md)

Sources:
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 06:08-06:30, 11:07-11:30, 12:58-13:20
