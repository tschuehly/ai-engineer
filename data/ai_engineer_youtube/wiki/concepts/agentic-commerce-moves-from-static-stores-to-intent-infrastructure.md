# Agentic Commerce Moves From Static Stores to Intent Infrastructure

Summary: Agentic commerce treats buyers, sellers, and the transaction protocol as AI-mediated participants rather than assuming users browse static product pages. The durable design shift is from page navigation toward explicit buying and selling intent that agents can reason over.

Use when:
- Designing shopping, procurement, marketplace, or checkout workflows for AI agents.
- Deciding whether a commerce agent should browse a website, call a product API, or negotiate against higher-level intent.

Details:
- Behrens defines a store as both a location and a protocol for facilitating transactions among merchants and buyers, then argues that AI digitizes the participants and their interactions rather than only the merchandise and distribution. (01:58-02:47)
- The agentic commerce stack changes static websites into merchant agents, consumer browsing into consumer agents, and low-level payment infrastructure into higher-level intent infrastructure while still optimizing for transactions. (02:21-02:47)
- Buyer intent can be explicitly captured from conversations or by asking a user agent, rather than inferred only from keyword searches, click data, and site metrics. (06:23-06:50)
- The hard product problem is resolving fuzzy intent such as "running shoes" into SKU-level inventory and transaction-ready options without forcing the user to provide a product-detail-page URL first. (06:57-07:18)
- Seller intent also becomes dynamic: merchants may expose realtime availability, contextual pricing, inline discounts, and bundles across merchants instead of only static product detail pages. (07:49-08:20)
- **The B2B mirror, where the agent procures infrastructure rather than goods.** Garvin separates the two markets explicitly — B2C is "agentic commerce," while in the Metronome case "we're talking about in a B2B context" — and the B2B transaction shown is an agent "literally procuring their initial Stripe instance as well as additional backend services" through a CLI. The seller-side obligation is the same discoverability problem in a different medium: "make your services discoverable to agents that may be building an application or working in the open web," with Vercel and Hugging Face named as providers onboarding into that environment. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 10:07-10:33, 17:14-17:31)
- **Autonomy is staged, and the industry is deliberately parked at the first stage for a liability reason.** Prio describes the present as "human in the loop" with autonomous shopping — an agent that "goes around, talks to different merchants… negotiate, does the payment" — as the ideal end state, and names what holds the gap open: "we're just not confident yet. We want more human in the loop, a merchant to be talking to a payment processor who will take the responsibility, or in this case, liability, to actually initiate the payments." The blocker is who is answerable for a wrong purchase, not model capability. His sizing — "about 45% of all agent sessions… are related to shopping" and "$7 billion… might go up to $65 billion by 2030" — is stated without a source. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 01:43-02:35, 04:11-04:17, 09:36-10:03)

- **What the unassisted path costs while the intent infrastructure is being built.** A worked shopping agent operating against ordinary retail sites — no protocol, no product feed, no cooperating merchant — decomposes into discovery, decision, user confirmation, and execution, and every stage is shaped by anti-bot defenses rather than by commerce semantics: blocked discovery truncates the choice set, unvalidated pages bill tokens for reading CAPTCHAs, an ungeolocated verification stage yields items that vanish at checkout, and checkout itself needs source-level browser stealth to complete. That is the concrete price of the status quo this page's protocols are meant to replace, and it sharpens the argument for them — not "browsing is inelegant" but "the access layer is a per-transaction cost with an unpredictable tail." See [Assign a Web-Access Primitive Per Pipeline Stage](assign-a-web-access-primitive-per-pipeline-stage.md). ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 03:45-04:47, 05:05-06:30, 08:39-09:44, 12:37-13:20)

Related topics:
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)
- [AI Monetization](../topics/ai-monetization.md)

Related concepts:
- [Measure AI intensity by human input to valuable output](measure-ai-intensity-by-human-input-to-valuable-output.md)
- [Agent Experience Means Autonomous Access, Understanding, and Operation](agent-experience-means-autonomous-access-understanding-and-operation.md)
- [Turn AI Product Intents Into Contained Workflows](turn-ai-product-intents-into-contained-workflows.md)
- [Separate Agent as Product, Agent as Buyer, and Agent as User](separate-agent-as-product-buyer-and-user.md)
- [Map the Agentic Commerce Protocol Stack by Layer](map-the-agentic-commerce-protocol-stack-by-layer.md)
- [Assign a Web-Access Primitive Per Pipeline Stage](assign-a-web-access-primitive-per-pipeline-stage.md)
- [Keep Geolocation Consistent Across Pipeline Stages](keep-geolocation-consistent-across-pipeline-stages.md)

Sources:
- [Machines of Buying and Selling Grace - Adam Behrens, New Generation](../sources/20250723_zlZz0mDF2eg.md), 01:58-02:47, 06:23-08:20
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 10:07-10:33, 17:14-17:31
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 01:43-02:35, 04:11-04:17, 09:36-10:03
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 03:45-04:47, 05:05-06:30, 08:39-09:44, 12:37-13:20
