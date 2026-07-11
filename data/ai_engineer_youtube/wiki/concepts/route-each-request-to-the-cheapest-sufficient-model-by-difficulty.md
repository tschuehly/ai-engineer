# Route Each Request to the Cheapest Sufficient Model by Difficulty

Summary: Don't send every agent call to the most expensive frontier model; classify each request's difficulty and route it to the cheapest model that can handle it — simple work to a cheap model, harder work to a mid model, only the hardest to a frontier model — so per-token cost tracks task difficulty instead of a fixed worst-case.

Use when:
- An agent uses one expensive model for every call, including simple inference steps that a cheaper model could do.
- A production agent's cost is dominated by model price rather than context size, and different requests vary in difficulty.
- Designing an agent loop where you can insert a routing decision before the model call.

Details:
- The lever: "I highly recommend don't use the most expensive model for everything you're doing… use multiple different models based on the use case, and then try to route to it inside your agent." Map difficulty to a tier — a newer frontier model for a very difficult task, a cheaper model (e.g. Claude Haiku) for something simple, Claude Sonnet for something in between. ([Erik Hanchett](../sources/20260628_uiP88SpCi1Q.md), 01:01-01:51)
- The router can be as simple as an `if` statement on task type, or "you can even have another model that's very cheap decide which model to use" — a cheap classifier picks the tier per request, so the routing overhead stays far below the cost of over-serving every call with the frontier model.
- This is a *difficulty*-triggered routing policy, distinct from other cheaper-model paths in the wiki: [verification guardrails let you downshift to cheaper models](verification-guardrails-let-you-downshift-to-cheaper-models.md) uses a check-and-retry harness (not task difficulty) as the trigger, and [abstract LLM inference behind one routing API](abstract-llm-inference-behind-one-routing-api.md) is the routing *mechanism* rather than the per-request policy. Use this concept for the "which tier does this request need" decision and those for the harness and plumbing.
- Caveats implicit in the pattern: routing adds logic and possibly one extra (cheap) classifier call per request, and mis-routing a hard task to a too-cheap model trades cost for quality, so the difficulty signal needs to be reliable enough that cheap-tier outputs still complete the task.

Related topics:
- [Inference](../topics/inference.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Shrink the Per-Step Payload the Agent Loop Re-Sends](shrink-the-per-step-payload-the-agent-loop-re-sends.md)
- [Verification Guardrails Let You Downshift to Cheaper Models](verification-guardrails-let-you-downshift-to-cheaper-models.md)
- [Abstract LLM inference behind one routing API](abstract-llm-inference-behind-one-routing-api.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Split discovery and validation across reasoning and deterministic models](split-discovery-and-validation-across-reasoning-and-deterministic-models.md)

Sources:
- [Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](../sources/20260628_uiP88SpCi1Q.md), 01:01-01:51, 04:50-05:03
