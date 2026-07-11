# Design AI Systems Requirements-First With a Four-Phase Framework

Summary: When AI writes the code, the valuable skill is deciding *what* to build; design an AI system through four sequenced phases — product requirements, system design, evaluation and monitoring, then optimization — so the hard product/spec decisions are made before any code is generated. Most AI systems fail in production because of bad decisions made in the earlier phases, not bad code.

Use when:
- Scoping a new production AI application and wanting a repeatable order of decisions before prompting a coding agent.
- A stakeholder wants to "just vibe-code an agent and ship it" for a real, high-stakes use case.
- Diagnosing why an AI system that demoed well cannot reach production.

Details:
- **Phase 1 — product requirements.** Quantify a *solution-agnostic* business problem: user-specific, states the current state, quantifies the pain with baselines, and does **not** prescribe agent vs multi-agent vs anything. Gather business constraints (regulatory/compliance, data-residency, procurement/approved-vendor, where humans are mandatory) and performance constraints (latency, monthly LLM-inference spend ceiling, uptime SLAs) up front as design inputs. Classify the **role of AI** along three dimensions: critical vs complementary, reactive vs proactive, and level of autonomy (constraints requiring human review cap the system at semi-autonomous). Define 1–2 **SMART** success metrics aligned to the business problem (e.g. cut urgent-claim processing from 2 days to 1 hour within 90 days of launch). (03:45-08:30)
- **Phase 2 — system design.** Work out a per-source **data strategy**: what data is needed, whether you have access, where it resides, its update cadence (pipelines must refresh often enough to avoid stale reasoning), what processing it needs (chunk/embed/metadata-extract long docs; strip PII from structured records), and the retrieval technique per source (vector/hybrid + metadata pre-filtering for terminology-heavy docs; exact match on IDs). **Map the request flow** before choosing an architecture, then compose the *simplest* mix of design patterns rather than jumping to an agent (see [choose an AI architecture by composing the simplest design patterns](choose-autonomy-level-by-task-uncertainty-and-control-needs.md)). Finish with UX and feedback design (input, output, where it lives, trigger, human role, self-explanation via citations, feedback capture) and a constraint-bounded stack (model, embedding model, vector DB, orchestration). (08:35-20:49)
- **Phase 3 — evaluation and monitoring.** Evaluation is before ship, monitoring is after; you need both. Define input/output **guardrails** (LLM systems are probabilistic and can produce unexpected/harmful output) and a [layered metric ladder that carries into production monitoring](layer-ai-application-metrics-from-guardrail-compliance-to-system-health.md). "You can't improve what you can't measure," so build evaluation in from the start. (20:56-25:10)
- **Phase 4 — optimize.** Accuracy looking good is not shippable; cost, latency, and reliability become non-negotiable in production, so expect more iterations between "accuracy is good" and ship. Optimize accuracy by controlling what enters the context window (prompt engineering, reranking, memory/persistence); optimize cost/latency (semantic caching, batch processing); optimize reliability (API-failure handling, structured outputs that guarantee decision + citations). (25:10-27:15)
- **Core discipline:** start with the simplest design, evaluate it, find gaps, and iterate — the most common failure is over-engineering before knowing what is actually failing, or not evaluating at all. (12:12-12:41, 28:00-28:22)

Related topics:
- [Workflows](../topics/workflows.md)
- [Product Strategy](../topics/product-strategy.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Sequence Production AI by Pillars and Choose the Model Last](sequence-production-ai-by-pillars-and-choose-the-model-last.md)
- [Spec-driven development turns prompts into requirements, design, and tasks](spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md)
- [Choose Autonomy Level by Task Uncertainty and Control Needs](choose-autonomy-level-by-task-uncertainty-and-control-needs.md)
- [Layer AI application metrics from guardrail compliance to system health](layer-ai-application-metrics-from-guardrail-compliance-to-system-health.md)

Sources:
- [AI System Design: From Idea to Production - Apoorva Joshi, MongoDB](../sources/20260628_T0HhO4YtTfE.md), 01:49-28:40
