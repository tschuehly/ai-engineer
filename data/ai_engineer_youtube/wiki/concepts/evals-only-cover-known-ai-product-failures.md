# Evals Only Cover Known AI Product Failures

Summary: Offline evals are useful regression tools, but they should not be treated as a complete measure of AI product quality. They mostly cover failures the team already knows how to name, so real production use and fresh user signals must keep discovering new issue classes.

Use when:
- A team wants eval scores to answer whether an AI product is good overall.
- A product is moving offline evals directly into production scoring without checking cost, coverage, or emerging behavior.

Details:
- Ben Hylak argues that evals do not tell teams how good a product is, because they cover known cases and can be saturated; newer models can score lower on some evals while still feeling better in real use. (08:31-09:18)
- LLM-as-judge scoring is tempting for subjective qualities, but the talk says strong teams usually prefer curated datasets and autogradable checks where deterministic pass/fail is possible. (09:21-10:12)
- Moving offline judges directly onto production traffic can be expensive, hard to configure accurately, and still limited to patterns the team already expected. (10:14-11:04)
- **A second, quieter way coverage disappears: the suite stops covering even the failures it did name.** Hylak's 2026 follow-up is that evals "break as soon as you have a new model, as soon as you like switch harnesses" — write an assertion that a question must trigger a particular tool call, move to a different agent CLI, "and now 80% of your evals suck." Nobody edits the suite; the assertions simply stop being about anything. So the coverage gap on this page has two sources — failures never named, and named failures whose assertions were coupled to a harness that changed ([A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md)). His decision test for whether a suite has earned its cost: "do you actually delay… upgrading to the new model on your product… 2 weeks to update your evals or not? I think most people would say no." ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 04:23-05:23)
- Mutagent frames the same limit for agents: "you cannot pre-guess the entire evaluation suite from the beginning" — seed it with domain experts writing metrics/criteria or with historical/synthesized data, but the real, complete suite is "a product of discovery," accumulating metrics, criteria, and edge/hard-case dataset items over time from user feedback and production failures. (12:06-13:37)
- **The same argument from the merchant side, phrased as whack-a-mole.** "Working with AI and conversational experiences without evals is playing whack-a-mole." What production surfaced for Prio that nobody had written a test for is commercially specific rather than generic — an agent answering programming questions, handing out a discount code, or revealing "who else is checking out this product" — which supports this page's point in a useful direction: the unknown failures are drawn from the *domain's* value surface, so the classes you are missing are the ones your business cares about and your safety vendor does not model. The Chipotle example is flagged by the speaker himself as unverified. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 16:14-16:38, 17:10-17:55)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Keep eval data constant and task logic variable](keep-eval-data-constant-and-task-logic-variable.md)
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Automate the Agent-Building Loop With an Agentic AI Engineer](automate-the-agent-building-loop-with-an-agentic-ai-engineer.md)
- [A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md)
- [Raise the Floor Before Maxing the Benchmark](raise-the-floor-before-maxing-the-benchmark.md)
- [Public Agent Surfaces Get Repurposed as Free General-Purpose Compute](public-agent-surfaces-get-repurposed-as-free-general-compute.md)

Sources:
- [Building AI Products That Actually Work - Ben Hylak (Raindrop), Sid Bendre (Oleve)](../sources/20250724_eSvXbb2EBYc.md), 08:31-11:04
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 04:23-05:23
- [The Agentic AI Engineer - Benedikt Sanftl, Mutagent](../sources/20260629_pSto5YaNGUo.md), 12:06-13:37
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 16:14-16:38, 17:10-17:55
