# Own the Context Layer and Rent Every Other Layer

Summary: Decide build-versus-buy once per architectural layer rather than once for the system. Orchestration, email, CRM, and enrichment are places where vendors are better and renting is correct; the context layer is the one to keep, because it encodes data models no generic tool can represent and because you cannot debug what you do not own.

Use when:
- Scoping an internal agent platform and deciding what to buy.
- Arguing against a build-everything or buy-everything default.
- Deciding where a small team's engineering capacity should go.

Details:
- The frame is per-layer, not per-system: "it's very tempting and trendy to say build everything. But what we found is that there are still key areas to build and rent access to at every single layer." ([Liu](../sources/20260826_L4I7WgiEquo.md), 17:25-17:35)
- The rented list is explicit — "we will not build a lot of these tools like orchestration, email, CRM. Vendors do that really well" — and matches the named stack: Temporal for durable orchestration, Clay for enrichment, Salesforce as CRM, Outreach and Nooks for outbound. "Since we are a lean team, we will not build our own email vendor or enrichment services like Clay. We use Clay." (08:44-08:52, 13:16-13:20, 17:52-18:02)
- **Two independent reasons are given for keeping the context layer, and the second is the less obvious one.** "We refuse to outsource the context layer because that's where our edge is. A generic tool can't capture all of our esoteric data models or workflows, and we do not want that context layer to be something we can't debug." Representational fit is the strategic reason; debuggability is an operational one that applies even where the data is not a differentiator. (18:02-18:17)
- The team's own claim about relative cost is the argument for building on the data model first: "internal agents are actually cheaper and faster to build than most people assume, and so since we have the most data on our data model, we build it there first and then we rented the generalizable parts later." Build order follows information advantage. (17:35-17:51)
- The ownership decision was made before the system was built, alongside the human-in-the-loop and eligibility decisions: "we decided that it was very important to own the context layer and we decided to rent everything else… we believe that we understood our customers the best, so we will not give that away." (08:37-09:00)
- The owned layer is a shared substrate rather than a private store, which is what makes owning it worth the cost: markdown plus databases and hierarchies, navigable by agents and designed for humans. (18:18-18:44)
- **Limit.** No vendor was evaluated on the record — no selection criteria, cost, migration experience, or failure with any of the rented systems is reported — and the "cheaper and faster than most people assume" claim carries no build cost, headcount, or timeline. (17:35-18:07)
- **The same conclusion with the ownership line drawn one notch differently, and an argument for renting the evals.** Berry agrees the data layer is where the work is, but treats the underlying facts as unavoidably rented — "there is literally hundreds of vendors… but none of those vendors is going to have a complete picture" — and locates the ownable part in the assembly: which providers to waterfall, which fields to refresh, and how entities resolve. He then makes the sharper concession: "either you or the vendor that you're using needs to run evals against these data providers," which allows renting the judgment about provider quality, not just the data. On orchestration he is explicitly indifferent — "whether you buy it or build it, I think this is like fundamentally the modern way to set this up" — which agrees with renting that layer while insisting on its shape. ([Berry](../sources/20260826_UhCY231d0FQ.md), 04:42-05:28, 09:24-09:32)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Product Strategy](../topics/product-strategy.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Build Core Agents and Buy Commodity Agent Workflows](build-core-agents-and-buy-commodity-agent-workflows.md)
- [Replace Buy-Versus-Build With Arbitrary Customizability](replace-buy-versus-build-with-arbitrary-customizability.md)
- [Decide the Agent Buy Boundary With Six Production Questions](decide-the-agent-buy-boundary-with-six-production-questions.md)
- [Put Humans and Agents on the Same Substrate Instead of an AI Layer on Top](put-humans-and-agents-on-the-same-substrate-instead-of-an-ai-layer-on-top.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Commoditize the Layer You Do Not Win On](commoditize-the-layer-you-do-not-win-on.md)
- [Waterfall Data Vendors and Run Evals to Decide Which to Trust](waterfall-data-vendors-and-run-evals-to-decide-which-to-trust.md)
- [Build Orchestration From a Few General-Purpose Node Types](build-orchestration-from-a-few-general-purpose-node-types.md)

Sources:
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 08:37-09:00, 13:16-13:20, 17:16-18:44
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 04:42-05:28, 09:24-09:32
