# State the Model Gateway as Three Invariants, Not a Feature List

Summary: Uber's internal model gateway is specified before it is described: no PII leaves the perimeter to any vendor by default, any guardrail added to the path has strictly bounded latency, and every request is attributable per user, per project, and per team. The invariants generate the implementation rather than summarizing it, and each one is falsifiable — you can point at a call that violated it — which a feature list is not.

Use when:
- Writing requirements for a company-wide LLM gateway and looking for a form that survives the next feature request.
- Arguing for or against a mandatory single endpoint for all model traffic.
- Deciding what a gateway must guarantee versus what it may merely offer.
- Reviewing an existing gateway and trying to find out what it actually promises.

Details:
- **The three invariants, stated ahead of any component.** "The three things that we wanted to ensure was: no PII ever leaves our perimeter to any of the vendor by default; any guardrail that we add here the latency of that is strictly bounded; and every request that goes through this… we need to be able to attribute per user, per project and per team." ([Medisetty](../sources/20260821_17-YSUHo6Lk.md), 01:48-02:16) Each contains an implicit rejection: no per-team exemption from redaction, no unbounded safety check, no unattributed call.
- **The implementation falls out of them.** One OpenAI/Anthropic-compatible endpoint that "all of our internal use cases, our coding harnesses, our external use cases" pass through, fronting a middleware chain: Spire for identity and authentication, "a data anonymizer that redacts 20 plus PII types," and "an AI guard that has five specialized models that handles various parts of safety and policy." (02:16-02:43)
- **The latency invariant is a number, and it covers the whole chain.** "All of that runs under 100 milliseconds" — identity, redaction, and five safety models together, not each. That is a materially harder commitment than a per-check timeout, and it is what forces the safety layer to be small specialized models rather than a frontier call; see [Fine-Tuned Encoder Discriminators Make Low-Latency Guardrails Practical](fine-tuned-encoder-discriminators-make-low-latency-guardrails-practical.md). (02:43-02:56)
- **Attribution has to reach two places to be useful.** Per caller, per user, per team, "both in real time but also in our data lake. This enables us to create all kinds of spend tiers and guardrails in a holistic way across our portfolio." Real-time attribution enforces; the lake copy is what lets you set the tier in the first place. The project ID is the join key: "you take the vanilla client, you set the project ID and we take care of everything else." (02:56-03:27)
- **The same chokepoint pays for something other than governance.** "We also use this layer for capturing audit log session traces which are then plugged into our benchmarking and all kinds of self-improvement loop efforts." A mandatory gateway is, incidentally, the only place in a large org where a representative trace corpus exists. (03:12-03:27)
- **Scale, as the argument that the invariants are affordable.** "800 plus projects internally… more than 100 million model requests per day," spanning frontier models and open-source models "whether that is hosted in our infrastructure or some of our vendors." (03:27-03:39)
- **Where this sits against the decentralization argument.** Manuja's position is that a company-wide gateway "is a single point of failure" and that teams asking for one actually want centralized *governance*, achievable with shared plugins across many deployments — see [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md). Uber is the counter-instance at scale, and the invariant framing is why: the first invariant is a *data-plane* property. A plugin that every deployment is supposed to run does not guarantee no PII left the perimeter; only a path everything must traverse does. Attribution and spend tiers would survive decentralization; default-on redaction is the one that does not.
- **Caveat.** Nothing about failure behaviour is stated — no fail-open/fail-closed policy, no availability figure, no incident, no report of what happens to the 100ms budget when a safety model degrades rather than dies. The talk also gives no cost for the gateway itself. Treat the 100ms figure as an existence proof that a five-model guardrail stack can be made cheap, not as a budget you can adopt without knowing what those five models are.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)

Related concepts:
- [An LLM Gateway Cannot Maximize Availability, Latency, Guardrails, and Cost at Once](an-llm-gateway-cannot-maximize-availability-latency-guardrails-and-cost.md)
- [Make the LLM Gateway the Agent Observability Chokepoint](make-the-llm-gateway-the-agent-observability-chokepoint.md)
- [Decentralize the Gateway, Centralize the Governance](decentralize-the-gateway-centralize-the-governance.md)
- [Treat Guardrails as a Failable Dependency With Its Own Time Budget](treat-guardrails-as-a-failable-dependency-with-a-time-budget.md)
- [Fine-Tuned Encoder Discriminators Make Low-Latency Guardrails Practical](fine-tuned-encoder-discriminators-make-low-latency-guardrails-practical.md)
- [Emit Attribution Dimensions So Budgets Can Target Any Cohort](emit-attribution-dimensions-so-budgets-can-target-any-cohort.md)
- [Stamp Agent Identity at the Proxy Because a Claimed Identity Resets the Budget](stamp-agent-identity-at-the-proxy-because-a-claimed-identity-resets-the-budget.md)
- [Abstract LLM Inference Behind One Routing API](abstract-llm-inference-behind-one-routing-api.md)
- [Crawl Internal APIs Into MCP Servers Instead of Asking Teams to Write Them](crawl-internal-apis-into-mcp-servers-instead-of-asking-teams-to-write-them.md)

Sources:
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 01:48-03:39
