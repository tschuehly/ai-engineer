# Declare Routing Preferences So a Bad Route Is Fixable

Summary: The objection that sank earlier auto-routers was not accuracy but opacity — "the router makes a choice and if that choice results in poor performance, you really have no way of improving it." The fix is to make the routing key a *declared artifact* the caller owns (named tasks, cost/latency/quality weights, preferred models, hard rules) rather than a learned score, so a bad route is a config line you can find and change instead of a model behaviour you can only complain about.

Use when:
- Evaluating or building a model router, and deciding what it routes on.
- A router picked the wrong model and the only available response is "the router decided that."
- Choosing between an inferred difficulty score and an explicit task taxonomy as the routing feature.
- Writing the requirements for any component that silently substitutes one model for another.

Details:
- **The failure being repaired.** "Many builders have tried auto routing before, but the problem was that it feels like a black box. The router makes a choice and if that choice results in poor performance, you really have no way of improving it." ([Kamath & Gillam](../sources/20260822_FvxY8oPoI8o.md), 04:21-04:42). This is a debuggability argument, not an accuracy one — a router that is right 90% of the time and inspectable beats one that is right 92% of the time and inert, because only the first one improves.
- **What "declared" means concretely.** Two forms, layered: natural-language task descriptions with weights on what matters, and deterministic rules over them. "You describe what matters for your workload, costs, latency, quality, preferred models or hard rules. Then the router uses that context to pick the right model per request" (04:42-05:07); "you describe a task in natural language and set what matters, cost, latency, and task description. You bring your rules and we execute them. Layer decision tree rules on top. Start from presets, change anything you want in a single line of code" (05:48-06:04). The natural-language half stays flexible; the rule half is what lets you *guarantee* a route rather than nudge it.
- **The routing key is a named task, not an estimated difficulty.** In the demo the router's config holds tasks — bug fixing, code generation, test writing, code snippets, code performance optimization — and each request is *matched* to one of them, with the matched task shown in the observability panel (06:29-07:10, 07:52-08:54). That is the amendment this page makes to [Route Each Request to the Cheapest Sufficient Model by Difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md): a difficulty score is a number nobody can argue with, while a task label is a claim you can inspect, disagree with, and correct. When a route is wrong you can tell *which* half failed — the match, or the task's model assignment — and they have different fixes.
- **The loop the artifact exists to serve.** "You validate with your own evaluations, not someone else's leaderboard. Route, evaluate, adjust, then feed that back in. That loop is key" (06:04-06:08). Declared preferences are the thing the loop edits; without them the "adjust" step has no target. See [Evaluate a Router Against the Always-Frontier Arm](evaluate-a-router-against-the-always-frontier-arm.md) for the measurement half.
- **This is the same lever a gateway operator asks for, arriving from the other side of the interface.** Manuja's argument is that a gateway "cannot maximize" availability, latency, guardrails and cost at once, so designers should "provide those levers to your callers and customers" rather than hard-coding one answer ([An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once](an-llm-gateway-cannot-maximize-availability-latency-guardrails-and-cost.md)). Declared routing preferences are one concrete instance of those levers — three of the four (latency, cost, and quality as a proxy for the guardrail axis) are literally the fields you fill in. Read together: the gateway operator says expose the trade; the router vendor ships a form for it.
- **The unresolved tension with the same operator.** Manuja names router models as "the slide that has given me the most scars," because they "hide that abstraction behind you… they pick which models to run," and his advice is to pin down whatever the router leaves free to make "requests as deterministic as possible with an undeterministic system" ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 08:17-09:22). Declared preferences narrow that gap without closing it — a hard rule or a manual ranking makes the choice deterministic, but the natural-language *match* from request to task remains a model decision on the critical path. Treat the rule layer, not the description layer, as the part you can rely on under an incident.
- **Caveats.** No mis-route is demonstrated anywhere in the source, so the claim that a declared config makes a bad route fixable is argued from the shape of the interface rather than shown working. The vendor's own roadmap pushes the other way: personalization "so that the router learns what works for your team over time" (14:28-15:09) reintroduces exactly the learned, drifting behaviour that the declared artifact was meant to displace, and the talk does not reconcile the two.

Related topics:
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Give Each Task a Model Pool With an Explicit Selection Policy](give-each-task-a-model-pool-with-an-explicit-selection-policy.md)
- [Evaluate a Router Against the Always-Frontier Arm](evaluate-a-router-against-the-always-frontier-arm.md)
- [A Router Must Be Cheap and Fast Enough to Disappear](a-router-must-be-cheap-and-fast-enough-to-disappear.md)
- [Route Each Request to the Cheapest Sufficient Model by Difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md)
- [Route Between Model Tiers by Quality Dimension, Not Only Cost](route-between-model-tiers-by-quality-dimension-not-only-cost.md)
- [An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once](an-llm-gateway-cannot-maximize-availability-latency-guardrails-and-cost.md)
- [Don't Trust a Single Leaderboard for Model Selection](do-not-trust-a-single-leaderboard-for-model-selection.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)
- [Abstract LLM Inference Behind One Routing API](abstract-llm-inference-behind-one-routing-api.md)
- [Compare Models by Task, Thinking Budget, Cost, and Latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Verification Guardrails Let You Downshift to Cheaper Models](verification-guardrails-let-you-downshift-to-cheaper-models.md)

Sources:
- [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../sources/20260822_FvxY8oPoI8o.md), 04:21-06:08, 06:29-08:54, 14:28-15:09
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 01:24-01:43, 08:17-09:22
