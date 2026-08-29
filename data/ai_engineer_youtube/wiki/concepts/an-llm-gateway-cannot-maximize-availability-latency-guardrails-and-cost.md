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

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Streaming Forecloses the Provider Fallback](streaming-forecloses-the-provider-fallback.md)
- [Prefer Per-Request Fallback to Retries and Circuit Breakers for LLM Calls](prefer-per-request-fallback-to-retries-and-circuit-breakers-for-llm-calls.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)
- [Treat Guardrails as a Failable Dependency With Its Own Time Budget](treat-guardrails-as-a-failable-dependency-with-a-time-budget.md)
- [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md)
- [Abstract LLM Inference Behind One Routing API](abstract-llm-inference-behind-one-routing-api.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)

Sources:
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 01:08-01:43, 03:16-03:27, 06:54-07:15, 09:24-09:43, 10:12-11:00, 12:04-12:28
