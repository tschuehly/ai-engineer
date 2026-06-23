# The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks

Source: [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](https://www.youtube.com/watch?v=ObTPqBGsEbA)
Uploaded: 2026-06-18
Transcript: `raw/20260618_ObTPqBGsEbA/ObTPqBGsEbA.en-orig.vtt`

## Summary

Sandipan Bhaumik, a Databricks data-and-AI technical lead, distills enterprise demo-to-production failures into a five-pillar playbook: evaluation, observability, data foundation, multi-agent orchestration, and governance. The recurring failure pattern is starting from model choice instead of measurement, which leaves teams unable to explain why an AI system underperforms in production. The talk argues those five pillars should exist before code, and that the model should be selected last using a living evaluation dataset. A retail-bank case study makes the sequencing concrete: a prior £85,000 six-month proof of concept failed, while an eight-week rebuild chose the model in week seven after first building evals, tracing, and a data foundation, and the tracing system later caught stale RAG answers after a policy change. The talk closes with a production incident playbook and three commonly missed lessons about eval-set governance, prompt versioning, and behavioral-eval cost.

## Extracted Concepts

- [Sequence Production AI by Pillars and Choose the Model Last](../concepts/sequence-production-ai-by-pillars-and-choose-the-model-last.md) - this source frames evaluation, observability, data foundation, orchestration, and governance as work that should precede model choice.
- [Layer Agent Evals as Deterministic, Semantic, and Behavioral Checks](../concepts/layer-agent-evals-as-deterministic-semantic-and-behavioral-checks.md) - this source separates cheap deterministic checks, LLM-as-judge semantic checks, and behavioral checks that catch loops and duplicate tool calls.
- [Agents Punish Bad Data and Need Question and Tracking Data Foundations](../concepts/agents-punish-bad-data-and-need-question-and-tracking-data-foundations.md) - this source explains why agent data quality dominates production effort and why tracing data needs its own schema strategy.
- [Run a Production AI Incident Playbook](../concepts/run-a-production-ai-incident-playbook.md) - this source defines a detect, diagnose, contain, fix, and grow-tests loop wired into ITSM alerting.

## Topic Links

- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)
- [Retrieval](../topics/retrieval.md)

## Notes

- The recurring enterprise anti-pattern is starting every AI conversation with model choice (GPT versus Claude debates), building a demo on controlled data, shipping it, and then being unable to explain production failures (01:32-02:55).
- Three gaps motivate the framework: an observability gap (cannot trace decisions), an evaluation gap (never defined the one business number being measured), and a governance gap (no accountability when AI fails at 3am) (03:22-04:17).
- The five pillars should be considered before starting a project and built gradually, preferably in sequence: evaluation, observability, data foundation, orchestration, and governance (04:44-07:30).
- Evaluation is treated as the specification for the AI system: define success in numbers, including acceptable false positives and a target deflection rate for a banking chatbot (07:30-08:25).
- The evaluation dataset is built from domain experts describing real on-the-ground answers and gray-area edge cases, then wired into an automated pipeline that scores live responses against the test set (08:25-09:22).
- Evaluation has three architectural layers: deterministic (regex/format, plus classic ML for NER, intent, and PII), semantic/non-deterministic (LLM-as-judge on safety, groundedness, relevance), and behavioral (tool calls, loops, and duplicate API calls). A correct answer that required three redundant database calls is fine in a demo but expensive at thousands of queries per day (09:22-12:31).
- Observability means tracing every agent decision (intent classification, account lookup, policy retrieval, reasoning, guardrails). Without it there is no way to resolve a customer dispute, and European regulators mandate it before production onboarding. Online monitoring can apply fallback or bounded-retry strategies when duplicate or failing calls appear (12:31-14:45).
- Data foundation is where the speaker spends ~60% of project time: agents do not forgive bad data the way forgiving humans do, so they confidently return wrong answers. He splits it into question data (what the AI answers from) and tracking data (the trace/observability data), which needs its own schema strategy and a centralized collection layer across frameworks like CrewAI and LangChain (14:45-19:52).
- The Databricks stack is described as cloud storage, a Delta Lake table layer, Unity Catalog for centralized permissions plus metadata tagging (table/column descriptions and PII tags that give AI query context), and Mosaic AI, Genie text-to-SQL, Agent Bricks, and MLflow on top (16:38-19:52).
- Orchestration patterns are summarized as orchestrator-worker (central control and logs), choreography (autonomous agents on a message bus, parallel, lower latency), and human-in-the-loop (a confidence threshold pulls in a human); the speaker references his separate deep-dive on state management, fault tolerance, and scaling (19:52-22:34).
- Governance from the AI perspective covers regulatory audit trails, pre-validation of PII via NER (47 PII breaches were caught during the testing phase), prompt versioning treated as change management ("prompt as code"), and model change management where vendor leaderboards are not useful in-context so model upgrades are tested on the team's own eval dataset (22:34-23:56).
- Case study: a retail bank received ~20,000 chatbot calls/month with ~60% simple queries; a prior £85,000 six-month POC failed because no one could measure why. The rebuild set goals of 60% deflection and ~85% accuracy, built the eval layer from 200 real agent answers in weeks one-two, built the data foundation, and selected the model in week seven of eight by running candidates against the eval dataset (24:24-29:05).
- Six weeks post-launch, an interest-rate policy change dropped CSAT (thumbs-down feedback); tracing revealed the new policy document had not been re-embedded into the vector database, so the agent served stale answers. The measurement system is what made the cause detectable (29:05-30:29).
- The production incident playbook is detect (eval dashboard), diagnose (tracing), contain (prompt rollback/version, deflect to human, saga/compensation/circuit-breaker fault tolerance), fix (LLM-judge reports and eval-set library), and grow tests (add the case back to the living dataset), wired into the existing ITSM alerting system (30:29-32:20).
- Three commonly missed lessons: the test-case library is a growing system that needs an owner and categorized rows (e.g., a security category) so changes are traceable; prompt versioning needs governed commit messages documenting why and which failure a change addresses; and layer-three behavioral evals get expensive, so CI should run a small eval subset on prompt changes and the full suite only on merge to main (32:20-35:41).
