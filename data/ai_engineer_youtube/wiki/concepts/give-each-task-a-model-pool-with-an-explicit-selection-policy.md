# Give Each Task a Model Pool With an Explicit Selection Policy

Summary: Instead of binding a task to one model, bind it to an ordered *pool* plus a named selection policy — "manual ranking" to pin a preferred model and fail over to the next when it is down, or "fastest" to pick whichever member has been quickest in a recent window. One structure then carries three things that are usually built separately: which model you prefer, which one serves this request, and what happens when it fails.

Use when:
- Configuring a model router, gateway, or agent runtime and deciding where the fallback list lives.
- A per-task model choice and a provider-failover list are drifting apart in two different config files.
- Deciding whether model selection should be pinned by preference or driven by observed health.
- Reviewing whether a routing layer's backup path has actually been specified per task rather than globally.

Details:
- **The shape.** In DigitalOcean's router each named task maps to more than one model: "you can specify more than one model per task… In the code generation, I have GLM 5.2 and GPT-5.2. And because I really want to always route to GLM 5.2 unless it's down, I use this manual ranking option. So it'll always go to GLM 5.2. If GLM fails, it'll fail over to GPT-5.2." ([Kamath & Gillam](../sources/20260822_FvxY8oPoI8o.md), 07:10-07:32)
- **Two policies with different semantics on the same pool.** Manual ranking is a *preference* that degrades into a failover chain. The other demonstrated policy is health-driven: bug fixing uses "selection policy fastest. So out of this model pool, if it matches to bug fixing, it'll pick whichever one's been fastest in about the last 30" — the window's unit is lost in the captions (07:32-07:52). The difference matters for reproducibility: a manually ranked task answers from the same model every time until an outage, while a fastest-wins task can answer from a different model each hour based on traffic you do not control.
- **Why the coupling to the task is the useful part.** A gateway's global fallback list assumes every request wants the same substitute. A per-task pool does not: the right backup for code generation is a peer coding model, and the right backup for a classification task is another cheap model, not a frontier one. This makes concrete a gap named from the operator side — [Your Fallback Provider Is Under-Tested and Under-Provisioned](your-fallback-provider-is-under-tested-and-under-provisioned.md) argues the backup path gets none of the primary's attention; a pool declared per task at least makes the backup *visible* in the same place as the primary, which is the precondition for testing it.
- **Relationship to per-request fallback.** [Prefer Per-Request Fallback to Retries and Circuit Breakers for LLM Calls](prefer-per-request-fallback-to-retries-and-circuit-breakers-for-llm-calls.md) supplies the mechanism — try A, then B in sequence, for this request, without changing global state — and this page supplies where the ordering of A and B comes from. The "fastest in a recent window" policy is the same idea as Manuja's demoted circuit breaker read as a positive rule: instead of parking a persistently failing provider in a cool-down, rank the pool by recent latency and let the slow one fall to the back on its own.
- **The pool doubles as the answer to single-model concentration risk.** Kamath names risk as the third pressure breaking the one-model habit and calls it "for me the most important one": "models can go down and if you bet your entire product and production on one model, you have no failover when something degrades" (01:50-02:10). That is the same position Manuja states as "their ceiling is your ceiling. Their outage is your outage." Note the argumentative gap in the source, though — risk is named as the most important reason and then never appears again; the entire demo is about cost, and no failover event is shown.
- **Caveats.** The failure predicate is unspecified: "if GLM fails" is never defined, and nothing is said about timeouts, partial responses, or a stream that has already started (where fallback is gone entirely — see [Streaming Forecloses the Provider Fallback](streaming-forecloses-the-provider-fallback.md)). The "fastest" policy's measurement is undescribed — over whose traffic, at what percentile, and how a cold or newly added pool member is treated. And a pool whose members differ in tool-calling schema or stop reasons inherits the transparency problem: fallback across heterogeneous models needs a normalization layer, which the pool config does not by itself provide.

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Declare Routing Preferences So a Bad Route Is Fixable](declare-routing-preferences-so-a-bad-route-is-fixable.md)
- [Prefer Per-Request Fallback to Retries and Circuit Breakers for LLM Calls](prefer-per-request-fallback-to-retries-and-circuit-breakers-for-llm-calls.md)
- [Your Fallback Provider Is Under-Tested and Under-Provisioned](your-fallback-provider-is-under-tested-and-under-provisioned.md)
- [Streaming Forecloses the Provider Fallback](streaming-forecloses-the-provider-fallback.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)
- [Route Each Request to the Cheapest Sufficient Model by Difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md)
- [Abstract LLM Inference Behind One Routing API](abstract-llm-inference-behind-one-routing-api.md)
- [Routing Savings Compound Across an Agent Session](routing-savings-compound-across-an-agent-session.md)
- [A Router Must Be Cheap and Fast Enough to Disappear](a-router-must-be-cheap-and-fast-enough-to-disappear.md)
- [An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once](an-llm-gateway-cannot-maximize-availability-latency-guardrails-and-cost.md)
- [Route Between Model Tiers by Quality Dimension, Not Only Cost](route-between-model-tiers-by-quality-dimension-not-only-cost.md)

Sources:
- [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../sources/20260822_FvxY8oPoI8o.md), 01:50-02:10, 07:10-07:52
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 01:46-01:57, 03:00-03:52
