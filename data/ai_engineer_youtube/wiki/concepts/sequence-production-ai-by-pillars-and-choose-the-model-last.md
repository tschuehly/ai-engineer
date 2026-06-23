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

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Layer Agent Evals as Deterministic, Semantic, and Behavioral Checks](layer-agent-evals-as-deterministic-semantic-and-behavioral-checks.md)
- [Agents Punish Bad Data and Need Question and Tracking Data Foundations](agents-punish-bad-data-and-need-question-and-tracking-data-foundations.md)
- [Run a Production AI Incident Playbook](run-a-production-ai-incident-playbook.md)
- [Use evals as durable AI system specifications](use-evals-as-durable-ai-system-specifications.md)
- [Last-Mile Domain Context Beats Model Chasing](last-mile-domain-context-beats-model-chasing.md)

Sources:
- [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../sources/20260618_ObTPqBGsEbA.md), 01:32-07:30, 24:24-29:33
