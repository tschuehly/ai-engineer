# A Router Must Be Cheap and Fast Enough to Disappear

Summary: A router sits on the critical path of every request it governs, so its own latency and price are subtracted from the savings it produces. That budget is tight enough to determine the implementation: routing is a narrow classification job, which is why a small purpose-built model — claimed here at under 200 ms, at no incremental charge — is the right shape, and why using a frontier model to choose a frontier model rarely pays.

Use when:
- Deciding whether to build a router, and what should make the routing decision.
- A routing layer is being prototyped with an LLM call to a general-purpose model.
- Weighing a router against a blanket cheap default with escalation on failure.
- Working out why a measured routing saving is smaller than the tier price gap predicted.

Details:
- **The budget stated as a product constraint.** "Because the routing model is specialized for this job, it's super fast, under 200 milliseconds, and it costs customers nothing extra." ([Kamath & Gillam](../sources/20260822_FvxY8oPoI8o.md), 05:07-05:23). The closing facts add the implementation: "it runs on a custom mixture of experts model purpose-built for routing," with "zero application code changes needed" and the routing model open sourced (13:47-14:28).
- **The arithmetic behind the constraint.** Every routed request pays the decision cost whether or not the route saves anything, so the router's overhead is a fixed tax against a variable benefit. On the calls that were already going to the cheap tier the tax is pure loss; on latency-sensitive work it eats directly into the budget the routing was supposed to protect. Sub-200 ms against multi-second generation is roughly a rounding error; a second general-purpose LLM call to make the choice is not, and it would also inherit that model's tail. This is the operational reason routing is not simply "ask a model which model to use."
- **Why a small specialized model is the right shape, not a compromise.** Routing is a narrow, high-frequency classification task with a fixed label set — exactly the profile in [Post-Train Small Models for Narrow Capabilities](post-train-small-models-for-narrow-capabilities.md), where small models are strongest when focused on a few valuable capabilities rather than made broadly average. The talk claims the specialized model beats "frontier models like the GPT-5 series models at routing task itself with a fraction of the latency" (05:23-05:35), which is the expected direction for a narrow task, though no accuracy figure or routing benchmark is given.
- **The zero-code-change adoption path is part of the same budget.** An OpenAI-compatible proxy in front of the routing model means the router can be adopted by changing a base URL — the integration cost is near zero, matching the switching-cost argument in [Abstract LLM Inference Behind One Routing API](abstract-llm-inference-behind-one-routing-api.md). The same caution transfers: the proxy hides provider differences in tool-calling schemas, token limits and stop reasons only to the extent someone has built the normalization, so "no code changes" describes the call site, not the blast radius.
- **The comparison this makes possible.** Once the decision is nearly free, a router beats the crude alternative — a blanket cheap default with escalation on failure, as in [Route Each Request to the Cheapest Sufficient Model by Difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md) — because escalation-on-failure pays for the failed attempt *and* the retry, which is far more than 200 ms. If the routing decision were expensive, the crude default would often win, and it still wins when nobody can build or validate the classifier.
- **What the router still adds that the budget does not cover.** It manufactures a mixed-workload endpoint and hides which model answered, which is a real operational cost even at zero latency: aggregate latency over a routed endpoint stops meaning anything ([Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)), and Manuja names router models as a top source of unexplained P99 spikes because they "hide that abstraction behind you… they pick which models to run" ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 08:17-09:22). A router that is free in decision latency is not free in observability.
- **Caveats.** "Under 200 milliseconds" is stated without a percentile, a load condition, or a measurement method, and a router's tail matters more than its median because it lands on every request. "Costs customers nothing extra" and "free and included" (13:47-14:28) are pricing statements, not cost statements — the routing model's compute is paid for somewhere, and a bundled price can change. The mixture-of-experts detail is asserted with no size, training data, or label set described. And nothing is said about what the router does when it cannot confidently match a request to any configured task.

Related topics:
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Declare Routing Preferences So a Bad Route Is Fixable](declare-routing-preferences-so-a-bad-route-is-fixable.md)
- [Give Each Task a Model Pool With an Explicit Selection Policy](give-each-task-a-model-pool-with-an-explicit-selection-policy.md)
- [Post-Train Small Models for Narrow Capabilities](post-train-small-models-for-narrow-capabilities.md)
- [Abstract LLM Inference Behind One Routing API](abstract-llm-inference-behind-one-routing-api.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)
- [Route Each Request to the Cheapest Sufficient Model by Difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md)
- [Use Small Models as Context-Management Tools Before Agent Reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)

Sources:
- [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../sources/20260822_FvxY8oPoI8o.md), 05:07-05:35, 13:47-14:28
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 08:17-09:22
