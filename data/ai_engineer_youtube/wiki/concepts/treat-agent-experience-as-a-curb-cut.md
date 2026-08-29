# Treat Agent Experience as a Curb Cut

Summary: Work done specifically to make a product usable by agents — machine-readable docs, clear tool descriptions, self-serve install, quotable structured claims — clears the path for humans too, the way curb cuts built for wheelchairs came to serve strollers and suitcases. This reframes agent-experience investment from a second product surface into an upgrade of the existing one, and it comes with two cheap starter actions.

Use when:
- Justifying agent-experience work that looks like it serves a non-paying user.
- A team treats "support for agents" as a parallel track competing with human-facing work.
- Looking for the smallest first step toward measuring agent experience.

Details:
- **The argument.** "Curb cuts were built for wheelchairs, built for a specific user to use them. But now everybody benefits from that — anybody with wheels, strollers and suitcases. So my argument is that by serving the agents, the human path gets cleared, too. There's just one more user in the room now, but they are still serving the human on the other end." ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 16:45-17:21)
- **Why it holds rather than being a slogan.** Each agent-facing improvement in this talk has a human beneficiary: a parameter name that matches expectations helps every reader of the API; content that names the customer's pain instead of the product category is better marketing copy for humans; removing a demo gate shortens the human evaluation path; a `llms.txt` map of the docs is a table of contents. The wiki records the same convergence from the accessibility direction — the accessibility tree is the one agent-readable surface many sites already have, so ordinary accessibility work is the cheapest agent-readability investment available. See [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md).
- **Where the analogy stops.** Curb cuts are a fixed capital improvement; agent experience is measured against models that change under you. The same talk's stale-content finding is the counterexample — re-running a fixed prompt set on a newer model made the outcome worse, which no physical curb cut does. Treat agent experience as a maintained surface with a rerun cadence, not a one-time ramp. See [Stale Product Content Compounds Through Newer Models](stale-product-content-compounds-through-newer-models.md).
- **Starter action, engineering side.** "Point a coding agent at your docs, and then look through that transcript and start developing your agent experience report." This is a zero-infrastructure version of the with-and-without benchmark: one agent, your real docs, and a transcript read for where it guessed, backtracked, or gave up. See [Benchmark Your Own Tool by Running Agents With and Without It](benchmark-your-tool-by-running-agents-with-and-without-it.md). (17:21-17:36)
- **Starter action, go-to-market side.** "Start developing some of these experiments with the GEO, putting together those prompts, and looking at the mentions versus recommendations." Note the distinction it draws — being mentioned and being recommended are separate counts, and only the second corresponds to adoption. (17:36-17:52)
- **Make the artifact itself agent-legible.** The talk was published with a QR code and toy repositories containing templates, described as making the whole talk "agent legible" so an attendee could send an agent to it rather than photograph slides. The principle applies to any material you expect to be consumed downstream: publish the machine-readable version alongside the human one. (17:52-17:56)
- **The audience-change framing behind it.** The talk's thesis is that developer relations is not dead but that its audience changed; the agent is "both the user of your tool in a very similar way to the developer" — reading docs, calling the API, hitting and recovering from errors — "but then it's also a recommender," which is the position bottom-up developer adoption always ran through. (04:15-05:22)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Agent Experience Means Autonomous Access, Understanding, and Operation](agent-experience-means-autonomous-access-understanding-and-operation.md)
- [Benchmark Your Own Tool by Running Agents With and Without It](benchmark-your-tool-by-running-agents-with-and-without-it.md)
- [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md)
- [Stale Product Content Compounds Through Newer Models](stale-product-content-compounds-through-newer-models.md)
- [Split Agent Advocacy Into Engineering, Product, and Marketing Flavors](split-agent-advocacy-into-engineering-product-and-marketing-flavors.md)
- [Agents Widen the Dev-Tool ICP Beyond Engineers](agents-widen-the-dev-tool-icp-beyond-engineers.md)
- [Make Web Foundations Agent-Ready Before Adopting WebMCP](make-web-foundations-agent-ready-before-adopting-webmcp.md)

Sources:
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 04:15-05:22, 16:45-17:56
