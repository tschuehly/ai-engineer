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
- **Two additions from a second source: where the ontology comes from, and a second thing it is for.** Fox insists it is discovered rather than designed — "you don't write that rubric in a vacuum. You have to put the system in production and look at the real outputs. Cluster what goes wrong and the failure modes surface on their own… Discover from your data, not guess on a whiteboard" — because "the ways that a real system goes wrong are effectively unbounded and synthetic test cases only cover the failures you already imagined." And the labels have a consumer beyond the backlog: "this ontology is your map, what to capture judgment on, what to retrieve against," indexing the judged-case corpus a judge reads at scoring time. He is explicit that the modes are "not a checklist that the judge runs, but they organize everything" — running the list at judge time would re-freeze the standard to the modes found so far. A team that builds an ontology only to rank engineering work has stopped one use short. See [Discover Failure Modes From Production Outputs, Not Synthetic Cases](discover-failure-modes-from-production-outputs-not-synthetic-cases.md). ([Fox](../sources/20260822_yqF6XhzbWBk.md), 14:01-14:59)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Treat Evals as the Home of Domain Knowledge](treat-evals-as-the-home-of-domain-knowledge.md)
- [Build Scoring Systems From Inspectable Quality Signals](build-scoring-systems-from-inspectable-quality-signals.md)
- [Discover Failure Modes From Production Outputs, Not Synthetic Cases](discover-failure-modes-from-production-outputs-not-synthetic-cases.md)
- [Assemble the Judging Standard Per Output From Retrieved Precedent](assemble-the-judging-standard-per-output-from-retrieved-precedent.md)

Sources:
- [Make your LLM app a Domain Expert: How to Build an Expert System - Christopher Lovejoy, Anterior](../sources/20250728_MRM7oA3JsFs.md), 07:10-10:35
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 14:01-14:59
