# Split Agent Advocacy Into Engineering, Product, and Marketing Flavors

Summary: "Make our product work well for agents" is three jobs with different skills and different artifacts — building the MCP interface and its instrumentation, owning the end-to-end agentic experience as a product surface, and owning how agents enter the funnel. Naming the three lets a team staff the ones it needs instead of assigning the whole thing to one person and getting whichever third they happen to be good at.

Use when:
- Assigning ownership for agent-facing product work that spans engineering, product, and marketing.
- A developer-relations or developer-experience function is being redefined around agent users.
- Deciding which agent-experience work is missing rather than merely under-resourced.

Details:
- **The premise: the seams got fuzzier, and that is workable.** Asked whether agent advocacy is engineering, product, or marketing, the answer is "yeah, yes, yes. It's all of those things. And with the rise of agents it hasn't gotten any clearer… everybody's role across the organization has gotten fuzzier. So that actually helps in a lot of ways." The three flavors are described as mix-and-match "depending on whatever skills and abilities various employees have… and whatever the product needs at a given time," not as three headcount requisitions. ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 13:10-14:05)
- **Engineering flavor.** Partners directly with the engineering team on "these interfaces for how the agent is talking to your product like through the MCP server and building out these evals and the instrumentation." The concrete artifacts are the tool surface, the with-and-without benchmark, and trace capture — see [Benchmark Your Own Tool by Running Agents With and Without It](benchmark-your-tool-by-running-agents-with-and-without-it.md). (14:05-14:18)
- **Product flavor.** Owns "the end-to-end agentic experience," translating evals for the product team and maintaining "agent experience rubrics" for how the agent encounters your content. This is the flavor that turns trace findings into prioritized product change rather than a list of tool-description edits. (14:18-14:31)
- **Marketing flavor.** Owns "that pipe gen and how the agents are entering the funnel and finding out about your product and then bringing the developers along with them by surfacing those recommendations." The measurement instrument for this flavor is the GEO prompt set — see [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md). (14:31-14:40)
- **The four classic DevRel functions survive with changed content.** *Enablement* now has two audiences — developers whose job became orchestrating fleets of agents, and the agents themselves, which requires "content that is machine readable, has agent friendly APIs." *Community* is "more important than ever" and inherits a new problem: developers bringing recording agents into shared spaces, so "if people are bringing their Claudes into the Discord and they're recording all of the conversations," privacy and data concerns become a community-builder's design question. *Feedback loop* keeps the voice-of-the-developer job and gains a scale humans never offered — thousands of agents can be spun up for experiments developers will not sit for. *Credibility* bifurcates, see [Human and Agent Credibility Reward Opposite Writing Styles](human-and-agent-credibility-reward-opposite-writing-styles.md). (14:40-16:45)
- **The diagnostic use.** Run the three flavors as a gap check. A team with a shipped MCP server and no GEO measurement has the engineering flavor and no marketing flavor; a team measuring mentions with no trace instrumentation has the reverse. Each flavor's absence produces a different silent failure — an unused tool, an undiscovered one, or one nobody owns improving.
- **Limit.** This is one practitioner's organizational proposal, under a year into the role, at one company, offered without evidence about how the split performs. Its value is as a decomposition for assigning ownership, not as a validated org design. ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), Provenance and Limits)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Go To Market](../topics/go-to-market.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Benchmark Your Own Tool by Running Agents With and Without It](benchmark-your-tool-by-running-agents-with-and-without-it.md)
- [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md)
- [Human and Agent Credibility Reward Opposite Writing Styles](human-and-agent-credibility-reward-opposite-writing-styles.md)
- [Separate Agent as Product, Agent as Buyer, and Agent as User](separate-agent-as-product-buyer-and-user.md)
- [Treat Agent Experience as a Curb Cut](treat-agent-experience-as-a-curb-cut.md)
- [Agents Widen the Dev-Tool ICP Beyond Engineers](agents-widen-the-dev-tool-icp-beyond-engineers.md)
- [Design MCP Servers as Agent Products](design-mcp-servers-as-agent-products.md)

Sources:
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 13:10-16:45
