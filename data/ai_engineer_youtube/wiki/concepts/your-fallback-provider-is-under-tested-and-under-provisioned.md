# Your Fallback Provider Is Under-Tested and Under-Provisioned

Summary: Teams provision and test the primary model provider well and treat the fallback as a formality, which inverts the correct priority: the backup is the last line of defence, so it should carry *more* headroom than the primary, and its API differences must be normalized and exercised before an outage discovers them for you.

Use when:
- Setting capacity, quota, or rate-limit requests with a secondary model provider.
- Reviewing a multi-provider setup that has never actually failed over in production.
- Building the compatibility layer between two "OpenAI-compatible" providers.
- Planning a game day or failover drill for an LLM-backed service.

Details:
- **The provisioning inversion, stated as a repeated observation.** "I've seen teams trip over and over again. They really provision and test their primary providers really well, but the second provider, the fallback provider, doesn't necessarily get the same level of love. And I would argue that your throughputs or your capacity or your headroom should be even higher for the second provider… because that's your last line of defense. If that goes down, your application goes down." ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 05:55-06:29)
- **The reason the asymmetry runs that way.** The fallback absorbs the primary's *entire* load at the moment it is invoked, and it is invoked precisely when something is already wrong. Sizing it to a fraction of normal traffic — the natural instinct, since it normally serves none — guarantees it saturates on first use.
- **"OpenAI-compatible" is a family resemblance, not an interface.** "While the industry is converging on an OpenAI API compatible format, I would say there are still nuances… They can have differences in your tool calling schemas, token limits, stop reasons and what have you." Each of those breaks a different part of a working request: a tool-schema difference breaks agent calls, a token-limit difference truncates, and a stop-reason difference makes your caller mis-handle a successful response. (04:35-05:00)
- **The two mitigations are separate work.** A normalization layer in the gateway "can ensure that you can do cross provider fallbacks" by reconciling those differences in one place instead of in every caller; and "you need to really test your fallbacks well," which means exercising the fallback path deliberately rather than waiting for it to be exercised by an incident. (05:00-05:07)
- **What this implies for the failover you have never run.** A fallback that has never carried production traffic is untested in both senses at once — its capacity is unmeasured and its response shape is unverified — so the first real failover tests two hypotheses simultaneously during an outage. Load-shedding and traffic prioritization exist partly because that test tends to fail; see [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md) for the rest of that machinery.
- **Caveat.** This is practitioner experience with no numbers attached: no failover incident, no saturation event, and no measured provider difference is reported, and the "even higher" headroom recommendation comes with no ratio. It also has an unpriced cost the talk does not mention — reserved capacity or committed spend with a second provider that normally serves zero traffic — which is exactly the availability-versus-cost trade in [An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once](an-llm-gateway-cannot-maximize-availability-latency-guardrails-and-cost.md).
- **The same hazard in a data waterfall, where the fallback rungs exist by design rather than for outages.** Layering data vendors until a field fills means "if I was just using Forager to get phone numbers for this set of countries, I'd only get halfway there," so providers two through N serve exactly the records the earlier rungs missed — a biased, low-volume slice that is rarely monitored. The remedy Berry names is the one this page implies: "either you or the vendor that you're using needs to run evals against these data providers," which means evaluating the fallbacks on the population they actually serve rather than on the whole set. ([Berry](../sources/20260826_UhCY231d0FQ.md), 04:42-05:28)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Prefer Per-Request Fallback to Retries and Circuit Breakers for LLM Calls](prefer-per-request-fallback-to-retries-and-circuit-breakers-for-llm-calls.md)
- [An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once](an-llm-gateway-cannot-maximize-availability-latency-guardrails-and-cost.md)
- [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md)
- [Abstract LLM Inference Behind One Routing API](abstract-llm-inference-behind-one-routing-api.md)
- [Read the Stop Reason Before You Read the Answer](read-the-stop-reason-before-you-read-the-answer.md)
- [Open Model Families Need Ecosystem-Compatible Tooling](open-model-families-need-ecosystem-compatible-tooling.md)
- [Waterfall Data Vendors and Run Evals to Decide Which to Trust](waterfall-data-vendors-and-run-evals-to-decide-which-to-trust.md)

Sources:
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 04:35-05:07, 05:55-06:29
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 04:42-05:28
