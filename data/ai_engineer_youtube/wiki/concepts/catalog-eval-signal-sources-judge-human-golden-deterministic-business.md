# Catalog Eval Signal Sources Across Judge, Human, Golden, Deterministic, and Business

Summary: Evaluation signal does not come from one source. Arize's framing is five "flavors" — LLM-as-judge, human feedback, golden datasets, deterministic checks, and business metrics — each with a different cost, trust basis, and place in the loop, and the cheapest source that gives the needed signal should be preferred.

Use when:
- Deciding what kind of eval to attach to a new AI feature, rather than reaching for LLM-as-judge by default.
- Justifying why a deterministic assertion (or a human label) is the right scorer for a given check instead of another model call.

Details:
- Five flavors of signal: (1) LLM-as-judge — seems simple but gets complex; (2) human feedback — end-user and reviewer signal, valuable to both technical and non-technical roles; (3) golden datasets — examples labeled by a trusted domain expert; (4) deterministic checks — logic/code with no LLM or human in the loop; (5) business metrics. (07:06-08:44)
- Golden datasets are the trust anchor that *tunes* the LLM judge: you run the judge against a domain-expert-labeled set and ask "can I get my LLM to approximate this person / this dataset I trust?", so the judge is calibrated to a human standard rather than trusted blindly. (07:38-08:05)
- Deterministic checks are the cheap default where the expected condition can be encoded without a model: e.g. a paragraph-to-JSON step — is it valid JSON, does it have the schema, are these fields non-null. "Determinism is super nice." (08:08-08:28)
- Business metrics resolve to one of three purposes — make money, save money, or save time — so eval design should trace back to which of those a feature serves. (08:31-08:44)
- Cost governs the choice: "you don't always have to use an LLM call or even humans"; prefer the cheapest source that still gives signal, because every eval has a recurring cost. (08:06-08:13)
- This is the source-of-signal axis; it is orthogonal to *where* in the execution tree the eval runs (see the scope axis) and to *how* a judge is structured (binary metrics, calibration).
- **Shipping into someone else's client adds a signal source this taxonomy does not have: the platform's own conformance verdict.** It behaves like a deterministic check whose oracle you do not own and whose specification moves without notice — "you want to make sure that the feeds are actually conforming, or else they will not support it," against schemas that are "similar, but still different" and a spec landscape where ACP-versus-UCP convergence is explicitly unsettled. It is free and binary, which makes it attractive by this page's cheapest-sufficient-signal rule, but its failure mode is silent de-listing rather than a bad score, so it needs its own alerting. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 09:19-09:30, 17:55-18:12, 18:44-19:08)

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Choose Eval Scope Across Span, Multispan, Trajectory, and Session](choose-eval-scope-across-span-multispan-trajectory-and-session.md)
- [Use Golden Data Sets and Mixed Scoring Functions for AI Application Confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Layer Agent Evals as Deterministic, Semantic, and Behavioral Checks](layer-agent-evals-as-deterministic-semantic-and-behavioral-checks.md)
- [Calibrate LLM judges like binary classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [AI Product Issues Need Signals and Intents](ai-product-issues-need-signals-and-intents.md)
- [Eval an Agent Surface for Protocol Compliance, Not Just Behavior](eval-agent-surfaces-for-protocol-compliance-not-just-behavior.md)

Sources:
- [LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize](../sources/20260607_JsCCrBF7F1g.md), 07:06-08:44
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 09:19-09:30, 17:55-19:08
