# Push a Product Feed, Because Per-Merchant Catalog Search Does Not Scale

Summary: The intuitive agentic-commerce design — the assistant calls each merchant's search API at query time — is not what the major specs implement. Both ACP and UCP require merchants to push a product feed the aggregator indexes ahead of time, for an M×N fan-out reason and a ranking-and-retail-media reason, which moves freshness, schema translation, and sync cost onto the merchant.

Use when:
- Designing how a merchant, marketplace, or catalog owner exposes inventory to shopping assistants.
- Weighing a pull API against a pushed feed for any agent-facing data surface with many consumers.
- Estimating the real integration cost of selling inside ChatGPT, Gemini, or Meta surfaces.

Details:
- The design that surprises engineers: "normally, you would assume that this would be a search catalog. However, both ACP and UCP right now, so Gemini and ChatGPT, does not support that search catalog call. They want you to send that feed to them." ([Prio](../sources/20260827_G7cgLjZtmMU.md), 08:35-08:57)
- The technical reason is fan-out at query time: "if you have M number of merchants and N number of products, now it has to call that many. While if you send the product feed ahead of time, we can index that and be ready to offload when you ask for something." Pre-indexing turns a fan-out per query into an ingest per merchant. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 09:06-09:19)
- The commercial reason is named first and left unexplored: "sponsored products, retail media related things, ranking." An aggregator that holds the index controls placement; an aggregator that federates search at query time does not. The talk does not say who ranks, on what signal, or whether position is purchasable — which is the central commercial question the design creates. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 08:57-09:12)
- Why the feed exists at all rather than crawling: "we don't want to go through your PDP and crawl and figure out every specific attribute. Merchant, just tell us. And also, those products change a lot. So, maybe you can tell us when they change as well." Push also solves change notification, which crawling handles badly. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 08:03-08:35)
- The merchant pays a schema tax, not a one-time integration. ACP, UCP, and Meta's product feed shown side by side are "similar, but still different. Everyone has an opinion. They think their opinion is the best one, and that's what they're rolling with. So, there's three different specifications right here." The practical shape is one canonical internal catalog plus N serializers — which is what Prio's giveaway catalog-sync service does, letting you "type in your own product and then turn it into ACP or UCP or meta." ([Prio](../sources/20260827_G7cgLjZtmMU.md), 09:19-09:30, 19:36-19:56)
- Feeds are a running process with a freshness window, not a handoff. In the demo, "every couple of seconds, we try to get the catalog in sync for what is in inventory, what's not." The window between syncs is where price and stock drift live, and it is a failure mode the pull design would not have had. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 15:00-15:13)
- This qualifies the more common wiki position that per-merchant feeds are the legacy path a unified product API replaces. Behrens argues feeds force chat products to "work individually with each merchant"; Prio reports the two largest surfaces choosing exactly that, and for a reason a unified API layer does not remove — the aggregator wants the index in its own hands. The reconciliation is that an aggregation layer is valuable *to the merchant* as a fan-out point for many feeds, not as a substitute for feeds.
- Caveat: the M×N argument is asserted, not worked through. It says nothing about caching, partial or category-scoped feeds, or hybrid designs where a feed carries the head of the catalog and a live call resolves the tail — all of which are unaddressed in the talk.

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)
- [AI Monetization](../topics/ai-monetization.md)

Related concepts:
- [Expose Commerce Data Through Agent-Native Product APIs](expose-commerce-data-through-agent-native-product-apis.md)
- [Map the Agentic Commerce Protocol Stack by Layer](map-the-agentic-commerce-protocol-stack-by-layer.md)
- [Agent Protocols Must Encode the Distinctions the User Interface Collapses](agent-protocols-must-encode-the-distinctions-the-ui-collapses.md)
- [Merchant-Owned Generative Surfaces Travel Into Chat Interfaces](merchant-owned-generative-surfaces-travel-into-chat-interfaces.md)
- [Agentic Commerce Moves From Static Stores to Intent Infrastructure](agentic-commerce-moves-from-static-stores-to-intent-infrastructure.md)

Sources:
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 08:03-09:30, 15:00-15:13, 19:36-19:56
