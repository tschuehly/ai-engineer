# Context as a Service Is Vertical Search for Agents

Summary: A distinct vendor category sits between general AI search and the old data-as-a-service incumbents: providers that crawl one slice of the web, resolve it into deduplicated entities in a knowledge graph, enrich those entities from multiple sources, and expose the result to agents over MCP, CLI, or API. They behave like vertical search engines — narrow domain, high quality inside it — and choosing between them and general search is a routing decision per task, not a vendor bake-off.

Use when:
- Deciding whether an agent's web-facing knowledge work should call a general AI search API, a domain-specific context vendor, or a pipeline you own.
- Serving several internal teams with different research needs and tempted to point all of them at one search tool.
- Mapping the vendor landscape between "search" and "data provider" and finding the labels do not fit.

Details:
- The definition, from Bright Data's Omer Primor: "We like to call them internally CaaS, context as a service, because that's what they do. They allow agents to tap into them, MCP, CLI, just pure or good old API, and actually start extracting data… to retrieve data so they can reason over for whatever knowledge work they are responsible for." (06:32-06:53)
- The step past crawling is what makes the category: "they don't only just discover the web… crawling… searching… accessing, extracting the data, and indexing it, they take it a step further. They actually develop knowledge graphs to start structuring all of the entities and to dedupe them. And they start enriching them with a lot of different sources, so they actually start merging all of that data." (07:06-07:27)
- The shape that results: "they kind of behave like vertical search engines… very, very, very good search engine for something very specific." Named verticals: e-commerce, travel, finance, market research, HR, real estate, retail, GTM, and sales intelligence. (06:53-07:04, 07:27-07:45)
- Positioning against the incumbents is explicit and hedged: "it's fine to think of CaaS as an evolution of DaaS, and it is in a way, but it's catering for a very specific need, as much as the AI search engines are different than Google. When agents need them, it's different than people." ZoomInfo is the worked example — it launched `gtm.ai` as "a secondary brand… catering specifically for the need of agents. Straight from Claude Code, straight from Codex, or any other agent. They understand the gap." (08:18-09:07)
- Price and quality already stratify inside the category rather than converging. In the test that accompanies this talk, the cheapest vendor was also the lowest-coverage one, which the speaker reads as market structure rather than failure: "niche players that have… lower quality data but much cheaper. They're already carving that niche of the long tail… of small shops or small usage that don't want to pay as much and don't need as much data." One unnamed vendor was "the bar farther[st] most expensive in the industry." (13:02-13:38)
- The consumption decision is per task, not per organization: "If I'm an AI engineer, I need to serve different teams. They may have different needs. It's very tempting to throw AI search at all of them, but maybe that's not optimal. Maybe I need a combination of both." He calls the discipline of choosing "web context engineering." (09:10-09:52)
- The category exists because the market that spawned it is crowding: the AI-search cohort (Perplexity, You.com, Tavily and others) indexes the web "especially for agents, not even looking at the humans involved anymore," Amazon shipped its own index for retrieving agent context on AgentCore, and Microsoft repackaged search into its agentic development and orchestration suite two weeks earlier. (04:28-05:35)
- Caveat before adopting the framing wholesale: the speaker leads product marketing at a web-data company, and the vertical examples he lists are all members of his employer's startup program — a disclosure he makes himself. The structural description of the pipeline survives that; the market sizing is not independently supported here. (07:45-08:06)
- **A vendor in this category describing what it uses its own index for internally.** Exa — "a search engine for agents… this web MCP web tool that agents can access" — runs its own crawl and embeddings to classify every company in its addressable market and attach anticipated spend, rather than to answer a query. That is a use case worth asking any context vendor about: whether the surface supports enumeration and filtering over the whole corpus, or only ranked retrieval per query, because market mapping needs the former and account research needs the latter. ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 00:40-00:58, 05:22-06:58)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [A Prebuilt Context Vendor Cannot Answer Outside Its Index](a-prebuilt-context-vendor-cannot-answer-outside-its-index.md)
- [Find the Crossover Point Between Renting and Owning Context](find-the-crossover-point-between-renting-and-owning-context.md)
- [Go Straight to the Known Source Instead of Searching for It](go-straight-to-the-known-source-instead-of-searching-for-it.md)
- [AI-Native Search APIs Serve Agent Query Shapes](ai-native-search-apis-serve-agent-query-shapes.md)
- [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md)
- [Knowledge graphs make agent memory traversable and explainable](knowledge-graphs-make-agent-memory-traversable-and-explainable.md)
- [Classify the Whole Addressable Market Instead of Searching It Account by Account](classify-the-whole-addressable-market-instead-of-searching-it.md)
- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](treat-go-to-market-as-a-live-model-of-your-world.md)

Sources:
- [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](../sources/20260814_Ot4OPrPH4xY.md), 04:28-09:52, 13:02-13:38
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 00:40-00:58, 05:22-06:58
