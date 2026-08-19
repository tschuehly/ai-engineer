# Sequence Production AI by Pillars and Choose the Model Last

Summary: Enterprise AI failures often come from starting at model choice instead of measurement. A more reliable sequence builds evaluation, observability, a data foundation, orchestration, and governance first, and selects the model last using the evaluation dataset those pillars produce.

Use when:
- Planning a demo-to-production engagement and deciding what to build first.
- Diagnosing why a working AI demo cannot reach or stay in production.

Details:
- Three gaps explain most stuck projects: an observability gap (no way to trace decisions), an evaluation gap (no defined business number being measured), and a governance gap (no accountability when AI fails). These motivate five pillars to consider before code: evaluation, observability, data foundation, orchestration, and governance. (03:22-07:30)
- The anti-pattern is starting every conversation with GPT-versus-Claude model debates, building a demo on controlled data, shipping it, and then being unable to explain production behavior. (01:32-02:55)
- Model selection should come last and is fast once the eval dataset exists: in an eight-week retail-bank rebuild the model was chosen in week seven by running candidates against the evaluation dataset and comparing scored responses, instead of spending weeks debating models up front. (24:24-29:05)
- The pillars are ideally built in sequence, but the speaker acknowledges real projects rarely follow a clean order; the point is that all five must be known and planned before building, not bolted on after a demo. (04:44-05:11)
- A prior £85,000 six-month proof of concept failed because no one could measure why; the rebuild succeeded by inverting the order and treating measurement infrastructure as the first deliverable. (25:22-29:33)
- **The architectural version of the same claim, from a regulated vendor's side of the table.** Anterior's forward-deployed team watched the pattern from inside customer organizations and names both shapes. Failure: "taking that initial POC … that showed the high accuracy … and then trying to build up from it, strapping on the enterprise requirements as you come across them. Okay, we need eval, we need … security, we need auditability, and bolting these on as additions to the … foundations of the POC. You end up with something very brittle, something very hard to … externalize and to generalize across different use cases." Success: "take the constraints of a production-ready, scaled enterprise … system seriously from the beginning and treat those as the architectural principles that you're going to build everything upon and then build back up towards that POC accuracy using your new primitives." Note what the second sentence concedes — the accuracy has to be re-earned on the new foundation, which is the cost this ordering actually charges. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 17:56-18:52)
- **The selection criterion for those foundations is what you want to stay simple.** "I like to think about architecture as taking your constraints very seriously and thinking about what you want to be simple within the system and then choosing the trade-offs for that. And of course, alongside that, some things will become hard, but it's the things that are simple that are most important to you." Applied concretely, choosing an event log made auditability trivial and reads expensive — a tradeoff worth taking only because the compliance question is the one that stops deployments. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 06:29-06:45, 17:16-17:37)
- **Most of these pillars are not new engineering.** "There are patterns that already exist across enterprises that solve for a lot of these things. And sure, with AI, we need to combine them in new, sometimes radical ways and bring in … other pieces, but there are patterns that have worked very well within finance, within defense, within big tech." The event-sourcing ledger borrowed from finance is the worked example. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 17:37-17:56)
- **What the POC's stakeholders get wrong is which part was hard.** After a POC hits its metrics, finance asks about next year's budget, the chief medical officer wants to publicize the accuracy, and sales asks when "powered by AI" goes on the website — "but the problem is that everyone here is assuming that … the AI was … the challenging part. But actually, as we know, often getting things into production is really where the challenge lies." The questions that then arrive — audit trail, data lifecycle, escalation mechanism, prompt injection, ongoing performance, integrations — are architecture questions, not model questions. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 03:14-05:18)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Let Evals Emerge From Your Architectural Primitives](let-evals-emerge-from-your-architectural-primitives.md)
- [An Audit Trail Is a Chain of Evidence, Not a Developer Log](an-audit-trail-is-a-chain-of-evidence-not-a-developer-log.md)
- [Layer Agent Evals as Deterministic, Semantic, and Behavioral Checks](layer-agent-evals-as-deterministic-semantic-and-behavioral-checks.md)
- [Agents Punish Bad Data and Need Question and Tracking Data Foundations](agents-punish-bad-data-and-need-question-and-tracking-data-foundations.md)
- [Run a Production AI Incident Playbook](run-a-production-ai-incident-playbook.md)
- [Use evals as durable AI system specifications](use-evals-as-durable-ai-system-specifications.md)
- [Last-Mile Domain Context Beats Model Chasing](last-mile-domain-context-beats-model-chasing.md)

Sources:
- [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../sources/20260618_ObTPqBGsEbA.md), 01:32-07:30, 24:24-29:33
- [Why Your Enterprise Tech Stack Isn't Ready for AI Agents — Christopher Lovejoy & Saul Howard](../sources/20260819_mav15aW9lLM.md), 03:14-05:18, 06:29-06:45, 17:16-18:52
