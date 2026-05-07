# Failure-Mode Ontologies Prioritize Domain AI Work

Summary: A failure-mode ontology turns domain-expert judgment into a structured map of how an AI system fails. Connecting those labels to the customer's top metrics gives PMs and engineers a ranked backlog instead of a pile of anecdotes.

Use when:
- Building an eval taxonomy for a specialized AI application.
- Prioritizing AI product work from expert-reviewed production errors.

Details:
- The talk recommends defining the few metrics users truly care about, such as minimizing false approvals in medical-necessity review, 07:10-08:21.
- Domain experts should lead the ontology work because non-experts inspecting traces in isolation may miss how the real workflow is judged, 08:22-09:15.
- In Anterior's medical-necessity workflow, broad failure categories included medical-record extraction, clinical reasoning, and rules interpretation, with finer subtypes underneath, 08:22-08:55.
- Once each reviewed error has a failure-mode label, teams can chart which failure types drive the north-star metric and prioritize fixes accordingly, 09:15-10:35.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Treat Evals as the Home of Domain Knowledge](treat-evals-as-the-home-of-domain-knowledge.md)
- [Build Scoring Systems From Inspectable Quality Signals](build-scoring-systems-from-inspectable-quality-signals.md)

Sources:
- [Make your LLM app a Domain Expert: How to Build an Expert System - Christopher Lovejoy, Anterior](../sources/20250728_MRM7oA3JsFs.md), 07:10-10:35
