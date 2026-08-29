# An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once

Summary: Every operational decision in an LLM gateway is a trade among four things that a degradation forces apart: availability, latency, guardrails, and cost. The design consequence is not that you should pick a favourite once, but that the gateway should expose the choice to its callers as a per-use-case lever instead of hard-coding one answer for everyone.

Use when:
- Writing the requirements for an internal LLM gateway, proxy, or model-routing service.
- A single reliability or latency policy is being proposed for traffic that includes embeddings, chat, agents, and reasoning calls.
- You need a vocabulary for why a mitigation that helps one property visibly hurts another.
- Reviewing a gateway you did not build and trying to find out which of the four it silently prioritizes.

Details:
- **The frame.** "Right at the heart of the gateway is a fight between four things. It's availability, latency, your guardrails and costs. In case of a degradation, you cannot maximize all four. You need to pick what you want." The tension is latent in healthy operation and only becomes forced during degradation, which is why it usually gets designed by accident. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 01:08-01:24)
- **The prescription is a lever, not a default.** Manuja splits his audience: if you *use* a gateway, "make that trade-off for your use case"; if you *design* one, "provide those levers to your callers and customers, so that your customers are happy." A gateway that decides fail-open versus fail-closed, or hedge versus don't-hedge, on behalf of every caller has made a product decision it does not have the information to make. (01:24-01:43)
- **Each of the talk's recommendations is a trade you can locate on the four axes.** Firing requests to two providers in parallel buys latency and availability and "just going to double your cost" (03:16-03:27). Hedging the tail past P90 of the budget buys P99 latency with duplicate spend (09:24-09:43). Failing open when a guardrail is down buys availability with safety; failing closed does the reverse — "that's the trade-off between availability and security" (10:12-10:40). Running guardrails as a serial pre-hook is "probably the safest, but it does add serial latency" (12:04-12:28). Streaming buys perceived latency by giving up the ability to fail over at all — see [Streaming Forecloses the Provider Fallback](streaming-forecloses-the-provider-fallback.md) (05:08-05:55).
- **The default rule for the guardrail axis generalizes to the others.** "The default choice should be the worst case that you can live with" — that is, pick the failure you would accept if the decision were made for you at 3 a.m., and make that the default, leaving the better outcomes to explicit opt-in. (10:54-11:00)
- **Why per-use-case matters more here than in ordinary service design.** The traffic behind one gateway is not homogeneous: embeddings and classification under a second, chat around three seconds, reasoning far longer (06:54-07:15). A policy tuned for the chat route is wrong for the reasoning route on every one of the four axes simultaneously, which is the same argument that forces per-route metrics in [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md).
- **Caveat.** The four-way framing is asserted as a framing device, not derived, and the talk works through only one of the six pairwise trades explicitly (availability against security, in the fail-open decision). No measurement of any trade appears anywhere in sixteen minutes; treat the axes as a checklist for finding unexamined decisions rather than as a model that predicts anything.


- **A vendor shipping the levers this page asks for, which is useful as a check on whether the framing survives implementation.** Manuja's ask of gateway designers is to "provide those levers to your callers and customers" instead of hard-coding one answer. DigitalOcean's router is one concrete form of that: "you describe what matters for your workload, costs, latency, quality, preferred models or hard rules. Then the router uses that context to pick the right model per request," expressed as natural-language task descriptions plus decision-tree rules over them, with presets as starting points ([Kamath & Gillam](../sources/20260822_FvxY8oPoI8o.md), 04:42-05:07, 05:48-06:08). Three of this page's four axes appear literally as fields — cost, latency, and quality — which is corroboration that the tradeoff is real enough for a product to expose it. The fourth, guardrails, is absent from the surface entirely, and the talk never mentions guardrails, safety filters, or governance; the router is presented as an optimization layer, not a policy layer. See [Declare Routing Preferences So a Bad Route Is Fixable](declare-routing-preferences-so-a-bad-route-is-fixable.md).
- **The exposed lever is a preference, not a guarantee, which is where the framing gets tested.** Declaring "latency matters most" for a task does not bound latency; it biases a per-request model choice whose own matching step is nondeterministic. A degradation still forces the four-way choice this page describes, and the router's answer to an outage is a pool ordering rather than an axis to sacrifice. Preference declaration is therefore best read as a way to state your position on the tradeoff *in advance*, not as a mechanism that enforces it.

- **The four axes are all request-scoped, and a fifth question sits outside them: what can the gateway do about a run?** Chawla and Koul's objection is not to any of these trades but to the granularity at which they are made — a gateway "monitors the model request," while what spends the money is "the loop between the agent call, the tool and the agent," "the spawning of multiple sub agents happening from a one main agent," and "the growing of context." Their reading of the cost axis in particular is that a gateway's whole action space is hard caps and downgrading to a cheaper model, both of which are decisions about the *next request*. This does not contradict the four-way framing; it says the framing is complete for one request and silent about the unit a budget is actually defined over. See [Put the Cost Control at the Agent Run, Not the Model Request](put-the-cost-control-at-the-agent-run-not-the-model-request.md). ([FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 02:14-02:57, 05:56-08:34)
Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Put the Cost Control at the Agent Run, Not the Model Request](put-the-cost-control-at-the-agent-run-not-the-model-request.md)
- [Streaming Forecloses the Provider Fallback](streaming-forecloses-the-provider-fallback.md)
- [Prefer Per-Request Fallback to Retries and Circuit Breakers for LLM Calls](prefer-per-request-fallback-to-retries-and-circuit-breakers-for-llm-calls.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)
- [Treat Guardrails as a Failable Dependency With Its Own Time Budget](treat-guardrails-as-a-failable-dependency-with-a-time-budget.md)
- [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md)
- [Abstract LLM Inference Behind One Routing API](abstract-llm-inference-behind-one-routing-api.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Declare Routing Preferences So a Bad Route Is Fixable](declare-routing-preferences-so-a-bad-route-is-fixable.md)
- [Give Each Task a Model Pool With an Explicit Selection Policy](give-each-task-a-model-pool-with-an-explicit-selection-policy.md)

Sources:
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 01:08-01:43, 03:16-03:27, 06:54-07:15, 09:24-09:43, 10:12-11:00, 12:04-12:28
- [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../sources/20260822_FvxY8oPoI8o.md), 04:42-05:07, 05:48-06:08
- [FinOps for AI Agents: Who Spent All the Tokens? — Tisha Chawla & Susheem Koul, Microsoft](../sources/20260822_GJX19pNhmSw.md), 02:14-02:57, 05:56-08:34
