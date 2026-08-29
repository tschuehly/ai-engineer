# Assign a Web-Access Primitive Per Pipeline Stage

Summary: An agent that touches the web usually has several stages with different requirements, and giving all of them the same access primitive — almost always a browser, because it is the one that can do everything — makes the cheap stages pay the expensive stage's bill. Choose per stage: a search API where the job is to find URLs, a scrape-to-markdown call where the job is to read a page, and a real browser only where inputs must be filled and state is genuinely dynamic.

Use when:
- Designing or auditing an agent that searches, reads, and then acts on real websites.
- A browser-driven agent is slow, expensive, and unreliable across the board, and the instinct is to optimize the browser rather than to remove it from three of four stages.
- Deciding what a web-access tool surface should expose to an agent, and at what granularity.

Details:
- **The failure this prevents.** A vibe-coded personal shopping agent "was using a browser automation framework for everything and it was slow, expensive and unreliable," producing "a product that does not work and is expensive to run." The diagnosis was not model quality: "he was missing… an infrastructural layer that would allow this agent to operate freely on the open web." ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 01:33-02:32)
- **The rule, borrowed from scraping rather than from agent design.** "Use a browser when you absolutely have to." It sits under a single organizing constraint — "cost matters" — alongside validating content and preferring lighter payloads, and the talk's whole structure is that rule applied stage by stage. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 02:59-03:45, 14:03-14:35)
- **Stage 1, discovery — a search API, not a browser and not a hardcoded list.** The original queried a fixed set of major retailers' search pages through browser automation. Six problems compounded: no stealth, so CAPTCHAs and hard access failures; retries that stretched the flow; an unpredictable cost per transaction; a choice set capped by the hardcoded list ("selection of items would only be limited to the few choices he put in"); JavaScript-heavy pages; and no geolocation. The replacement returns "a compact JSON which is less than 2,000 tokens per response" in "less than 700 milliseconds on average," so the agent "formulates fan out queries and selects the relevant URLs from search results" instead of being handed them. Because the payloads are small, "there's no need for complicated models" here — the stage gets a cheaper model as well as a cheaper fetch. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 05:05-07:56)
- **Stage 2, reading pages — a scraper that returns markdown.** No browser in the agent's process: a "lightweight REST API" that runs "hundreds of requests in parallel," returns markdown so raw HTML never reaches the model, and "runs a full browser under the hood" only when the site is dynamic. That last clause is the important one — the browser does not disappear, it moves out of the agent's cost and reliability envelope and into the provider's, where it is amortized. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 10:29-11:30)
- **Stage 3, acting — a browser, without apology.** "This time you absolutely need to use a browser. We need to process inputs and the content is highly dynamic." The criterion is stated as a conjunction: form input plus dynamic state. A stage that only reads meets neither. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 11:54-12:37)
- **How this differs from the per-page escalation ladder the wiki already holds.** [Climb a Humanness Ladder Only as High as the Page Forces](climb-a-humanness-ladder-only-as-high-as-the-page-forces.md) applies the same stopping rule *within* one page interaction, escalating from synthetic click to trusted input to human-like motion. This applies it *across* the pipeline, and the selection is made at design time from what the stage needs rather than at run time from how the page resists. The two compose: pick the primitive per stage, then, inside whatever stage kept the browser, climb only as far as the page forces.
- **The economic shape.** The expensive primitive is not merely slower; it is the one whose per-transaction cost is unpredictable, because retries against anti-bot defenses are unbounded. Moving three stages onto fixed-price calls converts most of the pipeline from a variable, tail-heavy cost into a quoted one, which is a different kind of win from a percentage saving.
- **Caveat.** Each replacement primitive here is the speaker's employer's product, and no end-to-end comparison is measured — no per-transaction cost, success rate, or latency for the rebuilt pipeline. The 2,000-token and 700-millisecond figures are stated specifications, not observations. The transferable part is the decomposition and the selection rule; the vendor choice is not evidence.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Retrieval](../topics/retrieval.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Climb a Humanness Ladder Only as High as the Page Forces](climb-a-humanness-ladder-only-as-high-as-the-page-forces.md)
- [Use Browser UI Control When APIs Are Absent](use-browser-ui-control-when-apis-are-absent.md)
- [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md)
- [Validate Retrieved Content Before Spending Tokens on It](validate-retrieved-content-before-spending-tokens-on-it.md)
- [Keep Geolocation Consistent Across Pipeline Stages](keep-geolocation-consistent-across-pipeline-stages.md)
- [Keep a Protocol Boundary So the Browser Backend Stays Swappable](keep-a-protocol-boundary-so-the-browser-backend-stays-swappable.md)
- [Separate Non-Deterministic Discovery From Deterministic Payment Execution](separate-non-deterministic-discovery-from-deterministic-payment.md)
- [Go Straight to the Known Source Instead of Searching for It](go-straight-to-the-known-source-instead-of-searching-for-it.md)
- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)
- [Move Mandatory Brittle Tool Steps Outside the Agent Loop](move-mandatory-brittle-tool-steps-outside-the-agent-loop.md)
- [Fail Loudly and Bill Only for Successful Results](fail-loudly-and-bill-only-for-successful-results.md)
- [Give Browser Agents a Compact Whole-Page Representation](give-browser-agents-a-compact-whole-page-representation.md)
- [Rendered State Is Not in the HTML](rendered-state-is-not-in-the-html.md)
- [AI-Native Search APIs Serve Agent Query Shapes](ai-native-search-apis-serve-agent-query-shapes.md)
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Vibe Coding Hangover Is a Maintainability Failure](vibe-coding-hangover-is-a-maintainability-failure.md)
- [Agentic Commerce Moves From Static Stores to Intent Infrastructure](agentic-commerce-moves-from-static-stores-to-intent-infrastructure.md)

Sources:
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 01:33-03:45, 05:05-07:56, 10:29-12:37, 14:03-14:35
