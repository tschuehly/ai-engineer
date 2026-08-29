# Eval an Agent Surface for Protocol Compliance, Not Just Behavior

Summary: When another company's assistant is your distribution channel, your agent surface has a second correctness criterion beyond behaving well: the feeds and responses must conform to that platform's spec or the platform drops you. Because the specs are still moving and there are several of them, conformance is a continuous test in the eval suite rather than a one-time integration milestone.

Use when:
- Publishing an agent-facing surface (feed, MCP server, checkout API) into a third-party assistant, marketplace, or app store.
- Building an eval suite for an agent product whose users arrive through someone else's client.
- Deciding what to test when the spec you integrate against is versioned by someone who does not tell you.

Details:
- The eval axis and its enforcement mechanism in one sentence: "protocol compliance, because when we're selling it to Gemini or chat.openai.com, you want to make sure that the feeds are actually conforming, or else they will not support it." The penalty is not a bug report, it is silent removal from the channel. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 17:55-18:12)
- Why it is continuous rather than one-time: there are at least three schemas to satisfy (ACP, UCP, Meta), they are "similar, but still different," and the specs themselves are explicitly unsettled — ACP-versus-UCP convergence and identity-consent standards are listed as still forming. Anything a merchant validated last quarter may now be non-conforming through no change of its own. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 09:19-09:30, 18:44-19:08)
- Prio's full list for a commerce agent is four classes, and they fail differently: behavior evals (the agent says or does the wrong thing), protocol compliance (the platform rejects you), latency benchmarks, and LLM-as-quality-judge. Only the first is what most teams mean by "evals." ([Prio](../sources/20260827_G7cgLjZtmMU.md), 17:55-18:44)
- Latency is treated as a revenue metric rather than an experience metric, which changes what threshold you set: "every second in retail on the shopping journey where you're actually not selling, there are chances that the other website's going to be faster, and people are just going to move away, or they just don't feel like it anymore." In a channel where the assistant can substitute another merchant mid-conversation, slowness is lost inventory, not a poor review. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 18:12-18:29)
- The judge is deliberately kept cheap and co-owned: "you don't have to use something fancy. Talk to your product friends and figure out what's the best way to do it, and use best use cases and write them out." ([Prio](../sources/20260827_G7cgLjZtmMU.md), 18:29-18:44)
- The alternative is stated as the cost of skipping it: "working with AI and conversational experiences without evals is playing whack-a-mole," offered as the lesson from building the demo and from doing agentic commerce at Best Buy. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 16:14-16:38)
- Caveat: the four classes come with no method. There is no dataset construction, threshold, pass criterion, judge-calibration step, or account of how a conformance test is written against a spec that is still changing — and the talk reports no latency figure despite recommending latency benchmarks. Take the taxonomy and supply the method from elsewhere.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Catalog Eval Signal Sources Across Judge, Human, Golden, Deterministic, and Business](catalog-eval-signal-sources-judge-human-golden-deterministic-business.md)
- [Public Agent Surfaces Get Repurposed as Free General-Purpose Compute](public-agent-surfaces-get-repurposed-as-free-general-compute.md)
- [Push a Product Feed, Because Per-Merchant Catalog Search Does Not Scale](push-a-product-feed-because-catalog-search-does-not-scale.md)
- [Evals Only Cover Known AI Product Failures](evals-only-cover-known-ai-product-failures.md)

Sources:
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 09:19-09:30, 16:14-16:38, 17:55-19:08
