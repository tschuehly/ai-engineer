# Invest in the Harness to Run Weaker and Local Models

Summary: A good harness can close much of the gap to frontier proprietary models, so investing in harness expertise — rather than always reaching for the biggest model — lets weaker, cheaper, or local open-source models perform at cutting-edge levels; the harness matters *more* the weaker the model, which turns "keep the harness simple, the model will do the rest" into a strategic dependency on a handful of model vendors.

Use when:
- Deciding whether to depend on a frontier proprietary API or to invest in a harness so a local/open-source model can do the job.
- Countering the "models are so good you just need a simple loop and a few tools" argument.
- Justifying harness/tooling investment on sovereignty, cost, or portability grounds, not just reliability.

Details:
- The controversial thesis: "the models are so good that you can just keep the harness simple" is "moving in the wrong direction because that is making us reliant on fancy proprietary models that can't be run locally"; the better goal is "a harness that is so good that we can get the performance of a cutting-edge model through a local open-source model." ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 00:48-01:42)
- Quantified evidence — Harness Bench: a benchmark *for harnesses* (106 tasks) that holds the model and evaluation fixed and varies only the harness; scores range 52.4%→76.2%, a >20-point swing "and only the harness changed." Critically, "for weaker models, the harness matters more." ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 01:47-02:47)
- The democratization argument: if the model matters more, "we're dependent on a handful of companies who are able to build and train these models"; if a good harness can compensate for a weaker model, "you can build your own harnesses… any of us can do [that]… and we don't have to depend on paid models." ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 02:47-03:12)
- Corollary: an agent is a model + a harness, so "better harness equals better performance, especially for weaker models" — the same lever that Talha Sheikh reaches from the cost side (a tight verification harness lets you downshift to a Haiku or open-source model). ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 31:29-31:52)

- **A second source turns this into a routine measurement and a domain claim.** Paul Klein IV cites Factory compared against Claude Code "using the same model but using their kind of custom harness," and generalizes: "when you build a harness optimized for the domain that your agent is operating in, it can actually achieve above model results in that domain. Harness engineering is a real thing." He credits Cursor as the first company to do harness engineering on top of the original LLMs. Two useful qualifications come with it. He explicitly declines to settle whether custom harnesses beat models that were RL'd for the task — "it's not clear yet if custom harnesses are going to beat out durable RL'd models… we're not going to debate that today" — and the practice that survives either answer is the measurable one: "you should still have some sort of harness on your model and measure the performance versus baseline model." That is the per-team version of Harness Bench, and it is cheap: hold the model fixed, run the task with and without your harness, and keep the number. ([Paul Klein IV](../sources/20260814_GqoNrUz8hEU.md), 04:13-05:46)

- **A worked instance on one harness component, run entirely on local models.** Stefania Druga applied exactly the Harness Bench discipline to a single block — memory recall — holding the model, core context, archival store, task, and benchmark fixed and varying only the recall policy. The winning policy (a ranked decisions ledger) beat vector similarity, recency, no-recall, and a model-judged gate, and held on a second local model and a second benchmark. Two things this adds to the page's argument. First, it shows the granularity at which harness engineering is actually measurable: not "our harness versus theirs" but one policy inside one block, which is cheap enough for a single engineer to run. Second, it strengthens the local-model case with a mechanism rather than an aspiration — the harness improvement here was *also* cheaper ("it's not just that it gives you better recall, it actually costs less"), so the harness investment did not trade tokens for capability. The price paid was wall-clock: local models "can only run in serial… they don't support batch querying," so the sweep ran for days. See [Ablate the Recall Policy With a Ladder and an Oracle](ablate-the-recall-policy-with-a-ladder-and-an-oracle.md) and [Run Harness Ablations on Local Models to Own Every Step](run-harness-ablations-on-local-models-to-own-every-step.md). ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 05:18-05:27, 08:17-09:41, 11:49-12:11)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Models](../topics/models.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Verification Guardrails Let You Downshift to Cheaper Models](verification-guardrails-let-you-downshift-to-cheaper-models.md)
- [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md)
- [Own open models for sovereignty and permissionless adoption](own-open-models-for-sovereignty-and-permissionless-adoption.md)
- [Build agent harnesses incrementally up a capability ladder](build-agent-harnesses-incrementally-up-a-capability-ladder.md)
- [Ablate the Recall Policy With a Ladder and an Oracle](ablate-the-recall-policy-with-a-ladder-and-an-oracle.md)
- [Run Harness Ablations on Local Models to Own Every Step](run-harness-ablations-on-local-models-to-own-every-step.md)

Sources:
- [What if the harness mattered more than the model? - Aditya Bhargava, Etsy](../sources/20260707_2e9ANoOEn28.md), 00:48-03:12, 31:29-31:52
- [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](../sources/20260814_GqoNrUz8hEU.md), 04:13-05:46
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 05:18-05:27, 08:17-09:41, 11:49-12:11
