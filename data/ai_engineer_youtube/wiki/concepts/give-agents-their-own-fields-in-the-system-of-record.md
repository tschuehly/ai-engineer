# Give Agents Their Own Fields in the System of Record

Summary: When an agent writes into a structured system, give it its own columns rather than letting it write the same fields that deterministic pipelines and humans write — the separation makes agent output attributable, revertible, and independently trustable without blocking the write path behind approval on every field.

Use when:
- An agent needs to persist judgments into a CRM, ticketing system, or other system of record.
- Deciding how to let unstructured model output land in a structured schema.
- Debugging a record where nobody can tell whether a value came from a person, a job, or a model.
- Designing the first write path for an agent that has so far only read.

Details:
- The rule is stated as a general recommendation, off a specific demo: the agent "critically… [is] also updating different values in my CRM that are just for the agents. So, I always recommend separating the fields that agents are updating from the fields that deterministic systems are updating or that people are updating." ([Berry](../sources/20260826_UhCY231d0FQ.md), 12:23-12:43)
- **The problem it addresses is an impedance mismatch, named earlier in the same section.** "The agents are often doing unstructured work and pushing that into systems that are highly structured like a CRM. And so the mapping of what the agent is producing is super important." Agent-owned fields are where that mapping is allowed to be lossy without corrupting anything that was already correct. (11:07-11:21)
- Three properties follow from the separation, none of which requires an approval step. Provenance is structural rather than logged, so "who wrote this" is answered by which column it is in. Rollback is a column-scoped operation instead of a per-record forensic exercise. And downstream consumers can opt in per field — a forecast can keep using the human-owned stage while a routing rule reads the agent-owned score.
- **It is the cheap alternative to gating writes, and a partial one.** [Read-Side Agents Scale First Because the Write Side Needs Approvals](read-side-agents-scale-first-because-the-write-side-needs-approvals.md) explains why internal deployments stay read-only: a wrong CRM update propagates into forecasts, routing, and compensation before anyone reads it. Separate fields do not make the write correct — they make it *contained*, so a bad agent value cannot silently overwrite a good human one. That is a different guarantee from [Verify AI Call Summaries Before CRM Sync](verify-ai-call-summaries-before-crm-sync.md), which checks the content before it lands; the two compose, and neither substitutes for the other.
- The containment holds only as far as consumption. Once a report, a routing rule, or another agent reads an agent-owned field, its errors are back in the shared world, so the boundary needs to be enforced in what reads the columns as well as in what writes them — which the talk does not discuss.
- The pattern generalizes past CRMs to any shared schema an agent writes into, and it is the write-side analogue of keeping generated artifacts keyed alongside modeled entities rather than merged into them — see [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md), where agent-generated research snippets are stored beside the versioned entities under the same IDs.
- **Limit.** Asserted from one screenshot with no evidence: no incident that motivated it, no field naming or governance convention, no policy for promoting an agent field into a human field once it is trusted, and no account of how conflicts are surfaced when the two disagree. (11:07-12:43)

Related topics:
- [Agents](../topics/agents.md)
- [Go To Market](../topics/go-to-market.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Run One Dormant, Long-Lived Agent Per Account](run-one-dormant-long-lived-agent-per-account.md)
- [Read-Side Agents Scale First Because the Write Side Needs Approvals](read-side-agents-scale-first-because-the-write-side-needs-approvals.md)
- [Verify AI Call Summaries Before CRM Sync](verify-ai-call-summaries-before-crm-sync.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Put Humans and Agents on the Same Substrate Instead of an AI Layer on Top](put-humans-and-agents-on-the-same-substrate-instead-of-an-ai-layer-on-top.md)
- [Mark Which Lines a Human Wrote So Readers Can Budget Attention](mark-which-lines-a-human-wrote-so-readers-can-budget-attention.md)
- [Use Field-Level Confidence Signals for Human Review](use-field-level-confidence-signals-for-human-review.md)
- [The Human-Agent Handoff Is the Hard Part Once Agents Are the Decision Layer](the-human-agent-handoff-is-the-hard-part-once-agents-are-the-decision-layer.md)

Sources:
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 11:07-12:43
